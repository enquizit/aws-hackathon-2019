# -*- coding: utf-8 -*-

import boto3
import attr
from attrs_mate import AttrsClass


@attr.s
class Event(AttrsClass):
    post_id = attr.ib()


def handler(event, context):
    from sls_forum.model.model import Post

    event = Event(**event)
    post = Post.by_id(_id=event.post_id)

    session = boto3.session.Session()
    s3 = session.client("s3")
    bucket = "eqtest-sls-forum"
    key = "website/post-view.html"
    response = s3.get_object(
        Bucket=bucket, Key=key
    )
    html = response["Body"].read().decode("utf-8")
    html = html.replace("{{ post_data }}", post.to_html_json())
    return html


if __name__ == "__main__":
    handler(event=dict(post_id="2f62675c-ce6d-4d16-ad64-73af53dd0db3"), context=None)