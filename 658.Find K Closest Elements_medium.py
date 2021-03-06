# 658. Find K Closest Elements

# Given a sorted array arr, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

# Solution
# Step 1: use a binary search algorithm to find the index of the target value,
# or the index just slightly bigger than the target value
# Step 2: calcuate the distance of right and left of the target value,
# and put the index of the smaller value into the index stack
# keep doing it until the index stack reach the length of k

# Note: if there is a equal value, keep putting the left one until left distance is bigger

# TC: O(logN + k)
# SC: O(k) : generate the request sublist

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        if len(arr) == 0:
            return []

        if k == 0:
            return [x]

        def binary_search(arr, x):
            s = 0
            e = len(arr) - 1
            while s <= e:
                mid = (s + e) // 2
                if x == arr[mid]:
                    return mid
                elif x > arr[mid]:
                    s = mid + 1
                elif x < arr[mid]:
                    e = mid - 1
            return s

        ind = binary_search(arr, x)

        def get_dis(arr, pos):
            if pos < 0 or pos >= len(arr):
                return float('Inf')
            else:
                return abs(arr[pos] - x)

        left, right = ind - 1, ind
        k_idx = []
        while (left >= 0 or right < len(arr)) and len(k_idx) < k:
            dl, dr = get_dis(arr, left), get_dis(arr, right)
            if dl < dr:
                k_idx.append(left)
                left -= 1
            elif dl > dr:
                k_idx.append(right)
                right += 1
            elif dl == dr:
                while dl == dr and k > len(k_idx):
                    k_idx.append(left)
                    left -= 1
                    dl = get_dis(arr, left)

        k_idx.sort()
        return [arr[i] for i in k_idx]

