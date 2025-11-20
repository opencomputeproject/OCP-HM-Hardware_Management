import json
from jsonschema import Draft202012Validator, validate
import sys

def load_schema(schema_path):
    with open(schema_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_json(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def validate_json(schema_path, json_path):
    schema = load_schema(schema_path)
    instance = load_json(json_path)

    try:
        Draft202012Validator.check_schema(schema)
        validate(instance=instance, schema=schema)
        print(f"✅ {json_path} is valid according to the schema.")
    except Exception as e:
        print(f"❌ Validation failed: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python validate_json.py <schema_file> <json_file>")
    else:
        validate_json(sys.argv[1], sys.argv[2])
