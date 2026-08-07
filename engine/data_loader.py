"""
Data Loader
"""

import json
from pathlib import Path


class DataLoader:

    def __init__(self, base_path: Path):

        self.base_path = base_path

    def load_json(self, filename: str):

        path = self.base_path / filename

        with open(path, "r", encoding="utf-8") as f:

            return json.load(f)

    def save_json(self, filename: str, data):

        path = self.base_path / filename

        with open(path, "w", encoding="utf-8") as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )

    def topics(self):

        return self.load_json("topics.json")

    def statistics(self):

        return self.load_json("statistics.json")

    def prompts(self):

        return self.load_json("prompts.json")
