# Dados do Quiz — Direitos Humanos
# 15 questões autorais, com uma pergunta por vídeo e fonte indicada em cada questão.

CAPA_SEGUNDOS = 2

QUIZZES = {
    "Direitos Humanos — dignidade e igualdade": [
        {
            "pergunta": "Segundo a Declaração Universal dos Direitos Humanos, como todas as pessoas nascem?",
            "alternativas": ['Livres e iguais em dignidade e direitos', 'Com direitos definidos pela renda', 'Com liberdade apenas após autorização do Estado'],
            "correta": 0,
            "explicacao": "O artigo 1º afirma que todos os seres humanos nascem livres e iguais em dignidade e direitos, e devem agir com espírito de fraternidade.",
            "fonte": "(Declaração Universal dos Direitos Humanos, art. 1º; Resolução ONU 217 A (III), 1948)",
        },
    ],
    "Direitos Humanos — vida, liberdade e segurança": [
        {
            "pergunta": "Quais direitos são reconhecidos a toda pessoa pelo artigo 3º da Declaração Universal?",
            "alternativas": ['Propriedade, nacionalidade e educação', 'Vida, liberdade e segurança pessoal', 'Trabalho, lazer e previdência'],
            "correta": 1,
            "explicacao": "O artigo 3º da Declaração Universal reconhece a toda pessoa o direito à vida, à liberdade e à segurança pessoal.",
            "fonte": "(Declaração Universal dos Direitos Humanos, art. 3º)",
        },
    ],
    "Direitos Humanos — proibição da escravidão": [
        {
            "pergunta": "O que estabelece a Declaração Universal dos Direitos Humanos sobre escravidão e servidão?",
            "alternativas": ['São permitidas por prazo determinado', 'São admitidas quando não há remuneração', 'São proibidas em todas as formas'],
            "correta": 2,
            "explicacao": "O artigo 4º proíbe que qualquer pessoa seja mantida em escravidão ou servidão e também proíbe o tráfico de escravos em todas as suas formas.",
            "fonte": "(Declaração Universal dos Direitos Humanos, art. 4º)",
        },
    ],
    "Direitos Humanos — tortura e tratamento degradante": [
        {
            "pergunta": "A Constituição Federal determina que ninguém será submetido a tortura nem a tratamento:",
            "alternativas": ['Desumano ou degradante', 'Restritivo ou disciplinar', 'Administrativo ou judicial'],
            "correta": 0,
            "explicacao": "A Constituição proíbe expressamente a tortura e o tratamento desumano ou degradante. A Declaração Universal também veda tortura e tratamentos ou castigos cruéis, desumanos ou degradantes.",
            "fonte": "(Constituição Federal, art. 5º, III; Declaração Universal dos Direitos Humanos, art. 5º)",
        },
    ],
    "Direitos Humanos — igualdade perante a lei": [
        {
            "pergunta": "De acordo com a Declaração Universal, todas as pessoas têm direito a:",
            "alternativas": ['Proteção desigual conforme sua nacionalidade', 'Igual proteção da lei, sem discriminação', 'Privilégios jurídicos por profissão'],
            "correta": 1,
            "explicacao": "O artigo 7º reconhece que todos são iguais perante a lei e têm direito, sem qualquer discriminação, a igual proteção legal.",
            "fonte": "(Declaração Universal dos Direitos Humanos, art. 7º)",
        },
    ],
    "Direitos Humanos — direito à nacionalidade": [
        {
            "pergunta": "Qual direito individual é reconhecido pelo artigo 15 da Declaração Universal?",
            "alternativas": ['Direito a escolher a nacionalidade de outra pessoa', 'Direito de retirar a nacionalidade de qualquer cidadão', 'Direito a uma nacionalidade'],
            "correta": 2,
            "explicacao": "O artigo 15 afirma que toda pessoa tem direito a uma nacionalidade e que ninguém será arbitrariamente privado dela nem do direito de mudá-la.",
            "fonte": "(Declaração Universal dos Direitos Humanos, art. 15)",
        },
    ],
    "Direitos Humanos — liberdade de pensamento e religião": [
        {
            "pergunta": "A liberdade de pensamento, consciência e religião inclui o direito de:",
            "alternativas": ['Mudar de religião ou crença e manifestá-la', 'Impor uma crença a todas as pessoas', 'Proibir publicamente todas as religiões'],
            "correta": 0,
            "explicacao": "O artigo 18 protege a liberdade de pensamento, consciência e religião, inclusive o direito de mudar de religião ou crença e de manifestá-la individual ou coletivamente, em público ou em particular.",
            "fonte": "(Declaração Universal dos Direitos Humanos, art. 18; Constituição Federal, art. 5º, VI)",
        },
    ],
    "Direitos Humanos — participação política": [
        {
            "pergunta": "Segundo a Declaração Universal, a vontade do povo deve ser expressa por eleições:",
            "alternativas": ['Realizadas somente quando o governo autorizar', 'Periódicas, legítimas e com sufrágio universal e igual', 'Restritas a quem possui patrimônio'],
            "correta": 1,
            "explicacao": "O artigo 21 prevê que a vontade do povo é a base da autoridade do governo e deve ser expressa em eleições periódicas e legítimas, por sufrágio universal e igual e voto secreto ou procedimento equivalente.",
            "fonte": "(Declaração Universal dos Direitos Humanos, art. 21)",
        },
    ],
    "Direitos Humanos — igualdade salarial": [
        {
            "pergunta": "De acordo com a Declaração Universal, pessoas que realizam trabalho igual têm direito a:",
            "alternativas": ['Remuneração inferior por motivo de origem', 'Remuneração definida apenas pela idade', 'Remuneração igual, sem discriminação'],
            "correta": 2,
            "explicacao": "O artigo 23 assegura remuneração igual por trabalho igual, sem qualquer distinção, e remuneração justa e satisfatória.",
            "fonte": "(Declaração Universal dos Direitos Humanos, art. 23, itens 2 e 3)",
        },
    ],
    "Direitos Humanos — repouso e lazer": [
        {
            "pergunta": "Qual direito relacionado ao descanso está previsto na Declaração Universal?",
            "alternativas": ['Repouso e lazer, incluindo férias periódicas remuneradas', 'Trabalho contínuo sem limite de jornada', 'Férias apenas para servidores públicos'],
            "correta": 0,
            "explicacao": "O artigo 24 reconhece o direito ao repouso e ao lazer, incluindo limitação razoável da jornada de trabalho e férias periódicas remuneradas.",
            "fonte": "(Declaração Universal dos Direitos Humanos, art. 24)",
        },
    ],
    "Direitos Humanos — direito à educação": [
        {
            "pergunta": "Segundo a Declaração Universal, qual deve ser o objetivo da educação?",
            "alternativas": ['Preparar exclusivamente para uma profissão', 'Promover o pleno desenvolvimento da personalidade e o respeito aos direitos humanos', 'Substituir a responsabilidade das famílias em todas as decisões'],
            "correta": 1,
            "explicacao": "O artigo 26 estabelece que a educação deve promover o pleno desenvolvimento da personalidade humana e fortalecer o respeito pelos direitos humanos e pelas liberdades fundamentais.",
            "fonte": "(Declaração Universal dos Direitos Humanos, art. 26, item 2)",
        },
    ],
    "Direitos Humanos — relações internacionais do Brasil": [
        {
            "pergunta": "Qual princípio rege as relações internacionais do Brasil, conforme a Constituição Federal?",
            "alternativas": ['Superioridade econômica entre os povos', 'Intervenção obrigatória em outros Estados', 'Prevalência dos direitos humanos'],
            "correta": 2,
            "explicacao": "A prevalência dos direitos humanos é um dos princípios expressamente previstos para reger as relações internacionais da República Federativa do Brasil.",
            "fonte": "(Constituição Federal, art. 4º, II)",
        },
    ],
    "Direitos Humanos — racismo": [
        {
            "pergunta": "Como a Constituição Federal classifica a prática do racismo?",
            "alternativas": ['Crime inafiançável e imprescritível, sujeito à pena de reclusão', 'Infração administrativa sujeita apenas a multa', 'Crime afiançável e prescritível'],
            "correta": 0,
            "explicacao": "O artigo 5º, inciso XLII, determina que a prática do racismo constitui crime inafiançável e imprescritível, sujeito à pena de reclusão, nos termos da lei.",
            "fonte": "(Constituição Federal, art. 5º, XLII)",
        },
    ],
    "Direitos Humanos — tratados internacionais": [
        {
            "pergunta": "Quando um tratado de direitos humanos pode ter equivalência a uma emenda constitucional no Brasil?",
            "alternativas": ['Quando aprovado por maioria simples em uma votação', 'Quando aprovado em cada Casa do Congresso, em dois turnos, por três quintos dos votos', 'Quando assinado apenas pelo presidente da República'],
            "correta": 1,
            "explicacao": "A Constituição prevê equivalência às emendas constitucionais para tratados e convenções internacionais sobre direitos humanos aprovados, em cada Casa do Congresso Nacional, em dois turnos, por três quintos dos votos dos respectivos membros.",
            "fonte": "(Constituição Federal, art. 5º, § 3º)",
        },
    ],
    "Direitos Humanos — liberdade de crença no Brasil": [
        {
            "pergunta": "Além da liberdade de consciência e de crença, o que a Constituição assegura?",
            "alternativas": ['A adoção de uma religião oficial obrigatória', 'A proibição de assistência religiosa em internações coletivas', 'O livre exercício dos cultos religiosos, na forma da lei'],
            "correta": 2,
            "explicacao": "A Constituição assegura a liberdade de consciência e crença e o livre exercício dos cultos religiosos, protegendo, na forma da lei, os locais de culto e suas liturgias.",
            "fonte": "(Constituição Federal, art. 5º, VI)",
        },
    ],
}

