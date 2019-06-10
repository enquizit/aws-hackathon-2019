# -*- coding: utf-8 -*-

import attr
from attrs_mate import AttrsClass
import mongoengine as me


@attr.s
class Event(AttrsClass):
    username = attr.ib()
    email = attr.ib()
    password = attr.ib()


def handler(event, context):
    from ..model.model import User
    from ..api import LbdResponse

    try:
        event = Event(**event)
        user = User.post(
            username=event.username,
            email=event.email,
            password=event.password,
        )
        response = LbdResponse(
            data=user.to_dict(),
            errors=list(),
            success=True,
            status=LbdResponse.StatusCode.Success,
        )
    except me.errors.NotUniqueError as e:
        response = LbdResponse(
            data=list(),
            errors=[(e.__class__.__name__, str(e))],
            success=False,
            status=LbdResponse.StatusCode.ResourceConflict,
        )
    except Exception as e:
        response = LbdResponse(
            data=list(),
            errors=[(e.__class__.__name__, str(e))],
            success=False,
            status=LbdResponse.StatusCode.ServerError
        )

    return response.to_dict()
