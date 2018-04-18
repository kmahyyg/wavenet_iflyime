#!/usr/bin/env python3.6
# -*- encoding: utf-8 -*-

# Auth Token: (Service account) $ gcloud auth application-default print-access-token
# Set up Gcloud SDK: gcloud auth activate-service-account --key-file=[PATH]

import os
import base64
import requests


def main():
    input("Execute: $ gcloud auth activate-service-account --key-file=[PATH] ")
    os.system('gcloud auth application-default print-access-token')
    apikey = input("Paste the key here:")
    ttstext = input("Text you want to transfer to a speech: ")
    baseurl = 'https://texttospeech.googleapis.com/v1beta1/text:synthesize'
    inputdatas = {
        'input': {'text': ttstext},
        'voice': {'languageCode': 'en-US', 'name': 'en-US-Wavenet-D', 'ssmlGender': 'MALE'},
        'audioConfig': {'audioEncoding': 'OGG_OPUS'}
    }
    custom_auth = {"Authorization": "Bearer " + str(apikey)}
    r = requests.post(baseurl, json=inputdatas, headers=custom_auth)
    json_resp = r.json()
    voiceb64 = json_resp['audioContent'].encode()
    decodeddata = base64.b64decode(voiceb64)
    savedata(decodeddata)
    print("Done!")
    return 0


def savedata(data):
    optfile = open(os.path.expanduser('./output.ogg'), 'wb')
    optfile.write(data)
    optfile.close()
    print("File saved at: " + os.path.expanduser('./output.ogg'))
    return 0


if __name__ == '__main__':
    cwd = os.getcwd()
    print("Current Working Directory: " + str(cwd))
    print("Please ensure that you have write permission to this directory.")
    main()
