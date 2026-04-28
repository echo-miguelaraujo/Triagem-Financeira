# Triagem Financeira — Clínica Médica

Script de automação para triagem financeira de pacientes no momento do atendimento.

## Problema resolvido

Clínicas médicas de médio porte frequentemente realizam a triagem financeira de forma manual, o que gera erros de cálculo, filas e inconsistências no valor cobrado. Este script automatiza esse processo com base em regras de negócio definidas pela clínica.

## Funcionalidades

- Cadastro do paciente com validação de entradas
- Cálculo automático do valor do atendimento por tipo e convênio
- Desconto adicional para pacientes idosos
- Emissão de comprovante de triagem formatado

## Tecnologias

- Python 3

## Como executar

```bash
python main.py
```

## Regras de negócio

- Consulta: R$ 200 | Exame: R$ 350 | Procedimento: R$ 800
- Desconto por convênio: Unimed 70% | Bradesco/SulAmérica/Amil 60% | Particular 0%
- Pacientes acima de 65 anos recebem 15% adicional de desconto
- Valor mínimo cobrado: R$ 50,00