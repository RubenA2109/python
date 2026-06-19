def saudacao():
    print("Olá a todos!")
    
def soma(x,y):
    return x+y

  
def conta(x,y,op):
    if op == '+':
        return x+y
    elif op == '-': 
        return x-y
    elif op == '*': 
        return x*y
    elif op == '/': 
        return x/y
    else: return 'Operador inválido'

print(conta(3,9,'+'))
print(conta(3,9,'-'))
print(conta(3,9,'*'))
print(conta(3,9,'/'))
print(conta(3,9,';'))

def somar(*nums):
    soma = sum([n for n in nums])
    return soma
print(somar(5,3,11,19,23,54,67,12))