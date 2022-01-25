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

    def check_is_raw(self):
        if self.is_raw is False:
            print("please use --raw flag in this puzzle")
            exit()

    def part1(self, data):
        self.check_is_raw()

        w = len(data[0])
        h = len(data)

        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        direction = 2
        collecting = []
        pos = (data[0].index("|"), 0)

        while 1:
            pos = tuple(i + j for i, j in zip(pos, directions[direction]))
            sign = data[pos[1]][pos[0]]

            if sign == " ":
                break
            elif sign != "+":
                if sign in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    collecting += [sign]
            else:
                next_directions = [d for i, d in enumerate(directions) if i not in [direction, (direction + 2) % 4]]
                next_pos = [d for d in [tuple(i + j for i, j in zip(pos, d)) for d in next_directions] if d[0] in range(w) and d[1] in range(h)]
                for p in next_pos:
                    if data[p[1]][p[0]] != " ":
                        direction = directions.index(tuple(i - j for i, j in zip(p, pos)))
                        break
        return "".join(collecting)

    def part2(self, data):
        self.check_is_raw()

        w = len(data[0])
        h = len(data)

        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        direction = 2
        steps = 1
        pos = (data[0].index("|"), 0)

        while 1:
            pos = tuple(i + j for i, j in zip(pos, directions[direction]))
            sign = data[pos[1]][pos[0]]
            steps += 1

            if sign == " ":
                break
            elif sign == "+":
                next_directions = [d for i, d in enumerate(directions) if i not in [direction, (direction + 2) % 4]]
                next_pos = [d for d in [tuple(i + j for i, j in zip(pos, d)) for d in next_directions] if d[0] in range(w) and d[1] in range(h)]
                for p in next_pos:
                    if data[p[1]][p[0]] != " ":
                        direction = directions.index(tuple(i - j for i, j in zip(p, pos)))
                        break
        return steps - 1
