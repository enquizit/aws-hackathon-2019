# -*- coding: utf-8 -*-

from mongoengine import connect
from .config_init import Config


client = connect(
    db=Config.DB_DATABASE,
    host=Config.DB_HOST,
    port=Config.DB_PORT,
    username=Config.DB_USERNAME,
    password=Config.DB_PASSWORD,
    alias=Config.DB_DATABASE,
)

