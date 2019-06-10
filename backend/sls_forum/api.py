# -*- coding: utf-8 -*-

import attr
from typing import Union, List, Dict
from attrs_mate import AttrsClass


@attr.s
class LbdResponse(AttrsClass):
    data = attr.ib()  # type: Union[Dict, List]
    errors = attr.ib()  # type: List
    success = attr.ib()  # type: bool
    status = attr.ib()  # int

    class StatusCode:
        Success = 200
        ResourceNotFound = 400
        ResourceConflict = 409
        ServerError = 500
