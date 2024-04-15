"""Heron's Square Root Function."""
def sqrt(num: float) -> float:
    # TODO: implement Heron's square root
    x = 1.0
    for _ in range(10):
        x = (x + num / x) * 0.5
    return x