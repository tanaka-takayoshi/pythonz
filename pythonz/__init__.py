
import os
import sys

from pythonz.basecommand import command_dict, load_all_commands
from pythonz.baseparser import parser
from pythonz.define import PATH_HOME_ETC
from pythonz.util import makedirs


def init_home():
    if not os.path.isdir(PATH_HOME_ETC):
        makedirs(PATH_HOME_ETC)

def main():
    options, args = parser.parse_args(sys.argv[1:])
    if options.help and not args:
        args = ['help']
    if not args:
        args = ['help'] # as default
    init_home()
    load_all_commands()
    command = args[0].lower()
    if command not in command_dict:
        parser.error("Unknown command: `%s`" % command)
        return
    command = command_dict[command]
    command.run(args[1:])

