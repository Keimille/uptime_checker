# cli.py

import argparse

def read_user_cli_args():
    """Handle the CLI arguments and options."""
    parser = argparse.ArgumentParser(
        prog="upchecker", description="check the availability of websites"
    )
    parser.add_argument(
        "-u",
        "--urls",
        "-f",
        "--input_file",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="enter one or more website URLs",
    )
    return parser.parse_args()

def display_check_result(result, url, error=""):
    """Display the result of a connectivity check."""
    print(f'The status of "{url}" is:', end=" ")
    if result:
        print('"Online!" 👍')
    else:
        print(f'"Offline?" 👎 \n  Error: "{error}"')    