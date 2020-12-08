print("day 8")

class BootLoaderSimulation:
    """
    Usage:

        example_instruction_set = '''nop +0
        acc +1
        jmp +4
        acc +3
        jmp -3
        acc -99
        acc +1
        jmp -4
        acc +6
        '''
        loader = BootLoaderSimulation(example_instruction_set)
        loader.run_instructions()
    """
    def __init__(self, instruction_string): 
        """
        Parse instructions.
        """
        # get instructions and values
        self.instructions, self.signed_integers = (
            self.process_file_text(instruction_string)
        )

    def accumulate(self, cleaned_integer):
        """
        acc instruction function
        """
        self.accumulator += cleaned_integer

    def jump(self, cleaned_integer):
        """
        jmp acc instruction function
        """
        self.position += cleaned_integer  

    def run_instructions(self):
        """
        executes the instructions provided in instruction set
        """
        # initialize operation variables
        self.position = 0
        self.accumulator = 0
        self.already_run_calculations = []

        # will terminate when the final step is run or if we repeat an instruction
        while self.position != len(self.instructions):
            # get current instructions for this position in instruction set, clean signed integers from file
            cmd = self.instructions[self.position]
            s_int = self.signed_integers[self.position]
            c_int = self.clean_signed_integer(s_int)
            
            # hash the command and see if it was already run
            command_hash = hash(f"{self.position}-{cmd}-{c_int}")
            if command_hash in self.already_run_calculations:
                raise Exception(f"Repeat execution of step {self.position}-{cmd}-{c_int}, accumulator is {self.accumulator}")
            else:
                self.already_run_calculations.append(command_hash)

            # run the commands using their respective functions and signed integer values
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
        """
        Cleans the instruction set.
        
        THEORETICAL TODO THAT ILL NEVER DO: Clean out empty lines and tabs that may exist with a python string input.
        """
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
