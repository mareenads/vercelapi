import json
import os
from typing import List, Optional # Import Optional for type hints if a name is not found

from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse # Optional, FastAPI can jsonify dicts/lists directly

app = FastAPI()

# Construct the absolute path to the JSON file
# Vercel deploys files relative to the project root,
# so we need to go up one level from 'api' directory to find students_data.json
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE_PATH = os.path.join(BASE_DIR, '..', 'q-vercel-python.json')

# Load the student marks data once when the app starts
# This makes subsequent API calls much faster as the file isn't re-read.
student_lookup = {}
try:
    with open(DATA_FILE_PATH, 'r') as f:
        all_students_data = json.load(f)
        # Create a dictionary for quick lookup by name
        student_lookup = {student['name']: student['mark'] for student in all_students_data}
except FileNotFoundError:
    print(f"Error: Data")
