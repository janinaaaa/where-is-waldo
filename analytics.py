from shutil import rmtree
from json import dump, load

def write_analytics(field, analytics_data):
    try:
        with open("output/analytics.json", "r") as f:
            data = load(f)
    except FileNotFoundError:
        data = {}

    data[field] = analytics_data

    with open("output/analytics.json", "w") as f:
        dump(data, f, indent=4)

def clean_analytics():
    try:
        rmtree("output", ignore_errors=True)
    except Exception as e:
        # Print to error log
        print(f"Error: {e}")
        