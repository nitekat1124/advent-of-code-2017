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
        cur_pos = 0
        skip_size = 0
        jump = 0

        insts = [*map(int, data[0].split(","))]
        nodes = [*range(5 if len(insts) == 4 else 256)]

        for inst in insts:
            nodes[:inst] = nodes[:inst][::-1]

            cur_pos = (inst + skip_size) % len(nodes)
            jump += cur_pos
            nodes = nodes[cur_pos:] + nodes[:cur_pos]

            skip_size += 1

        jump %= len(nodes)
        nodes = nodes[-jump:] + nodes[:-jump]
        return nodes[0] * nodes[1]

    def part2(self, data):
        cur_pos = 0
        skip_size = 0
        jump = 0

        insts = [*map(ord, data[0])] + [17, 31, 73, 47, 23]
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
            dense_hash += [f"{reduce(lambda x, y: x ^ y, parts):02x}"]
        return "".join(dense_hash)
