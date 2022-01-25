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
        self.rules = self.parse_rules(data)
        iterations = 2 if len(self.rules) == 2 else 5
        grid = [
            [".", "#", "."],
            [".", ".", "#"],
            ["#", "#", "#"],
        ]

        for _ in range(iterations):
            n = len(grid)
            if n % 2 == 0:
                n = n // 2
                s = 2
            else:
                n = n // 3
                s = 3

            blocks = [[r[j * s : (j + 1) * s] for r in grid[i * s : (i + 1) * s]] for i in range(n) for j in range(n)]
            grid = self.build_grid([self.apply_rules(b) for b in blocks])

        return sum([row.count("#") for row in grid])

    def part2(self, data):
        self.rules = self.parse_rules(data)
        iterations = 18
        grid = [
            [".", "#", "."],
            [".", ".", "#"],
            ["#", "#", "#"],
        ]

        for _ in range(iterations):
            n = len(grid)
            if n % 2 == 0:
                n = n // 2
                s = 2
            else:
                n = n // 3
                s = 3

            blocks = [[r[j * s : (j + 1) * s] for r in grid[i * s : (i + 1) * s]] for i in range(n) for j in range(n)]
            grid = self.build_grid([self.apply_rules(b) for b in blocks])

        return sum([row.count("#") for row in grid])

    def parse_rules(self, data):
        rules = {}
        for line in data:
            key, val = line.split(" => ")
            rules[key] = val
        return rules

    def apply_rules(self, b):
        block_keys = self.build_block_keys(b)
        for k in block_keys:
            if k in self.rules:
                return [list(i) for i in self.rules[k].split("/")]

    def build_block_keys(self, b):
        keys = []
        for t in range(8):
            b = [[x[i] for x in b][::-1] for i in range(len(b))]
            keys += ["/".join(["".join(i) for i in b])]
            if t == 3:
                b = [i[::-1] for i in b]
        return keys

    def build_grid(self, blocks):
        s = int(len(blocks) ** 0.5)
        grid = [list("".join(["".join(b[j]) for b in blocks[i * s : (i + 1) * s]])) for i in range(s) for j in range(len(blocks[0]))]
        return grid
