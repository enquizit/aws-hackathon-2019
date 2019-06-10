# -*- coding: utf-8 -*-

import boto3
import json
import attr
from datetime import datetime, timedelta
from attrs_mate import AttrsClass
from sls_forum.model.model import User, Session, fingerprint


@attr.s
class Event(AttrsClass):
    username = attr.ib()
    password = attr.ib()


def handler(event, context):
    event = Event(**event)

    # failed
    try:
        user = User.objects(username=event.username).get()
    except Exception as e:
        return

    # success
    if fingerprint.of_text(event.password) == user.password_digest:
        utc_1hour_later = datetime.utcnow() + timedelta(seconds=3600)
        auth_session = Session(user_id=user._id, expire_at=utc_1hour_later)
        auth_session.save()
        session_id = auth_session._id
        return

    # failed
    else:
        return


if __name__ == "__main__":
    handler(dict(username="Alice", password="password"), None)