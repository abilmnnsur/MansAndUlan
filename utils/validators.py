def validate_input(text: str) -> bool:
    if not text or len(text.strip()) == 0:
        return False
    return True


def validate_split_input(text: str) -> bool:
    parts = text.split(",")
    return len(parts) == 2 and all(part.strip() for part in parts)
