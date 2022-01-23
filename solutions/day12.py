import networkx as nx
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
        g = nx.DiGraph()

        nodes = []
        for line in data:
            a, b = line.split(" <-> ")
            b = b.split(", ")
            nodes += [a]
            for bb in b:
                g.add_edge(a, bb)

        return sum(1 for node in nodes if nx.has_path(g, "0", node))

    def part2(self, data):
        g = nx.DiGraph()

        nodes = []
        for line in data:
            a, b = line.split(" <-> ")
            b = b.split(", ")
            nodes += [a]
            for bb in b:
                g.add_edge(a, bb)

        groups = 0
        while len(nodes) > 0:
            base = nodes[0]
            connected = [base]
            for node in nodes:
                if nx.has_path(g, base, node):
                    connected += [node]
            for node in set(connected):
                nodes.remove(node)
            groups += 1
        return groups
