# -*- coding: utf-8 -*-

import pytest
from pytest import raises, approx
from sls_forum.model.model import User, Post
from sls_forum.handlers import user_http_post
from sls_forum.handlers import user_http_get
from sls_forum.handlers import user_http_get_all
from sls_forum.handlers import post_http_post
from sls_forum.handlers import post_http_get
from sls_forum.handlers import post_http_post_comment
from sls_forum.handlers import post_http_patch


# def setup_module(module):
#     entity_list = [User, Post]
#     for entity in entity_list:
#         try:
#             entity.col().remove()
#         except:
#             pass

def test():
    # response_user_http_post = user_http_post.handler(
    #     user_http_post.Event(
    #         username="Alice",
    #         email="alice@email.com",
    #         password="password",
    #     ).to_dict(),
    #     context=None
    # )
    # print(response_user_http_post)
    # user create a post
    response_post_http_post = post_http_post.handler(
        post_http_post.Event(
            author_id="8d66ac45-80bd-4c12-abd1-bbfb3d065b1f",
            title="So excited to be Here!",
            content="Hello Everyone, this is my first time AWS Hackathon",
        ).to_dict(),
        context=None,
    )
    print(response_post_http_post)



if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
