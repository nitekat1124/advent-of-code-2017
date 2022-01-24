from collections import defaultdict
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
        registers = defaultdict(int)
        sound = []
        i = 0
        while i < len(data):
            inst = data[i].split()
            jmp = 1
            if inst[0] == "snd":
                sound += [registers[inst[1]]]
            elif inst[0] == "set":
                registers[inst[1]] = registers[inst[2]] if inst[2] in registers else int(inst[2])
            elif inst[0] == "add":
                registers[inst[1]] += registers[inst[2]] if inst[2] in registers else int(inst[2])
            elif inst[0] == "mul":
                registers[inst[1]] *= registers[inst[2]] if inst[2] in registers else int(inst[2])
            elif inst[0] == "mod":
                registers[inst[1]] %= registers[inst[2]] if inst[2] in registers else int(inst[2])
            elif inst[0] == "rcv":
                # v = sound[-1] if len(sound) else 0
                if registers[inst[1]] != 0:
                    # sound.pop()
                    return sound[-1]
            elif inst[0] == "jgz":
                if registers[inst[1]] > 0:
                    jmp = registers[inst[2]] if inst[2] in registers else int(inst[2])
            i += jmp
        return sound[-1]

    def part2(self, data):
        self.q = [[], []]
        self.i = [0, 0]
        self.r = [defaultdict(int), defaultdict(int)]
        self.r[0]["p"] = 0
        self.r[1]["p"] = 1
        self.s = [0, 0]

        while 1:
            r = self.run(data)
            if r is not None and len(self.q[0]) == 0 and len(self.q[1]) == 0:
                return r

    def run(self, data):
        jumps = []
        for pid in [0, 1]:
            jmp = 0
            if self.i[pid] < len(data):
                inst = data[self.i[pid]].split()
                jmp = 1
                if inst[0] == "snd":
                    v = self.r[pid][inst[1]] if inst[1] in self.r[pid] else int(inst[1])
                    self.q[1 - pid] += [v]
                    self.s[pid] += 1
                elif inst[0] == "set":
                    self.r[pid][inst[1]] = self.r[pid][inst[2]] if inst[2] in self.r[pid] else int(inst[2])
                elif inst[0] == "add":
                    self.r[pid][inst[1]] += self.r[pid][inst[2]] if inst[2] in self.r[pid] else int(inst[2])
                elif inst[0] == "mul":
                    self.r[pid][inst[1]] *= self.r[pid][inst[2]] if inst[2] in self.r[pid] else int(inst[2])
                elif inst[0] == "mod":
                    self.r[pid][inst[1]] %= self.r[pid][inst[2]] if inst[2] in self.r[pid] else int(inst[2])
                elif inst[0] == "rcv":
                    if len(self.q[pid]) > 0:
                        self.r[pid][inst[1]] = self.q[pid].pop(0)
                    else:
                        jmp = 0
                elif inst[0] == "jgz":
                    t = self.r[pid][inst[1]] if inst[1] in self.r[pid] else int(inst[1])
                    if t > 0:
                        jmp = self.r[pid][inst[2]] if inst[2] in self.r[pid] else int(inst[2])
                self.i[pid] += jmp
            jumps += [jmp]
        if jumps == [0, 0]:
            return self.s[1]
        return None
