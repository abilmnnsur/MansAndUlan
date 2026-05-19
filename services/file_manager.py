import json
import os
from datetime import datetime

class FileManager:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def save_record(self, user_id: int, qr_type: str, content: str):
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            data = []

        record = {
            "user_id": user_id,
            "qr_type": qr_type,
            "content": content,
            "timestamp": datetime.now().isoformat()
        }
        data.append(record)

        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def get_user_history(self, user_id: int, limit: int = 5) -> list:
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            user_data = [item for item in data if item["user_id"] == user_id]
            return user_data[-limit:]
        except (json.JSONDecodeError, FileNotFoundError):
            return []