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
import numpy as np


def get_drivers() -> List[Driver]:
    t1 = datetime.datetime(2023, 1, 1, 12)
    d1 = Driver("D1", None, t1, 3)
    t2 = datetime.datetime(2023, 1, 1, 17, 30)
    d2 = Driver("D2", None, t2, 2)

    return [d1, d2]


def get_passengers() -> List[Passenger]:
    t1 = datetime.datetime(2023, 1, 1, 9)
    p1 = Passenger("P1", None, t1)
    t2 = datetime.datetime(2023, 1, 1, 12)
    p2 = Passenger("P2", None, t2)
    t3 = datetime.datetime(2023, 1, 1, 15)
    p3 = Passenger("P3", None, t3)
    t4 = datetime.datetime(2023, 1, 1, 18)
    p4 = Passenger("P4", None, t4)

    return [p1, p2, p3, p4]


def validate(drivers: List[Driver], passengers: List[Passenger]) -> bool:
    total_capacity = np.sum([d.capacity for d in drivers])
    M = len(passengers)

    return M <= total_capacity
