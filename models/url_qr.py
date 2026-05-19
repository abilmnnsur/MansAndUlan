from .base_qr import BaseQR


class URLQR(BaseQR):
    def get_formatted_data(self) -> str:
        if not self.data.startswith("http"):
            return f"https://{self.data}"
        return self.data

    def get_type(self) -> str:
        return "URL"
