#!/usr/bin/env python
import argparse
import argcomplete
import os

import pysoup


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('-q', '--quiet', help='no output to screen', action='store_true')

    commands = parser.add_subparsers(dest='command')

    cmd_install = commands.add_parser('install', help='install dependencies for a python project')
    cmd_install.add_argument('-g', '--global-installation', help='install dependencies as global', action='store_true')
    cmd_install.add_argument('-r', '--require-custom-file', help='use custom yaml file', default='soup.yaml')

    argcomplete.autocomplete(parser)
    args = parser.parse_args()

    if args.command == 'install':
        cwd = os.getcwd()
        target_file = args.require_custom_file
        is_global = args.global_installation
        is_quiet = args.quiet
        pysoup.PySoup.start_with_args('install', cwd, target_file, is_global, is_quiet)

if __name__ == '__main__':
    main()
