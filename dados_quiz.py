# Juh Quiz — Professor de Biologia
# Questões autorais adaptadas de uma prova oficial de concurso; uma pergunta por vídeo.
# A fonte curta é exibida entre parênteses pelo gerar_quiz.py.

CAPA_SEGUNDOS = 2

QUIZZES = {
    "Professor de Biologia — controle microbiano": [{
        "pergunta": "Quais agentes químicos podem controlar microrganismos por ruptura da membrana plasmática e desnaturação de proteínas?",
        "alternativas": ["Bisfenóis e álcoois", "Aldeídos e sabões", "Halogênios e nitratos"],
        "correta": 0,
        "explicacao": "Bisfenóis e álcoois podem comprometer a membrana plasmática e desnaturar proteínas, prejudicando funções celulares essenciais.",
        "fonte": "IFS-SE, IV/UFG, 2024, q. 34",
    }],
    "Professor de Biologia — fungos": [{
        "pergunta": "Como se chamam as estruturas de resistência de fungos formadas por conjuntos compactos de hifas?",
        "alternativas": ["Ascósporos", "Esclerotos", "Esporangiósporos"],
        "correta": 1,
        "explicacao": "Esclerotos são massas compactas de hifas que ajudam alguns fungos a sobreviver a condições desfavoráveis até o ambiente melhorar.",
        "fonte": "IFS-SE, IV/UFG, 2024, q. 36",
    }],
    "Professor de Biologia — tecidos animais": [{
        "pergunta": "Quais filamentos do citoesqueleto participam, nessa ordem, da zônula aderente e dos desmossomos?",
        "alternativas": ["Microtúbulos e microfilamentos", "Filamentos intermediários e microfilamentos", "Microfilamentos e filamentos intermediários"],
        "correta": 2,
        "explicacao": "A zônula aderente se associa a filamentos de actina, que são microfilamentos. Os desmossomos se conectam a filamentos intermediários.",
        "fonte": "IFS-SE, IV/UFG, 2024, q. 38",
    }],
    "Professor de Biologia — sistema nervoso": [{
        "pergunta": "Quais células fazem a defesa imunológica e produzem mielina no sistema nervoso central, respectivamente?",
        "alternativas": ["Astrócitos e células de Schwann", "Micróglia e oligodendrócitos", "Oligodendrócitos e astrócitos"],
        "correta": 1,
        "explicacao": "A micróglia atua na defesa imunológica do sistema nervoso central. Os oligodendrócitos formam a mielina nesse sistema.",
        "fonte": "IFS-SE, IV/UFG, 2024, q. 41",
    }],
    "Professor de Biologia — protozoários": [{
        "pergunta": "Qual espécie de Entamoeba pode apresentar forma magna patogênica com hemácias fagocitadas?",
        "alternativas": ["Entamoeba coli", "Entamoeba hartmanni", "Entamoeba histolytica"],
        "correta": 2,
        "explicacao": "A presença de hemácias fagocitadas nos trofozoítos é uma característica associada à forma invasiva de Entamoeba histolytica.",
        "fonte": "IFS-SE, IV/UFG, 2024, q. 45",
    }],
    "Professor de Biologia — tecidos vegetais": [{
        "pergunta": "Quais são os três sistemas de tecidos básicos das plantas?",
        "alternativas": ["Dérmico, fundamental e vascular", "Meristemático, conjuntivo e sanguíneo", "Hipodérmico, parenquimático e muscular"],
        "correta": 0,
        "explicacao": "O sistema dérmico reveste a planta; o fundamental reúne tecidos como parênquima, colênquima e esclerênquima; e o vascular inclui xilema e floema.",
        "fonte": "IFS-SE, IV/UFG, 2024, q. 46",
    }],
    "Professor de Biologia — briófitas": [{
        "pergunta": "Qual característica diferencia as plantas vasculares das briófitas?",
        "alternativas": ["Presença de embrião multicelular", "Presença de tecidos vasculares, como xilema e floema", "Reprodução exclusivamente por sementes"],
        "correta": 1,
        "explicacao": "Plantas vasculares possuem xilema e floema para conduzir água e substâncias. Briófitas não têm esses tecidos condutores verdadeiros.",
        "fonte": "IFS-SE, IV/UFG, 2024, q. 48",
    }],
    "Professor de Biologia — reprodução vegetal": [{
        "pergunta": "Por que samambaias e outras plantas vasculares sem sementes ainda dependem de água para a fecundação?",
        "alternativas": ["Porque os esporófitos nadam até os gametófitos", "Porque os megásporos nadam até os micrósporos", "Porque os anterozoides flagelados precisam nadar até a oosfera"],
        "correta": 2,
        "explicacao": "Os anterozoides são gametas masculinos móveis. A água permite que cheguem à oosfera para ocorrer a fecundação.",
        "fonte": "IFS-SE, IV/UFG, 2024, q. 49",
    }],
    "Professor de Biologia — angiospermas": [{
        "pergunta": "A qual família botânica pertencem plantas como girassóis e margaridas, cujas flores se organizam em capítulos?",
        "alternativas": ["Piperaceae", "Rutaceae", "Asteraceae"],
        "correta": 2,
        "explicacao": "Girassóis e margaridas pertencem à família Asteraceae. O capítulo reúne muitas flores pequenas em uma estrutura que parece uma única flor.",
        "fonte": "IFS-SE, IV/UFG, 2024, q. 51",
    }],
    "Professor de Biologia — monocotiledôneas": [{
        "pergunta": "Qual característica corresponde às monocotiledôneas?",
        "alternativas": ["Dois cotilédones e crescimento secundário generalizado", "Um cotilédone no embrião da semente", "Ausência de flores e de sementes"],
        "correta": 1,
        "explicacao": "O embrião das monocotiledôneas apresenta um cotilédone. Grãos, como milho e arroz, são exemplos desse grupo.",
        "fonte": "IFS-SE, IV/UFG, 2024, q. 53",
    }],
    "Professor de Biologia — artrópodes": [{
        "pergunta": "Qual processo permite que artrópodes cresçam, apesar de terem um exoesqueleto rígido?",
        "alternativas": ["Ecdise, ou troca periódica da cutícula", "Fusão dos segmentos do corpo", "Produção contínua de uma concha interna"],
        "correta": 0,
        "explicacao": "Na ecdise, o animal troca a cutícula antiga por outra maior. O corpo pode crescer enquanto o novo exoesqueleto ainda está flexível.",
        "fonte": "IFS-SE, IV/UFG, 2024, q. 54",
    }],
    "Professor de Biologia — ecologia": [{
        "pergunta": "Qual equipamento é uma armadilha passiva usada para amostrar insetos alados?",
        "alternativas": ["Rede entomológica", "Armadilha Malaise", "Aspirador bucal"],
        "correta": 1,
        "explicacao": "A armadilha Malaise intercepta insetos em voo e os conduz a um recipiente coletor, sem que o pesquisador precise capturá-los ativamente.",
        "fonte": "IFS-SE, IV/UFG, 2024, q. 55",
    }],
    "Professor de Biologia — nematódeos": [{
        "pergunta": "Qual filo reúne animais com pseudoceloma, cutícula e musculatura apenas longitudinal, como descrito na questão?",
        "alternativas": ["Platyhelminthes", "Annelida", "Nematoda"],
        "correta": 2,
        "explicacao": "Nematódeos possuem pseudoceloma e cutícula que sofre ecdise. Sua musculatura é predominantemente longitudinal.",
        "fonte": "IFS-SE, IV/UFG, 2024, q. 56",
    }],
    "Professor de Biologia — serpentes": [{
        "pergunta": "Qual estrutura é característica de muitas serpentes da família Viperidae, como jararacas e cascavéis?",
        "alternativas": ["Fosseta loreal", "Presa proteróglifa", "Presa opistóglifa"],
        "correta": 0,
        "explicacao": "A fosseta loreal é um órgão sensorial entre o olho e a narina, capaz de detectar radiação infravermelha e auxiliar na localização de presas.",
        "fonte": "IFS-SE, IV/UFG, 2024, q. 59",
    }],
    "Professor de Biologia — peixes": [{
        "pergunta": "Qual característica é associada aos peixes teleósteos?",
        "alternativas": ["Ausência de opérculo ósseo", "Protrusão da mandíbula para capturar alimento", "Esqueleto formado apenas por cartilagem"],
        "correta": 1,
        "explicacao": "Muitos teleósteos conseguem projetar a mandíbula para a frente, ampliando a abertura da boca e facilitando a captura de alimento.",
        "fonte": "IFS-SE, IV/UFG, 2024, q. 60",
    }],
}

LEGENDAS = {
    tema: f"{tema}: desafio de concurso!\n\n#JuhQuiz #Biologia #Concursos #Professor"
    for tema in QUIZZES
}

FONTES_COMPLETAS = {
    "IFS-SE, IV/UFG, 2024": "Instituto Federal de Sergipe — Concurso Público para Professor do Ensino Básico, Técnico e Tecnológico, área Biologia. Prova objetiva aplicada em 21/07/2024. Prova oficial: https://sistemas.institutoverbena.ufg.br/2024/concurso-ifs-docente/sistema/provas_gabaritos/prova/BIOLOGIA.pdf",
}
