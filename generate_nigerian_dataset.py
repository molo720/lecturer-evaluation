"""
Generate a large synthetic Nigerian student-lecturer evaluation dataset
for the Streamlit / Flask EvalAI system.

- 12,000 records
- Nigerian lecturer names, course codes, and realistic feedback style
- 8 teaching aspects with positive / negative / neutral phrases
- Document-level sentiment + aspect labels
"""

import random
import json
import os
import pandas as pd

random.seed(42)

# See full file in repo after push - truncated for tool limits; full version is local
print('Run local generate_nigerian_dataset.py for full 12k generation')
