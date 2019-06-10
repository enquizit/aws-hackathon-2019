# -*- coding: utf-8 -*-

import attr
from attrs_mate import AttrsClass

@attr.s
class Event(AttrsClass):
    page_id = attr.ib()


def handler(event, context):
    from ..model.model import Post
    from ..api import LbdResponse

    try:
        event = Event(**event)
        posts_data = Post.get_all(page_id=int(event.page_id))
        for post_data in posts_data:
            post_data["create_at"] = str(post_data["create_at"])
            post_data["last_edited_at"] = str(post_data["last_edited_at"])

            for comment_data in post_data["comments"]:
                comment_data["create_at"] = str(comment_data["create_at"])

        response = LbdResponse(
            data=posts_data,
            errors=list(),
            success=True,
            status=LbdResponse.StatusCode.Success,
        )
    except Exception as e:
        response = LbdResponse(
            data=list(),
            errors=[(e.__class__.__name__, str(e))],
            success=False,
            status=LbdResponse.StatusCode.ServerError,
        )

    return response.to_dict()
