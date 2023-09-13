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
import numpy as np
from typing import Tuple, List, Dict
from src.datastructs import Passenger, Driver
from src.constants import t_Solution


def solve(drivers: List[Driver], passengers: List[Passenger]) -> t_Solution:

    total_capacity = np.sum([d.capacity for d in drivers])
    N = len(drivers)
    M = len(passengers)

    if M > total_capacity:
        raise ValueError("Cars don't have enough capacity for all the passengers!")

    A = create_matrix(drivers, passengers)

    X = np.argsort(A, axis=None)

    passenger_assigned_tracker = {p: False for p in passengers}
    drivers_remaining_capacity = {d: d.capacity for d in drivers}
    actual_groups = {d: [] for d in drivers}

    for x in X:
        n = x % N
        m = x // N

        driver = drivers[n]
        passenger = passengers[m]

        # Ensure we're only assigning to a car that still has capacity
        remaining_capacity = drivers_remaining_capacity[driver]
        if remaining_capacity == 0:
            continue
        # If the passenger has already been assigned, ignore
        if passenger_assigned_tracker[passenger]:
            continue

        # decrement this car's remaining capacity
        drivers_remaining_capacity[driver] = remaining_capacity - 1
        # Track the passenger as being assigned
        passenger_assigned_tracker[passenger] = True

        # Track the actual group members of each car
        actual_groups[driver].append(passenger)

    return actual_groups


def create_matrix(drivers: List[Driver], passengers: List[Passenger]):
    L = create_distance_matrix(drivers, passengers)
    T = create_time_difference_matrix(drivers, passengers)

    wL, wT = get_weights()

    return wL * L**2 + wT * T**2


def create_distance_matrix(drivers: List[Driver], passengers: List[Passenger]) -> np.ndarray:
    N = len(drivers)
    M = len(passengers)

    return np.ones((N, M))


def create_time_difference_matrix(drivers: List[Driver], passengers: List[Passenger]) -> np.ndarray:
    N = len(drivers)
    M = len(passengers)

    T = np.zeros((N, M), float)

    for i in range(N):
        for j in range(M):
            T[i, j] = (drivers[i].leave_time - passengers[j].leave_time).seconds

    return T


def get_weights() -> Tuple[float, float]:
    # TODO: implement
    return (0, 1)