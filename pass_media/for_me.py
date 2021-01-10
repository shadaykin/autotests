from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time, random
import pytest
import sys



params = {
  "default_cas_fields": [
    "nickname_hash",
    "last_name"
  ],
  "redirect_uris": "https://localhost\r\nhttps://locaohffs\r\n",
  "name": "fdsdgfs",
  "required_fields": ["nickname","first_name"],
  "public_url": "https://localhostq",
  "rate_limit_minute": "0",
  "rate_limit_day": "0",
  "public": "false",
  "optional_fields": "nickname"
}

for key in params['default_cas_fields']:
    if 'hash' in key:
        print('optional')
    else:
        print('req')