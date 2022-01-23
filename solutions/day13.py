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
        layers = {}
        for line in data:
            a, b = line.split(": ")
            layers[int(a)] = int(b)

        severity = sum(i * layers[i] for i in layers if i % (2 * layers[i] - 2) == 0)
        return severity

    def part2(self, data):
        layers = {}
        for line in data:
            a, b = line.split(": ")
            layers[int(a)] = int(b)

        delay = 0
        while 1:
            # if any((i + delay) % (2 * layers[i] - 2) == 0 for i in layers):
            #     delay += 1
            for i in layers:
                if (i + delay) % (2 * layers[i] - 2) == 0:
                    delay += 1
                    break
            else:
                return delay
