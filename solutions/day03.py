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
        n = int(data[0])

        side_length = int(n ** 0.5)
        if side_length % 2 == 0:
            side_length += 1

        max_i = side_length ** 2

        hl = side_length // 2
        max_i -= hl
        while abs(max_i - n) > hl:
            max_i -= hl * 2

        return abs(max_i - n) + hl

    def part2(self, data):
        squares = {
            1: ((0, 0), 1),
        }

        n = int(data[0])

        while max(i[1] for i in squares.values()) <= n:
            side_length = int(len(squares) ** 0.5) + 2
            r0 = len(squares) + 1
            r1 = side_length ** 2

            directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
            start = tuple([*map(sum, zip(squares[r0 - 1][0], (1, 1)))])

            for i in range(4):
                for j in range(side_length - 1):
                    start = (start[0] + directions[i][0], start[1] + directions[i][1])
                    squares[r0 + (side_length - 1) * i + j] = (start, 0)

            neighbors = [(0, -1), (-1, 0), (0, 1), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
            for i in range(r0, r1 + 1):
                r = 0
                for k in neighbors:
                    p = tuple([*map(sum, zip(squares[i][0], k))])
                    r += sum(v[1] for v in squares.values() if v[0] == p)
                squares[i] = (squares[i][0], r)

        return min(v[1] for v in squares.values() if v[1] > n)
