# -*- coding: utf-8 -*-

import pytest

from sls_forum.model.model import User, Author, Comment, Post


class TestUser(object):
    def test_post(self):
        user = User.post(username="alice", email="alice@gmail.com", password="password")
        user.save()


# class TestPost(object):
#     def test_to_json(self):
#         user = User(username="Alice", email="alice@gmail.com")
#         user.save()





if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
