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
import datetime


class Location:
    pass


class Passenger:
    _name: str
    _location: Location
    _leave_time: datetime.datetime

    # _UUID: str

    def __init__(self, name: str, location: Location,
                 leave_time: datetime.datetime):
        self._name = name
        self._location = location
        self._leave_time = leave_time

    @property
    def name(self) -> str:
        return self._name

    @property
    def location(self) -> Location:
        return self._location

    @property
    def leave_time(self) -> datetime.datetime:
        return self._leave_time


class Driver(Passenger):
    _capacity: int

    def __init__(self, name: str, location: Location,
                 leave_time: datetime.datetime, capacity: int):
        super().__init__(name, location, leave_time)
        self._capacity = capacity

    @property
    def capacity(self) -> int:
        return self._capacity
