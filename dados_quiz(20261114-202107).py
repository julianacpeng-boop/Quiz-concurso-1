# Juh Quiz — Corpo humano: fatos que parecem mentira
# Questões autorais de curiosidades científicas, uma pergunta por vídeo.
# A fonte curta é exibida entre parênteses pelo gerar_quiz.py.

CAPA_SEGUNDOS = 2

QUIZZES = {
    "Corpo humano — esqueleto adulto": [{
        "pergunta": "Quantos ossos tem, em geral, o esqueleto de uma pessoa adulta?",
        "alternativas": ["186", "206", "226"],
        "correta": 1,
        "explicacao": "O esqueleto adulto costuma ser descrito com 206 ossos. Durante o crescimento, alguns ossos se fundem, por isso o total não é igual em todas as fases da vida.",
        "fonte": "MedlinePlus/NIH, esqueleto",
    }],
    "Corpo humano — menor osso": [{
        "pergunta": "Qual é o menor osso do corpo humano?",
        "alternativas": ["Martelo", "Bigorna", "Estribo"],
        "correta": 2,
        "explicacao": "O estribo fica no ouvido médio. Ele faz parte da cadeia de três ossículos que transmite vibrações sonoras até o ouvido interno.",
        "fonte": "NCBI Bookshelf, ouvido médio",
    }],
    "Corpo humano — córnea": [{
        "pergunta": "Qual afirmação sobre a córnea é verdadeira?",
        "alternativas": ["Ela não tem vasos sanguíneos e é muito sensível", "Ela não tem nervos e quase não sente toque", "Ela recebe oxigênio somente pelo sangue"],
        "correta": 0,
        "explicacao": "A córnea não tem vasos sanguíneos, o que ajuda a mantê-la transparente. Ela tem muitas terminações nervosas e recebe nutrientes das lágrimas e do humor aquoso.",
        "fonte": "NCBI Bookshelf, anatomia do olho",
    }],
    "Corpo humano — pele": [{
        "pergunta": "Qual é o maior órgão do corpo humano?",
        "alternativas": ["Fígado", "Pele", "Pulmão"],
        "correta": 1,
        "explicacao": "A pele cobre a superfície externa do corpo, funciona como barreira de proteção e também participa da regulação da temperatura.",
        "fonte": "NIH/NCBI, anatomia da pele",
    }],
    "Corpo humano — estômago": [{
        "pergunta": "O que ajuda a proteger a parede do estômago do ácido e das enzimas digestivas?",
        "alternativas": ["Uma camada de gordura que reveste o órgão", "A saliva que chega pelo esôfago", "Uma barreira de muco e bicarbonato"],
        "correta": 2,
        "explicacao": "Células da mucosa produzem muco e bicarbonato. Essa barreira reduz o contato do ácido e da pepsina com o revestimento do estômago.",
        "fonte": "NCBI Bookshelf, fisiologia gástrica",
    }],
    "Corpo humano — saliva": [{
        "pergunta": "A saliva começa a digestão de qual tipo de alimento?",
        "alternativas": ["Amido, um carboidrato", "Proteínas", "Gorduras"],
        "correta": 0,
        "explicacao": "A saliva contém amilase, uma enzima que inicia a quebra do amido ainda na boca. A digestão continua em outras partes do sistema digestório.",
        "fonte": "NIDDK/NIH, digestão",
    }],
    "Corpo humano — batimentos cardíacos": [{
        "pergunta": "O que inicia o sinal elétrico normal que ajuda a organizar cada batimento do coração?",
        "alternativas": ["Um impulso que começa no estômago", "Células marca-passo do nó sinoatrial", "Um sinal produzido pelos pulmões"],
        "correta": 1,
        "explicacao": "Em condições normais, o sinal elétrico começa no nó sinoatrial, formado por células marca-passo, e se espalha pelo coração para coordenar os batimentos.",
        "fonte": "NHLBI/NIH, batimento cardíaco",
    }],
    "Corpo humano — glóbulos vermelhos": [{
        "pergunta": "O que é curioso sobre uma hemácia humana madura?",
        "alternativas": ["Ela tem dois núcleos", "Ela produz anticorpos", "Ela não tem núcleo"],
        "correta": 2,
        "explicacao": "A hemácia humana madura perde o núcleo durante sua formação. Isso deixa mais espaço para hemoglobina, que transporta oxigênio.",
        "fonte": "NCBI Bookshelf, células do sangue",
    }],
    "Corpo humano — vida das hemácias": [{
        "pergunta": "Por quanto tempo, aproximadamente, uma hemácia costuma circular no sangue?",
        "alternativas": ["Cerca de 120 dias", "Cerca de 12 dias", "Cerca de 12 meses"],
        "correta": 0,
        "explicacao": "Uma hemácia vive em média cerca de 120 dias. Depois, células especializadas a removem e a medula óssea produz novas hemácias.",
        "fonte": "MedlinePlus/NIH, sangue",
    }],
    "Corpo humano — fígado": [{
        "pergunta": "O fígado pode recuperar parte do seu volume após uma remoção cirúrgica parcial?",
        "alternativas": ["Não; o fígado não cresce novamente", "Sim; o tecido remanescente pode aumentar e restaurar volume", "Sim; ele sempre volta a ser idêntico ao órgão original"],
        "correta": 1,
        "explicacao": "O fígado tem uma capacidade notável de regeneração e pode recuperar volume após uma remoção parcial. Isso não significa que qualquer lesão seja reversível ou que o órgão volte a ser idêntico em todos os detalhes.",
        "fonte": "NIH/NIDDK, regeneração hepática",
    }],
    "Corpo humano — rins": [{
        "pergunta": "Em adultos saudáveis, quanto os rins filtram aproximadamente por dia e quanto disso costuma virar urina?",
        "alternativas": ["14 litros filtrados e 10 litros de urina", "14 litros filtrados e 1 litro de urina", "Cerca de 140 litros filtrados e 1 a 2 litros de urina"],
        "correta": 2,
        "explicacao": "Os rins filtram repetidamente grande volume de sangue. Grande parte da água e das substâncias úteis retorna ao sangue; em geral, cerca de 1 a 2 litros terminam como urina por dia.",
        "fonte": "NIDDK/NIH, funcionamento dos rins",
    }],
    "Corpo humano — cérebro": [{
        "pergunta": "Em repouso, que parcela aproximada da energia do corpo é consumida pelo cérebro?",
        "alternativas": ["Cerca de 20%", "Cerca de 2%", "Cerca de 60%"],
        "correta": 0,
        "explicacao": "Embora represente uma pequena fração do peso corporal, o cérebro consome aproximadamente 20% da energia do corpo em repouso.",
        "fonte": "NCBI Bookshelf, fisiologia cerebral",
    }],
    "Corpo humano — soluço": [{
        "pergunta": "O soluço costuma envolver qual sequência?",
        "alternativas": ["Contração do coração e fechamento do esôfago", "Movimento involuntário do diafragma e fechamento rápido das cordas vocais", "Contração do estômago e abertura da traqueia"],
        "correta": 1,
        "explicacao": "O soluço começa com um movimento involuntário do diafragma. Em seguida, as cordas vocais se fecham rapidamente, produzindo o som característico.",
        "fonte": "MedlinePlus/NIH, soluços",
    }],
    "Corpo humano — arrepios": [{
        "pergunta": "O que faz os pelos se levantarem e a pele ficar arrepiada?",
        "alternativas": ["O inchaço das glândulas sudoríparas", "A contração dos músculos do coração", "A contração de pequenos músculos ligados aos folículos dos pelos"],
        "correta": 2,
        "explicacao": "Pequenos músculos chamados eretores do pelo se contraem e puxam os folículos. Isso provoca a piloereção, conhecida como arrepio ou pele arrepiada.",
        "fonte": "NIH/NCBI, folículo piloso",
    }],
    "Corpo humano — olfato e sabor": [{
        "pergunta": "Por que a comida pode parecer sem sabor quando estamos com o nariz congestionado?",
        "alternativas": ["Porque o olfato contribui para perceber o sabor dos alimentos", "Porque a língua deixa de produzir saliva", "Porque o nariz controla a temperatura da comida"],
        "correta": 0,
        "explicacao": "A percepção do sabor combina paladar, aroma, textura e temperatura. Quando o olfato fica reduzido, muitos alimentos parecem sem graça.",
        "fonte": "NIDCD/NIH, paladar e olfato",
    }],
}

