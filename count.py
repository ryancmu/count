#coding:utf-8
import os
from sys import argv
#统计指定文件行数
def getFileLength(filename):
    with open(filename, 'r') as f:
        length = len(f.readlines())
    return length
#获取目录下所有文件名
def getAllFilesInDir(dir):
    allFile = []
    for root, dirs, files in os.walk(dir):
        files = [os.path.join(root,f) for f in files]
        allFile.extend(files)
    return allFile
#统计指定文件后缀的所有文件总行数
def getTotalLength(allFile, extension):
    totalLength = 0
    for f in allFile:
        if os.path.splitext(f)[-1][1:] in extension:
            print f
            totalLength += getFileLength(f)
    return totalLength
if __name__ == '__main__': 
    allFile = getAllFilesInDir(argv[1])
    print getTotalLength(allFile,  argv[2].split(','))
