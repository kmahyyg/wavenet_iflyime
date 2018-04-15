#!/usr/bin/env python3.6
#-*- encoding: utf-8 -*-

import os,requests,base64,time,hashlib

# add envvars to help find the apikey
cwd = os.getcwd()
os.chdir(cwd)
secretkey = str(cwd) + '/apikey.json'


