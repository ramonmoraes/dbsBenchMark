# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_schema_creator 1'] = [
    ''' is_person: bool . 
''',
    ''' name: string . 
''',
    ''' is_judge: bool . 
''',
    ''' is_disctrict: bool . 
''',
    ''' estate: string . 
''',
    ''' is_courtsection: bool . 
''',
    ''' is_lawyer: bool . 
''',
    ''' number: string . 
''',
    ''' is_kind: bool . 
''',
    ''' last_name: string . 
''',
    ''' is_subject: bool . 
''',
    ''' is_lawsuit: bool . 
'''
]
