from .base_qr import BaseQR


class WifiQR(BaseQR):
    def __init__(self, ssid: str, password: str, encryption: str = "WPA"):
        formatted = f"WIFI:T:{encryption};S:{ssid};P:{password};;"
        super().__init__(formatted)

    def get_formatted_data(self) -> str:
        return self.data

    def get_type(self) -> str:
        return "Wi-Fi"
