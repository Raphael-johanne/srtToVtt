#!/usr/bin/env python2
# coding: utf-8

import sys
import re

def main():
    from pprint import pprint
    fileName = sys.argv[1]

    srtFileResource = open(fileName, "r")
    srtFile = srtFileResource.read()
    srtFileResource.close()

    vttFileResource = open(fileName + '.vtt', 'w')

    vtt = srt_webvtt(srtFile)
 
    vttFileResource.write(vtt)
    vttFileResource.close() 

def srt_webvtt(data):

    srt = data.replace('/\r+/g', '')
    srt = srt.replace('/^\s+|\s+$/g', '')
    
    cuelist = srt.split('\r\n\r\n')
    result = ""
    pprint(len(cuelist))
    if len(cuelist) > 0:
        result += "WEBVTT\n\n"
        
        for cue in cuelist:
            if cue != '': 
                result = result + convertSrtCue(cue)

    return result

def separate(array,separator):

    results = []
    a = array[:]
    i = 0
    while i<=len(a)-len(separator):
        if a[i:i+len(separator)]==separator:
            results.append(a[:i])
            a = a[i+len(separator):]
            i = 0
        else: i+=1
    results.append(a)
    return results

def convertSrtCue(caption):

    content = ""
    s = separate(caption,'\n')

    line = 0

    cue = s[0] + "\n"
    line = line + 1
    
    m = re.search('(\d+):(\d+):(\d+),(\d+)\s*--?>\s*(\d+):(\d+):(\d+),(\d+)', s[1])
    if m:
        cue = cue + m.group(1)+":"+m.group(2)+":"+m.group(3)+"."+m.group(4)+" --> "+m.group(5)+":"+m.group(6)+":"+m.group(7)+"."+m.group(8)+"\n"
        line = line + 1
    
    i = 0
    for entry in s:
        if line == 0 or line == 1:
            continue
        if 0 <= line < len(s):
            cue = cue + s[line] + "\n"
            line = line + 1

    return cue + "\n"

if __name__ == '__main__':
    main()
