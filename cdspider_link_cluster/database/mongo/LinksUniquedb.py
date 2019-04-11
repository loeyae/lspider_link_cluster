#-*- coding: utf-8 -*-

# Licensed under the Apache License, Version 2.0 (the "License"),
# see LICENSE for more details: http://www.apache.org/licenses/LICENSE-2.0.

"""
:author:  Zhang Yi <loeyae@gmail.com>
:date:    2018-1-9 21:58:31
:version: SVN: $Id: Urlsdb.py 2116 2018-07-04 03:56:12Z zhangyi $
"""
import time
from cdspider_link_cluster.database.base import LinksUniqueDB as BaseLinksUniqueDB
from cdspider.cdspider.database.mongo.Mongo import Mongo

class LinksUniqueDB(Mongo, BaseLinksUniqueDB):

    __tablename__ = 'urlsUnique'

    incr_key = ''

    def __init__(self, connector, table=None, **kwargs):
        super(UrlsUniqueDB, self).__init__(connector, table = table, **kwargs)
        collection = self._db.get_collection(self.table)
        indexes = collection.index_information()
        if not 'urlmd5' in indexes:
            collection.create_index('urlmd5', unique=True, name='urlmd5')
        if not 'url' in indexes:
            collection.create_index('url', name='url')

    def insert(self, obj = {}):
        _id = super(UrlsUniqueDB, self).insert(setting=obj)
        return obj['urlmd5']

    def update(self, id, obj = {}):
        obj['utime'] = int(time.time())
        return super(UrlsUniqueDB, self).update(setting=obj, where={'uid': int(id)}, multi=False)

    def update_many(self, obj = {},where=None):
        if where=={} or where==None:
            return
        obj['utime'] = int(time.time())
        return super(UrlsUniqueDB, self).update(setting=obj, where=where, multi=True)

    def delete(self, id, where = {}):
        obj = {"status": self.STATUS_DELETED}
        obj['utime'] = int(time.time())
        if not where:
            where = {'uid': int(id)}
        else:
            where.update({'uid': int(id)})
        return super(UrlsUniqueDB, self).update(setting=obj, where=where, multi=False)

    def delete_by_site(self, sid, where = {}):
        obj = {"status": self.STATUS_DELETED}
        obj['utime'] = int(time.time())
        if not where:
            where = {"sid": int(sid)}
        else:
            where.update({"sid": int(sid)})
        return super(UrlsUniqueDB, self).update(setting=obj, where=where, multi=True)

    def delete_by_project(self, pid, where = {}):
        obj = {"status": self.STATUS_DELETED}
        obj['utime'] = int(time.time())
        if not where:
            where = {'pid': int(pid)}
        else:
            where.update({'pid': int(pid)})
        return super(UrlsUniqueDB, self).update(setting=obj, where=where, multi=True)

    def active(self, id, where = {}):
        obj = {"status": self.STATUS_ACTIVE}
        obj['utime'] = int(time.time())
        if not where:
            where = {'uid': int(id)}
        else:
            where.update({'uid': int(id)})
        return super(UrlsUniqueDB, self).update(setting=obj, where=where, multi=False)

    def disable(self, id, where = {}):
        obj = {"status": self.STATUS_INIT}
        obj['utime'] = int(time.time())
        if not where:
            where = {'uid': int(id)}
        else:
            where.update({'uid': int(id)})
        return super(UrlsUniqueDB, self).update(setting=obj, where=where, multi=False)

    def disable_by_site(self, sid, where = {}):
        obj = {"status": self.STATUS_INIT}
        obj['utime'] = int(time.time())
        if not where:
            where = {"sid": int(sid)}
        else:
            where.update({"sid": int(sid)})
        return super(UrlsUniqueDB, self).update(setting=obj, where=where, multi=True)

    def disable_by_project(self, pid, where = {}):
        obj = {"status": self.STATUS_INIT}
        obj['utime'] = int(time.time())
        if not where:
            where = {'pid': int(pid)}
        else:
            where.update({'pid': int(pid)})
        return super(UrlsUniqueDB, self).update(setting=obj, where=where, multi=True)

    def get_detail(self, id):
        return self.get(where={'uid': int(id)})

    def get_list(self, where = {}, select=None, **kwargs):
        kwargs.setdefault('sort', [('uid', 1)])
        return self.find(where=where, select=select, **kwargs)

    def get_new_list(self, id, sid, where = {}, select=None, **kwargs):
        kwargs.setdefault('sort', [('uid', 1)])
        if not where:
            where = {}
        where['uid'] = {'$gt': int(id)}
        where['sid'] = int(sid)
        return self.find(where = where, select=select, **kwargs)

    def get_new_list_by_pid(self, id, pid, where = {}, select=None, **kwargs):
        kwargs.setdefault('sort', [('uid', 1)])
        if not where:
            where = {}
        where['uid'] = {'$gt': int(id)}
        where['pid'] = pid
        return self.find(where = where, select=select, **kwargs)
