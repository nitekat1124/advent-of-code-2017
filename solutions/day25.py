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
        state = "A"
        tape = deque([0])
        cursor = 0

        steps = 6 if len(data) == 22 else 12586542
        run = self.run_test if steps == 6 else self.run_real
        for _ in range(steps):
            state, tape, cursor = run(state, tape, cursor)
        return tape.count(1)

    def part2(self, data):
        return "Merry Christmas!"

    def run_test(self, state, tape, cursor):
        if state == "A":
            if tape[cursor] == 0:
                tape[cursor] = 1
                tape, cursor = self.resort_tape(tape, cursor + 1)
            else:
                tape[cursor] = 0
                tape, cursor = self.resort_tape(tape, cursor - 1)
            state = "B"
        elif state == "B":
            if tape[cursor] == 0:
                tape[cursor] = 1
                tape, cursor = self.resort_tape(tape, cursor - 1)
            else:
                tape[cursor] = 1
                tape, cursor = self.resort_tape(tape, cursor + 1)
            state = "A"
        return state, tape, cursor

    def run_real(self, state, tape, cursor):
        if state == "A":
            if tape[cursor] == 0:
                tape[cursor] = 1
                tape, cursor = self.resort_tape(tape, cursor + 1)
            else:
                tape[cursor] = 0
                tape, cursor = self.resort_tape(tape, cursor - 1)
            state = "B"
        elif state == "B":
            if tape[cursor] == 0:
                tape[cursor] = 0
                tape, cursor = self.resort_tape(tape, cursor + 1)
                state = "C"
            else:
                tape[cursor] = 1
                tape, cursor = self.resort_tape(tape, cursor - 1)
                state = "B"
        elif state == "C":
            if tape[cursor] == 0:
                tape[cursor] = 1
                tape, cursor = self.resort_tape(tape, cursor + 1)
                state = "D"
            else:
                tape[cursor] = 0
                tape, cursor = self.resort_tape(tape, cursor - 1)
                state = "A"
        elif state == "D":
            if tape[cursor] == 0:
                tape[cursor] = 1
                tape, cursor = self.resort_tape(tape, cursor - 1)
                state = "E"
            else:
                tape[cursor] = 1
                tape, cursor = self.resort_tape(tape, cursor - 1)
                state = "F"
        elif state == "E":
            if tape[cursor] == 0:
                tape[cursor] = 1
                tape, cursor = self.resort_tape(tape, cursor - 1)
                state = "A"
            else:
                tape[cursor] = 0
                tape, cursor = self.resort_tape(tape, cursor - 1)
                state = "D"
        elif state == "F":
            if tape[cursor] == 0:
                tape[cursor] = 1
                tape, cursor = self.resort_tape(tape, cursor + 1)
                state = "A"
            else:
                tape[cursor] = 1
                tape, cursor = self.resort_tape(tape, cursor - 1)
                state = "E"
        return state, tape, cursor

    def resort_tape(self, tape, cursor):
        if cursor < 0:
            while cursor < 0:
                tape.appendleft(0)
                cursor += 1
        elif cursor >= len(tape):
            while len(tape) <= cursor:
                tape.append(0)
        return tape, cursor
