from src.pontuacao_cpf import adicionar_pontuacao_cpf
from src.validacao import validar_cpf
from src.config import TIPOS_ATENDIMENTO, TIPOS_CONVENIO


nome_cliente = input("Digite o nome do cliente: ").title()
cpf_cliente = input("Digite o CPF do cliente: ")

validar_cpf(cpf_cliente)

idade_cliente = int(input("Digite a idade do cliente: "))

tipo_atendimento = input("Digite o tipo de atendimento (1 - Consulta, 2 - Exame, 3 - Procedimento): ")
if tipo_atendimento not in TIPOS_ATENDIMENTO:
    print('ERRO, Tento Novamente.')
else:
    pass

tipo_convenio = input("Digite o tipo de convênio (1 - Unimed, 2 - Bradesco Saúde, 3 - SulAmérica, 4 - Amil, 5 - Particular): ")
if tipo_convenio not in TIPOS_CONVENIO:
    print('ERRO, Tento Novamente.')
else:
    pass


cpf = adicionar_pontuacao_cpf(cpf_cliente)

print(f'''
Nome do cliente: {nome_cliente}
CPF do cliente: {cpf}
Idade do cliente: {idade_cliente}
Tipo de atendimento: {tipo_atendimento} - {TIPOS_ATENDIMENTO[tipo_atendimento]}
Tipo de convênio: {tipo_convenio} - {TIPOS_CONVENIO[tipo_convenio]}
''')