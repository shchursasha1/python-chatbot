def count_tokens(text: str) -> int:
    """Estimate token count: 1 token ≈ 4 chars in English."""
    # Add 3 to round up partial tokens
    return max(1, (len(text) + 3) // 4)