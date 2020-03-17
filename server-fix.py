from flask import Flask, request, jsonify, send_from_directory
from os import path, stat, remove, SEEK_END
from json import load
from hashlib import sha1
from stagger import read_tag
from stagger.id3 import *
from stagger.errors import NoTagError
import MySQLdb

CONFIG_FILE = "./config.json"
SERV_PORT = 0
DATA_DIR = ""
DB_HOST = ""
DB_PORT = 0
DB_USER = ""
DB_PASSWD = "" 
DB_DB = ""

app = Flask(__name__)
db = None
cursor = None

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file_data"]
    if file:
        file.seek(0, SEEK_END)
        file_length = file.tell()
        if (file_length > 2000000):
            return "File too big!"
        file.seek(0, 0)
        if (file.filename[-4:] != '.mp3'):
            return "Not MP3"
        filename = hash_file(file) + file.filename[-4:]
        file.save(path.join(app.config["UPLOAD_FOLDER"], filename))
        msg = db_insert_file(filename, file)
        return msg
    return "No file"
    
@app.route("/")
def web():
    f = open('web.html', 'r')
    html_content = f.read()
    f.close()
    return html_content

def hash_file(file):
    file_data = file.read()
    file.seek(0)
    return sha1(file_data).hexdigest()

def db_connect():   
    db = MySQLdb.connect(
        host = DB_HOST,
        port = DB_PORT,
        user = DB_USER,
        passwd = DB_PASSWD,
        db = DB_DB
    )

    return db, db.cursor()

def db_insert_file(filename, file):
    id3_file = None
    
    try: 
        id3_file = read_tag(path.join(app.config["UPLOAD_FOLDER"], filename))
    except NoTagError:
        query = "INSERT IGNORE INTO ytfs_meta (filename) VALUES ('{0}');".format(filename)
        cursor.execute(query)
        db.commit()
        return "Succesfully add MP3 (No Title)"

    try:
        title = id3_file.title.replace("'", "\\'")
       
        query = "INSERT IGNORE INTO ytfs_meta (filename, title) " + \
            "VALUES ('{0}', '{1}');".format(filename, title)
        cursor.execute(query)
        db.commit()
        return "Sucessfully add MP3 (%s)" % (title)
    except:
        return "Error"

def load_config(
):
    global SERV_PORT, DATA_DIR, DB_HOST, DB_PORT, DB_USER, DB_PASSWD, DB_DB
    config_data = None

    with open(CONFIG_FILE) as config:
        config_data = load(config)
    
    SERV_PORT = int(config_data["server"]["port"])
    DATA_DIR = config_data["server"]["data_dir"]
    DB_HOST = config_data["db"]["host"]
    DB_PORT = config_data["db"]["port"]
    DB_USER = config_data["db"]["username"]
    DB_PASSWD = config_data["db"]["password"]
    DB_DB = config_data["db"]["db"]

if __name__ == "__main__":
    load_config()
    app.config["UPLOAD_FOLDER"] = DATA_DIR
    db, cursor = db_connect()
    if db: print("Connected to database!")
    app.run(
        host = "0.0.0.0",
        port = SERV_PORT
    )
