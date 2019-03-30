# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_table_name 1'] = 'simplemodelTable'

snapshots['test_simlpe_create_table 1'] = 'CREATE TABLE simplemodelTable (foo string);'
