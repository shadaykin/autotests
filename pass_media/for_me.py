from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time, random
import pytest
import sys


tokens = dict(
    test_201='2efe49abccad96de57e7c96923eccf90f6b1886c',
    other_201='740ea2823503035e6fdef524db3ad81f77ea705c')

env = 'test_201'

header = tokens['other'+env.split('test')[1]]

print(header)
