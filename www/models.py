#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Models for user, blog, comment.
'''

import time, uuid, asyncio

from orm import Model, StringField, BooleanField, FloatField, TextField, create_pool

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, column_type='varchar(50)')
    email = StringField(column_type='varchar(50)')
    passwd = StringField(column_type='varchar(50)')
    admin = BooleanField()
    name = StringField(column_type='varchar(50)')
    image = StringField(column_type='varchar(500)')
    created_at = FloatField(default=time.time)

class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key=True, default=next_id, column_type='varchar(50)')
    user_id = StringField(column_type='varchar(50)')
    user_name = StringField(column_type='varchar(50)')
    user_image = StringField(column_type='varchar(500)')
    name = StringField(column_type='varchar(50)')
    summary = StringField(column_type='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)

class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, column_type='varchar(50)')
    blog_id = StringField(column_type='varchar(50)')
    user_id = StringField(column_type='varchar(50)')
    user_name = StringField(column_type='varchar(50)')
    user_image = StringField(column_type='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)

if __name__ == "__main__":
    
    async def test(loop):
        await create_pool(loop=loop, host='localhost', port=3306, user='www-data', password='www-data', db='awesome')
        u = User(name='Test1', email='test1@example.com', passwd='1234567890', image='about:blank')
        await u.save()

    # 获取EventLoop:
    loop = asyncio.get_event_loop()
    # 执行coroutine
    loop.run_until_complete(test(loop))
    loop.close()
