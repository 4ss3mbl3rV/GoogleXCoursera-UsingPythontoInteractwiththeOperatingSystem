#! /usr/bin/env python3
import requests, socket

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'

def check_connectivity():
    request = requests.get('https://www.google.com')
    return request.status_code == 200
