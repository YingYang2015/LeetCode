# 252 meeting room

# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
# determine if a person could attend all meetings.
#
# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return false.


# 解题思路：
# 就是找是否interval有overlap，如果有的话就return false，如果没有就return true
# step 1：先按照每个interval的start来sort
# step 2：看看end是否大于下一个start

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# TC: O(NlogN): sort的速度
# SC: O(1)

class Solution(object):
    def canAttendMeetings(self, v):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """

        v.sort(key = lambda val: val.start)
        n = len(v)
        for i in range(n-1):
            if v[i+1].start < v[i].end:
                return False
        return True


