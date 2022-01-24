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
        rounds = 40000000
        a = int(data[0].split()[-1])
        b = int(data[1].split()[-1])
        fa = 16807
        fb = 48271
        div = 2147483647
        count = 0
        for _ in range(rounds):
            a = (a * fa) % div
            b = (b * fb) % div
            if a % 65536 == b % 65536:
                count += 1
        return count

    def part2(self, data):
        rounds = 5000000
        a = int(data[0].split()[-1])
        b = int(data[1].split()[-1])
        fa = 16807
        fb = 48271
        count = 0
        for ga, gb in zip(self.gen_a(a, fa, True), self.gen_b(b, fb, True)):
            rounds -= 1
            if ga % 65536 == gb % 65536:
                count += 1
            if rounds == 0:
                return count

    def gen_a(self, a, fa, pass_criteria=False):
        while 1:
            a = (a * fa) % 2147483647
            if not pass_criteria or (a % 4 == 0):
                yield a

    def gen_b(self, b, fb, pass_criteria=False):
        while 1:
            b = (b * fb) % 2147483647
            if not pass_criteria or (b % 8 == 0):
                yield b
