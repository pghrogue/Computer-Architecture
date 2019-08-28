LDI = 0b10000010
PRN = 0b01000111
HLT = 0b00000001

class Dispatch:

    def __init__(self, cpu):
        self.cpu = cpu
        self.dispatchtable = {}
        self.dispatchtable[LDI] = self.handle_ldi
        self.dispatchtable[PRN] = self.handle_prn
        self.dispatchtable[HLT] = self.handle_hlt

        
    def handle_ldi(self, operand_a, operand_b):
        cpu.reg[operand_a] = operand_b

    def handle_prn(self, operand_a, operand_b):
        print(cpu.reg[operand_a])

    def handle_hlt(self):
        cpu.halt = True


    def run(self, IR):
        operand_a = cpu.ram_read(cpu.pc + 1)
        operand_b = cpu.ram_read(cpu.pc + 2)

        self.dispatchtable[IR](operand_a, operand_b)