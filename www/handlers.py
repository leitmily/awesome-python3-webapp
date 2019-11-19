#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from coroweb import get, post


' url handlers '

@get('/')
def test(request):
    return 'hello world!'
