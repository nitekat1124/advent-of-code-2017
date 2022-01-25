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
        grid = defaultdict(lambda: ".")
        for y, line in enumerate(data):
            for x, c in enumerate(line):
                grid[(x, y)] = c

        pos = (len(data[0]) // 2, len(data) // 2)
        d = 0
        ds = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        infection = 0

        for _ in range(10000):
            c = grid[pos]
            if c == "#":
                d = (d + 1) % 4
                grid[pos] = "."
                pos = tuple(i + j for i, j in zip(pos, ds[d]))
            else:
                d = (d + 3) % 4
                grid[pos] = "#"
                pos = tuple(i + j for i, j in zip(pos, ds[d]))
                infection += 1

        return infection

    def part2(self, data):
        grid = defaultdict(lambda: ".")
        for y, line in enumerate(data):
            for x, c in enumerate(line):
                grid[(x, y)] = c

        pos = (len(data[0]) // 2, len(data) // 2)
        d = 0
        ds = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        infection = 0
        for _ in range(10000000):
            c = grid[pos]
            if c == ".":
                d = (d + 3) % 4
                grid[pos] = "W"
                pos = tuple(i + j for i, j in zip(pos, ds[d]))
            elif c == "W":
                infection += 1
                grid[pos] = "#"
                pos = tuple(i + j for i, j in zip(pos, ds[d]))
            elif c == "#":
                d = (d + 1) % 4
                grid[pos] = "F"
                pos = tuple(i + j for i, j in zip(pos, ds[d]))
            elif c == "F":
                d = (d + 2) % 4
                grid[pos] = "."
                pos = tuple(i + j for i, j in zip(pos, ds[d]))
        return infection
