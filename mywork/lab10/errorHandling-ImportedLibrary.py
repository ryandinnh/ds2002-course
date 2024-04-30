"""
original code:
import json

# Invalid JSON data
data = "{invalid_json_key: 'value'}"

try:
  # Attempt to load the JSON data
  json.loads(data)
except json.JSONDecodeError as e:
  # Print the JSON import error
  print(f"JSON import error: {e}")

"""

import json

# Invalid JSON data
data = '{"invalid_json_key": "value"}'

try:
    # Attempt to load the JSON data
    json.loads(data)
except json.JSONDecodeError as e:
    print(f"JSON import error: {e}")

#error thrown: JSON import error: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
#so error is in the data variable line:
#its the formatting of the json data it should be '' on the outside and "" on the var names

#if nothing prints then no exception is triggered