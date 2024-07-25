class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)
    

class Conta ():
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        """
        Retorna uma string legível da instância da conta.
        
        Returns:
            str: Uma string legível que representa a conta.
        """
        return f"Titular: {self.titular} ---> Saldo Atual (R$): {self.saldo:.2f}"

    def depositar(self, valor):
        print(f"Saldo Inicial (R$): {self.saldo:.2f}")
        self.saldo = self.saldo + valor
        print(f"Depósito (R$): {valor:.2f}")
        print(self)
        return self # O retorno 'self' permite o encadeamento de métodos.
        
    
    def sacar(self, valor):
        print(f"Saldo inicial (R$): {self.saldo:.2f}")
        if self.saldo >=  valor:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f}")
            print(self)
        else:
            print(f"Tentativa de saque de R$ {valor:.2f}")
            print("Operação não realizada. Saldo insuficiente")
            print(self)
        return self