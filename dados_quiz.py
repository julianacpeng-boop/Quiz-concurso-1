# -*- coding: utf-8 -*-
"""15 questões autorais de raciocínio lógico inspiradas em provas de concursos.

As referências indicam provas e itens que cobraram o mesmo assunto. Os
enunciados abaixo são autorais, com números e situações próprios.
"""

CAPA_SEGUNDOS = 2

QUIZZES = {
    'Tabela-verdade': [{
        'pergunta': 'Uma proposição é formada por quatro proposições simples. Quantas linhas terá sua tabela-verdade completa?',
        'alternativas': ['8 linhas', '16 linhas', '32 linhas'],
        'correta': 1,
        'explicacao': 'Cada proposição simples pode assumir dois valores: verdadeiro ou falso. Com quatro proposições, o total de combinações é 2⁴, ou seja, 16 linhas.',
        'fonte': 'Base: PM/SC Soldado, Cebraspe 2023, questão 51 (autoral)'
    }],
    'Conectivos lógicos': [{
        'pergunta': 'Considere P falsa e Q verdadeira. Qual é o valor lógico de “não P ou Q”?',
        'alternativas': ['Verdadeiro', 'Falso', 'Não é possível determinar'],
        'correta': 0,
        'explicacao': 'Como P é falsa, “não P” é verdadeira. Na disjunção, basta uma das partes ser verdadeira para que toda a proposição seja verdadeira.',
        'fonte': 'Base: PM/SC Soldado, Cebraspe 2023, questão 52 (autoral)'
    }],
    'Conjuntos': [{
        'pergunta': 'Para que “se P, então Q” seja verdadeira para todos os elementos de um universo, qual relação deve existir entre os conjuntos de verdade de P e Q?',
        'alternativas': ['O conjunto de P deve estar contido no conjunto de Q', 'Os conjuntos devem ser sempre disjuntos', 'O conjunto de Q deve estar contido no conjunto de P'],
        'correta': 0,
        'explicacao': 'A condicional só é falsa quando P é verdadeira e Q é falsa. Para impedir esse caso em todo o universo, todo elemento que satisfaz P também deve satisfazer Q; portanto, o conjunto de P fica contido no de Q.',
        'fonte': 'Base: PM/SC Soldado, Cebraspe 2023, questão 53 (autoral)'
    }],
    'Tautologia': [{
        'pergunta': 'Qual das expressões abaixo é verdadeira em qualquer situação?',
        'alternativas': ['P e não P', 'P ou não P', 'Se P, então não P'],
        'correta': 1,
        'explicacao': 'P ou não P é sempre verdadeira: se P for verdadeira, a primeira parte basta; se P for falsa, sua negação será verdadeira. Essa expressão é uma tautologia.',
        'fonte': 'Base: PM/SC Soldado, Cebraspe 2023, questão 55 (autoral)'
    }],
    'Negação': [{
        'pergunta': 'Qual é a negação lógica de: “Marina estudou e foi aprovada”?',
        'alternativas': ['Marina não estudou ou não foi aprovada', 'Marina não estudou e não foi aprovada', 'Marina estudou ou foi aprovada'],
        'correta': 0,
        'explicacao': 'Pela lei de De Morgan, a negação de “P e Q” é “não P ou não Q”. Basta que uma das duas afirmações originais seja falsa para a frase conjunta ser falsa.',
        'fonte': 'Base: PM/SC Soldado, Cebraspe 2023, questão 56 (autoral)'
    }],
    'Interseção de conjuntos': [{
        'pergunta': 'Em um grupo de 100 candidatos, 62 estudaram matemática e 71 estudaram português. Qual é o menor número possível que estudou as duas matérias?',
        'alternativas': ['33 candidatos', '62 candidatos', '71 candidatos'],
        'correta': 0,
        'explicacao': 'No mínimo, a interseção é a soma dos dois grupos menos o total: 62 + 71 − 100 = 33. Com menos que isso, haveria mais de 100 pessoas no conjunto total.',
        'fonte': 'Base: PM/SC Soldado, Cebraspe 2023, questão 57 (autoral)'
    }],
    'Porcentagem': [{
        'pergunta': 'Um salário recebe desconto de 10% e, depois, desconto de 20% sobre o valor restante. Que porcentagem do salário inicial sobra?',
        'alternativas': ['70%', '72%', '80%'],
        'correta': 1,
        'explicacao': 'Após o primeiro desconto, sobra 90% do salário. O segundo desconto deixa 80% desse valor: 0,90 × 0,80 = 0,72. Portanto, sobram 72% do salário inicial.',
        'fonte': 'Base: PM/SC Soldado, Cebraspe 2023, questão 58 (autoral)'
    }],
    'Média e mediana': [{
        'pergunta': 'Os valores registrados foram 4, 6, 8, 10 e 12. Qual é a soma da média aritmética com a mediana?',
        'alternativas': ['16', '18', '20'],
        'correta': 0,
        'explicacao': 'A média é (4 + 6 + 8 + 10 + 12) ÷ 5 = 8. Como os valores estão ordenados, a mediana é o valor central, também 8. A soma é 16.',
        'fonte': 'Base: CBMPA CFO, Cebraspe 2023, questão 16 (autoral)'
    }],
    'Progressão aritmética': [{
        'pergunta': 'Em uma progressão aritmética, o primeiro termo é 5 e o terceiro é 9. Qual é a soma dos dez primeiros termos?',
        'alternativas': ['130', '140', '150'],
        'correta': 1,
        'explicacao': 'Do primeiro ao terceiro termo há dois intervalos. Assim, a razão é (9 − 5) ÷ 2 = 2. O décimo termo é 5 + 9 × 2 = 23; a soma é 10 × (5 + 23) ÷ 2 = 140.',
        'fonte': 'Base: CBMPA CFO, Cebraspe 2023, questão 17 (autoral)'
    }],
    'Área': [{
        'pergunta': 'Uma sala retangular mede 8 metros de comprimento por 5 metros de largura. Qual é sua área?',
        'alternativas': ['13 m²', '26 m²', '40 m²'],
        'correta': 2,
        'explicacao': 'A área do retângulo é calculada multiplicando comprimento por largura: 8 × 5 = 40 metros quadrados.',
        'fonte': 'Base: CBMPA CFO, Cebraspe 2023, questão 18 (autoral)'
    }],
    'Tabela-verdade composta': [{
        'pergunta': 'Se P é verdadeira, Q é falsa e R é verdadeira, qual é o valor de P e (Q se, e somente se, não R)?',
        'alternativas': ['Verdadeiro', 'Falso', 'A expressão não tem valor lógico'],
        'correta': 0,
        'explicacao': 'Como R é verdadeira, não R é falsa. Q também é falsa, então “Q se, e somente se, não R” é verdadeira, pois os dois lados têm o mesmo valor. Mas P e verdadeiro resulta em verdadeiro — atenção: P é verdadeira, portanto a expressão inteira é verdadeira.',
        'fonte': 'Base: CBMPA CFO, Cebraspe 2023, questão 23 (autoral)'
    }],
    'Equivalência lógica': [{
        'pergunta': 'Qual expressão é logicamente equivalente a “se P, então Q”?',
        'alternativas': ['Não P ou Q', 'P e não Q', 'Q e não P'],
        'correta': 0,
        'explicacao': 'A condicional “se P, então Q” só é falsa quando P é verdadeira e Q é falsa. “Não P ou Q” também é falsa exatamente nessa situação, por isso as duas expressões são equivalentes.',
        'fonte': 'Base: CBMPA CFO, Cebraspe 2023, questão 24 (autoral)'
    }],
    'Contrapositiva': [{
        'pergunta': 'Qual é a contrapositiva de: “Se estudo, então passo na prova”?',
        'alternativas': ['Se não passo na prova, então não estudei', 'Se passo na prova, então estudei', 'Se não estudei, então não passo na prova'],
        'correta': 0,
        'explicacao': 'A contrapositiva de “se P, então Q” é “se não Q, então não P”. Ela é logicamente equivalente à condicional original.',
        'fonte': 'Base: SERPRO, Cebraspe 2023, questão 36 (autoral)'
    }],
    'Condicional': [{
        'pergunta': 'A frase “Se o sistema está ligado, então a tela acende” é falsa em qual situação?',
        'alternativas': ['O sistema está ligado e a tela não acende', 'O sistema está desligado e a tela acende', 'O sistema está desligado e a tela não acende'],
        'correta': 0,
        'explicacao': 'Uma condicional só é falsa quando a condição inicial ocorre, mas o resultado prometido não acontece. Portanto, o sistema está ligado e a tela permanece apagada.',
        'fonte': 'Base: SERPRO, Cebraspe 2023, questão 37 (autoral)'
    }],
    'Proposições compostas': [{
        'pergunta': 'Qual afirmação composta é verdadeira?',
        'alternativas': ['“7 é primo e 5 é ímpar”', '“9 é múltiplo de 3 e 25 é múltiplo de 3”', '“4 divide 16 ou 3 divide 16” é falsa'],
        'correta': 0,
        'explicacao': 'As duas partes da primeira opção são verdadeiras, então a conjunção é verdadeira. Na segunda, 25 não é múltiplo de 3. Na terceira, 4 divide 16, tornando verdadeira a disjunção, não falsa.',
        'fonte': 'Base: IBGE, IBFC 2026, questão 16 (autoral)'
    }],
}

LEGENDAS = {
    tema: f'Questão de raciocínio lógico para concurso: responda e confira a explicação.\n#JuhQuiz #RaciocinioLogico #Concursos #ConcursoPublico'
    for tema in QUIZZES
}
