# -*- coding: utf-8 -*-

def handler(event, context):
    if event.get("name"):
        return "Hello {}!".format(event.get("name"))
    else:
        return "Hello World!"
