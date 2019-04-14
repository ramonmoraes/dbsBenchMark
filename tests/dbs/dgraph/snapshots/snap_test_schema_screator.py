# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots["test_schema_creator 1"] = [
    """ name: string . 
""",
    """ is_person: bool . 
""",
    """ estate: string . 
""",
    """ is_lawsuit: bool . 
""",
    """ is_lawyer: bool . 
""",
    """ is_judge: bool . 
""",
    """ number: string . 
""",
    """ is_disctrict: bool . 
""",
    """ last_name: string . 
""",
    """ is_courtsection: bool . 
""",
    """ is_kind: bool . 
""",
]
