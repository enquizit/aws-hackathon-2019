# -*- coding: utf-8 -*-

import boto3

def handler(event, context):
    session = boto3.session.Session()
    s3 = session.client("s3")
    bucket = "eqtest-sls-forum"
    key = "website/index.html"
    response = s3.get_object(
        Bucket=bucket, Key=key
    )
    html = response["Body"].read().decode("utf-8")
    return html