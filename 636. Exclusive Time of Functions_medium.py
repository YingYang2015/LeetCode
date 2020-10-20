# 636. Exclusive Time of Functions

# 解题思路：用stack
        # 遍历logs，每一次放到stack里，
        # some senarios
        # 1. end
        # 遇到相同的function k, start + end -> res[k] += end-start+1
        # pop both from stack
        # 暂时记录一下上一次end的时间, pre_endts
        # 看下一个是什么，决定 怎么update之前的那个
        # 2. start
        # 看目前是否有保留的pre_endts>0，
        # 如果有：res[k_pre] += start_new-(end+1), pre_endts = -1
        # 如果没有：res[k_pre] += start_new - start_pre
        # push to this stack

# TC: O(N)
# SC: O(N/2), number of elements needed in stack
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:


        if not logs:
            return []

        res = [0] * n

        stack = []
        pre_endts = -1

        for job in logs:
            k, status, ts = job.split(':')
            k, ts = int(k), int(ts)

            if not stack:
                stack.append((k, status, ts))
            else:
                k_pre, status_pre, ts_pre = stack.pop()
                if status == 'start':
                    if pre_endts > 0:
                        res[k_pre] += ts - (pre_endts + 1)
                        pre_endts = -1
                    else:
                        res[k_pre] += ts - ts_pre
                    stack.append((k_pre, status_pre, ts_pre))
                    stack.append((k, status, ts))

                if status == 'end':
                    pre_endts = ts
                    res[k_pre] += ts - ts_pre + 1
                    if stack:
                        k_0, status_0, ts_0 = stack.pop()
                        ts_0 = ts + 1
                        stack.append((k_0, status_0, ts_0))
        return res