LEGENDAS = {
    "Direitos Humanos — dignidade e igualdade": "Questão de Direitos Humanos: dignidade e igualdade. Responda antes da explicação. #JuhQuiz #DireitosHumanos #Concursos #Estudos",
    "Direitos Humanos — vida, liberdade e segurança": "Questão de Direitos Humanos: vida, liberdade e segurança. #JuhQuiz #DireitosHumanos #Concursos #Estudos",
    "Direitos Humanos — proibição da escravidão": "Questão de Direitos Humanos: proibição da escravidão. #JuhQuiz #DireitosHumanos #Concursos #Estudos",
    "Direitos Humanos — tortura e tratamento degradante": "Questão de Direitos Humanos: proteção contra tortura. #JuhQuiz #DireitosHumanos #Concursos #Estudos",
    "Direitos Humanos — igualdade perante a lei": "Questão de Direitos Humanos: igualdade perante a lei. #JuhQuiz #DireitosHumanos #Concursos #Estudos",
    "Direitos Humanos — direito à nacionalidade": "Questão de Direitos Humanos: direito à nacionalidade. #JuhQuiz #DireitosHumanos #Concursos #Estudos",
    "Direitos Humanos — liberdade de pensamento e religião": "Questão de Direitos Humanos: liberdade de pensamento e religião. #JuhQuiz #DireitosHumanos #Concursos #Estudos",
    "Direitos Humanos — participação política": "Questão de Direitos Humanos: participação política. #JuhQuiz #DireitosHumanos #Concursos #Estudos",
    "Direitos Humanos — igualdade salarial": "Questão de Direitos Humanos: igualdade salarial. #JuhQuiz #DireitosHumanos #Concursos #Estudos",
    "Direitos Humanos — repouso e lazer": "Questão de Direitos Humanos: repouso e lazer. #JuhQuiz #DireitosHumanos #Concursos #Estudos",
    "Direitos Humanos — direito à educação": "Questão de Direitos Humanos: direito à educação. #JuhQuiz #DireitosHumanos #Concursos #Estudos",
    "Direitos Humanos — relações internacionais do Brasil": "Questão de Direitos Humanos: Constituição e relações internacionais. #JuhQuiz #DireitosHumanos #Concursos #Estudos",
    "Direitos Humanos — racismo": "Questão de Direitos Humanos: o que diz a Constituição sobre racismo? #JuhQuiz #DireitosHumanos #Concursos #Estudos",
    "Direitos Humanos — tratados internacionais": "Questão de Direitos Humanos: tratados e Constituição. #JuhQuiz #DireitosHumanos #Concursos #Estudos",
    "Direitos Humanos — liberdade de crença no Brasil": "Questão de Direitos Humanos: liberdade de crença no Brasil. #JuhQuiz #DireitosHumanos #Concursos #Estudos",
}
