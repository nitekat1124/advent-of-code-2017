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
        insts = [int(i) for i in data]
        steps = 0
        i = 0

        while i in range(len(insts)):
            inst = insts[i]
            insts[i] += 1
            i = i + inst
            steps += 1
        return steps

    def part2(self, data):
        insts = [int(i) for i in data]
        steps = 0
        i = 0

        while i in range(len(insts)):
            inst = insts[i]
            if inst > 2:
                insts[i] -= 1
            else:
                insts[i] += 1
            i = i + inst
            steps += 1
        return steps
