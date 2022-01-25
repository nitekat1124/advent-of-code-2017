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
        registers = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0}

        i = 0
        mul_counter = 0
        while i < len(data):
            inst = data[i].split()
            jmp = 1
            if inst[0] == "set":
                registers[inst[1]] = registers[inst[2]] if inst[2] in registers else int(inst[2])
            elif inst[0] == "sub":
                registers[inst[1]] -= registers[inst[2]] if inst[2] in registers else int(inst[2])
            elif inst[0] == "mul":
                mul_counter += 1
                registers[inst[1]] *= registers[inst[2]] if inst[2] in registers else int(inst[2])
            elif inst[0] == "jnz":
                t = registers[inst[1]] if inst[1] in registers else int(inst[1])
                if t != 0:
                    jmp = registers[inst[2]] if inst[2] in registers else int(inst[2])
            i += jmp
        return mul_counter

    """
    def part2_for_anaylysed(self, data):
        # registers = {"a": 1, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0}
        registers = {"a": 1, "b": 124900, "c": 124900, "d": 124899, "e": 107900, "f": 1, "g": 0, "h": 0}

        # i = 0
        i = 19
        while i < len(data):
            print(i, data[i])
            inst = data[i].split()
            jmp = 1
            if inst[0] == "set":
                registers[inst[1]] = registers[inst[2]] if inst[2] in registers else int(inst[2])
            elif inst[0] == "sub":
                registers[inst[1]] -= registers[inst[2]] if inst[2] in registers else int(inst[2])
            elif inst[0] == "mul":
                registers[inst[1]] *= registers[inst[2]] if inst[2] in registers else int(inst[2])
            elif inst[0] == "jnz":
                t = registers[inst[1]] if inst[1] in registers else int(inst[1])
                if t != 0:
                    jmp = registers[inst[2]] if inst[2] in registers else int(inst[2])
            i += jmp
            print(registers)
        return registers["h"]
    """

    def part2(self, data):
        h = 0
        for x in range(107900, 124900 + 1, 17):
            for i in range(2, x):
                if x % i == 0:
                    h += 1
                    break
        print(h)
