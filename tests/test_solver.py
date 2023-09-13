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
from src import solver
from src.datastructs import Driver, Passenger
import datetime
import pytest

def get_test_time(hour, minute = 0):
    return datetime.datetime(2023, 1, 1, hour, minute)

def test_solver_one_driver_one_passenger():
    t = get_test_time(9)
    d1 = Driver("D", None, t, 1)
    p1 = Passenger("P", None, t)

    test_drivers = [d1]
    test_passengers = [p1]

    test_solution = solver.solve(test_drivers, test_passengers)

    expected_solution = {
        d1: [p1]
    }

    assert(test_solution == expected_solution)


def test_solver_same_leave_times():
    t1 = get_test_time(12)
    d1 = Driver("D1", None, t1, 1)
    t2 = get_test_time(17)
    d2 = Driver("D2", None, t2, 1)

    t1 = get_test_time(12)
    p1 = Passenger("P1", None, t1)
    t2 = get_test_time(17)
    p2 = Passenger("P2", None, t2)

    test_drivers = [d1, d2]
    test_passengers = [p1, p2]

    test_solution = solver.solve(test_drivers, test_passengers)

    expected_solution = {
        d1: [p1],
        d2: [p2]
    }

    assert(test_solution == expected_solution)


def test_solver_different_leave_times():
    t1 = get_test_time(12)
    d1 = Driver("D1", None, t1, 1)
    t2 = get_test_time(17, 30)
    d2 = Driver("D2", None, t2, 1)

    t1 = get_test_time(9)
    p1 = Passenger("P1", None, t1)
    t2 = get_test_time(16)
    p2 = Passenger("P2", None, t2)

    test_drivers = [d1, d2]
    test_passengers = [p1, p2]

    test_solution = solver.solve(test_drivers, test_passengers)

    expected_solution = {
        d1: [p1],
        d2: [p2]
    }

    assert (test_solution == expected_solution)


def test_solver_same_passenger_leave_times():
    t1 = get_test_time(12)
    d1 = Driver("D1", None, t1, 1)
    t2 = get_test_time(17, 30)
    d2 = Driver("D2", None, t2, 1)

    t1 = get_test_time(9)
    p1 = Passenger("P1", None, t1)
    t2 = get_test_time(9)
    p2 = Passenger("P2", None, t2)

    test_drivers = [d1, d2]
    test_passengers = [p1, p2]

    test_solution = solver.solve(test_drivers, test_passengers)

    expected_solution = {
        d1: [p1],
        d2: [p2]
    }

    assert (test_solution == expected_solution)


def test_solver_all_passengers_to_one_car():
    t = get_test_time(12)
    td = get_test_time(14)
    d1 = Driver("D1", None, td, 4)
    d2 = Driver("D2", None, td, 4)

    p1 = Passenger("P1", None, t)
    p2 = Passenger("P2", None, t)
    p3 = Passenger("P3", None, t)
    p4 = Passenger("P4", None, t)

    test_drivers = [d1, d2]
    test_passengers = [p1, p2, p3, p4]

    test_solution = solver.solve(test_drivers, test_passengers)

    expected_solution = {
        d1: [p1, p2, p3, p4],
        d2: []
    }

    assert (test_solution == expected_solution)
