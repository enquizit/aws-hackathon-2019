# -*- coding: utf-8 -*-

import json
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
    username = me.fields.StringField(required=True)


class Comment(me.EmbeddedDocument):
    author = me.fields.EmbeddedDocumentField(Author)
    content = me.fields.StringField(required=True)
    create_at = me.fields.DateTimeField(default=lambda: datetime.utcnow())

    def to_html_json(self):
        dict_data = self.to_mongo()
        dict_data["create_at"] = str(dict_data["create_at"])
        return json.dumps(dict_data)


class Post(BaseModel):
    title = me.fields.StringField(required=True)
    content = me.fields.StringField()
    create_at = me.fields.DateTimeField(default=lambda: datetime.utcnow())
    last_edited_at = me.fields.DateTimeField(default=lambda: datetime.utcnow())

    author = me.fields.EmbeddedDocumentField(Author)
    comments = me.fields.ListField(me.fields.EmbeddedDocumentField(Comment))

    meta = {
        "db_alias": Config.DB_DATABASE,
        "collection": "post"
    }

    def to_html_json(self):
        dict_data = self.to_mongo()
        dict_data["create_at"] = str(dict_data["create_at"])
        dict_data["last_edited_at"] = str(dict_data["last_edited_at"])
        for comment_data in dict_data["comments"]:
            comment_data["create_at"] = str(comment_data["create_at"])
        return json.dumps(dict_data)

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

    @classmethod
    def post_comment(cls, post_id, author_id, content):
        user = User.get(_id=author_id)
        comment = Comment(
            author=Author(
                _id=user._id,
                username=user.username,
            ),
            content=content,
        )
        cls.objects(_id=post_id).update_one(push__comments=comment.to_mongo())
        return comment

    @classmethod
    def patch(cls, post_id, content):
        cls.objects(_id=post_id).update_one(set__content=content)


class Session(BaseModel):
    user_id = me.fields.StringField()
    expire_at = me.fields.DateTimeField()

    meta = {
        "db_alias": Config.DB_DATABASE,
        "collection": "session"
    }
