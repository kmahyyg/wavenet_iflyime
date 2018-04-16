#!/usr/bin/env python3.6
# -*- encoding: utf-8 -*-

import base64
import hashlib
import json
import os
import requests
import time
import urllib.parse

from apikey import *

# add envvars to help user locate the output file
cwd = os.getcwd()
print("Current Working Directory: " + str(cwd))
print("Please ensure that you have write permission to this directory.")


def write_tofile(datas):
    filepath = os.path.expanduser('./output.wav')
    outputfile = open(filepath, 'wb')
    outputfile.write(datas)
    outputfile.close()
    print("File output to: " + filepath)


def tts_ifly():
    baseurl = 'http://api.xfyun.cn/v1/service/v1/tts'
    custom_header = {"X-Appid": iflyappid, "X-CurTime": str(int(time.time()))}
    # audio params and base64 encode
    audioparams = {"auf": "audio/L16;rate=16000", "aue": "raw", "voice_name": "xiaoyan", "volume": "70"}
    xparamfin = json.dumps(audioparams)
    xparamfin = xparamfin.encode('utf8')
    xparamfin = base64.b64encode(xparamfin)
    xparamfin = xparamfin.decode('utf8')
    # md5(apikey + curtime + params).hexdigest() = checksum
    check2nd = (ttskey + custom_header['X-CurTime'] + xparamfin).encode('utf8')
    xchecksum = hashlib.md5(check2nd).hexdigest()
    custom_header["X-Param"] = xparamfin
    custom_header["X-CheckSum"] = xchecksum
    # content-type according to the docs
    custom_header["Content-Type"] = "application/x-www-form-urlencoded; charset=utf-8"
    # ask user for TTS TEXT
    ttsoritxt = input("Please input the text you want to transfer to speech:")
    body = {"text": ttsoritxt}
    bodyencode = urllib.parse.urlencode(body)
    bodyencode = bodyencode.encode('utf8')
    # post data
    r = requests.post(baseurl, headers=custom_header, data=bodyencode)
    if r.headers.get('content-type') == 'text/plain':
        resulterr = json.dumps(r.json())
        return print(resulterr)
    elif r.headers.get('content-type') == 'audio/mpeg':
        auddata = r.content
        write_tofile(auddata)
        return print("Done!")
    else:
        return print("Unknown Error!")


def main():
    for i in authorizedIP:
        print('Authorized IP:' + i)
    input("Please ensure that your IP is in the list. Press anykey to continue.")
    tts_ifly()


if __name__ == '__main__':
    main()
