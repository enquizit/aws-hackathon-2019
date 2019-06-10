# -*- coding: utf-8 -*-

import attr
from attrs_mate import AttrsClass
import mongoengine as me

@attr.s
class Event(AttrsClass):
    post_id = attr.ib()


def handler(event, context):
    from ..model.model import Post
    from ..api import LbdResponse

    try:
        event = Event(**event)
        post = Post.get(_id=event.post_id)
        post_data = post.to_mongo()
        post_data["create_at"] = str(post_data["create_at"])
        post_data["last_edited_at"] = str(post_data["last_edited_at"])
        response = LbdResponse(
            data=post_data,
            errors=list(),
            success=True,
            status=LbdResponse.StatusCode.Success,
        )
    except me.errors.DoesNotExist as e:
        response = LbdResponse(
            data=list(),
            errors=[(e.__class__.__name__, str(e))],
            success=False,
            status=LbdResponse.StatusCode.ResourceNotFound,
        )

    except Exception as e:
        response = LbdResponse(
            data=list(),
            errors=[(e.__class__.__name__, str(e))],
            success=False,
            status=LbdResponse.StatusCode.ServerError,
        )

    return response.to_dict()
