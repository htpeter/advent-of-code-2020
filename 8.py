print("day 8")

ACTIONS = ["acc", "jpm", "nop"]

class BootLoaderSimulation:
    def __init__(self, instruction_string): 
        # get instructions and values
        self.instructions, self.signed_integers = (
            self.process_file_text(instruction_string)
        )

        print(self.instructions)
        print(self.signed_integers)

    def accumulate(self, cleaned_integer):
        self.accumulator += cleaned_integer

    def jump(self, cleaned_integer):
        self.position += cleaned_integer  

    def run_instructions(self):
        # initialize operation variables
        self.position = 0
        self.accumulator = 0

        # terminate when the final step is run and we aggregate 1 final time
        while self.position != len(self.instructions):
            cmd = self.instructions[self.position]
            s_int = self.signed_integers[self.position]
            c_int = self.clean_signed_integer(s_int)
            print(f"running {cmd} {c_int}")
            print(self.position)
            if cmd == "acc":
                self.accumulate(c_int)
                self.position += 1

            elif cmd == "jmp":
                self.jump(c_int)

            elif cmd == "nop":
                self.position += 1

    def clean_signed_integer(self, signed_integer):
        if "+" in signed_integer:
            return int(signed_integer.replace("+", ""))
        elif "-" in signed_integer:
            return (int(signed_integer.replace("-", "")) * -1)
        else:
            raise Exception("Integer unsigned")

    def process_file_text(self, file_text):
        items = file_text.split("\n")
        instructions = [i.split(" ")[0] for i in items]
        signed_integers = [i.split(" ")[-1] for i in items]

        return instructions, signed_integers

    def __repr__(self):
        return self.instructions, self.signed_integers

if __name__ == "__main__":
    example_instruction_set = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
    loader = BootLoaderSimulation(example_instruction_set)
    loader.run_instructions()