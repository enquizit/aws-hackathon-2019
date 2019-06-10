# -*- coding: utf-8 -*-

import pytest
from pytest import raises, approx
from sls_forum.handlers.post_http_post import handler


def test():
    response = handler(
        dict(
            author_id="151b5a47-3e07-4e82-a0d3-cf4c8b726b9a",
            title="My First Post",
            content="Hello World!",
        ), None
    )
    print(response)


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
