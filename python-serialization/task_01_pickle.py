#!/usr/bin/python3
"""
Module for converting CSV data to JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to a JSON file named data.json.
    Returns True if successful, False otherwise.
    """
    try:
        data = []
        # CSV dosyasını oku ve her satırı sözlüğe çevir
        with open(csv_filename, encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data.append(row)

        # Listeyi JSON formatında data.json dosyasına yaz
        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file)

        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
