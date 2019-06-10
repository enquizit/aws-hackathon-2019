# -*- coding: utf-8 -*-

import attr
from attrs_mate import AttrsClass


@attr.s
class Event(AttrsClass):
    author_id = attr.ib()
    post_id = attr.ib()
    content = attr.ib()


def handler(event, context):
    from ..model.model import Post
    from ..api import LbdResponse

    try:
        event = Event(**event)
        comment = Post.post_comment(
            author_id=event.author_id,
            post_id=event.post_id,
            content=event.content
        )
        response = LbdResponse(
            data=comment.to_mongo(),
            errors=list(),
            success=True,
            status=LbdResponse.StatusCode.Success
        )
    except Exception as e:
        response = LbdResponse(
            data=list(),
            errors=[(e.__class__.__name__, str(e))],
            success=False,
            status=LbdResponse.StatusCode.ServerError,
        )

    return response.to_dict()
