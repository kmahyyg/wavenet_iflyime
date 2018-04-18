# TTS using Cloud Resources

## Sign up for an API KEY

Go to [XunFei Voice Cloud](http://www.xfyun.cn/) to register a new account and follow the instructions to create a 
WEBAPI APP first. After that, Enable the TTS service and add your IP to the whitelist.  (For Chinese TTS)

Go to [Google Cloud](https://cloud.google.com) to register a TTS API and enable it in Billing Tab. After that, Create a
Service account key and save it secretly. After that, follow the instructions. (NOTE: You'd better use it in Google
Compute Engine, because Google Cloud SDK is too sucked, still Python 2.7 ......) For more details, you need to see their
documents, This program use WaveNet model which is developed under Tensorflow with a better effect.  (For English TTS)

## Configuration

Put your APPID and APIKEY with IP Whitelist in the apikey.py.example and follow the format.

## Usage

```bash
user@testvm $ cp ./apikey.py.example ./apikey.py
user@testvm $ pip3.6 install -r ./requirements.txt
user@testvm $ python3.6 ./main.py  # For Chinese TTS
user@testvm $ python3 ./wavenet_gcloud.py  # For English TTS 
```

## Follow the text instruction

Follow the instruction shown on your screen.

## All Done

The output file is ```output.wav``` or ```output.ogg``` in your current working directory.
The current working directory will be shown at the very beginning of the program running.
