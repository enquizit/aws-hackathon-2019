# -*- coding: utf-8 -*-

import pytest
from sls_forum.handlers.post_http_get import handler


def test():
    response = handler(dict(post_id="1771a5de-62b6-4ca6-9e51-1fcedf50921d"), None)
    print(response)


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
