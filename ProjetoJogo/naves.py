from colorama import Fore, Style

class NaveModelo:
    def __init__(self, nome, cor, simbolo, perda_energia):
        self.nome = nome
        self.cor = cor
        self.simbolo = simbolo
        self.perda_energia = perda_energia
        self.energia = 100

    def perder_energia(self):
        self.energia = max(0, self.energia - self.perda_energia)
        return self.energia

class NaveExtra(NaveModelo):
    def __init__(self, nome, cor, simbolo, perda_energia, energia_extra):
        super().__init__(nome, cor, simbolo, perda_energia)
        self.energia_extra = energia_extra

    def mostrar_dados(self):
        cor_terminal = self.get_cor_terminal()
        if self.energia == 0:
            print(f"{cor_terminal}{self.nome} ({self.simbolo}) - DESTRUÍDA{Style.RESET_ALL}")
        else:
            print(f"{cor_terminal}{self.nome} ({self.simbolo}) - Energia: {self.energia}{Style.RESET_ALL}")

    def get_cor_terminal(self):
        cores = {
            "RED": Fore.RED,
            "BLUE": Fore.BLUE,
            "GREEN": Fore.GREEN,
            "CYAN": Fore.CYAN,
            "MAGENTA": Fore.MAGENTA,
            "WHITE": Fore.WHITE,
            "YELLOW": Fore.YELLOW
        }
        return cores.get(self.cor.upper(), Fore.WHITE)

    def aplicar_energia_extra(self):
        self.energia = min(100, self.energia + self.energia_extra)
