# -*- coding: utf-8 -*-

import uuid
import mongoengine as me
from mongoengine_mate import ExtendedDocument


class BaseModel(ExtendedDocument):
    meta = {
        "abstract": True,
    }

    _id = me.fields.StringField(default=lambda: str(uuid.uuid4()))


    ITEM_PER_PAGE = 20

    @classmethod
    def get(cls, _id):
        return cls.by_id(_id)

    @classmethod
    def get_all(cls, page_id):
        skip = cls.ITEM_PER_PAGE * (page_id - 1)
        return list(cls.col().find().skip(skip).limit(cls.ITEM_PER_PAGE))
