# -*- coding: utf-8 -*-

import boto3
import attr
from attrs_mate import AttrsClass


@attr.s
class Event(AttrsClass):
    title = attr.ib()
    content = attr.ib()
    user_id = attr.ib()


def handler(event, context):
    from sls_forum.model.model import User, Author, Post

    event = Event(**event)

    user = User.get(_id=event.user_id)

    post = Post(
        title=event.title,
        content=event.content,
        author=Author(_id=user._id, username=user.username)
    )
    post.save()
    return "https://ikqde3ymi8.execute-api.us-east-1.amazonaws.com/dev/post-view/{}".format(post._id)

    # session = boto3.session.Session()
    # s3 = session.client("s3")
    # bucket = "eqtest-sls-forum"
    # key = "website/post-view.html"
    # response = s3.get_object(
    #     Bucket=bucket, Key=key
    # )
    # html = response["Body"].read().decode("utf-8")
    # html = html.replace("{{ post_data }}", post.to_html_json())
    # return html


if __name__ == "__main__":
    handler(event=dict(post_id="2f62675c-ce6d-4d16-ad64-73af53dd0db3"), context=None)
