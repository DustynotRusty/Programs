class Solution:
    def repeatedNumber(self, A):
        num = len(A)
        lst = []
        a = 0
        b = 0
        f = 0
        xor1 = A[0]
        for i in range(1, num):
            xor1 = xor1 ^ A[i]
        for i in range(1, num + 1):
            xor1 = xor1 ^ i
        bit = xor1 & ~(xor1 - 1)
        for i in range(num):
            if (A[i] & bit) != 0:
                a = a ^ A[i]
            else:
                b = b ^ A[i]
        for i in range(1, num + 1):
            if (i & bit) != 0:
                a = a ^ i
            else:
                b = b ^ i
        for i in range(num):
            if a == A[i]:
                f = 1
                break
        if f == 0:
            lst.append(b)
            lst.append(a)
        else:
            lst.append(a)
            lst.append(b)
        return lst
