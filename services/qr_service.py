import requests
import asyncio
from models.base_qr import BaseQR

class QRService:
    API_URL = "https://api.qrcode-monkey.com//qr/custom"

    @classmethod
    async def generate(cls, qr_obj: BaseQR) -> bytes:
        payload = {
            "data": qr_obj.get_formatted_data(),
            "config": {"body": "square", "eye": "frame0", "eyeBall": "ball0"},
            "size": 500,
            "download": False,
            "file": "png"
        }

        def fetch():
            response = requests.post(cls.API_URL, json=payload)
            response.raise_for_status()
            return response.content

        return await asyncio.to_thread(fetch)