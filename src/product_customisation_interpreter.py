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
import csv
import os.path
from typing import List

def interpret(filename: str, clean: bool):
    # The 'product customisation' CSV is not laid out like a CSV at all (!)
    # so need to wrangle it before it can be interpreted

    content = read_file(filename)
    # Pre-clean: Remove all ; delimiters from the text fields (only via user input in fields)
    path, fname = os.path.split(filename)
    fname_str, ext = os.path.splitext(fname)
    cleaned_filename = os.path.join(path, fname_str + "-cleaned" + ext)
    with open(filename, "r") as f:
        with open(cleaned_filename, "w") as fc:
            for l in f:
                l = l.replace(";", "")
                fc.write(l)
    print(f"Cleaned the output to: {cleaned_filename}")


    key_idx = 5
    value_idx = 6
    product_id_idx = 1
    initial_skip_rows = 4

    actual_csv_headers = []
    actual_csv_data = []

    with open(cleaned_filename, "r") as f:
        csv_data = csv.reader(f, delimiter=",")

        old_product_id = ""
        current_row = {}

        i = -1
        for row in csv_data:
            i = i + 1
            if i < initial_skip_rows:
                continue
            if len(row) == 0:
                continue

            key = row[key_idx]
            value = row[value_idx]
            product_id = row[product_id_idx]

            # Onto a new CSV row if the product_name no longer matches
            if old_product_id != product_id:
                old_product_id = product_id
                if len(current_row) != 0:
                    actual_csv_data.append(current_row)
                current_row = {}

            current_row[key] = value

            if key not in actual_csv_headers:
                actual_csv_headers.append(key)

    full_wrangled_path = os.path.join(path, fname_str + "-wrangled" + ext)
    with open(full_wrangled_path, "w") as f:
        act_csv = csv.DictWriter(f, fieldnames=actual_csv_headers)
        act_csv.writeheader()

        for r in actual_csv_data:
            act_csv.writerow(r)


def read_file(filename) -> List[str]:
    with open(filename, "r") as f:
        return f.readlines()


def clean_input(contents: List[str], strings_to_clean=";") -> List[str]:
    cleaned_contents = []
    for l in contents:
        for sc in strings_to_clean:
            l = l.replace(sc, "")
        cleaned_contents.append(l)

    return cleaned_contents
