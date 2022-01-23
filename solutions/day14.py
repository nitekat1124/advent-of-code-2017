from collections import deque
from functools import reduce
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
        key = data[0]
        nums = [*range(128)]
        return sum(self.knot_hash(f"{key}-{n}").count("1") for n in nums)

    def part2(self, data):
        key = data[0]
        nums = [*range(128)]
        self.grid = [list(self.knot_hash(f"{key}-{n}")) for n in nums]

        regions = 0
        for y in range(128):
            for x in range(128):
                if self.grid[y][x] == "1":
                    self.mark_region(x, y)
                    regions += 1

        return regions

    # minor modify from day 10
    def knot_hash(self, key):
        cur_pos = 0
        skip_size = 0
        jump = 0

        insts = [*map(ord, key)] + [17, 31, 73, 47, 23]
        nodes = [*range(256)]

        for _ in range(64):
            for inst in insts:
                nodes[:inst] = nodes[:inst][::-1]

                cur_pos = (inst + skip_size) % len(nodes)
                jump += cur_pos
                nodes = nodes[cur_pos:] + nodes[:cur_pos]

                skip_size += 1

        jump %= len(nodes)
        nodes = nodes[-jump:] + nodes[:-jump]

        dense_hash = []
        for _ in range(16):
            parts = nodes[:16]
            nodes = nodes[16:]
            dense_hash += [f"{reduce(lambda x, y: x ^ y, parts):08b}"]
        return "".join(dense_hash)

    def mark_region(self, x, y):
        q = deque([(x, y)])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            x1, y1 = q.popleft()
            if self.grid[y1][x1] == "1":
                self.grid[y1][x1] = "#"
                for dx, dy in directions:
                    x2, y2 = x1 + dx, y1 + dy
                    if (x2) in range(128) and (y2) in range(128) and self.grid[y2][x2] == "1":
                        q.append((x2, y2))
