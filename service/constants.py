"""Módulo 'constants' de georef-ar-api

Contiene variables con valores constantes.
"""

from flask import current_app
from service import names as N

API_NAME = 'georef-ar-api'

MAX_RESULT_LEN = current_app.config['MAX_RESULT_LEN']
MAX_RESULT_WINDOW = current_app.config['MAX_RESULT_WINDOW']

INDEX_SOURCES = {
    N.STATES: N.SOURCE_IGN,
    N.DEPARTMENTS: N.SOURCE_IGN,
    N.MUNICIPALITIES: N.SOURCE_IGN,
    N.LOCALITIES: N.SOURCE_BAHRA,
    N.STREETS: N.SOURCE_INDEC
}

MIN_AUTOCOMPLETE_CHARS = 4
DEFAULT_SEARCH_SIZE = 10
DEFAULT_FUZZINESS = 'AUTO:4,8'
ADDRESS_PARSER_CACHE_SIZE = 5000

STATE_ID_LEN = 2
DEPT_ID_LEN = 5
MUNI_ID_LEN = 6
LOCALITY_ID_LEN = 11
STREET_ID_LEN = 13
