"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """

    with open(neo_csv_path, 'r') as f:
        neo_csv = csv.DictReader(f)
        neos = []
        for row in neo_csv:
            neo = NearEarthObject(**row)
            neos.append(neo)
    return neos

def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    with open(cad_json_path, 'r') as cad:
        cad_json = json.load(cad)
        cads =[]
        for row in cad_json["data"]:
            ca = CloseApproach(**dict(zip(cad_json["fields"], row)))
            cads.append(ca)
        return cads
                    
    #     try:
    #         cad = CloseApproach(
    #             designation=row["des"],
    #             time=row["cd"],
    #             distance=float(row["dist"]),
    #             velocity=float(row["v_rel"]),
    #         )
    #     except Exception as e:
    #         print(e)
    #     else:
    #         cads.append(cad)
    # return cads
