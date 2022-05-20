#!/usr/bin/env python3
import base64
from pydoc import pager
import requests


url = 'https://raw.githubusercontent.com/TheBuffSeagull/Project-Learn-to-Code/master/USERNAMES.txt'
page = requests.get(url)
print(page.text)