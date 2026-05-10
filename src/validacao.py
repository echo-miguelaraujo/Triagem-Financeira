from validate_docbr import CPF
from src.config import TIPOS_ATENDIMENTO, TIPOS_CONVENIO

def validar_cpf(cpf_cliente):
    cpf = CPF()

    while cpf.validate(cpf_cliente) == False:
        print('CPF inválido, tente novamente.')
        cpf_cliente = input("Digite o CPF do cliente: ")
    return cpf_cliente

def validar_atendimento(tipo_atendimento):
    while tipo_atendimento not in TIPOS_ATENDIMENTO:
        print('Tipo de atendimento inválido, tente novamente.')
        tipo_atendimento = input("Digite o tipo de atendimento (1 - Consulta, 2 - Exame, 3 - Procedimento): ")
    return tipo_atendimento

def validar_convenio(tipo_convenio):
    while tipo_convenio not in TIPOS_CONVENIO:
        print('Convênio inválido, tente novamente.')
        tipo_convenio = input("Digite o tipo de convênio (1 - Unimed, 2 - Bradesco Saúde, 3 - SulAmérica, 4 - Amil, 5 - Particular): ")
    return tipo_convenio