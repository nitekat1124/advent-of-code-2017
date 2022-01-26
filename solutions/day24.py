from collections import deque
from copy import deepcopy
from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def solve(self, part_num: int):
        self.test_runner(part_num)

        func = getattr(self, f"part{part_num}")
        result = func(self.data)
        return result

    def test_runner(self, part_num):
        test_inputs = self.get_test_input()
        test_results = self.get_test_result(part_num)
        test_counter = 1

        func = getattr(self, f"part{part_num}")
        for i, r in zip(test_inputs, test_results):
            if len(r):
                if (tr := str(func(i))) == r[0]:
                    print(f"test {test_counter} passed")
                else:
                    print(f"your result: {tr}")
                    print(f"test answer: {r[0]}")
                    print(f"test {test_counter} NOT passed")
            test_counter += 1
        print()

    def part1(self, data):
        components = [tuple(sorted(map(int, line.split("/")))) for line in data]
        q = deque([[i] for i in components if i[0] == 0])
        bridges = [i for i in q]

        while q:
            b = q.pop()
            t = b[-1][1]
            cs = [c for c in components if t in c]
            for c in cs:
                if c[1] == t:
                    c = (c[1], c[0])
                if c not in b and (c[1], c[0]) not in b:
                    b2 = deepcopy(b) + [c]
                    q.appendleft(b2)
                    bridges += [b2]

        return max([sum(sum(c) for c in b) for b in bridges])

    def part2(self, data):
        components = [tuple(sorted(map(int, line.split("/")))) for line in data]
        q = deque([[i] for i in components if i[0] == 0])
        bridges = [i for i in q]

        while q:
            b = q.pop()
            t = b[-1][1]
            cs = [c for c in components if t in c]
            for c in cs:
                if c[1] == t:
                    c = (c[1], c[0])
                if c not in b and (c[1], c[0]) not in b:
                    b2 = deepcopy(b) + [c]
                    q.appendleft(b2)
                    bridges += [b2]
        max_leng = max([len(b) for b in bridges])
        return max([sum(sum(c) for c in b) for b in [b for b in bridges if len(b) == max_leng]])
