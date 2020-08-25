from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time, random
import pytest


a = False
b = 0
while not a and b < 2:
    b += 1
    a = True


print(a)
