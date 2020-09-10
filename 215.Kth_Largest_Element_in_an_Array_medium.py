# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Example 1:
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5


# Solution 1: Sort
# Solution 2: minheap
# Solution 3: Divide and Conquer

# solution 1: sort
# TC: O(NlogN)
# SC: O(N)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Method 1: sort
        nums.sort(key = lambda x: x)
        n = len(nums)
        return nums[n-k]

# Solution 2: minheap
# TC: O(NlogK)
# SC: O(K)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Method 2: min heap
        # step 1: create a min heap with size k with the first k elements in nums
        h = nums[0:k]
        heapq.heapify(h)
        # step 2: loop i from k to n-1
        # if num[i] <= topnode, continue
        # if num[i] > top node, replace with the top node
        for i in range(k, len(nums)):
            top_node = heapq.heappop(h)
            if nums[i] <= top_node:
                heapq.heappush(h, top_node)
            else:
                heapq.heappush(h, nums[i])

        # step 3:

        return heapq.heappop(h)



# Solution 3: divide and conquer
# TC: O(N)
# SC: O(N)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Solution 3: divide and conqure
        # transform to find the n-k smallest value

        # step 1: define a function randomly pick a pivor in nums
        # arrange all smaller ones to the left, and bigger ones to the right

        # step 2: compare k with pivot_index,
        # if pivot_index == k：return nums[k]
        # if pivot_index > k：go to the left, sort the left
        # if pivot_index < k: go to the right, sort the right
        # until pivot_index == k, return nums[k]

        def sort_nums(nums, left, right):
            pivot_index = right
            pivot = nums[pivot_index]
            store_index = left

            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            nums[store_index], nums[pivot_index] = nums[pivot_index], nums[store_index]

            return nums, store_index

        n = len(nums)
        k_smallest = n - k

        left = 0
        right = n - 1
        pivot_index = 0
        # print(k_smallest)
        nums, pivot_index = sort_nums(nums, left, right)
        while pivot_index != k_smallest:
            nums, pivot_index = sort_nums(nums, left, right)
            # print(nums, pivot_index)
            if pivot_index == k_smallest:
                return nums[pivot_index]
            elif pivot_index > k_smallest:
                right = pivot_index - 1
            elif pivot_index < k_smallest:
                left = pivot_index + 1

        return nums[pivot_index]