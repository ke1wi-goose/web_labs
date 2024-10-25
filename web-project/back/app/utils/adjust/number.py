async def number_adjustment(num: str) -> int:
    return int(num.replace("(", "").replace(")", "").replace("-", ""))