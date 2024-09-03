# eu fiz novas funções e modifiquei algumas funções que foram feitas em grupo na sala, para melhorar o entendimento e a funcionalidade do sistema, Kassio, leia as anotaçoesa
# descobri que é quase impossivel criar um crm valido, pois o crm é um numero unico para cada medico, e nao tem como criar um crm valido
# e tirei as list comprehension para melhor entendimento, pois acho que nao é necessario para esse sistema
# fui eu que fiz a logica do indice, para mostrar o indice do medico, paciente e consulta, para melhor entendimento

# importando a função sleep da biblioteca time
from time import sleep

lista_medicos = [] # lista medicos
lista_pacientes = [] # lista pacientes
lista_consultas = [] # lista consultas

def cpf_valido(cpf):
    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    else:
        # Converte o CPF em uma lista de inteiros
        cpf_int = []
        for digit in cpf:
            cpf_int.append(int(digit))

        # Verifica se todos os dígitos são iguais (CPF inválido)
        if cpf_int == cpf_int[::-1]:
            return False

        # Calcula o primeiro dígito verificador
        soma1 = 0
        for i in range(9):
            soma1 += cpf_int[i] * (10 - i)
        digito1 = (soma1 * 10 % 11) % 10

        # Calcula o segundo dígito verificador
        soma2 = 0
        for i in range(10):
            soma2 += cpf_int[i] * (11 - i)
        digito2 = (soma2 * 10 % 11) % 10

        # Verifica se os dígitos calculados são iguais aos fornecidos
        return digito1 == cpf_int[9] and digito2 == cpf_int[10]

# Função para cadastrar médico 
# feito em grupo na sala  
def cadastrar_medico():
    nome_medico = input("Digite o nome do médico: ")
    especialidade = input("Digite a especialidade: ")
    credencial_medico = input("Digite a credencial do médico: ")
    limite_atendimentos = int(input("Quantos pacientes o médico pode atender por dia: "))

    for medico in lista_medicos:
        if medico['credencial'] == credencial_medico:
            print("Médico já cadastrado no sistema!")
            return

    medico = {
        'nome': nome_medico,
        'credencial': credencial_medico,
        'especialidade': especialidade,
        'limite_atendimento': limite_atendimentos
    }

    lista_medicos.append(medico)
    print("Carregando...")
    sleep(1)
    print("Médico cadastrado com sucesso!")

# Função para listar médicos
# feito em grupo na sala mas modificado por mim, pensando em alguma situaçao que alguem tente listar medicos e suas especialidades
#  para mostrar os medicos disponiveis para um possivel paciente
def listar_medicos():
    print("Carregando médicos...")
    sleep(1)
    if not lista_medicos:
        print("Nenhum medico cadastrado no sistema!")
        return
    
    print('Medicos disponiveis:')
    for medico in lista_medicos:

        ''' O método .index(medico) percorre a lista internamente para encontrar o índice, 
        o que pode ser custoso se a lista for grande. Uma alternativa seria usar um enumerate, que atribui o índice automaticamente:
        o método .index(medico) retorna o índice do médico atual dentro da lista lista_medicos.'''

        indice = lista_medicos.index(medico) + 1 
        print(f" {indice} - Médico: {medico['nome']}, Especialidade: {medico['especialidade']}")



def excluir_medico():
    print("listando medicos...")
    sleep(1)
    try:
        medico_exclude= int(input("Qual indice do medico que deseja excluir:"))
        if medico_exclude < 0 or medico_exclude > len(lista_medicos):
            print("Indice invalido")
            return 
        else:
            lista_medicos.pop(medico_exclude - 1) #.pop é um metodo que remove o item de uma lista dado o seu indice, o indice é passado como argumento para o metodo .pop 
            print("Medico excluido com sucesso!")
    except ValueError:
        print("Digite apenas o indice, não o nome do medico, ou qualquer outra credencial na lista")
    

# Função para cadastrar paciente
# feito em grupo na sala
def cadastrar_paciente():
    nome_paciente = input("Digite o nome do paciente: ")
    cpf_paciente = input("Digite o CPF do paciente (somentes numeros): ")

    # Verifica se o CPF é válido
    if not cpf_valido(cpf_paciente):
        print("CPF inválido, entre com um CPF válido!")
        return
    
    for paciente in lista_pacientes:
        if paciente['cpf_paciente'] == cpf_paciente: #itera em toda a lista de pacientes, olhando especificamente para o valor atribuido a "cpf_paciente" para verificar se o paciente ja esta cadastrado, se o for igual ao cpf_paciente que esta sendo cadastrado, o paciente ja foi cadastrado
            print("Paciente já cadastrado no sistema!")
            return
        
    email_paciente = input("Digite o email do paciente: ")
    paciente = {
        'nome_paciente': nome_paciente, 
        'cpf_paciente': cpf_paciente, 
        'email_paciente': email_paciente
    }
    
    lista_pacientes.append(paciente)
    print("Carregando...")
    sleep(1)
    print("Paciente cadastrado com sucesso!")


