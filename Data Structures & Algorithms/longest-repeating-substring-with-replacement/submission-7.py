from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = Counter()
        left = 0
        answer = 0
        for right in range(len(s)):
            window[s[right]] += 1   # no .get() needed

            while (max(window.values()) + k) < (right - left + 1):
                window[s[left]] -= 1
                left += 1

            answer = max(answer, right - left + 1)
        return answer