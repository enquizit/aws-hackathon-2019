# -*- coding: utf-8 -*-

import boto3
import json
import attr
from attrs_mate import AttrsClass


@attr.s
class Event(AttrsClass):
    page_id = attr.ib()


def handler(event, context):
    from sls_forum.model.model import Post

    event = Event(**event)
    post_listpage_data = Post.get_all(page_id=int(event.page_id))
    for post_data in post_listpage_data:
        post_data["create_at"] = str(post_data["create_at"])
        post_data["last_edited_at"] = str(post_data["last_edited_at"])

        for comment_data in post_data["comments"]:
            comment_data["create_at"] = str(comment_data["create_at"])

    session = boto3.session.Session()
    s3 = session.client("s3")
    bucket = "eqtest-sls-forum"
    key = "website/post-listpage.html"
    response = s3.get_object(
        Bucket=bucket, Key=key
    )
    html = response["Body"].read().decode("utf-8")
    html = html.replace("{{ post_listpage_data }}", json.dumps(post_listpage_data))
    return html


if __name__ == "__main__":
    handler(dict(page_id=1), None)