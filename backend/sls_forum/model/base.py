# -*- coding: utf-8 -*-

import uuid
import mongoengine as me
from mongoengine_mate import ExtendedDocument

class BaseModel(ExtendedDocument):
    meta = {
        "abstract": True,
    }

    _id = me.fields.StringField(default=lambda: str(uuid.uuid4()))

    @classmethod
    def get(cls, _id):
        return cls.by_id(_id)