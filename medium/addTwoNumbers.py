class Solution:
    def addTwoNumbers(self, l1, l2):
        rv_lst1 = int("".join([str(i) for i in (list(reversed(l1)))]))
        rv_lst2 = int("".join([str(n) for n in (list(reversed(l2)))]))
        return int("".join([t for t in (str(rv_lst1+rv_lst2)[::-1])]))
print(Solution.addTwoNumbers(Solution,[2,4,3],[5,6,4]))