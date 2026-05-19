from .base_qr import BaseQR


class ContactQR(BaseQR):
    def __init__(self, name: str, phone: str):
        formatted = f"BEGIN:VCARD\nVERSION:3.0\nFN:{name}\nTEL:{phone}\nEND:VCARD"
        super().__init__(formatted)

    def get_formatted_data(self) -> str:
        return self.data

    def get_type(self) -> str:
        return "Contact"
