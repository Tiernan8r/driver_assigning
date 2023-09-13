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


def output(solution: t_Solution):
    print("{")
    for driver in solution.keys():
        print(f"{driver.name}: [")
        for passenger in solution[driver]:
            print(f"\t- {passenger.name}\n")
        print("]\n")
    print("}")
