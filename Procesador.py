import Alu

class Procesador:
    def __init__(self, uc, pc, mar, mbr, ir, acumulador, alu):
        self.uc = uc
        self.pc = pc
        self.mar = mar
        self.mbr = mbr
        self.ir = ir
        self.acumulador = acumulador
        self.alu = Alu() 

    
    
