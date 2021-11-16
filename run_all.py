#!/usr/bin/env python
#-*- coding:utf-8 -*- 

#author:maxiunan
# import
#
# def main():
#     try:
#         global driver
#         driver = driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#         driver.implicitly_wait(10)

import os
import unittest
from time import sleep
from appium import webdriver
import traceback

from selenium.webdriver.common import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import selenium
from appium import webdriver


class Windows(object):
    def __init__(self,app,host='localhost',port=4723):
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Windows'
        self.desired_caps['app']=app
        self.desired_caps['deviceName'] = 'WindowsPC'
        self.host = host
        self.port = port
        self.appVersion = None

        try:
            self.driver = webdriver.Remote('http://{}:{}/wd/hub'.format(self.host,self.port),self.desired_caps)
        except Exception as e:
            raise  AssertionError(e)
        self.wait = WebDriverWait(self.driver,30)
        #隐式等待
        self.driver.implicitly_wait(10)
if __name__ == '__main__':
    app = "C:\Program Files (x86)\Tencent\WeChat\WeChat.exe"
    notepad = Windows(app)

