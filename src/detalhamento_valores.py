from src.config import TIPOS_CONVENIO, TIPOS_ATENDIMENTO

def valor_atendimento(tipo_atendimento):
    valor_atendimento = float(TIPOS_ATENDIMENTO[tipo_atendimento][1])
    return valor_atendimento

def calculo_convenio(tipo_convenio, tipo_atendimento):
    porc_desconto_convenio = float(TIPOS_CONVENIO[tipo_convenio][1])
    preco_base = valor_atendimento(tipo_atendimento)
    valor_descontado_convenio = preco_base * porc_desconto_convenio
    valor_desconto_convenio = preco_base - valor_descontado_convenio
    return porc_desconto_convenio, valor_descontado_convenio, valor_desconto_convenio

def calculo_idade(idade_cliente, valor_desconto_convenio):
    if idade_cliente >= 65:
        porc_desconto_idade = 0.15
    else:
        porc_desconto_idade = 0
    preco_base = valor_desconto_convenio
    valor_descontado_idade = preco_base * porc_desconto_idade
    valor_final = preco_base - valor_descontado_idade
    if valor_final < 50:
        valor_final = 50.00
    return porc_desconto_idade, valor_descontado_idade, valor_final