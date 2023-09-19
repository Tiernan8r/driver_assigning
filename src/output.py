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
from src.constants import t_Solution

TABLE_WIDTH = 72


def output(solution: t_Solution):
    usable_width = TABLE_WIDTH - 3
    half = usable_width // 2
    remainder = usable_width - (half * 2)

    sep = "+" + "-" * half + "+" + "-" * half + "-" * remainder + "+"
    print(sep)
    print("|" + "NAME".ljust(half) + "|" + "LEAVE TIME".ljust(half) + " " * remainder + "|")
    print(sep)

    for driver in solution.keys():
        time_str = driver.leave_time.time().isoformat(timespec="minutes")
        print("|" + driver.name.ljust(half) + "|" + time_str.ljust(half) + " " * remainder + "|")
        print(sep)
        for passenger in solution[driver]:
            print("|" + passenger.name.ljust(usable_width) + " " * remainder + "|")
            print(sep)
