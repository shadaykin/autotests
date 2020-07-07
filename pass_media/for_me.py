from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time, random
import pytest


browser = webdriver.Chrome()
browser.get('https://ya.ru')


