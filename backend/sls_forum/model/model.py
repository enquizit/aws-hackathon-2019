# -*- coding: utf-8 -*-

import attr
from attrs_mate import AttrsClass
import mongoengine as me
from datetime import datetime
from .base import BaseModel
from ..db import Config
from ..pkg.fingerprint import fingerprint


class User(BaseModel):
    username = me.fields.StringField(required=True, unique=True)
    email = me.fields.EmailField(required=True, unique=True)
    password_digest = me.fields.StringField()

    meta = {
        "db_alias": Config.DB_DATABASE,
        "collection": "user"
    }

    @classmethod
    def post(cls, username, email, password):
        password_digest = fingerprint.of_text(password)
        user = User(username=username, email=email, password_digest=password_digest)
        user.save()
        return user


class Author(me.EmbeddedDocument):
    _id = me.fields.StringField()
    username = me.fields.StringField(required=True, unique=True)


class Comment(me.EmbeddedDocument):
    author = me.fields.EmbeddedDocumentField(Author)
    content = me.fields.StringField(required=True)
    create_at = me.fields.DateTimeField(default=lambda: datetime.utcnow())


class Post(BaseModel):
    title = me.fields.StringField(required=True)
    content = me.fields.StringField()
    create_at = me.fields.DateTimeField(default=lambda: datetime.utcnow())
    last_edited_at = me.fields.DateTimeField()

    author = me.fields.EmbeddedDocumentField(Author)
    comments = me.fields.ListField(me.fields.EmbeddedDocumentField(Comment))

    meta = {
        "db_alias": Config.DB_DATABASE,
        "collection": "post"
    }

    @classmethod
    def post(cls, author_id, title, content):
        user = User.get(_id=author_id)
        post = cls(
            title=title,
            content=content,
            author=Author(_id=user._id, username=user.username)
        )
        post.save()
        return post

    # @classmethod
    # def post_comment(cls, post_id, author_id, content):
    #     pass
