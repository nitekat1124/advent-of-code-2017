from collections import deque
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
        _, root = self.parse_programs(data)
        return root

    def part2(self, data):
        programs, root = self.parse_programs(data)
        self.get_weights(programs, root)

        q = deque([root])
        target_weight = -1
        while q:
            node = q.popleft()
            if len(programs[node][1]) > 0:
                child = {}
                for c in programs[node][1]:
                    w = programs[c][0] + (programs[c][2] if programs[c][2] != -1 else 0)
                    child[c] = w
                if len(set(child.values())) == 1:
                    return target_weight - sum(child.values())
                else:
                    ws = [*set(child.values())]
                    for w in ws:
                        if [*child.values()].count(w) == 1:
                            target = [c[0] for c in child.items() if c[1] == w][0]
                            q.append(target)
                            target_weight = [i for i in ws if i != w][0]

    def parse_programs(self, data):
        programs = {}
        for line in data:
            if " -> " in line:
                parent, children = line.split(" -> ")
                children = children.split(", ")
                parent, weight = parent.split()
                programs[parent] = [int(weight[1:-1]), children, 0]
            else:
                parent, weight = line.split()
                programs[parent] = [int(weight[1:-1]), [], -1]
        nodes = programs.keys()
        children = []
        for node in nodes:
            children.extend(programs[node][1])
        for node in nodes:
            if node not in children:
                return programs, node

    def get_weights(self, programs, node):
        if programs[node][2] == -1:
            return programs[node][0]
        else:
            w = sum(self.get_weights(programs, child) for child in programs[node][1])
            programs[node][2] = w
            return programs[node][0] + w
