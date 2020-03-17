import re
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

def sandbox_block(mod):
    flist = dir(__builtins__.__import__(mod))
    for f in flist:
        exec('__builtins__.__import__("%s").%s = None' % (mod, f))

def sandbox_block_function(mod, f):
    exec('__builtins__.__import__("%s").%s = None' % (mod, f))

@app.route('/_calculate')
def calculate():
    a = request.args.get('number1', '0')
    operator = request.args.get('operator', '+')
    b = request.args.get('number2', '0')
    m = re.match('^.*\\d$', a)
    n = re.match('^.*\\d$', b)
    if m is None or n is None or operator not in '+-*/':
        return jsonify(result='Error')
    if operator == '/':
        result = eval(a + operator + str(float(b)))
    else:
        result = eval(a + operator + b)
    return jsonify(result=result)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    sandbox_block_function('os', 'system')
    sandbox_block_function('os', 'spawn')
    sandbox_block_function('os', 'popen')
    sandbox_block_function('os', 'popen2')
    sandbox_block_function('os', 'popen3')
    sandbox_block_function('os', 'popen4')
    sandbox_block_function('os', 'open')
    sandbox_block_function('os', 'openpty')
    sandbox_block_function('os', 'spawnl')
    sandbox_block_function('os', 'spawnle')
    sandbox_block_function('os', 'spawnlp')
    sandbox_block_function('os', 'spawnlpe')
    sandbox_block_function('os', 'spawnv')
    sandbox_block_function('os', 'spawnve')
    sandbox_block_function('os', 'spawnvp')
    sandbox_block_function('os', 'spawnvpe')
    sandbox_block_function('os', 'walk')
    sandbox_block_function('linecache', 'getline')
    sandbox_block('subprocess')
    sandbox_block('pickle')
    sandbox_block('cPickle')
    sandbox_block('fileinput')
    sandbox_block('glob')
    sandbox_block('shutil')
    sandbox_block('popen2')
    sandbox_block('commands')
    app.run()
