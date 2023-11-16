class Alu:
    def __init__(self, codop, op1, op2, rs):
        self.codop = codop # Codop
        self.op1 = op1  # Operando 1
        self.op2 = op2  # Operando 2
        self.rs = rs    # Resultado

    def realizar_operacion(self, operador, num1, num2):
        return self.operacion_aritmetica(num1, num2, operador)
    
    
    def operacion_aritmetica(self, num1, num2, operador):
        if operador == '0000':
            return num1 + num2
        elif operador == '0001':
            return num1 - num2
        elif operador == '0010':
            return num1 * num2
        elif operador == '0100':
            if num2 != 0:
                return num1 / num2
            else:
                return "¡Error! División por cero."
        else:
            return "Operador no válido."