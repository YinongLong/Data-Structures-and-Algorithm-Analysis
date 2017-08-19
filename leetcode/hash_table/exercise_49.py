# -*- coding: utf-8 -*-
from __future__ import print_function

class Solution(object):

    def _update_records(self, records, word, idx):
        chars = list(word)
        chars.sort()
        identity = ''.join(chars)
        container = records.get(identity, [])
        container.append(idx)
        records[identity] = container

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        records = dict()
        for idx, word in enumerate(strs):
            self._update_records(records, word, idx)
        result = []
        for idx_list in records.values():
            result.append([])
            for idx in idx_list:
                result[-1].append(strs[idx])
        return result


strs = ['eat', 'ate', 'tea', 'tan', 'nat', 'bat']
s = Solution()
print(s.groupAnagrams(strs))
