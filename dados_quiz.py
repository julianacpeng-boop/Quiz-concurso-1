# -*- coding: utf-8 -*-
"""15 questões autorais sobre direitos trabalhistas, com fontes legais."""

CAPA_SEGUNDOS = 2

QUIZZES = {
    'Fracionamento das férias': [{
        'pergunta': 'Com a concordância do empregado, as férias podem ser divididas em até três períodos. Qual é a duração mínima de um deles?',
        'alternativas': ['14 dias corridos', '10 dias corridos', '7 dias corridos'],
        'correta': 0,
        'explicacao': 'A CLT permite dividir as férias em até três períodos, desde que haja concordância do empregado. Um período deve ter pelo menos 14 dias corridos e os demais, no mínimo, 5 dias corridos cada.',
        'fonte': 'Fonte: CLT, art. 134, § 1º (questão autoral)'
    }],
    'Venda de parte das férias': [{
        'pergunta': 'Ao pedir o abono pecuniário, qual parte do período de férias o empregado pode converter em dinheiro?',
        'alternativas': ['Até um terço', 'Metade', 'Todo o período'],
        'correta': 0,
        'explicacao': 'O empregado pode converter em abono pecuniário até um terço do período de férias a que tem direito. O pedido deve ser feito no prazo previsto na CLT.',
        'fonte': 'Fonte: CLT, art. 143 (questão autoral)'
    }],
    'Licença-maternidade': [{
        'pergunta': 'Qual é a duração geral da licença-maternidade prevista na CLT?',
        'alternativas': ['120 dias', '90 dias', '180 dias em todos os casos'],
        'correta': 0,
        'explicacao': 'A regra geral assegura 120 dias de licença-maternidade sem prejuízo do emprego e do salário. A prorrogação pode existir em situações previstas em lei, como no Programa Empresa Cidadã.',
        'fonte': 'Fonte: Constituição Federal, art. 7º, XVIII; CLT, art. 392 (questão autoral)'
    }],
    'Licença-paternidade': [{
        'pergunta': 'A partir de 2027, qual será a duração prevista para a licença-paternidade na primeira etapa da ampliação legal?',
        'alternativas': ['10 dias', '15 dias', '20 dias'],
        'correta': 0,
        'explicacao': 'A Lei nº 15.371/2026 prevê ampliação gradual: 10 dias em 2027 e 15 dias em 2028. A etapa de 20 dias está prevista para 2029, condicionada aos critérios fiscais definidos na lei.',
        'fonte': 'Fonte: Lei nº 15.371/2026, regras de vigência e ampliação (questão autoral)'
    }],
    'Estabilidade da gestante': [{
        'pergunta': 'Até quando vai, em regra, a estabilidade provisória da trabalhadora gestante?',
        'alternativas': ['Cinco meses após o parto', 'Um mês após o parto', 'Até o início da licença-maternidade'],
        'correta': 0,
        'explicacao': 'A proteção contra dispensa arbitrária ou sem justa causa começa com a confirmação da gravidez e vai até cinco meses após o parto, conforme o ADCT.',
        'fonte': 'Fonte: ADCT, art. 10, II, alínea b; CLT, art. 391-A (questão autoral)'
    }],
    'Pausas para amamentação': [{
        'pergunta': 'Durante a jornada, quantos descansos especiais a trabalhadora tem para amamentar o filho até os seis meses de idade?',
        'alternativas': ['Dois descansos de meia hora', 'Um descanso de uma hora', 'Três descansos de vinte minutos'],
        'correta': 0,
        'explicacao': 'A CLT prevê dois descansos especiais de meia hora cada um durante a jornada, até que a criança complete seis meses. A regra também abrange filho adotivo.',
        'fonte': 'Fonte: CLT, art. 396 (questão autoral)'
    }],
    'Consultas durante a gravidez': [{
        'pergunta': 'Sem desconto salarial, a gestante pode se afastar do trabalho pelo tempo necessário para quantas consultas médicas, no mínimo?',
        'alternativas': ['Seis consultas', 'Duas consultas', 'Quatro consultas'],
        'correta': 0,
        'explicacao': 'A CLT garante dispensa pelo tempo necessário para a realização de, no mínimo, seis consultas médicas e exames complementares durante a gravidez.',
        'fonte': 'Fonte: CLT, art. 392, § 4º, inciso II (questão autoral)'
    }],
    'Adoção e licença-maternidade': [{
        'pergunta': 'A empregada que adota ou obtém guarda judicial para fins de adoção tem direito a qual período de licença?',
        'alternativas': ['120 dias', '60 dias', '30 dias'],
        'correta': 0,
        'explicacao': 'A CLT estende à empregada que adota ou obtém guarda judicial para adoção o direito à licença-maternidade de 120 dias, sem prejuízo do emprego e do salário.',
        'fonte': 'Fonte: CLT, arts. 392 e 392-A (questão autoral)'
    }],
    'Prazo do décimo terceiro': [{
        'pergunta': 'Qual é o prazo legal para o pagamento da segunda parcela do décimo terceiro salário?',
        'alternativas': ['Até 20 de dezembro', 'Até 30 de novembro', 'Até 31 de janeiro'],
        'correta': 0,
        'explicacao': 'A segunda parcela deve ser paga até 20 de dezembro. A primeira parcela pode ser paga entre fevereiro e novembro, observadas as regras legais.',
        'fonte': 'Fonte: Lei nº 4.749/1965, art. 1º (questão autoral)'
    }],
    'Adicional de hora extra': [{
        'pergunta': 'Qual é o adicional mínimo constitucional para o serviço extraordinário em relação à hora normal?',
        'alternativas': ['50%', '25%', '10%'],
        'correta': 0,
        'explicacao': 'A Constituição determina que a remuneração do serviço extraordinário seja pelo menos 50% superior à da hora normal. Acordos ou normas podem prever percentual maior.',
        'fonte': 'Fonte: Constituição Federal, art. 7º, XVI; CLT, art. 59, § 1º (questão autoral)'
    }],
    'Trabalho noturno urbano': [{
        'pergunta': 'No trabalho urbano, qual é o período noturno definido pela CLT?',
        'alternativas': ['Das 22h às 5h', 'Das 20h às 4h', 'Das 21h às 6h'],
        'correta': 0,
        'explicacao': 'Para o trabalho urbano, a CLT considera noturno o trabalho realizado entre 22h de um dia e 5h do dia seguinte. Há regras próprias para atividades rurais.',
        'fonte': 'Fonte: CLT, art. 73, § 2º (questão autoral)'
    }],
    'Intervalo para refeição': [{
        'pergunta': 'Em uma jornada contínua superior a seis horas, qual é o intervalo mínimo geral para repouso e alimentação, observadas as regras de negociação coletiva?',
        'alternativas': ['Uma hora', 'Quinze minutos', 'Duas horas obrigatórias'],
        'correta': 0,
        'explicacao': 'A regra geral da CLT prevê intervalo mínimo de uma hora para jornadas superiores a seis horas. A negociação coletiva pode reduzi-lo, respeitado o limite legal mínimo de 30 minutos.',
        'fonte': 'Fonte: CLT, arts. 71 e 611-A, inciso III (questão autoral)'
    }],
    'Depósito do FGTS': [{
        'pergunta': 'Para o empregado comum regido pela CLT, qual percentual da remuneração mensal o empregador deposita normalmente no FGTS?',
        'alternativas': ['8%', '5%', '11%'],
        'correta': 0,
        'explicacao': 'A regra geral é o depósito mensal de 8% da remuneração na conta vinculada do trabalhador. Esse depósito é obrigação do empregador, não um desconto do salário do empregado.',
        'fonte': 'Fonte: Lei nº 8.036/1990, art. 15 (questão autoral)'
    }],
    'Falta justificada para doar sangue': [{
        'pergunta': 'Comprovada a doação voluntária de sangue, quantos dias de ausência ao trabalho são justificados pela CLT a cada período de 12 meses?',
        'alternativas': ['Um dia', 'Dois dias', 'Cinco dias'],
        'correta': 0,
        'explicacao': 'A CLT permite a ausência por um dia, a cada 12 meses de trabalho, em caso de doação voluntária de sangue devidamente comprovada.',
        'fonte': 'Fonte: CLT, art. 473, inciso IV (questão autoral)'
    }],
    'Descanso semanal remunerado': [{
        'pergunta': 'Qual é a duração mínima do repouso semanal remunerado previsto na Constituição?',
        'alternativas': ['24 horas consecutivas', '12 horas consecutivas', '36 horas consecutivas'],
        'correta': 0,
        'explicacao': 'A Constituição assegura repouso semanal remunerado de, no mínimo, 24 horas consecutivas, preferencialmente aos domingos.',
        'fonte': 'Fonte: Constituição Federal, art. 7º, inciso XV; Lei nº 605/1949 (questão autoral)'
    }],
}

LEGENDAS = {
    tema: f'Direitos trabalhistas: responda e confira a explicação.\n#JuhQuiz #DireitosTrabalhistas #Trabalho #CLT'
    for tema in QUIZZES
}
