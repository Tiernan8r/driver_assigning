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
from src.datastructs import Passenger, Driver
from typing import List
import datetime
import time

def get_drivers() -> List[Driver]:
    t1 = datetime.datetime(2023, 1, 1, 12)
    d1 = Driver("A", None, t1, 1)
    t2 = datetime.datetime(2023, 1, 1, 17, 30)
    d2 = Driver("B", None, t2, 1)

    return [d1, d2]

def get_passengers() -> List[Passenger]:
    t1 = datetime.datetime(2023, 1, 1, 9)
    p1 = Passenger("Pa", None, t1)
    t2 = datetime.datetime(2023, 1, 1, 9)
    p2 = Passenger("Pb", None, t2)

    return [p1, p2]

def validate(drivers: List[Driver], passengers: List[Passenger]) -> bool:
    # TODO: implement sanity check on total driver capacity >= num passengers
    return True