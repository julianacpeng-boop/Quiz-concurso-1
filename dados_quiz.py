# Quiz com 15 questões adaptadas do ENEM 2026.
# Os enunciados e alternativas foram reescritos para vídeos curtos.
# `correta` é o índice da alternativa: 0 = A, 1 = B, 2 = C.

CAPA_SEGUNDOS = 2

TEMA = "ENEM 2026 — Português e Matemática"

QUIZZES = {
    TEMA: [
        {
            "pergunta": "Pesquisadores registram línguas indígenas ameaçadas de desaparecer. Qual é a importância principal desse trabalho?",
            "alternativas": [
                "Padronizar a fala de diferentes povos.",
                "Substituir as línguas por idiomas mais usados.",
                "Reconhecer e preservar a diversidade linguística."
            ],
            "correta": 2,
            "explicacao": "Ao documentar línguas e suas formas próprias de organizar ideias, a pesquisa reconhece a diversidade cultural e linguística. Registrar não significa padronizar nem substituir esses idiomas.",
            "fonte": "ENEM 2026, Linguagens, questão 8 (adaptada)"
        },
        {
            "pergunta": "Um artigo de lei apresenta princípios para proteger crianças no uso da internet, como segurança e educação digital. A função principal desse trecho é: ",
            "alternativas": [
                "Apresentar fundamentos que orientam a lei.",
                "Narrar um caso de violência virtual.",
                "Ensinar o passo a passo de uma denúncia."
            ],
            "correta": 0,
            "explicacao": "O trecho enumera fundamentos gerais que servem de base para a lei. Ele informa princípios, sem narrar um caso específico ou descrever um procedimento de denúncia.",
            "fonte": "ENEM 2026, Linguagens, questão 22 (adaptada)"
        },
        {
            "pergunta": "A quarta capa de um livro resume a história e destaca temas como identidade, origem e afeto. Qual é o objetivo principal desse texto?",
            "alternativas": [
                "Explicar a biografia completa do autor.",
                "Apresentar aspectos que despertam interesse pela obra.",
                "Detalhar a divisão dos capítulos."
            ],
            "correta": 1,
            "explicacao": "A quarta capa costuma apresentar brevemente o enredo e temas relevantes para despertar o interesse do leitor. Não substitui a biografia nem descreve necessariamente a estrutura dos capítulos.",
            "fonte": "ENEM 2026, Linguagens, questão 23 (adaptada)"
        },
        {
            "pergunta": "Em Angola, a primeira refeição do dia pode ser chamada de “mata-bicho”. Esse exemplo mostra que o português: ",
            "alternativas": [
                "Possui uma única palavra correta em todos os países.",
                "Muda apenas na escrita, sem diferenças de vocabulário.",
                "Apresenta variedades com vocabulários próprios."
            ],
            "correta": 2,
            "explicacao": "A palavra usada em Angola evidencia uma diferença lexical entre variedades do português. A língua é compartilhada, mas pode apresentar vocabulário próprio em cada comunidade.",
            "fonte": "ENEM 2026, Linguagens, questão 43 (adaptada)"
        },
        {
            "pergunta": "Uma reportagem aponta que poucas universitárias escolhem cursos de ciência, tecnologia, engenharia e matemática. Esse dado é usado para sustentar qual ideia?",
            "alternativas": [
                "Ainda há desigualdade de participação de gênero na ciência.",
                "Essas carreiras deixaram de ser oferecidas nas universidades.",
                "As estudantes desconhecem todas as áreas científicas."
            ],
            "correta": 0,
            "explicacao": "O baixo percentual de mulheres em áreas STEM funciona como evidência de desigualdade de participação. O dado não prova que os cursos não existam ou que as estudantes desconheçam as áreas.",
            "fonte": "ENEM 2026, Linguagens, questão 44 (adaptada)"
        },
        {
            "pergunta": "Uma resenha descreve uma série em quadrinhos como feita “com humor mordaz”. Que tipo de marca essa expressão traz ao texto?",
            "alternativas": [
                "Uma informação neutra sobre a data de publicação.",
                "Uma avaliação do resenhista sobre a obra.",
                "Uma descrição objetiva do enredo."
            ],
            "correta": 1,
            "explicacao": "A expressão “humor mordaz” qualifica o modo como a obra provoca o leitor e revela a avaliação de quem escreveu a resenha. Não é apenas dado de publicação nem resumo do enredo.",
            "fonte": "ENEM 2026, Linguagens, questão 18 (adaptada)"
        },
        {
            "pergunta": "Uma canção incorpora palavras regionais ligadas aos rios e às plantas da Amazônia paraense. Esse recurso contribui principalmente para: ",
            "alternativas": [
                "Valorizar a identidade linguística e cultural da região.",
                "Eliminar as diferenças entre variedades do português.",
                "Apresentar os costumes locais como lendas."
            ],
            "correta": 0,
            "explicacao": "O uso de vocabulário regional na canção dá visibilidade a palavras e referências próprias do Pará, valorizando a identidade linguística da região. A questão não propõe apagar diferenças nem tratar esses elementos como lenda.",
            "fonte": "ENEM 2026, Linguagens, questão 21 (adaptada)"
        },
        {
            "pergunta": "Dois carros elétricos consomem energia por distância: o modelo A usa 20 MJ a cada 40 km na cidade e 30 km na estrada; o B usa 25 MJ a cada 50 km e 45 km, respectivamente. Em 100 km na cidade e 90 km na estrada, qual gasta menos?",
            "alternativas": [
                "Modelo A, com 110 MJ.",
                "Modelo B, com 100 MJ.",
                "Os dois gastam 125 MJ."
            ],
            "correta": 1,
            "explicacao": "No modelo A: 100/40 × 20 + 90/30 × 20 = 50 + 60 = 110 MJ. No modelo B: 100/50 × 25 + 90/45 × 25 = 50 + 50 = 100 MJ. Portanto, o modelo B consome menos energia.",
            "fonte": "ENEM 2026, Matemática, questão 137 (adaptada)"
        },
        {
            "pergunta": "Uma pessoa tem R$ 50.000 aplicados a 1% ao mês e compra um equipamento por R$ 49.000 à vista. Quanto ficará aplicado após dois meses, considerando juros compostos?",
            "alternativas": [
                "R$ 1.020,10.",
                "R$ 1.010,00.",
                "R$ 1.200,00."
            ],
            "correta": 0,
            "explicacao": "Após pagar à vista, restam R$ 1.000. Com juros compostos de 1% por dois meses: 1.000 × 1,01² = R$ 1.020,10.",
            "fonte": "ENEM 2026, Matemática, questão 160 (adaptada)"
        },
        {
            "pergunta": "Um notebook custa R$ 5.000 e perde 10% do valor imediatamente. Depois, desvaloriza 20% ao ano. Qual expressão representa seu valor após t anos?",
            "alternativas": [
                "V = 5.000 × 0,20ᵗ.",
                "V = 4.500 × 0,90ᵗ.",
                "V = 4.500 × 0,80ᵗ."
            ],
            "correta": 2,
            "explicacao": "A queda imediata deixa o notebook com 5.000 × 0,90 = R$ 4.500. A cada ano ele conserva 80% do valor, isto é, multiplica-se por 0,80. Logo, V = 4.500 × 0,80ᵗ.",
            "fonte": "ENEM 2026, Matemática, questão 161 (adaptada)"
        },
        {
            "pergunta": "Uma célula mede 0,48 micrômetro. Sabendo que 1 micrômetro equivale a 10⁻³ milímetro, qual é essa medida em milímetros?",
            "alternativas": [
                "4,8 × 10⁻⁴ mm.",
                "4,8 × 10⁻³ mm.",
                "4,8 × 10⁻⁷ mm."
            ],
            "correta": 0,
            "explicacao": "0,48 × 10⁻³ mm = 4,8 × 10⁻⁴ mm. Ao deslocar a vírgula uma casa para a direita para obter 4,8, o expoente diminui uma unidade.",
            "fonte": "ENEM 2026, Matemática, questão 162 (adaptada)"
        },
        {
            "pergunta": "Uma pintura mede 80 cm por 60 cm. Uma figurinha semelhante terá área de 48 cm². Qual será a escala linear da figurinha em relação à pintura?",
            "alternativas": [
                "1 : 5.",
                "1 : 100.",
                "1 : 10."
            ],
            "correta": 2,
            "explicacao": "A pintura tem área 4.800 cm². A razão entre as áreas é 4.800/48 = 100. Como a escala de comprimento é a raiz quadrada da razão entre áreas, √100 = 10; a escala é 1:10.",
            "fonte": "ENEM 2026, Matemática, questão 167 (adaptada)"
        },
        {
            "pergunta": "Duas rodas percorrem 1.800 m. Seus diâmetros são 0,6 m e 0,4 m. Use π = 3. Quantas voltas a roda menor dá a mais?",
            "alternativas": [
                "400 voltas.",
                "500 voltas.",
                "600 voltas."
            ],
            "correta": 1,
            "explicacao": "Com π = 3, a roda de 0,6 m percorre 1,8 m por volta: 1.800/1,8 = 1.000 voltas. A roda de 0,4 m percorre 1,2 m por volta: 1.800/1,2 = 1.500 voltas. A menor dá 500 voltas a mais.",
            "fonte": "ENEM 2026, Matemática, questão 168 (adaptada)"
        },
        {
            "pergunta": "Uma tabela recomenda D-28 para 61–70 kg e 1,71–1,80 m; para 71–80 kg e 1,71–1,80 m, recomenda D-30 ou D-33, com D-30 destacada como a melhor opção. Qual é indicada para alguém com 71 kg e 1,71 m?",
            "alternativas": [
                "D-28.",
                "D-33.",
                "D-30."
            ],
            "correta": 2,
            "explicacao": "A pessoa está na faixa de 71 a 80 kg e na coluna de 1,71 a 1,80 m. Seguindo o critério da tabela, escolhe-se a opção destacada como mais adequada: D-30.",
            "fonte": "ENEM 2026, Matemática, questão 175 (adaptada)"
        },
        {
            "pergunta": "Uma loja vende 1.000 peças: blusas e vestidos. Cada blusa dá lucro de R$ 12; vestido pago em dinheiro dá R$ 40, e no cartão o lucro é 10% menor. Um quarto dos vestidos foi pago em dinheiro. Se x é o número de blusas, qual expressão representa o lucro total?",
            "alternativas": [
                "40.000 − 28x.",
                "37.000 − 25x.",
                "36.000 − 24x."
            ],
            "correta": 1,
            "explicacao": "Cada vestido gera lucro médio de (1/4 × 40) + (3/4 × 36) = R$ 37. Como há 1.000 − x vestidos, o lucro deles é 37(1.000 − x). Somando o lucro das blusas, 12x + 37.000 − 37x = 37.000 − 25x.",
            "fonte": "ENEM 2026, Matemática, questão 165 (adaptada)"
        }
    ]
}

LEGENDAS = {
    TEMA: "Português e Matemática no estilo do ENEM 2026. Responda antes da explicação!\n\n#JuhQuiz #ENEM #Estudos #Conhecimento"
}
