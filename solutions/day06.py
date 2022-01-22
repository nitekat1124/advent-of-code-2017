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
        banks = [*map(int, data[0].split())]
        banks_length = len(banks)
        seen = {tuple(banks)}

        while 1:
            _max = max(banks)
            _max_idx = banks.index(_max)
            amount = banks[_max_idx]

            if amount >= banks_length - 1:
                left_amount = amount % (banks_length - 1)
                dist_amount = amount - left_amount
            else:
                left_amount = 0
                dist_amount = amount

            i = (_max_idx + 1) % banks_length
            while dist_amount > 0:
                if i != _max_idx:
                    banks[i] += 1
                    dist_amount -= 1
                i = (i + 1) % banks_length
            banks[_max_idx] = left_amount

            tbanks = tuple(banks)
            if tbanks in seen:
                return len(seen)
            seen.add(tbanks)

    def part2(self, data):
        banks = [*map(int, data[0].split())]
        banks_length = len(banks)
        seen = [tuple(banks)]

        while 1:
            _max = max(banks)
            _max_idx = banks.index(_max)
            amount = banks[_max_idx]

            if amount >= banks_length - 1:
                left_amount = amount % (banks_length - 1)
                dist_amount = amount - left_amount
            else:
                left_amount = 0
                dist_amount = amount

            i = (_max_idx + 1) % banks_length
            while dist_amount > 0:
                if i != _max_idx:
                    banks[i] += 1
                    dist_amount -= 1
                i = (i + 1) % banks_length
            banks[_max_idx] = left_amount

            tbanks = tuple(banks)
            if tbanks in seen:
                return len(seen) - seen.index(tbanks)
            seen += [tbanks]
