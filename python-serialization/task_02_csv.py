#!/usr/bin/env python3
"""Convert CSV data to JSON format using serialization."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Read a CSV file and write its content to data.json as JSON.

    Return True if conversion succeeds, otherwise False.
    """
    try:
        with open(csv_filename, newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except (FileNotFoundError, OSError):
        return False
