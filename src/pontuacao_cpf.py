
def adicionar_pontuacao_cpf(cpf_cliente):
    cpf = cpf_cliente
    cpf_formatado = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
    return cpf_formatado