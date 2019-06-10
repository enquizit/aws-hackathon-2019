# -*- coding: utf-8 -*-

from superjson import json
from pathlib_mate import PathCls as Path


class Config(object):
    DB_HOST = None
    DB_PORT = None
    DB_DATABASE = None
    DB_USERNAME = None
    DB_PASSWORD = None

    RAW_CONFIG_FILE = Path(__file__).parent.change(new_basename="config.json")

    @classmethod
    def update_from_config(cls):
        data = json.loads(Path(cls.RAW_CONFIG_FILE).read_text(encoding="utf-8"))
        for key, value in data.items():
            if hasattr(cls, key):
                setattr(cls, key, value)
