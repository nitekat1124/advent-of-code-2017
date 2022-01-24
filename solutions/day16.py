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
        programs = list("abcde") if len(data[0]) == 12 else list("abcdefghijklmnop")

        for i in data[0].split(","):
            if i.startswith("s"):
                programs = programs[-int(i[1:]) :] + programs[: -int(i[1:])]
            elif i.startswith("x"):
                a, b = sorted(map(int, i[1:].split("/")))
                programs[a], programs[b] = programs[b], programs[a]
            elif i.startswith("p"):
                a, b = i[1:].split("/")
                ai, bi = programs.index(a), programs.index(b)
                programs[ai], programs[bi] = programs[bi], programs[ai]
        return "".join(programs)

    def part2(self, data):
        programs = list("abcde") if len(data[0]) == 12 else list("abcdefghijklmnop")
        rounds = 2 if len(data[0]) == 12 else 1000000000
        org = "".join(programs)

        insts = []
        for i in data[0].split(","):
            if i.startswith("s"):
                insts.append(("s", int(i[1:])))
            elif i.startswith("x"):
                a, b = sorted(map(int, i[1:].split("/")))
                insts.append(("x", a, b))
            elif i.startswith("p"):
                a, b = i[1:].split("/")
                insts.append(("p", a, b))

        x = 0
        while x < rounds:
            for i in insts:
                if i[0] == "s":
                    programs = programs[-i[1] :] + programs[: -i[1]]
                elif i[0] == "x":
                    a, b = i[1:]
                    programs[a], programs[b] = programs[b], programs[a]
                elif i[0] == "p":
                    a, b = i[1:]
                    ai, bi = programs.index(a), programs.index(b)
                    programs[ai], programs[bi] = programs[bi], programs[ai]

            # after how many rounds the programs are back in the original state
            if "".join(programs) == org:
                rounds = (rounds) % (x + 1)
                x = 0
            else:
                x += 1

        return "".join(programs)
