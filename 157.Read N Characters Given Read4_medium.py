# 157	Read N Characters Given Read4

# 题目大意: 用read4函数读取n个字符。
# Time Complexity: O(N)
# Space Complexity: O(1) Not counting results


"""
The read4 API is already defined for you.
    @param buf, a list of characters
    @return an integer
    def read4(buf):
# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

# Input: file = "abc", n = 4
# Output: 3
#
# Input: file = "abcde", n = 5
# Output: 5

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        buf4 = [' ']*4
        EOF = False
        num_read = 0 #已经read了多少
        while num_read < n and not EOF:
            cur_num = read4(buf4)
            delta = min(cur_num, n-num_read)
            buf[num_read:num_read+delta] = buf4[:delta]
            num_read += delta
            if cur_num<4:
                EOF = True

        return num_read