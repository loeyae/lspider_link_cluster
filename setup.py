# -*- coding: utf-8 -*-
# Licensed under the Apache License, Version 2.0 (the "License"),
# see LICENSE for more details: http://www.apache.org/licenses/LICENSE-2.0.

__author__ = "Zhang Yi <loeyae@gmail.com>"
__date__ = "$2019-2-19 9:16:07$"

from setuptools import setup, find_packages

setup(
    name="cdspider_link_cluster",
    version="0.1.3",
    description="数据采集框架URL聚类",
    author='Zhang Yi',
    author_email='loeyae@gmail.com',
    license="Apache License, Version 2.0",
    url="https://github.com/loeyae/lspider_link_cluster.git",
    install_requires=[
        'cdspider>=0.1.4',
    ],
    packages=find_packages(),
    entry_points={
        'cdspider.dao.mongo': [
            'LinksDB=cdspider_link_cluster.database.mongo:LinksDB',
        ],
        'cdspider.handler': [
            'links-cluster=cdspider_link_cluster.handler:LinksClusterHandler',
        ]
    }
)
