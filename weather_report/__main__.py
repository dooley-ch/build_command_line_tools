# *******************************************************************************************
#  File:  __main__.py
#
#  Created: 04-07-2022
#
#  Copyright (c) 2022 James Dooley <james@dooley.ch>
#
#  History:
#  04-07-2022: Initial version
#
# *******************************************************************************************

import os
import atexit
from pathlib import Path
import core.commands as cmds
import core.utils as utils


# noinspection PyBroadException
def exit_routine() -> None:
    try:
        utils.log_end()
    except:
        # We swallow any errors on exit
        pass


def main():
    """
    The application entry point
    """
    # Set the working folder
    working_folder: Path = Path(__file__).parent
    os.chdir(working_folder)

    # Set up the exit routine
    atexit.register(exit_routine)

    # Configure logging
    utils.configure_logging('command_line_tools', __file__)
    utils.log_start()

    # Process commands
    cmds.app()


if __name__ == '__main__':
    main()
