from typing import List


class WordFilter:

    def __init__(self, words: List[str]):
        self.pre, self.suf = TrieNode(), TrieNode()
        self.words = words
        for i, word in enumerate(words):
            self.pre.insert(word, i)
            self.suf.insert(word[::-1], i)

    def f(self, pref: str, suff: str) -> int:
        matches = self.pre.search(pref).intersection(
            self.suf.search(suff[::-1]))
        if len(matches) == 0:
            return -1
        return sorted([self.words[i] for i in matches], key=lambda x: len(x))[-1]


class TrieNode:
    def __init__(self):
        self.children = {}
        self.idxs = set()

    def insert(self, word, idx):
        head = self
        self.idxs.add(idx)
        for c in word:
            if c not in head.children:
                head.children[c] = TrieNode()
            head = head.children[c]
            head.idxs.add(idx)

    def search(self, word):
        head = self
        for c in word:
            if c not in head.children:
                return set()
            head = head.children[c]
        return head.idxs


obj = WordFilter(["apple"])
param_1 = obj.f("a", "e")
