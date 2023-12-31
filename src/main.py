#!/usr/bin/env python
# Copyright 2023 Tiernan8r
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import sys
# Required to guarantee that the 'src' module is accessible when
# this file is run directly.
if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())

from typing import List
import src.input as input
import src.solver as solver
import src.output as output
import argparse
from src.constants import PROGRAM_NAME, PROGRAM_DESCRIPTION, PROGRAM_EPILOG

def main(argv: List[str]):

    parser = argparse.ArgumentParser(
        prog=PROGRAM_NAME,
        description=PROGRAM_DESCRIPTION,
        epilog=PROGRAM_EPILOG
    )

    parser.add_argument("-g", "--gui", action="store_true", default=False, help="Use interactive GUI")

    args = parser.parse_args()

    if args.gui:
        # show the GUI
        #TODO...
        print("GUI HERE...")
        return

    drivers = input.get_drivers()
    passengers = input.get_passengers()

    solution = solver.solve(drivers, passengers)

    print("SOLUTION")
    output.output(solution)
    print("DONE")


if __name__ == "__main__":
    main(sys.argv)
