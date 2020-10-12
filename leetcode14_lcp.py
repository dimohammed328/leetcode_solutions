def longestCommonPrefix(strs):
    minLen = min(len(s) for s in strs)
    ret = ""
    idx = 0
    run = True
    while run and idx < minLen:
        c = strs[0][idx]
        for s in strs:
            if s[0] != c:
                run = False
        if run:
            ret += c
        idx += 1
    return ret

print(longestCommonPrefix(["flower","flow","flight"]))