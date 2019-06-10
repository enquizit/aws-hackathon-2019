# -*- coding: utf-8 -*-

import pytest
from sls_forum.handlers.user_http_get import handler


def test():
    response = handler(dict(user_id="not-exist"), None)
    print(response)


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