# Função para listar pacientes
# feito por mim para alguam situaçao que alguem tente listar os pacientes cadastrados no sistema para saber quem ja esta cadastrado
def listar_pacientes():
    print("Carregando pacientes...")
    sleep(1)
    if not lista_pacientes:
        print("Nenhum paciente cadastrado no sistema!")
        return

    for paciente in lista_pacientes:
        indice = lista_pacientes.index(paciente) + 1 

        print(f"{indice}- Paciente: {paciente['nome_paciente']}, CPF: {paciente['cpf_paciente']}, Email: {paciente['email_paciente']}")




# Função para verificar se o médico atingiu o limite de consultas
# feito em grupo na sala mas modificado por mim, tirando os list compression para melhor entendimento
def verificar_limite_consultas(medico_escolhido, dia_consulta):
    consultas_do_dia = []
    for consulta in lista_consultas:
        if consulta['medico_escolhido'] == medico_escolhido and consulta['dia_consulta'] == dia_consulta: #itera em toda a lista de consultas, olhando especificamente para o valor atribuido a "medico_escolhido" e "dia_consulta" para verificar se o medico ja atingiu o limite de consultas, se o for igual ao medico_escolhido e dia_consulta que esta sendo cadastrado, o medico ja atingiu o limite de consultas
            consultas_do_dia.append(consulta)

    medico = None
    for med in lista_medicos:
        if med['nome'] == medico_escolhido:
            medico = med
            break

    if medico and len(consultas_do_dia) < medico['limite_atendimento']:
        return True
    
    print("Médico atingiu o máximo de consultas!")
    return False

# Função para agendar consulta
# feito em grupo na sala
def agendar_consulta():
    nome_paciente = input("Digite o nome do paciente: ")
    cpf_paciente = input("Digite o CPF do paciente (somentes numeros): ")

    # nova mudança: verificar se o paciente já está cadastrado 
    paciente_cadastrado = False
    for paciente in lista_pacientes:
        if paciente['cpf_paciente'] == cpf_paciente and paciente['nome_paciente'] == nome_paciente:
            paciente_cadastrado = True
            break

    if not paciente_cadastrado:
        cadastrar_paciente()

    print("Carregando médicos disponíveis no consultório...")
    sleep(1)
    listar_medicos()

    medico_escolhido = input("Com que médico deseja se consultar: ")

    medico_existe = False
    for medico in lista_medicos:
        if medico['nome'] == medico_escolhido:
            medico_existe = True
            break

    if not medico_existe:
        print("Médico indisponível no consultório!")
        return

    dia_consulta = input("Qual o dia da consulta: ")

    if not verificar_limite_consultas(medico_escolhido, dia_consulta):
        print("Este médico já atingiu o limite de consultas para o dia!")
        return

    hora_consulta = input("Qual o horário da consulta: ")

    consulta = {
        'nome_paciente': nome_paciente,
        'cpf_paciente': cpf_paciente,
        'medico_escolhido': medico_escolhido,
        'dia_consulta': dia_consulta,
        'hora_consulta': hora_consulta
    }

    lista_consultas.append(consulta)
    print("Consulta agendada com sucesso!")

# Função para listar consultas
# feito por mim
def listar_consultas():
    print("Carregando consultas...")
    sleep(1)
    if not lista_consultas:
        print("Nenhuma consulta agendada!")
        return
    
    for consulta in lista_consultas:
        indice = lista_consultas.index(consulta) + 1 
        print(f"{indice}- Consulta agendada: Paciente {consulta['nome_paciente']} com o médico {consulta['medico_escolhido']} no dia {consulta['dia_consulta']} às {consulta['hora_consulta']}.")




# Funções para excluir vao ser feitas posterirmente, pois ainda nao foi feito em grupo na sala com jp e kassio 

'''vai ser usado essa logica 
o professor mostrou essa logica qnd foi feito em grupo na sala as dois primeiros exercicios de listas, tuplas, dicionarios e conjuntos


isso foi tirado da atividade que ele passou 

# Exemplo de lista
frutas = ['maçã', 'banana', 'laranja']
# frutas.append('uva')  # Adiciona 'uva' ao final da lista # nao vai ser usado
frutas.remove('banana')  # Remove 'banana' da lista # vai ser usado especificamente para excluir um medico, paciente ou consulta da suas respectivas listas
print(frutas)  # Saída: ['maçã', 'laranja', 'uva']
'''