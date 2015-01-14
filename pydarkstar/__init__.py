__version__ = 0.1

from . import logutils
import logging

logutils.setError()

try:
    import sqlalchemy
except ImportError as e:
    logging.exception(e.__class__.__name__)
    logging.error('pip install sqlalchemy')
    exit(-1)

try:
    import pymysql
except ImportError as e:
    logging.exception(e.__class__.__name__)
    logging.error('pip install pymysql')
    exit(-1)

try:
    import bs4
except ImportError as e:
    logging.exception(e.__class__.__name__)
    logging.error('pip install beautifulsoup4')
    exit(-1)

from . import common
from . import darkobject
from . import database
from . import item
from . import itemlist
from . import logutils
from . import options
from . import rc
from . import timeutils

from . import scrub
from . import tables
from . import auction