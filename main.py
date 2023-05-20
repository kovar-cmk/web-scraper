#!/bin/python
import requests
from collections import namedtuple
from random import randrange


proxies = {"http": "127.0.0.1:8080"}
user_pars = { "user-agent":"Mozila/5.0 (X11; :Linux i686; rv:64.0) Geko/20100101 Firefox/64.0"}

t = input("please enter your target utl ,sir: ")
r = requests.get(t, proxies=proxies, headers=user_pars)
for cookie in r.cookies:
    print(cookie)