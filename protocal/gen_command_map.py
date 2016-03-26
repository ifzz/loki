#!/usr/bin/python

import sys
import os
import re
import binascii

'''
def FindFileByPattern(pattern='.*', base = "."):
    re_file = re.compile(pattern)
    if base == ".":
        base = os.getcwd()
    final_file_list = []
    cur_list = os.listdir(base)
    for item in cur_list:
        full_path = os.path.join(base, item)
        if os.path.isfile(full_path):
            if re_file.search(full_path):
                final_file_list.append(full_path)
        else:
            final_file_list += FindFileByPattern(pattern, full_path) 
    return final_file_list


if __name__ == "__main__":
    files = FindFileByPattern(".proto", ".")
    for f in files:
        print(f)

        '''
def ParseFile(filename):
    print("Processing file {0}".format(filename))
    f = open(filename, 'r')
    try:
        allText = f.read()
    finally:
        f.close()

    
    matchObj = re.search(r'package\s+(\w+);', allText, re.M)
    if matchObj:
        namespace = matchObj.group(1)

    msgPat = re.compile(r'message\s+(\w+)')
    finds = msgPat.findall(allText)
    #print(finds)
    #print("")
    if namespace == "":
        print("a package name is necessary")
        exit(0)
    prefix = namespace + '.'
    luaFile = filename.replace(".proto", "_proto.lua")
    with open(luaFile, "w") as luafile:
        luafile.write("-- do not edit this file manully\n\n")

        luafile.write('require "script/CommandMap"\n\n')
        luafile.write("local m = CommandMap.m\n")
        luafile.write("local M = CommandMap.M\n")
        luafile.write("local R = CommandMap.Register\n\n")

        luafile.write("if {0} == nil then {0} = {1} end\n\n".format(namespace, "{}"))
        # id = xxx
        for n in finds:
            fullname = prefix + n
            crcNum = abs(binascii.crc32(fullname.encode(encoding="utf-8")))
            luafile.write(fullname + " = {0}\n".format(crcNum))

        luafile.write("\n")
        # m[id] = "xxx"
        #name2id = []
        for n in finds:
            fullname = prefix + n
            luafile.write('R({0},"{1}")\n'.format(fullname, fullname))

        luafile.write("\n")
        '''
        for i in name2id:
            luafile.write('M["{0}"] = {1}\n'.format(i[0], i[1]))
            '''


if __name__ == "__main__":
    '''
    argc = len(sys.argv)
    for a in sys.argv:
        print(a)
    print()
    '''
    path = "."
    files = os.listdir(path)
    protofiles = []
    for f in files:
        fullpath = path + '/' + f
        if f[0] == '.':
            continue
        if (os.path.isfile(fullpath)):
            if fullpath.endswith(".proto"):
                protofiles.append(f)

    for f in protofiles:
        ParseFile(f)
    os.system("./move_proto.sh")


