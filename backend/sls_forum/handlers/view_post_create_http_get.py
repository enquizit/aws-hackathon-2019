# -*- coding: utf-8 -*-

import boto3
import attr
from attrs_mate import AttrsClass


@attr.s
class Event(AttrsClass):
    user_id = attr.ib()


def handler(event, context):
    event = Event(**event)

    session = boto3.session.Session()
    s3 = session.client("s3")
    bucket = "eqtest-sls-forum"
    key = "website/post-create.html"
    response = s3.get_object(
        Bucket=bucket, Key=key
    )
    html = response["Body"].read().decode("utf-8")
    html = html.replace("{{ user_id }}", event.user_id)
    return html


if __name__ == "__main__":
    handler(event=dict(user_id="2f62675c-ce6d-4d16-ad64-73af53dd0db3"), context=None)
