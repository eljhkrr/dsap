def disjoint1(A, B, C):
    """Return True if there is no element common to all 3 lists."""
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False
    return True
