def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s_count = {}
    t_count = {}
    for s_char in s:
        # looping through each character in s
        if s_char in s_count:
            s_count[s_char] += 1
        else:
            s_count[s_char] = 1
    for t_char in t:
        if t_char in t_count:
            t_count[t_char] += 1
        else:
            t_count[t_char] = 1
    return t_count == s_count
