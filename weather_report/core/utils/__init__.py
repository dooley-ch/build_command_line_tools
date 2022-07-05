# *******************************************************************************************
#  File:  __init__.py
#
#  Created: 05-07-2022
#
#  History:
#  05-07-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__contact__ = "james@developernotes.org"
__copyright__ = "Copyright (c) 2022 James Dooley <james@dooley.ch>"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

__all__ = ['find_folder', 'find_config_folder', 'find_logs_folder', 'find_data_folder', 'find_database_folder',
           'configure_logging', 'log_start', 'log_end', 'log_activity']

from ._core import *
from ._config import *