LEGENDAS = {
    tema: f"{tema}: fatos do corpo humano que parecem mentira!\n\n#JuhQuiz #CorpoHumano #Curiosidades #Saude"
    for tema in QUIZZES
}

FONTES_COMPLETAS = {
    "Esqueleto adulto — MedlinePlus/NIH": "https://medlineplus.gov/ency/imagepages/9065.htm",
    "Estribo — NCBI Bookshelf": "https://www.ncbi.nlm.nih.gov/books/NBK482338/",
    "Córnea — NCBI Bookshelf": "https://www.ncbi.nlm.nih.gov/books/NBK470340/",
    "Pele — NIH/NCBI Bookshelf": "https://www.ncbi.nlm.nih.gov/books/NBK470464/",
    "Proteção do estômago — NCBI Bookshelf": "https://www.ncbi.nlm.nih.gov/books/NBK535425/",
    "Saliva e digestão — NIDDK/NIH": "https://www.niddk.nih.gov/health-information/digestive-diseases/digestive-system-how-it-works",
    "Sinais elétricos cardíacos — NHLBI/NIH": "https://www.nhlbi.nih.gov/health/heart/heart-beats",
    "Hemácias sem núcleo — NCBI Bookshelf": "https://www.ncbi.nlm.nih.gov/books/NBK279392/",
    "Vida das hemácias — MedlinePlus/NIH": "https://medlineplus.gov/blood.html",
    "Regeneração do fígado — NIH/NIDDK": "https://beta.nih.gov/news-events/nih-research-matters/cells-maintain-repair-liver-identified",
    "Filtragem dos rins — NIDDK/NIH": "https://www.niddk.nih.gov/health-information/kidney-disease/kidneys-how-they-work",
    "Energia cerebral — NCBI Bookshelf": "https://www.ncbi.nlm.nih.gov/books/NBK551718/",
    "Soluços — MedlinePlus/NIH": "https://medlineplus.gov/hiccups.html",
    "Arrepios — NIH/NCBI Bookshelf": "https://www.ncbi.nlm.nih.gov/books/NBK470321/",
    "Paladar e olfato — NIDCD/NIH": "https://www.nidcd.nih.gov/health/taste-disorders",
}
