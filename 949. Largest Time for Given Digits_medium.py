# 949. Largest Time for Given Digits
#
# Input: A = [1,2,3,4]
# Output: "23:41"


# 解题思路：
# 因为只有四个，所以可以permutate所有的combination
# 前两个construct hour，后两个construct minute
# 删除不valid的，然后选最大的

# TC: O(1): Since the length of the input array is fixed, it would take the same constant time to generate its permutations, regardless the content of the array. Therefore, the time complexity to generate the permutations would be O(1)
# SC: O(1): time_list 的长度
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:

        if not arr:
            return ''

        # four index h1, h2, m1, m2
        # index total = 0+1+2+3 = 6
        time_list = {}
        for h1 in range(4):
            for h2 in range(4):
                for m1 in range(4):
                    # 注意：这一步保证index不相同
                    if h1 == h2 or h1 == m1 or h2 == m1:
                        continue

                    m2 = 6 - m1 - h1 - h2

                    hh = arr[h1] * 10 + arr[h2]
                    mm = arr[m1] * 10 + arr[m2]
                    if (hh >= 0 and hh < 24) and (mm >= 0 and mm < 60):
                        time = hh * 60 + mm

                        # 注意：这里处理只有一个digit的情况
                        shh = '0' + str(hh) if len(str(hh)) == 1 else str(hh)
                        smm = '0' + str(mm) if len(str(mm)) == 1 else str(mm)

                        time_list[time] = shh + ':' + smm

        if not time_list:
            return ''
        max_time = time_list[max(time_list.keys())]
        return max_time
