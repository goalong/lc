#
# [165] Compare Version Numbers
#
# https://leetcode.com/problems/compare-version-numbers/description/
#
# algorithms
# Medium (20.72%)
# Total Accepted:    97K
# Total Submissions: 468.2K
# Testcase Example:  '"1"\n"0"'
#
# Compare two version numbers version1 and version2.
# If version1 > version2 return 1, if version1 < version2 return -1, otherwise
# return 0.
# 
# You may assume that the version strings are non-empty and contain only digits
# and the . character.
# The . character does not represent a decimal point and is used to separate
# number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it
# is the fifth second-level revision of the second first-level revision.
# 
# Here is an example of version numbers ordering:
# 0.1 < 1.1 < 1.2 < 13.37
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # 1 star.
        v1, v2 = version1.split('.'), version2.split('.')
        n1, n2 = len(v1), len(v2)
        i = 0
        while i < max(n1, n2):
            first = int(v1[i]) if i < n1 else 0
            second = int(v2[i]) if i < n2 else 0
            if first > second:
                return 1
            elif first < second:
                return -1
            i += 1
        return 0
