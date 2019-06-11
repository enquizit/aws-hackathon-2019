# -*- coding: utf-8 -*-

import attr
from attrs_mate import AttrsClass
import mongoengine as me

@attr.s
class Event(AttrsClass):
    user_id = attr.ib()


def handler(event, context):
    from ..model.model import User
    from ..api import LbdResponse

    try:
        event = Event(**event)
        user = User.get(_id=event.user_id)
        response = LbdResponse(
            data=user.to_mongo(),
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
