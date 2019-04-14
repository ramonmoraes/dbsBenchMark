# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots["test_get_type 1"] = "varchar(255)"

snapshots["test_get_type 2"] = "boolean"

snapshots["test_get_type 3"] = "int"

snapshots["test_table_name 1"] = "simplemodelTable"

snapshots[
    "test_simlpe_create_table 1"
] = """CREATE TABLE IF NOT EXISTS simplemodelTable (
    id INT AUTO_INCREMENT,
    foo varchar(255),
    PRIMARY KEY (id)
);"""
