def sanitize_input(text: str) -> str:
    """Simple input sanitizer to prevent prompt injection and strip unwanted chars."""
    
    # Remove problematic chars, excessive whitespace, etc.
    sanitized = text.replace("\x00", "").strip()
    return sanitized
