# TTS using iFlyIME Cloud

## Sign up for an API KEY

Go to [XunFei Voice Cloud](http://www.xfyun.cn/) to register a new account and follow the instructions to create a 
WEBAPI APP first. After that, Enable the TTS service and add your IP to the whitelist.

## Configuration

Put your APPID and APIKEY with IP Whitelist in the apikey.py.example and follow the format.

## Usage

```bash
user@testvm $ cp ./apikey.py.example ./apikey.py
user@testvm $ pip3.6 install -r ./requirements.txt
user@testvm $ python3.6 ./main.py
```

## Follow the text instruction

Follow the instruction shown on your screen.

## All Done

The output file is ```output.wav``` in your current working directory.
The current working directory will be shown at the very beginning of the program running.