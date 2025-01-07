from shutil import rmtree
from json import dump, load

def get(field_path):
    print("get")
    try:
        with open("output/analytics.json", "r") as f:
            existing_data = load(f)
    except FileNotFoundError:
        return None

    # split field string "some/path" into ["some", "path"] ignore leading and trailing slashes
    fields = field_path.strip("/").split("/")

    if len(fields) == 0:
        raise ValueError("Field path cannot be empty")

    return _get(fields, existing_data)

def _get(fields, existing_data):
    if len(fields) == 1:
        return existing_data.get(fields[0])
    else:
        return _get(fields[1:], existing_data.get(fields[0]))

def write(analytics_data, field_path):
    print("write")
    try:
        with open("output/analytics.json", "r") as f:
            existing_data = load(f)
    except FileNotFoundError:
        existing_data = {}

    # split field string "some/path" into ["some", "path"] ignore leading and trailing slashes
    fields = field_path.strip("/").split("/")

    if len(fields) == 0:
        raise ValueError("Field path cannot be empty")

    _write(fields, existing_data, analytics_data)

    with open("output/analytics.json", "w") as f:
        dump(existing_data, f, indent=4)

def _write(fields, existing_data, new_data):
    if len(fields) == 1:
        existing_data[fields[0]] = new_data
    else:
        if fields[0] not in existing_data:
            existing_data[fields[0]] = {}  # Initialize only if the key doesn't exist
        elif not isinstance(existing_data[fields[0]], dict):
            raise ValueError(f"Field {fields[0]} is not a dictionary")
        _write(fields[1:], existing_data[fields[0]], new_data)


def append(analytics_data, field_path):
    print("append")
    try:
        with open("output/analytics.json", "r") as f:
            existing_data = load(f)
    except FileNotFoundError:
        existing_data = {}

    # split field string "some/path" into ["some", "path"]
    fields = field_path.split("/")

    if len(fields) == 0:
        raise ValueError("Field path cannot be empty")

    _append(fields, existing_data, analytics_data)

    with open("output/analytics.json", "w") as f:
        dump(existing_data, f, indent=4)

def _append(fields, existing_data, new_data):
    if len(fields) == 1:
        if fields[0] not in existing_data:
            existing_data[fields[0]] = []  # Initialize as a list if it doesn't exist
        elif not isinstance(existing_data[fields[0]], list):
            raise ValueError(f"Field {fields[0]} is not a list")
        existing_data[fields[0]].append(new_data)
    else:
        if fields[0] not in existing_data:
            existing_data[fields[0]] = {}  # Initialize only if the key doesn't exist
        elif not isinstance(existing_data[fields[0]], dict):
            raise ValueError(f"Field {fields[0]} is not a dictionary")
        _append(fields[1:], existing_data[fields[0]], new_data)



def clean():
    try:
        rmtree("output", ignore_errors=True)
    except Exception as e:
        # Print to error log
        print(f"Error: {e}")