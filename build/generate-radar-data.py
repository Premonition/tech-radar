#!/usr/bin/env python3

import yaml
import json
from string import Template

# The goal of this script is to parse a YAML and output a `radar_visualization.js` file.
# This file is read in by the boilerplate index.html file and results in a tech radar
# using Zalando's tech radar library
# The YAML parser is my own, this is based off some other scripts out there which use CSV as an input.
# But we don't like CSV.


# Remember, this is a js function with a json function as an arg.
def main():
    wrapper = Template("radar_visualization($template);")
    title = "Demo Prem Tech Radar - 2023-03-02"
    visualization_json = {
        "svg_id": "radar",
        "width": 1450,
        "height": 1000,
        "colors": {"background": "#fff", "grid": "#bbb", "inactive": "#ddd"},
        "title": title,
        "quadrants": [
            {"name": "Techniques"},
            {"name": "Tooling"},
            {"name": "Platforms"},
            {"name": "Languages & Frameworks"},
        ],
        "rings": [
            {"name": "ADOPT", "color": "#93c47d"},
            {"name": "TRIAL", "color": "#93d2c2"},
            {"name": "ASSESS", "color": "#fbdb84"},
            {"name": "HOLD", "color": "#efafa9"},
        ],
        "print_layout": True,
    }
    categories = [
        "techniques",
        "tooling",
        "platforms",
        "languages-and-frameworks",
    ]

    entries = []
    with open("./input.yml", "r") as file:
        raw_yaml = yaml.safe_load(file)
        file.close()

    for category in categories:
        all_data_in_category = raw_yaml[category]
        for data in all_data_in_category:
            result = parse_entry(category, data)
            if result is not None:
                entries.append(result)
            else:
                print("None found")

    visualization_json["entries"] = entries

    json_dump = json.dumps(visualization_json)
    final_string = wrapper.substitute(template=json_dump)
    with open("../docs/radar_visualization.js", "w+") as output:
        output.write(final_string)
        output.close()

    return


def parse_entry(category, data):
    label = list(data.keys())[0]
    stage = data[label]["stage"]
    movement = data[label]["moved"]
    result = {
        "quadrant": parse_category(category),
        "ring": parse_stage(stage),
        "label": label,
        "active": True,
        "moved": parse_movement(movement),
    }
    if result["ring"] != -1 and result["quadrant"] != -1:
        return result
    else:
        return None


def parse_stage(stage):
    match stage:
        case "adopt":
            return 0
        case "trial":
            return 1
        case "assess":
            return 2
        case "hold":
            return 3
        case _:
            return -1


def parse_movement(movement):
    match movement:
        case "up":
            return 1
        case "down":
            return -1
        case _:
            return 0


def parse_category(category):
    match category:
        case "techniques":
            return 0
        case "tooling":
            return 1
        case "platforms":
            return 2
        case "languages-and-frameworks":
            return 3
        case _: 
            return -1


if __name__ == "__main__":
    main()
