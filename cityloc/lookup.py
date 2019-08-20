# -*- encoding: utf-8 -*-
"""
    cityloc: Look up world city coordinates and country codes
    Copyright (c) 2019 Sveinbjorn Thordarson
"""

from __future__ import unicode_literals
from __future__ import print_function

from .db import shared_db


def _run_query(q, qargs):
    db_conn = shared_db.connection()
    res = db_conn.cursor().execute(q, qargs)
    return [dict(row) for row in res]


def _capitalize_first_char(s):
    return s[:1].upper() + s[1:] if s else s


def city_lookup(city_name, country=None):
    """ Look up all cities matching criterion """

    city_name = _capitalize_first_char(city_name.strip())

    q = "SELECT * FROM cities WHERE (name=? OR name_ascii=?)"
    l = [city_name, city_name]
    if country:
        q += " AND country=? "
        l.append(country)

    q += " ORDER BY capital DESC, population DESC, country ASC, name ASC"

    return _run_query(q, l)


def capital_for_cc(country_code):
    """ Return info on capital city, given an 3166-1 alpha-2 country code """
    cc = country_code.upper()

    q = "SELECT * FROM cities WHERE capital=1 AND country=?"

    res = _run_query(q, [cc])
    if res:
        return res[0]

    return None
