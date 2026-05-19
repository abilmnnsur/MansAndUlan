from .base_qr import BaseQR


class TextQR(BaseQR):
    def get_formatted_data(self) -> str:
        return self.data

    def get_type(self) -> str:
        return "Text"
