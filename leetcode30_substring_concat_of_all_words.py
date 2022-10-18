from typing import List
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []
        l = len(words[0])
        c = Counter(words)
        for i in range(l):
            w = c.copy()
            wc = len(words)
            start, end = i, i
            while end <= len(s) - l:
                word = s[end:end+l]
                if wc == 0:
                    w[s[start:start+l]] += 1
                    wc += 1
                    result.append(start)
                    start = start+l
                elif word in w and w[word] > 0:
                    w[word] -= 1
                    wc -= 1
                    end = end+l
                elif word in w:
                    while w[word] == 0:
                        nw = s[start:start+l]
                        w[nw] += 1
                        wc += 1
                        start = start+l
                    w[word] -= 1
                    wc -= 1
                    end = end+l
                else:
                    w = c.copy()
                    wc = len(words)
                    start, end = end + l, end+l
            if wc == 0:
                result.append(start)
        return result


s = Solution()
print(s.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]
                      ))
