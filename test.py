def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # ss = list(itertools.permutations(range(1,n+1),n))[k-1]
        # return "".join(str(s) for s in ss)
        return self.get_permutation_from_list([i for i in range(1, n + 1)], k)

    def get_permutation_from_list(self, sorted_list_n, k):
        if k < 1 or k > factorial(len(sorted_list_n)):
            if len(sorted_list_n) == 1:
                return str(sorted_list_n[0])
            else:
                return ""
        length = len(sorted_list_n)
        fact = factorial(length - 1)
        # First digit
        shang = (k - 1) // fact
        s = sorted_list_n[shang]
        sorted_list_n.remove(s)
        if len(sorted_list_n):
            return str(s) + self.get_permutation_from_list(sorted_list_n, k - shang * fact)
        else:
            return str(s)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            n = int(line);
            line = next(lines)
            k = int(line);
            ret = Solution().getPermutation(n, k)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()