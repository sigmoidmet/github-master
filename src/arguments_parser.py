import os
import argparse

import yaml

__arguments_file = "../resources/arguments.yml"
__file_dir = os.path.dirname(__file__)

__name_field = "name"
__help_field = "help"
__action_field = "action"
__short_field = "short"
__argn_field = "argn"


def get_parser() -> argparse.ArgumentParser:
    config = __get_arguments_config()

    parser = argparse.ArgumentParser(description=config['description'])

    for positional_arg in config['positional']:
        __add_argument(parser, positional_arg)

    for optional_arg in config['optional']:
        optional_arg[__name_field] = "--" + optional_arg[__name_field]
        optional_arg[__short_field] = "-" + optional_arg[__short_field]
        __add_argument(parser, optional_arg)

    return parser


def __get_arguments_config() -> dict:
    with open(os.path.join(__file_dir, __arguments_file), "r") as file:
        return yaml.safe_load(file)


def __add_argument(parser: argparse.ArgumentParser, arg: dict) -> None:
    if __action_field in arg:
        parser.add_argument(arg[__short_field],
                            arg[__name_field],
                            help=arg[__help_field],
                            action=arg[__action_field])
    else:
        parser.add_argument(arg[__name_field],
                            nargs=arg.get(__argn_field, "?"),
                            help=arg[__help_field])
