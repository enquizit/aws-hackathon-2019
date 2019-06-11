# -*- coding: utf-8 -*-

import pytest
from pytest import raises, approx
from sls_forum.handlers.user_http_post import handler


def test():
    response = handler(dict(username="alice", email="alice@email.com", password="password"), None)
    print(response)


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
