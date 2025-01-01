import json


class FileSystemService:
    @staticmethod
    def parse_json(file_path: str) -> dict:
        with open(file_path, 'r') as file:
            return json.load(file)
