# 896. Monotonic Array

# TC: O(N)
# SC: O(1)
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:

        n = len(A)
        if n <= 2:
            return True

        sign = 0
        for i in range(1, n):
            s = A[i] - A[i - 1]
            if s > 0:
                if sign == -1:
                    return False
                else:
                    sign = 1

            elif s < 0:
                if sign == 1:
                    return False
                else:
                    sign = -1

        return True