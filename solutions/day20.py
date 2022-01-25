import re
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
        particles = []
        for i, line in enumerate(data):
            p, v, a = re.findall(r"\<.*?\>", line)
            particles += [
                {
                    "p": [*map(int, p[1:-1].split(","))],
                    "v": [*map(int, v[1:-1].split(","))],
                    "a": [*map(int, a[1:-1].split(","))],
                    "idx": i,
                }
            ]

        particles = sorted(particles, key=lambda p: (sum(abs(i) for i in p["a"]), sum(abs(i) for i in p["v"]), sum(abs(i) for i in p["p"])))
        return particles[0]["idx"]

    def part2(self, data):
        particles = []
        for idx, line in enumerate(data):
            p, v, a = re.findall(r"\<.*?\>", line)
            particles += [
                {
                    "p": [*map(int, p[1:-1].split(","))],
                    "v": [*map(int, v[1:-1].split(","))],
                    "a": [*map(int, a[1:-1].split(","))],
                    "idx": idx,
                }
            ]
        for _ in range(1000):
            collisions = set()
            points = {}

            for idx, p in enumerate(particles):
                particles[idx]["v"] = [i + j for i, j in zip(p["v"], p["a"])]
                particles[idx]["p"] = [i + j for i, j in zip(p["p"], p["v"])]
                if tuple(particles[idx]["p"]) in points:
                    collisions.add(idx)
                    collisions.add(points[tuple(particles[idx]["p"])])
                else:
                    points[tuple(particles[idx]["p"])] = idx

            collisions = sorted(list(collisions))[::-1]
            for idx in collisions:
                del particles[idx]

        return len(particles)
