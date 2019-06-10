# -*- coding: utf-8 -*-

import pytest
from pytest import raises, approx
from sls_forum.config_init import Config

def test_config_init():
    print(Config.DB_DATABASE)



if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
