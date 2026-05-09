from validate_docbr import CPF

def validar_cpf(cpf_cliente):
    cpf = CPF()
    if cpf.validate(cpf_cliente):
        print('CPF Válido.')
    else:
        print('CPF Inválido, tente novamente')

