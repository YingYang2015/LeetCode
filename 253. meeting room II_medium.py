# 253. meeting room II

# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],…] (si < ei),
# find the minimum number of conference rooms required.
#
# Example 1:
#
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# Example 2:
#
# Input: [[7,10],[2,4]]
# Output: 1

# 解题思路：
# step 1：先按照每个interval的start来sort
# step 2：利用heap, h存目前的meeting room要结束的时间，最小的在最上面
# step 3：每一次看下一个meeting(interval)的时候，
#   start time如果 >heap.pop的话，就pop，然后把end time放到heap里
#   start time如果 <heap.pop的话，不pop，把end time放到heap里
# 最后count heap的大小，就是所需的meeting room的数量

# TC：O(NlogN): sort的complexity， otherwise，O(N)
# SC: O(N): 最多N个在heap里

import heapq
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key = lambda x: x.start)
        h = []
        heapq.push(h, intervals[0].end)

        n = len(intervals)

        for i in range(1,n):
            min_end_time = h.pop()
            if intervals[i].start >= min_end_time:
                heapq.heappush(h, intervals[i].end)
            else:
                heapq.heappush(h, min_end_time)
                heapq.heappush(h, intervals[i].end)

        return len(h)


