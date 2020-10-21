# 721. Accounts Merge
# merge accounts with the same email.
# 输出要求：要把名字写上，里面的email sort
# Input:
# accounts =
# [["John", "johnsmith@mail.com", "john00@mail.com"],
# ["John", "johnnybravo@mail.com"],
# ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
# ["Mary", "mary@mail.com"]]
# Output:
# [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
# ["John", "johnnybravo@mail.com"],
# ["Mary", "mary@mail.com"]]

#解题思路：
# Union Find的问题
# 大致上遍历每一个email，如果发现email以前已经存在了，就和上面的account merge
# 具体做法： 模版
# step 1：
# define一个UnionFind Class：
    # 每个account都有一个index，这个class就是用来建立每一个account的parent index
    # find(x)：找到account x的parent index
    # union(x,y): 当accounts x, y有共同的email的时候，让x的parent index = y的parent index
# step 2：
# 2.1 首先建立一个 email：index 的dict (email_accidx)：存每个email的 account index，
# 如果一个email有两个account index x,y，说明他们两个index有同样的parent，
# union(x,y),这样就update x的parent和y一样
# 2.2 建立一个 account_index: email的 dict (parentacc_emails)，这时email可以是多个
# 通过 email_accidx, 知道每一个email所属的account index x，通过find(x), 可以归为同样的parent account
# 2.3 通过parent account index，回到 accounts里，找到名字，sort email

# TC:O(∑a_i log a_i), log a_i 是因为排序， a_i是每个account的length
# SC: O(N)
class UnionFind:
    def __init__(self, n):
        # self.p 存储每一个account index的parent index，初始就是自己
        self.p = [i for i in range(n)]

    def find(self, x):
        # recursively find the parent index for x
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        # make x's parent account index the same as y's parent account index
        self.p[self.find(x)] = self.find(y)
    # def connected(self, p, q):
    #     return self.find(p) == self.find(q)


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        if n == 0:
            return []

        res = []
        uf = UnionFind(n)
        # 2.1. 首先建立一个 email：index 的dict (email_accidx)：存每个email的 account index，
        # # 如果一个email有两个account index x,y，说明他们两个index有同样的parent，
        # # union(x,y),这样就update x的parent和y一样
        email_accidx = {}
        for i in range(n):
            for e in accounts[i][1:]:
                accidx = email_accidx.get(e)
                if accidx == None:
                    email_accidx[e] = i
                else:
                    uf.union(i, accidx)

        # 2.2 建立一个 account_index: email的 dict (parentacc_emails)，这时email可以是多个
        # 通过 email_accidx, 知道每一个email所属的account index x，通过find(x), 可以归为同样的parent account

        parentacc_emails = collections.defaultdict(list)
        for e, accidx in email_accidx.items():
            parent_acc = uf.find(accidx)
            parentacc_emails[parent_acc].append(e)
        # 2.3
        for accidx, e in parentacc_emails.items():
            username = accounts[accidx][0]
            e.sort()
            res.append([username] + e)

        return res



