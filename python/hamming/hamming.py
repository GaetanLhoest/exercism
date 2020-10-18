def distance(strand_a: str, strand_b: str) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError("The two stands don't have the same size")
    return sum(s[0] != s[1] for s in zip(strand_a, strand_b))
