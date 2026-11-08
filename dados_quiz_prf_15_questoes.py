# Dados do Quiz — PRF (15 questões de disciplinas variadas)
# Questões autorais elaboradas com base nos conteúdos do concurso PRF/Cebraspe 2021.
# O gerador transforma cada questão em um vídeo individual.

CAPA_SEGUNDOS = 2

QUIZZES = {
    "portugues_prf": [
        {
            "pergunta": "Na frase “A equipe chegou ___ unidade operacional”, qual forma completa corretamente a lacuna?",
            "alternativas": ["à", "a", "há"],
            "correta": 0,
            "explicacao": "O verbo chegar rege a preposição “a”. Como “unidade” admite o artigo feminino “a”, ocorre a contração: a + a = à.",
            "fonte": "Edital PRF 2021, Anexo I, Língua Portuguesa: emprego do sinal indicativo de crase. Questão autoral.",
        },
        {
            "pergunta": "Qual frase apresenta concordância verbal correta?",
            "alternativas": ["Faz dois anos que a unidade foi inaugurada.", "Fazem dois anos que a unidade foi inaugurada.", "Houveram mudanças no procedimento."],
            "correta": 0,
            "explicacao": "Quando indica tempo decorrido, o verbo “fazer” é impessoal e fica na terceira pessoa do singular. O verbo “haver”, com sentido de existir, também é impessoal: houve mudanças.",
            "fonte": "Edital PRF 2021, Anexo I, Língua Portuguesa: concordância verbal. Questão autoral.",
        },
        {
            "pergunta": "Em “O agente revisou o relatório porque havia uma divergência”, a palavra “porque” expressa:",
            "alternativas": ["Causa ou explicação", "Conclusão", "Condição"],
            "correta": 0,
            "explicacao": "Nesse contexto, “porque” introduz a causa ou explicação para a revisão do relatório: havia uma divergência.",
            "fonte": "Edital PRF 2021, Anexo I, Língua Portuguesa: coesão e emprego de conectores. Questão autoral.",
        },
    ],
    "matematica_prf": [
        {
            "pergunta": "Uma viatura percorreu 240 km em 4 horas, mantendo velocidade média constante. Qual foi a velocidade média?",
            "alternativas": ["60 km/h", "80 km/h", "960 km/h"],
            "correta": 0,
            "explicacao": "A velocidade média é a distância dividida pelo tempo: 240 ÷ 4 = 60 km/h.",
            "fonte": "Edital PRF 2021, Anexo I, Raciocínio Lógico-Matemático: razão e proporção, taxas de variação. Questão autoral.",
        },
        {
            "pergunta": "Uma equipe analisou 350 registros e encontrou inconsistências em 20% deles. Quantos registros tinham inconsistências?",
            "alternativas": ["70", "35", "175"],
            "correta": 0,
            "explicacao": "Calculamos 20% de 350: 0,20 × 350 = 70 registros.",
            "fonte": "Edital PRF 2021, Anexo I, Raciocínio Lógico-Matemático: porcentagem. Questão autoral.",
        },
        {
            "pergunta": "Em um mapa na escala 1:50.000, a distância entre dois pontos é de 4 cm. Qual é a distância real?",
            "alternativas": ["2 km", "200 m", "20 km"],
            "correta": 0,
            "explicacao": "Cada centímetro representa 50.000 cm. Então 4 cm representam 200.000 cm, ou 2.000 m, equivalentes a 2 km.",
            "fonte": "Edital PRF 2021, Anexo I, Raciocínio Lógico-Matemático: escalas e interpretação de mapas. Questão autoral.",
        },
    ],
    "raciocinio_logico_prf": [
        {
            "pergunta": "Qual número completa a sequência: 3, 7, 11, 15, ___?",
            "alternativas": ["19", "18", "21"],
            "correta": 0,
            "explicacao": "A sequência aumenta de 4 em 4. Portanto, 15 + 4 = 19.",
            "fonte": "Edital PRF 2021, Anexo I, Raciocínio Lógico-Matemático: regularidades e padrões em sequências. Questão autoral.",
        },
        {
            "pergunta": "Todo agente de uma equipe usa identificação funcional. Rui é agente dessa equipe. O que se conclui?",
            "alternativas": ["Rui usa identificação funcional.", "Rui pode ou não usar identificação funcional.", "Nenhum agente usa identificação funcional."],
            "correta": 0,
            "explicacao": "A premissa afirma que todos os agentes da equipe usam identificação funcional. Como Rui pertence ao grupo, a conclusão necessária é que Rui também usa a identificação.",
            "fonte": "Edital PRF 2021, Anexo I, Raciocínio Lógico-Matemático: lógica proposicional e argumentação. Questão autoral.",
        },
        {
            "pergunta": "Ao lançar um dado comum de seis faces, qual é a probabilidade de sair um número par?",
            "alternativas": ["1/2", "1/3", "2/3"],
            "correta": 0,
            "explicacao": "Os resultados pares são 2, 4 e 6: três resultados favoráveis entre seis possíveis. A probabilidade é 3/6 = 1/2.",
            "fonte": "Edital PRF 2021, Anexo I, Raciocínio Lógico-Matemático: probabilidade. Questão autoral.",
        },
    ],
    "legislacao_transito_prf": [
        {
            "pergunta": "Em cruzamento não sinalizado, entre vias de mesma importância, qual veículo tem preferência de passagem?",
            "alternativas": ["O que vem pela direita do condutor", "O que vem pela esquerda", "O veículo maior"],
            "correta": 0,
            "explicacao": "O Código de Trânsito Brasileiro estabelece, como regra geral para cruzamento não sinalizado, a preferência do veículo que se aproxima pela direita do condutor.",
            "fonte": "Código de Trânsito Brasileiro, Lei nº 9.503/1997, art. 29, III, “c”. Questão autoral baseada no conteúdo de Legislação de Trânsito do edital PRF 2021.",
        },
        {
            "pergunta": "O uso do cinto de segurança é obrigatório para:",
            "alternativas": ["Condutor e passageiros em todas as vias do território nacional, salvo exceções regulamentadas", "Somente o condutor em rodovias", "Somente os passageiros do banco dianteiro"],
            "correta": 0,
            "explicacao": "O CTB prevê o uso obrigatório do cinto de segurança pelo condutor e passageiros em todas as vias do território nacional, ressalvadas situações regulamentadas pelo Contran.",
            "fonte": "Código de Trânsito Brasileiro, Lei nº 9.503/1997, art. 65. Questão autoral baseada no conteúdo de Legislação de Trânsito do edital PRF 2021.",
        },
        {
            "pergunta": "Quando uma ambulância em serviço de urgência aciona alarme sonoro e iluminação intermitente, os demais condutores devem:",
            "alternativas": ["Deixar livre a passagem pela faixa da esquerda, deslocando-se para a direita e parando se necessário", "Acelerar para seguir à frente dela", "Parar imediatamente no meio da via"],
            "correta": 0,
            "explicacao": "Ao perceber veículo de emergência com dispositivos regulamentares acionados, os condutores devem facilitar a passagem, deslocando-se para a direita e parando se necessário, mantendo livre a faixa da esquerda.",
            "fonte": "Código de Trânsito Brasileiro, Lei nº 9.503/1997, art. 29, VII. Questão autoral baseada no conteúdo de Legislação de Trânsito do edital PRF 2021.",
        },
    ],
    "fisica_prf": [
        {
            "pergunta": "Uma viatura está a 72 km/h. Qual é essa velocidade em metros por segundo?",
            "alternativas": ["20 m/s", "25 m/s", "72 m/s"],
            "correta": 0,
            "explicacao": "Para converter km/h em m/s, divide-se por 3,6: 72 ÷ 3,6 = 20 m/s.",
            "fonte": "Edital PRF 2021, Anexo I, Física: grandezas, unidades e cinemática. Questão autoral.",
        },
    ],
    "direito_constitucional_prf": [
        {
            "pergunta": "Segundo a Constituição Federal, a Polícia Rodoviária Federal é:",
            "alternativas": ["Órgão permanente, organizado e mantido pela União", "Órgão temporário subordinado aos estados", "Empresa pública responsável por fiscalizar somente rodovias estaduais"],
            "correta": 0,
            "explicacao": "A Constituição define a Polícia Rodoviária Federal como órgão permanente, organizado e mantido pela União e estruturado em carreira, destinado ao patrulhamento ostensivo das rodovias federais.",
            "fonte": "Constituição Federal de 1988, art. 144, § 2º. Tema previsto no edital PRF 2021, Direito Constitucional. Questão autoral.",
        },
    ],
    "direitos_humanos_prf": [
        {
            "pergunta": "Qual princípio orienta a aplicação dos direitos humanos a todas as pessoas?",
            "alternativas": ["Universalidade e igualdade em dignidade e direitos", "Concessão de direitos apenas a cidadãos de um país", "Aplicação condicionada à renda da pessoa"],
            "correta": 0,
            "explicacao": "Os direitos humanos são universais: pertencem a todas as pessoas, sem discriminação, e todos nascem livres e iguais em dignidade e direitos.",
            "fonte": "Declaração Universal dos Direitos Humanos, arts. 1º e 2º; conteúdo de Direitos Humanos do edital PRF 2021. Questão autoral.",
        },
    ],
}

LEGENDAS = {
    "portugues_prf": "Desafio PRF: Português. Responda antes da explicação. #JuhQuiz #PRF #Portugues #Concursos",
    "matematica_prf": "Desafio PRF: Matemática. Responda antes da explicação. #JuhQuiz #PRF #Matematica #Concursos",
    "raciocinio_logico_prf": "Desafio PRF: Raciocínio Lógico. Responda antes da explicação. #JuhQuiz #PRF #RaciocinioLogico #Concursos",
    "legislacao_transito_prf": "Desafio PRF: Legislação de Trânsito. Responda antes da explicação. #JuhQuiz #PRF #Transito #Concursos",
    "fisica_prf": "Desafio PRF: Física. Responda antes da explicação. #JuhQuiz #PRF #Fisica #Concursos",
    "direito_constitucional_prf": "Desafio PRF: Direito Constitucional. Responda antes da explicação. #JuhQuiz #PRF #Direito #Concursos",
    "direitos_humanos_prf": "Desafio PRF: Direitos Humanos. Responda antes da explicação. #JuhQuiz #PRF #DireitosHumanos #Concursos",
}

