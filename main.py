from src.pontuacao_cpf import adicionar_pontuacao_cpf
from src.validacao import validar_cpf, validar_atendimento, validar_convenio
from src.config import TIPOS_ATENDIMENTO, TIPOS_CONVENIO
from src.detalhamento_valores import calculo_convenio, valor_atendimento, calculo_idade


nome_cliente = input("Digite o nome do cliente: ").title()
cpf_cliente = input("Digite o CPF do cliente: ")
cpf_cliente = validar_cpf(cpf_cliente)
cpf = adicionar_pontuacao_cpf(cpf_cliente)

idade_cliente = int(input("Digite a idade do cliente: "))

tipo_atendimento = input("Digite o tipo de atendimento (1 - Consulta, 2 - Exame, 3 - Procedimento): ")
tipo_atendimento = validar_atendimento(tipo_atendimento)

tipo_convenio = input("Digite o tipo de convênio (1 - Unimed, 2 - Bradesco Saúde, 3 - SulAmérica, 4 - Amil, 5 - Particular): ")
tipo_convenio = validar_convenio(tipo_convenio)

valor_atendimento = valor_atendimento(tipo_atendimento)
porc_convenio, valor_descontado_convenio, valor_desconto_convenio = calculo_convenio(tipo_convenio, tipo_atendimento)
porc_idade, valor_descontado_idade, valor_final = calculo_idade(idade_cliente, valor_desconto_convenio)

print(f'''
Nome do cliente: {nome_cliente}
CPF do cliente: {cpf}
Idade do cliente: {idade_cliente}

Tipo de atendimento: {TIPOS_ATENDIMENTO[tipo_atendimento][0]}
Tipo de convênio: {TIPOS_CONVENIO[tipo_convenio][0]}

Valor total do atendimento: R${valor_atendimento:.2f}''')
if tipo_convenio == '5':
    print('Sem desconto de convênio.')
else:    
    print(f'''
Desconto do convênio: R${valor_descontado_convenio:.2f} ({porc_convenio * 100:.0f}%)
    Valor com desconto: R${valor_desconto_convenio:.2f}''')
if idade_cliente >= 65:
    print(f'''
Desconto por idade: R${valor_descontado_idade:.2f} ({porc_idade * 100:.0f}%)
    Valor com desconto: R${valor_final:.2f}''')
else:
    print('Sem desconto por idade.')

print(f'Total a pagar: R${valor_final}')