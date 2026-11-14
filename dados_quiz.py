# Juh Quiz — Professor de Matemática do Ensino Fundamental
# Questões adaptadas de provas oficiais; uma pergunta por vídeo.
# A fonte curta é exibida entre parênteses pelo gerar_quiz.py.

CAPA_SEGUNDOS = 2

QUIZZES = {
    "Professor de Matemática — BNCC": [{
        "pergunta": "Quais são as cinco unidades temáticas de Matemática previstas na BNCC para o Ensino Fundamental?",
        "alternativas": ["Aritmética, Álgebra, Geometria, Estatística e Informática", "Números, Álgebra, Geometria, Grandezas e medidas, Probabilidade e Estatística", "Números, Cálculo, Formas, Medidas e Educação financeira"],
        "correta": 1,
        "explicacao": "A BNCC organiza a Matemática do Ensino Fundamental em Números, Álgebra, Geometria, Grandezas e medidas, e Probabilidade e Estatística.",
        "fonte": "Itumbiara-GO, IV/UFG, 2025, q. 31",
    }],
    "Professor de Matemática — pensamento algébrico": [{
        "pergunta": "Nos anos iniciais, uma forma de desenvolver o pensamento algébrico é pedir que os alunos:",
        "alternativas": ["Memorizem fórmulas de equações do segundo grau", "Usem letras em todas as operações desde o primeiro ano", "Identifiquem regularidades e descrevam regras de sequências"],
        "correta": 2,
        "explicacao": "Reconhecer padrões e explicar como uma sequência se repete ou cresce ajuda a desenvolver o pensamento algébrico desde os primeiros anos.",
        "fonte": "Itumbiara-GO, IV/UFG, 2025, q. 31",
    }],
    "Professor de Matemática — juros compostos": [{
        "pergunta": "R$ 1.000 são aplicados a juros compostos de 8% ao ano. Qual é o montante após dois anos?",
        "alternativas": ["R$ 1.166,40", "R$ 1.160,00", "R$ 1.180,00"],
        "correta": 0,
        "explicacao": "Nos juros compostos, o fator de crescimento é aplicado em cada ano: 1.000 × 1,08² = R$ 1.166,40.",
        "fonte": "Itumbiara-GO, IV/UFG, 2025, q. 33",
    }],
    "Professor de Matemática — estatística": [{
        "pergunta": "As notas de cinco alunos foram 6, 7, 8, 8 e 9. Qual é a média aritmética?",
        "alternativas": ["7", "8", "7,6"],
        "correta": 2,
        "explicacao": "Somando as notas, obtemos 38. Dividindo por cinco alunos, a média é 7,6.",
        "fonte": "Itumbiara-GO, IV/UFG, 2025, q. 35",
    }],
    "Professor de Matemática — geometria e medidas": [{
        "pergunta": "Uma rampa sobe 1,5 m e avança 2 m na horizontal. Qual é seu comprimento?",
        "alternativas": ["2,5 m", "3 m", "3,5 m"],
        "correta": 0,
        "explicacao": "A rampa é a hipotenusa de um triângulo retângulo. Pelo teorema de Pitágoras, √(1,5² + 2²) = √6,25 = 2,5 m.",
        "fonte": "Itumbiara-GO, IV/UFG, 2025, q. 36",
    }],
    "Professor de Matemática — função exponencial": [{
        "pergunta": "O gráfico de f(x) foi transformado em g(x) = f(x − 4) + 3. Como o gráfico se desloca?",
        "alternativas": ["4 unidades à esquerda e 3 para baixo", "4 unidades à direita e 3 para cima", "3 unidades à direita e 4 para cima"],
        "correta": 1,
        "explicacao": "Subtrair 4 dentro do argumento desloca o gráfico quatro unidades para a direita. Somar 3 fora da função desloca-o três para cima.",
        "fonte": "Itumbiara-GO, IV/UFG, 2025, q. 37",
    }],
    "Professor de Matemática — volume da esfera": [{
        "pergunta": "Uma esfera de raio 3 cm é dividida em uma cunha de 60°. Qual é o volume dessa parte?",
        "alternativas": ["9π cm³", "12π cm³", "6π cm³"],
        "correta": 2,
        "explicacao": "A cunha corresponde a 60/360, ou seja, 1/6 da esfera. Como o volume da esfera é (4/3)π × 3³ = 36π cm³, a cunha tem 6π cm³.",
        "fonte": "Itumbiara-GO, IV/UFG, 2025, q. 38",
    }],
    "Professor de Matemática — função quadrática": [{
        "pergunta": "Qual é a abscissa do vértice da parábola f(x) = x² − 8x + 12?",
        "alternativas": ["4", "−4", "8"],
        "correta": 0,
        "explicacao": "Na função quadrática, a abscissa do vértice é −b/(2a). Aqui, −(−8)/(2 × 1) = 4.",
        "fonte": "Itumbiara-GO, IV/UFG, 2025, q. 39",
    }],
    "Professor de Matemática — equações e frações": [{
        "pergunta": "Ana e Bruno têm juntos R$ 1.200. Cada um contribui com o mesmo valor para um jogo. Esse valor é 1/3 da quantia de Ana e 1/5 da quantia de Bruno. Quanto custa o jogo?",
        "alternativas": ["R$ 250", "R$ 300", "R$ 400"],
        "correta": 1,
        "explicacao": "Se cada contribuição é x, Ana tem 3x e Bruno tem 5x. Então 8x = 1.200, logo x = 150. Como ambos contribuem, o jogo custa R$ 300.",
        "fonte": "São José dos Campos-SP, FGV, 2025, q. 43",
    }],
    "Professor de Matemática — plano cartesiano": [{
        "pergunta": "Qual ponto da reta que passa por (0, 3) e (3, 9) tem coordenadas iguais?",
        "alternativas": ["(−2, −2)", "(3, 3)", "(−3, −3)"],
        "correta": 2,
        "explicacao": "A reta tem inclinação 2 e equação y = 2x + 3. Para coordenadas iguais, fazemos y = x: x = 2x + 3, então x = −3 e y = −3.",
        "fonte": "São José dos Campos-SP, FGV, 2025, q. 48",
    }],
    "Professor de Matemática — porcentagem": [{
        "pergunta": "De R$ 500, uma pessoa gasta 20%. Depois gasta 25% do que restou e, por fim, 10% do novo saldo. Que porcentagem dos R$ 500 sobra?",
        "alternativas": ["54%", "55%", "60%"],
        "correta": 0,
        "explicacao": "Após cada gasto, multiplicamos o saldo pelo percentual restante: 500 × 0,80 × 0,75 × 0,90 = 270. Isso corresponde a 54% de R$ 500.",
        "fonte": "São José dos Campos-SP, FGV, 2025, q. 49",
    }],
    "Professor de Matemática — probabilidade": [{
        "pergunta": "Em um grupo há 2 professores de Matemática, 3 de Português e 4 de Ciências. Sorteiam-se dois. Qual é a probabilidade de serem da mesma disciplina?",
        "alternativas": ["1/3", "5/18", "1/2"],
        "correta": 1,
        "explicacao": "Há 36 pares possíveis. Os pares da mesma disciplina são 1 de Matemática, 3 de Português e 6 de Ciências, totalizando 10. Assim, 10/36 = 5/18.",
        "fonte": "São José dos Campos-SP, FGV, 2025, q. 46",
    }],
    "Professor de Matemática — volume da pirâmide": [{
        "pergunta": "Uma pirâmide tem base quadrada de lado 6 cm e altura 4 cm. Qual é seu volume?",
        "alternativas": ["36 cm³", "72 cm³", "48 cm³"],
        "correta": 2,
        "explicacao": "O volume é um terço da área da base vezes a altura: (1/3) × 6² × 4 = 48 cm³.",
        "fonte": "São José dos Campos-SP, FGV, 2025, q. 50",
    }],
    "Professor de Matemática — raciocínio lógico": [{
        "pergunta": "Ana, Bruno e Carla: exatamente uma pessoa pegou uma moeda e exatamente uma afirmação é falsa. Ana diz “Bruno pegou”; Bruno diz “Carla pegou”; Carla diz “Bruno está mentindo”. Quem pegou a moeda?",
        "alternativas": ["Bruno", "Ana", "Carla"],
        "correta": 0,
        "explicacao": "Se Bruno pegou a moeda, Ana diz a verdade, Bruno mente e Carla diz a verdade. Há exatamente uma afirmação falsa, como o enunciado exige.",
        "fonte": "Itumbiara-GO, IV/UFG, 2025, q. 41",
    }],
    "Professor de Matemática — criptaritmo": [{
        "pergunta": "Cada letra representa um algarismo diferente e A não é zero. Se A + AB + ABC + ABCD = 2026, quanto vale B − C + D − A?",
        "alternativas": ["8", "10", "12"],
        "correta": 1,
        "explicacao": "A igualdade determina A = 1, B = 8, C = 2 e D = 5. Portanto, B − C + D − A = 8 − 2 + 5 − 1 = 10.",
        "fonte": "São José dos Campos-SP, FGV, 2025, q. 51",
    }],
}

LEGENDAS = {
    tema: f"{tema}: desafio de concurso para professor!\n\n#JuhQuiz #Matematica #Concursos #Professor"
    for tema in QUIZZES
}

# Referências completas consultadas; a fonte curta acima aparece no vídeo.
FONTES_COMPLETAS = {
    "Itumbiara-GO, IV/UFG, 2025": "Prefeitura de Itumbiara-GO, PEB II — Matemática, prova de 20/07/2025. https://sistemas.institutoverbena.ufg.br/2025/prefeitura-itumbiara/sistema/provas_gabaritos/prova/professor%20de%20educacao%20basica%20peb%20II%20matematica.pdf",
    "São José dos Campos-SP, FGV, 2023": "Prefeitura de São José dos Campos-SP, Edital 02/2025, Professor II — Matemática. https://conhecimento.fgv.br/concursos/prefsjc-educacao25 ; prova: https://conhecimento.fgv.br/sites/default/files/concursos/cnsp0207-professor-ii-matematica-cnsp0207-tipo-1.pdf",
}
