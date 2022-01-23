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
        directions = {
            "n": (0, -2),
            "ne": (1, -1),
            "se": (1, 1),
            "s": (0, 2),
            "sw": (-1, 1),
            "nw": (-1, -1),
        }
        pos = (0, 0)
        for d in data[0].split(","):
            pos = (pos[0] + directions[d][0], pos[1] + directions[d][1])
        step = self.calc_step_by_pos(pos)
        return step

    def part2(self, data):
        directions = {
            "n": (0, -2),
            "ne": (1, -1),
            "se": (1, 1),
            "s": (0, 2),
            "sw": (-1, 1),
            "nw": (-1, -1),
        }
        max_step = 0
        pos = (0, 0)
        for d in data[0].split(","):
            pos = (pos[0] + directions[d][0], pos[1] + directions[d][1])
            step = self.calc_step_by_pos(pos)
            if step > max_step:
                max_step = step
        return max_step

    def calc_step_by_pos(self, pos):
        a, b = pos
        if a * b < 0:
            step = abs(a) + abs(a + b) // 2
        else:
            a, b = abs(a), abs(b)
            step = a + (b - a) // 2

        return step
