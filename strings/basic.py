def remove_outer_paranthesis(s:str) -> str:
    count = 0
    ans = ""
    for c in s:
        if c == "(":
            count += 1
        elif c == ")":
            count -= 1

        if count > 1:
            ans = ans + c

    return ans
