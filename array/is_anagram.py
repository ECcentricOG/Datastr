def is_anagram(s: str, t:str) -> bool:
    if len(s) != len(t):
        return False
    
    d = {}

    for c in s:
        d[c] = d.get(c, 0) + 1

    for c in t:
        if c not in d:
            return False
        if d[c] == 1:
            d.pop(c)
        else:
            d[c] -= 1

    if len(d) > 0:
        return False
    return True
