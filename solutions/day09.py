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
        stream = data[0]
        while "!" in stream:
            idx = stream.index("!")
            stream = stream[:idx] + stream[idx + 2 :]

        while "<" in stream:
            idx = stream.index("<")
            idx2 = stream.index(">", idx)
            stream = stream[:idx] + stream[idx2 + 1 :]

        weight = 0
        score = 0

        for c in stream:
            if c == "{":
                weight += 1
                score += weight
            if c == "}":
                weight -= 1

        return score

    def part2(self, data):
        stream = data[0]
        while "!" in stream:
            idx = stream.index("!")
            stream = stream[:idx] + stream[idx + 2 :]

        garbage_length = 0
        while "<" in stream:
            idx = stream.index("<")
            idx2 = stream.index(">", idx)
            stream = stream[:idx] + stream[idx2 + 1 :]
            garbage_length += idx2 - idx - 1

        return garbage_length
