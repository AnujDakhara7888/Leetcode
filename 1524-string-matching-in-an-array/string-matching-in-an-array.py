class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i]==words[j]:
                    continue
                if words[i] in words[j] and words[i] not in ans:
                    ans.append(words[i])

        return ans

        