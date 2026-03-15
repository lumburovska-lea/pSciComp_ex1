"""
For each person that is taking the class pSciComp,
we write a personalized greeting to a file in greetings.txt.

we run it by uv run --env-file .env scripts/drafts/say_hello.py
"""

import os
from types import SimpleNamespace

from exohw.greetings import make_greetings
from exohw.io import load_json_file

# Read data directory locations from the environment, with defaults.
# Pillar: Environment
input_dir = os.environ.get("INPUT_DIR", "data/raw")
output_dir = os.environ.get("OUTPUT_DIR", "data/final")

# Load configuration: target course name and data key mappings.
# Pillar: Configuration
_cfg = load_json_file('config/config.json')
course = _cfg['course']
keys = SimpleNamespace(**_cfg['keys'])

# Load the input dataset from a dedicated data file.
# Pillar: Data
people = load_json_file(f'{input_dir}/people.json')

# Build a greeting for each person enrolled in the target course.
# Pillar: Code, Data, Configuration
greetings = make_greetings(people, course, keys)

# Write all collected greetings to an output file on disk.
# Pillars: Code, Environment
with open(f'{output_dir}/greeting.txt', 'w') as f:
    f.writelines(greetings)
