# -*- coding: utf-8 -*-

import boto3
import attr
from attrs_mate import AttrsClass


@attr.s
class Event(AttrsClass):
    post_id = attr.ib()
    user_id = attr.ib()
    content = attr.ib()


def handler(event, context):
    from sls_forum.model.model import User, Author, Post, Comment

    event = Event(**event)

    comment = Post.post_comment(
        author_id=event.user_id,
        post_id=event.post_id,
        content=event.content
    )
    return "https://ikqde3ymi8.execute-api.us-east-1.amazonaws.com/dev/post-view/{}".format(event.post_id)


if __name__ == "__main__":
    handler(event=dict(post_id="2f62675c-ce6d-4d16-ad64-73af53dd0db3"), context=None)
