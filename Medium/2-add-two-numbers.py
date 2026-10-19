/**
 * LeetCode #2: Add Two Numbers
 * Difficulty: Medium
 * Language: Python
 * Date: 2026-10-19T08:25:11.753Z
 */

class Solution:
    def lengthOfLongestSubstring(self, s):
        seen = set()
        left = 0
        answer = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            answer = max(answer, right - left + 1)

        return answer