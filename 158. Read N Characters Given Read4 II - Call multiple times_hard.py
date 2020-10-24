# 158	Read N Characters Given Read4 II, call multiple times

# 题目大意: 用read4函数读取每次可以读取<=4个字符。这次和157不一样，可以调用多次read(buf, n)
# n means每次调用读几个，这一次depends on上一次
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

# Example 1:
#
# File file("abc");
# Solution sol;
# // Assume buf is allocated and guaranteed to have enough space for storing all characters from the file.
# sol.read(buf, 1); // After calling your read method, buf should contain "a". We read a total of 1 character from the file, so return 1.
# sol.read(buf, 2); // Now buf should contain "bc". We read a total of 2 characters from the file, so return 2.
# sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.
# Example 2:
#
# File file("abc");
# Solution sol;
# sol.read(buf, 4); // After calling your read method, buf should contain "abc". We read a total of 3 characters from the file, so return 3.
# sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.

# 解题思路
# 通过状态值： cur_used知道当前读到哪里了，如果已经读完了现在读了的四个cur_read, 就要新读了

class Solution:
    def __init__(self):
        self.cur_read = 0 # 当前read4 read了几个
        self.cur_used = 0 # 当前已经用了几个，是一个状态值
        self.buf4 = ['']*4
        self.EOF = False # file是否结束了，这个现在放在init里，方便可以每次read的时候可以看到状态

    def read(self, buf, n):
        num_read = 0 # 这一次已经读了多少个了，需要到 n，如果够的话，不够的话就是num_read了

        while num_read < n and not self.EOF:
            if self.cur_read == self.cur_used:
                self.cur_read = read4(self.buf4)
                # 重新开始，因为新读的里面还没有用过
                self.cur_used = 0
                if self.cur_read == 0:
                    self.EOF = True
            else:
                # 这一次还有多少可以读，够了的话就结束了，不够的话循环回去读新的
                delta = min(self.cur_read - self.cur_used, n-num_read)
                buf[num_read:num_read+delta] = self.buf4[self.cur_used:self.cur_used+delta]
                self.cur_used += delta
                num_read += delta

        return num_read