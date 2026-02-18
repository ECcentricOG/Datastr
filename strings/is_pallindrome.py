def is_pallindrome(s:str) -> bool:
    n = len(s)
    left = n - 1
    right = 0

    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        else:
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

    return True
