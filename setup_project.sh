#!/bin/bash

cpath=`pwd`

sed "s;{{ project_path }};$cpath;g" crontab_template > crontab

echo copy your token here
read token

sed "s;YOUR_AUTH_TOKEN;$token;g" src/evernote_api.py.tmpl > src/evernote_api.py
