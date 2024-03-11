import datetime

def calcular_idade(data_nascimento):
    hoje = datetime.date.today()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade

def calcular_signo(data_nascimento):
    dia = data_nascimento.day
    mes = data_nascimento.month
    
    if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return "Aquário"
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        return "Peixes"
    elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return "Áries"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return "Touro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "Gêmeos"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return "Câncer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "Leão"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "Virgem"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "Escorpião"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "Sagitário"
    else:
        return "Capricórnio"

def main():
    nome = input("Digite seu nome: ")
    sobrenome = input("Digite seu sobrenome: ")
    data_str = input("Digite sua data de nascimento (DD/MM/AAAA): ")
    
    try:
        data_nascimento = datetime.datetime.strptime(data_str, "%d/%m/%Y").date()
        idade = calcular_idade(data_nascimento)
        signo = calcular_signo(data_nascimento)
        
        print(f"Olá {nome} {sobrenome}, você tem {idade} anos, e seu signo é {signo}.")
    except ValueError:
        print("Data de nascimento inválida. Certifique-se de digitar no formato correto (DD/MM/AAAA).")

if __name__ == "__main__":
    main()
