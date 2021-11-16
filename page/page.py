#!/usr/bin/env python
#-*- coding:utf-8 -*- 

#author:maxiunan

class Page(object):
    """基础类，用于页面的继承"""


    def __init__(self, selenium_driver):
        self.driver = se
        self.timeout = 30

        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '7.0',
            'deviceName': '',
            'appPackage': 'com.tencent.mm',
            'appActivity': '.ui.LauncherUI',
            'automationName': 'Uiautomator2',
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'noReset': True,
            'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
        }


    # def on_page(self):
    #     print "当前页面:"  + str(self.driver.current_url)
    #     return self.driver.current_url == (self.base_url + self.url)

    def _open(self, url):
        url = self.base_url + url
        print url
        self.driver.get(url)
        # assert self.on_page(), 'Did not land on %s' %url

    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)