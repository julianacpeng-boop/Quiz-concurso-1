# -*- coding: utf-8 -*-
"""15 questões autorais de Matemática em estilo de concurso."""

CAPA_SEGUNDOS = 2

QUIZZES = {
    'Média e mediana': [{
        'pergunta': 'Em cinco plantões, uma equipe registrou 12, 14, 15, 17 e 22 atendimentos. Qual é a soma da média com a mediana?',
        'alternativas': ['31', '30', '32'],
        'correta': 0,
        'explicacao': 'A média é (12 + 14 + 15 + 17 + 22) ÷ 5 = 16. A mediana é o valor central da sequência ordenada: 15. A soma é 31.',
        'fonte': 'Fonte: CBMPA, Cebraspe 2023, questão 16 (questão autoral inspirada no conteúdo)'
    }],
    'Progressão aritmética': [{
        'pergunta': 'Uma sequência começa em 5 e aumenta 3 unidades a cada termo. Qual é a soma dos 12 primeiros termos?',
        'alternativas': ['258', '246', '270'],
        'correta': 0,
        'explicacao': 'O 12º termo é 5 + 11 × 3 = 38. A soma é 12 × (5 + 38) ÷ 2 = 258.',
        'fonte': 'Fonte: CBMPA, Cebraspe 2023, questão 17 (questão autoral inspirada no conteúdo)'
    }],
    'Área de figuras': [{
        'pergunta': 'Uma fachada tem formato de retângulo de 12 m por 8 m, com um triângulo de base 12 m e altura 4 m no topo. Qual é a área total?',
        'alternativas': ['120 m²', '112 m²', '144 m²'],
        'correta': 0,
        'explicacao': 'O retângulo tem área 12 × 8 = 96 m². O triângulo tem área (12 × 4) ÷ 2 = 24 m². Total: 120 m².',
        'fonte': 'Fonte: CBMPA, Cebraspe 2023, questão 18 (questão autoral inspirada no conteúdo)'
    }],
    'Volume': [{
        'pergunta': 'Uma sala retangular mede 5 m de comprimento, 4 m de largura e 3 m de altura. Qual é o volume interno?',
        'alternativas': ['60 m³', '12 m³', '45 m³'],
        'correta': 0,
        'explicacao': 'O volume do paralelepípedo é comprimento × largura × altura: 5 × 4 × 3 = 60 m³.',
        'fonte': 'Fonte: CBMPA, Cebraspe 2023, questão 19 (questão autoral inspirada no conteúdo)'
    }],
    'Raízes de função': [{
        'pergunta': 'A função f(x) = x² − 5x + 6 zera em quais valores de x?',
        'alternativas': ['2 e 3', '−2 e −3', '1 e 6'],
        'correta': 0,
        'explicacao': 'Fatorando, x² − 5x + 6 = (x − 2)(x − 3). Portanto, as raízes são x = 2 e x = 3.',
        'fonte': 'Fonte: CBMPA, Cebraspe 2023, questão 20 (questão autoral inspirada no conteúdo)'
    }],
    'Máximo de função quadrática': [{
        'pergunta': 'A altura de um objeto é dada por h(t) = −2t² + 12t + 5. Qual é a altura máxima?',
        'alternativas': ['23', '21', '25'],
        'correta': 0,
        'explicacao': 'O vértice ocorre em t = −b ÷ 2a = −12 ÷ (−4) = 3. Então h(3) = −18 + 36 + 5 = 23.',
        'fonte': 'Fonte: CBMPA, Cebraspe 2023, questão 21 (questão autoral inspirada no conteúdo)'
    }],
    'Equação do segundo grau': [{
        'pergunta': 'Uma função de custo é C(x) = x² − 10x + 24. Para quais valores de x o custo é zero?',
        'alternativas': ['4 e 6', '2 e 12', '−4 e −6'],
        'correta': 0,
        'explicacao': 'A expressão fatorada é (x − 4)(x − 6). Igualando cada fator a zero, obtemos x = 4 ou x = 6.',
        'fonte': 'Fonte: CBMPA, Cebraspe 2023, questão 22 (questão autoral inspirada no conteúdo)'
    }],
    'Conjuntos': [{
        'pergunta': 'Em um grupo de 100 candidatos, 65 estudaram Matemática e 80 estudaram Português. Qual é o menor número possível que estudou as duas matérias?',
        'alternativas': ['45', '35', '65'],
        'correta': 0,
        'explicacao': 'Para minimizar a interseção, somamos os grupos e subtraímos o total: 65 + 80 − 100 = 45. Pelo menos 45 estudaram ambas.',
        'fonte': 'Fonte: PM/SC, Cebraspe 2023, questão 57 (questão autoral inspirada no conteúdo)'
    }],
    'Porcentagem sucessiva': [{
        'pergunta': 'Um salário bruto de R$ 3.000 sofre desconto de 14% e, sobre o restante, mais 27,5%. Qual é o salário líquido?',
        'alternativas': ['R$ 1.870,50', 'R$ 1.755,00', 'R$ 2.175,00'],
        'correta': 0,
        'explicacao': 'Após 14%, restam 86%: R$ 2.580. Descontando 27,5% desse valor, restam 72,5% × R$ 2.580 = R$ 1.870,50.',
        'fonte': 'Fonte: PM/SC, Cebraspe 2023, questão 58 (questão autoral inspirada no conteúdo)'
    }],
    'Juros simples': [{
        'pergunta': 'Um capital de R$ 2.000 rende juros simples de 1,5% ao mês durante 4 meses. Qual é o montante ao final?',
        'alternativas': ['R$ 2.120', 'R$ 2.150', 'R$ 2.060'],
        'correta': 0,
        'explicacao': 'Os juros são J = 2.000 × 0,015 × 4 = R$ 120. Montante: R$ 2.000 + R$ 120 = R$ 2.120.',
        'fonte': 'Fonte: CBMPA, Cebraspe 2023, questão 16 (média e operações; questão autoral)'
    }],
    'Regra de três composta': [{
        'pergunta': 'Seis profissionais revisam 180 fichas em 5 horas. Mantido o mesmo ritmo, quantas fichas 8 profissionais revisam em 6 horas?',
        'alternativas': ['288', '240', '300'],
        'correta': 0,
        'explicacao': 'A produção por profissional-hora é 180 ÷ (6 × 5) = 6 fichas. Em 8 × 6 = 48 profissional-horas, serão 48 × 6 = 288 fichas.',
        'fonte': 'Fonte: CBMPA, Cebraspe 2023, questão 17 (sequências e cálculo; questão autoral)'
    }],
    'Frações': [{
        'pergunta': 'Uma unidade de saúde recebeu 250 máscaras. Se 3/5 foram destinadas à enfermaria, quantas máscaras foram destinadas a esse setor?',
        'alternativas': ['150', '125', '100'],
        'correta': 0,
        'explicacao': 'Calculamos 3/5 de 250: 250 ÷ 5 = 50 e 50 × 3 = 150 máscaras.',
        'fonte': 'Fonte: CBMPA, Cebraspe 2023, questão 16 (média e cálculo numérico; questão autoral)'
    }],
    'Probabilidade': [{
        'pergunta': 'Uma caixa contém 3 cartões vermelhos, 2 azuis e 5 amarelos. Ao retirar um cartão ao acaso, qual é a probabilidade de ele não ser amarelo?',
        'alternativas': ['1/2', '1/3', '2/5'],
        'correta': 0,
        'explicacao': 'Há 5 cartões não amarelos entre 10 no total. Assim, a probabilidade é 5/10 = 1/2.',
        'fonte': 'Fonte: CBMPA, Cebraspe 2023, questão 16 (análise de dados; questão autoral)'
    }],
    'Razão e proporção': [{
        'pergunta': 'A razão entre técnicos e enfermeiros em uma equipe é 2:5. Se há 35 enfermeiros, quantos técnicos há?',
        'alternativas': ['14', '12', '17'],
        'correta': 0,
        'explicacao': 'Se 5 partes correspondem a 35 enfermeiros, cada parte vale 7. Os técnicos correspondem a 2 partes: 2 × 7 = 14.',
        'fonte': 'Fonte: CBMPA, Cebraspe 2023, questão 17 (proporções em sequências; questão autoral)'
    }],
    'Desconto comercial': [{
        'pergunta': 'Após um desconto de 15%, um equipamento passou a custar R$ 204. Qual era o preço antes do desconto?',
        'alternativas': ['R$ 240', 'R$ 234,60', 'R$ 250'],
        'correta': 0,
        'explicacao': 'R$ 204 corresponde a 85% do preço original. Então, 204 ÷ 0,85 = R$ 240.',
        'fonte': 'Fonte: PM/SC, Cebraspe 2023, questão 58 (porcentagens; questão autoral)'
    }],
}

LEGENDAS = {
    tema: f'Questão de Matemática para concurso: responda e confira a explicação.\n#JuhQuiz #Matematica #Concursos #ConcursoPublico'
    for tema in QUIZZES
}
