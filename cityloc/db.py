# -*- encoding: utf-8 -*-
"""
    cityloc: Look up world city coordinates and country codes
    Copyright (c) 2019 Sveinbjorn Thordarson
"""

from __future__ import unicode_literals

import sqlite3
from pkg_resources import resource_filename


DB_REL_PATH = "resources/cities.db"


class SharedDB:
    def __init__(self):
        self.db_conn = None

    def connection(self):

        # Open connection lazily
        if not self.db_conn:
            db_path = resource_filename(__name__, DB_REL_PATH)
            self.db_conn = sqlite3.connect(db_path, check_same_thread=False)
            self.db_conn.row_factory = lambda c, r: dict(
                zip([col[0] for col in c.description], r)
            )

        return self.db_conn


shared_db = SharedDB()
