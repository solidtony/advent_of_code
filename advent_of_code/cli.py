"""Contains all CLI related"""
from argparse import ArgumentParser
import sys
from typing import Callable

from advent_of_code import year_2024

YEAR_MODULE_MAP = {
    2024:year_2024
}

class CommandLineTool:
    """Command line tool for advent of code."""
    def __init__(self):
        """Initializes all argument parsing functionality"""
        self.add_top_parser()
    
    def add_top_parser(self):
        self.parser = ArgumentParser(
            description = 'CLI to run solutions to Advent of Code (https://adventofcode.com/).'
        )
        self.parser.add_argument(
            '-y',
            '--year',
            help='Advent of Code year',
            type=int,
            choices=YEAR_MODULE_MAP.keys(),
            required=True
        )
        self.parser.add_argument(
            '-d',
            '--day',
            help='Advent of Code day',
            type=int,
            choices=[day for day in range(1,26)],
            required=True
        )
        self.parser.add_argument(
            '-p',
            '--part',
            help='Advent of Code part for selected day',
            type=int,
            choices=[1,2],
            required=True
        )
        self.parser.add_argument(
            '-i',
            '--input',
            help="Optional input file to run solution on. If not included, will run with the default file.",
            type=str,
            required=False,
            default=None
        )

    def run(self, argv):
        """Runs the main logic of advent of code"""
        args = self.parser.parse_args(argv)
        part_function = self._get_part_function(args.year, args.day, args.part)
        if args.input:
            part_function(input_path=args.input)
        else:
            part_function()

    def _get_part_function(self, year:int, day:int, part:int) -> Callable:
        year_module = YEAR_MODULE_MAP[year]
        day_module = getattr(year_module, f'day_{day}')
        part_function = getattr(day_module, f'part_{part}')
        return part_function

def main(argv=None):
    """Main command line interface"""
    if argv is None:
        argv = sys.argv[1:]

    CommandLineTool().run(argv)

    return None

if __name__ == '__main__':
    sys.exit(main())
