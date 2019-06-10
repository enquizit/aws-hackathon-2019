# -*- coding: utf-8 -*-

import pytest
from pytest import raises, approx
from sls_forum.model.model import User, Post


def setup_module(module):
    entity = User()
    for entity in entity_list:
        try:
            User.col().remove()



if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
