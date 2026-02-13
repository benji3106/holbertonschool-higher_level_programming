#!/usr/bin/python3
"""
Module to convert CSV data to JSON format.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to JSON format and save it to data.json.

    Args:
        csv_filename (str): The name of the CSV file.

    Returns:
        True if successful, False otherwise.
    """
    try:
        data = []

        # Read CSV file
        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data.append(row)

        # Write JSON file
        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file)

        return True

    except (FileNotFoundError, OSError, csv.Error):
        return False
