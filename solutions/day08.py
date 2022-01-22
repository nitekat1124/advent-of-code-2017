from collections import defaultdict
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
        register = defaultdict(int)
        for inst in data:
            target, op, val, _, *cond = inst.split()

            check = False
            if cond[1] == ">":
                check = register[cond[0]] > int(cond[2])
            elif cond[1] == "<":
                check = register[cond[0]] < int(cond[2])
            elif cond[1] == ">=":
                check = register[cond[0]] >= int(cond[2])
            elif cond[1] == "<=":
                check = register[cond[0]] <= int(cond[2])
            elif cond[1] == "==":
                check = register[cond[0]] == int(cond[2])
            elif cond[1] == "!=":
                check = register[cond[0]] != int(cond[2])

            if check:
                register[target] += [-1, 1][op == "inc"] * int(val)
        return max(register.values())

    def part2(self, data):
        _max = 0
        register = defaultdict(int)
        for inst in data:
            target, op, val, _, *cond = inst.split()

            check = False
            if cond[1] == ">":
                check = register[cond[0]] > int(cond[2])
            elif cond[1] == "<":
                check = register[cond[0]] < int(cond[2])
            elif cond[1] == ">=":
                check = register[cond[0]] >= int(cond[2])
            elif cond[1] == "<=":
                check = register[cond[0]] <= int(cond[2])
            elif cond[1] == "==":
                check = register[cond[0]] == int(cond[2])
            elif cond[1] == "!=":
                check = register[cond[0]] != int(cond[2])

            if check:
                register[target] += [-1, 1][op == "inc"] * int(val)

            _max = max(_max, *register.values())
        return _max
