# encoding: utf-8
"""
File:       config
Author:     twotrees.us@gmail.com
Date:       2020年7月25日  30周星期六 18:55
Desc:
"""
from .base_data_item import BaseDataItem

class AppConfig(BaseDataItem):
    def __init__(self):
        self.user = None
        self.password = None
        self.port = None
        self.proxy_mode = None
        self.inited = False

    def filename(self):
        return 'config/app_config.json'