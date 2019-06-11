# -*- coding: utf-8 -*-

import pytest
from pprint import pprint
from sls_forum.model.model import User, Post
from sls_forum.handlers import user_http_post
from sls_forum.handlers import user_http_get
from sls_forum.handlers import user_http_get_all
from sls_forum.handlers import post_http_post
from sls_forum.handlers import post_http_get
from sls_forum.handlers import post_http_post_comment
from sls_forum.handlers import post_http_patch
from sls_forum.handlers import post_http_get_all


def setup_module(module):
    entity_list = [User, Post]
    for entity in entity_list:
        try:
            entity.col().remove()
        except:
            pass

def test():
    # create an user
    response_user_http_post = user_http_post.handler(
        user_http_post.Event(
            username="Alice",
            email="alice@email.com",
            password="password",
        ).to_dict(),
        context=None
    )
    # get user info
    response_user_http_get = user_http_get.handler(
        user_http_get.Event(
            user_id=response_user_http_post["data"]["_id"]
        ).to_dict(),
        context=None,
    )
    # user create a post
    response_post_http_post = post_http_post.handler(
        post_http_post.Event(
            author_id=response_user_http_get["data"]["_id"],
            title="So excited to be Here!",
            content="Hello Everyone, this is my first time AWS Hackathon",
        ).to_dict(),
        context=None,
    )
    response_post_http_get = post_http_get.handler(
        post_http_get.Event(
            post_id=response_post_http_post["data"]["_id"],
        ).to_dict(),
        context=None,
    )

    response_post_http_post_comment = post_http_post_comment.handler(
        post_http_post_comment.Event(
            author_id=response_user_http_post["data"]["_id"],
            post_id=response_post_http_post["data"]["_id"],
            content="Welcome to AWS Hackathon!"
        ).to_dict(),
        context=None,
    )

    response_post_http_patch = post_http_patch.handler(
        post_http_patch.Event(
            post_id=response_post_http_post["data"]["_id"],
            content="Hello Everyone, actually, it is my second time :>"
        ).to_dict(),
        context=None,
    )

    response_post_http_patch = post_http_patch.handler(
        post_http_patch.Event(
            post_id=response_post_http_post["data"]["_id"],
            content="Hello Everyone, actually, it is my second time :>"
        ).to_dict(),
        context=None,
    )

    response_user_http_get_all = user_http_get_all.handler(
        user_http_get_all.Event(page_id=1).to_dict(),
        context=None,
    )
    response_post_http_get_all = post_http_get_all.handler(
        post_http_get_all.Event(page_id=1).to_dict(),
        context=None,
    )
    pprint(response_post_http_get_all)



if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
