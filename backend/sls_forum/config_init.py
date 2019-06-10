# -*- coding: utf-8 -*-

from .config import Config

try:
    Config.update_from_config()
except:
    pass

Config.DB_HOST = "ds139775.mlab.com"
Config.DB_PORT = 39775
Config.DB_DATABASE = "sls_forum"
Config.DB_USERNAME = "enquizit"
Config.DB_PASSWORD = "Yp#c3adpG6y5"
