# Juh Quiz — Ciência e conhecimento em alta — 15 questões
# Questões autorais, uma pergunta por vídeo.
# A fonte curta é exibida entre parênteses pelo gerar_quiz.py.

CAPA_SEGUNDOS = 2

QUIZZES = {
    "Ciência em alta — voz clonada por IA": [{
        "pergunta": "Uma voz familiar liga pedindo dinheiro com urgência. Qual atitude é mais segura?",
        "alternativas": ["Transferir porque a voz parece conhecida", "Desligar e ligar para um número que você já conhece", "Pedir que a pessoa envie um áudio com o próprio nome"],
        "correta": 1,
        "explicacao": "Ferramentas de inteligência artificial podem imitar uma voz usando trechos curtos de áudio. A FTC recomenda verificar a história por outro canal, ligando para um número conhecido da pessoa.",
        "fonte": "FTC, clonagem de voz",
    }],
    "Ciência em alta — supercomputador Jaci": [{
        "pergunta": "O que o modelo MONAN, operado no supercomputador Jaci do INPE, ajuda a fazer?",
        "alternativas": ["Criar imagens de satélite em tempo real para celulares", "Produzir previsões numéricas do tempo", "Controlar remotamente os satélites brasileiros"],
        "correta": 1,
        "explicacao": "O INPE iniciou a operação do MONAN no supercomputador Jaci para produzir previsões numéricas do tempo. O sistema oferece previsões globais de médio prazo, de até 11 dias.",
        "fonte": "INPE/MCTI, MONAN/Jaci",
    }],
    "Ciência em alta — El Niño": [{
        "pergunta": "O El Niño está associado principalmente a qual mudança no oceano?",
        "alternativas": ["Resfriamento permanente do Atlântico Sul", "Aumento da salinidade no Mar Mediterrâneo", "Aquecimento anormal das águas do Pacífico equatorial"],
        "correta": 2,
        "explicacao": "O El Niño é a fase quente de um padrão oceano-atmosfera ligado ao aquecimento das águas superficiais do Pacífico equatorial central e oriental. Ele pode alterar padrões de chuva e temperatura em várias regiões.",
        "fonte": "NOAA, El Niño",
    }],
    "Ciência em alta — IA e drones ambientais": [{
        "pergunta": "O que prevê o projeto de lei que avançou no Senado sobre IA e drones ambientais?",
        "alternativas": ["Usar dados e tecnologias para monitorar riscos ambientais", "Substituir a fiscalização ambiental por decisões automáticas", "Autorizar drones a aplicar multas sem análise humana"],
        "correta": 0,
        "explicacao": "A proposta prevê reunir informações de satélites, sensores, drones e sistemas de IA para monitorar riscos como incêndios e desmatamento. O projeto ainda seguirá para análise de outra comissão; alertas automatizados não substituiriam a validação humana para sanções.",
        "fonte": "Senado, PL 1.297/2026",
    }],
    "Ciência em alta — comer skincare": [{
        "pergunta": "A trend diz que comer gelatina substitui o skincare. O que as pesquisas permitem afirmar?",
        "alternativas": ["Gelatina comum garante o mesmo efeito de qualquer cosmético", "Estudos de suplementos de colágeno têm resultados variados e não provam que gelatina substitua cuidados com a pele", "A pele absorve diretamente o colágeno ingerido sem digestão"],
        "correta": 1,
        "explicacao": "Há pesquisas sobre suplementos específicos de peptídeos de colágeno, mas os resultados e a qualidade das evidências variam. Isso não demonstra que comer gelatina comum substitua cuidados dermatológicos ou produza um resultado garantido.",
        "fonte": "PubMed, colágeno oral",
    }],
    "Ciência em alta — calor e corpo": [{
        "pergunta": "Por que a umidade alta pode dificultar o resfriamento do corpo pelo suor?",
        "alternativas": ["Porque o suor deixa de ser produzido", "Porque a umidade aumenta a temperatura dos músculos", "Porque o suor evapora mais devagar e remove menos calor"],
        "correta": 2,
        "explicacao": "A evaporação do suor ajuda a retirar calor da pele. Quando o ar está muito úmido, o suor evapora mais lentamente e o corpo pode ter mais dificuldade para se resfriar.",
        "fonte": "CDC/NIOSH, calor",
    }],
    "Ciência em alta — microplásticos": [{
        "pergunta": "O que é mais correto dizer hoje sobre microplásticos e saúde humana?",
        "alternativas": ["Há lacunas importantes e a avaliação dos riscos ainda precisa de mais pesquisas", "Já foi provado que qualquer quantidade causa doença", "Está provado que microplásticos não têm nenhum efeito possível"],
        "correta": 0,
        "explicacao": "A OMS revisou evidências sobre exposição por água, alimentos e ar e apontou incertezas e lacunas de pesquisa. Encontrar partículas não significa, por si só, que já se conheça o risco de cada exposição para a saúde.",
        "fonte": "OMS, microplásticos",
    }],
    "Ciência em alta — luz no fundo do mar": [{
        "pergunta": "Como alguns animais marinhos produzem luz própria?",
        "alternativas": ["Acumulando luz solar durante toda a vida", "Por uma reação química chamada bioluminescência", "Refletindo luz de vulcões submarinos"],
        "correta": 1,
        "explicacao": "A bioluminescência é a produção de luz por uma reação química no organismo. No oceano, diferentes animais usam essa luz em comportamentos como comunicação, defesa ou atração de presas.",
        "fonte": "NOAA, bioluminescência",
    }],
    "Ciência em alta — falsas memórias": [{
        "pergunta": "A memória funciona como uma gravação perfeita dos acontecimentos?",
        "alternativas": ["Sim, cada lembrança fica armazenada sem mudanças", "Sim, mas só para acontecimentos da infância", "Não. Ao lembrar, o cérebro reconstrói informações e pode distorcê-las"],
        "correta": 2,
        "explicacao": "A memória não é uma reprodução idêntica de uma gravação. A pesquisa descreve a lembrança como um processo de reconstrução, que pode incorporar erros ou informações posteriores.",
        "fonte": "PubMed, memória",
    }],
    "Ciência em alta — corpo no espaço": [{
        "pergunta": "Por que o rosto de um astronauta pode parecer mais inchado em microgravidade?",
        "alternativas": ["Parte dos fluidos do corpo se desloca em direção à cabeça", "O sangue deixa de circular nas pernas", "Os ossos do rosto absorvem água do ar"],
        "correta": 0,
        "explicacao": "Em microgravidade, os fluidos corporais se deslocam em direção à cabeça. A NASA acompanha esse efeito, que também pode estar relacionado a mudanças na pressão dos olhos e na visão.",
        "fonte": "NASA, corpo no espaço",
    }],
    "Ciência em alta — previsão de terremotos": [{
        "pergunta": "A ciência consegue prever exatamente a data, o local e a magnitude de um grande terremoto?",
        "alternativas": ["Sim, com semanas de antecedência", "Não; é possível estimar probabilidades e riscos, mas não prever exatamente os três dados", "Sim, observando o comportamento dos animais"],
        "correta": 1,
        "explicacao": "Segundo o USGS, ainda não é possível prever exatamente quando, onde e com que magnitude ocorrerá um grande terremoto. Cientistas calculam probabilidades de risco para áreas e períodos definidos.",
        "fonte": "USGS, terremotos",
    }],
    "Ciência em alta — mitos sobre raios": [{
        "pergunta": "Um raio só atinge o objeto mais alto por perto?",
        "alternativas": ["Sim, ele sempre escolhe o ponto mais alto", "Sim, desde que o objeto seja de metal", "Não. Pode atingir o solo em um campo aberto, por exemplo"],
        "correta": 2,
        "explicacao": "Objetos altos e isolados são atingidos com frequência, mas isso não é uma regra absoluta. O Serviço Nacional de Meteorologia dos EUA informa que um raio também pode atingir um campo aberto.",
        "fonte": "NWS, raios",
    }],
    "Ciência em alta — como vacinas funcionam": [{
        "pergunta": "Como uma vacina ajuda o sistema imunológico a se preparar?",
        "alternativas": ["Apresenta um antígeno ou imita uma infecção para ensinar defesas específicas", "Elimina todos os microrganismos do corpo antes da exposição", "Impede que o corpo produza qualquer resposta inflamatória"],
        "correta": 0,
        "explicacao": "As vacinas envolvem as defesas naturais do corpo e ajudam o sistema imunológico a reconhecer um agente específico sem os perigos de uma infecção completa, conforme o tipo de vacina.",
        "fonte": "CDC, vacinas",
    }],
    "Ciência em alta — resistência antimicrobiana": [{
        "pergunta": "Na resistência antimicrobiana, quem se torna resistente aos medicamentos?",
        "alternativas": ["Os microrganismos, que deixam de responder a certos medicamentos", "O corpo humano, que aprende a ignorar os remédios", "As vacinas, que passam a causar infecções"],
        "correta": 0,
        "explicacao": "A resistência ocorre quando microrganismos, como bactérias, mudam e deixam de responder a medicamentos. O uso excessivo ou inadequado de antimicrobianos contribui para o problema.",
        "fonte": "OMS, resistência",
    }],
    "Ciência em alta — energia solar": [{
        "pergunta": "O que acontece dentro de uma célula fotovoltaica quando a luz solar é absorvida?",
        "alternativas": ["A luz é armazenada como calor e vira vento", "A água da placa se transforma em eletricidade", "A energia da luz é convertida em energia elétrica"],
        "correta": 2,
        "explicacao": "Materiais semicondutores nas células fotovoltaicas absorvem energia da luz e a convertem em eletricidade. Um inversor pode transformar a corrente contínua gerada pelos módulos em corrente alternada para uso doméstico.",
        "fonte": "DOE, energia solar",
    }],
}

LEGENDAS = {
    tema: f"{tema}: teste seus conhecimentos de ciência!\n\n#JuhQuiz #Ciencia #Curiosidades #Conhecimento"
    for tema in QUIZZES
}

FONTES_COMPLETAS = {
    "IA e clonagem de voz — FTC Consumer Advice": "https://consumer.ftc.gov/consumer-alerts/2024/04/fighting-back-against-harmful-voice-cloning",
    "MONAN e supercomputador Jaci — INPE/MCTI": "https://www.gov.br/inpe/pt-br/assuntos/ultimas-noticias/inpe-anuncia-inicio-da-operacao-do-monan-para-previsoes-de-tempo-1",
    "El Niño — NOAA, Understanding El Niño & ENSO": "https://www.noaa.gov/understanding-el-nino",
    "Projeto sobre IA e drones ambientais — Senado Notícias, PL 1.297/2026": "https://www12.senado.leg.br/noticias/materias/2026/11/04/avanca-projeto-que-preve-uso-de-ia-e-drones-na-protecao-ambiental",
    "Colágeno oral e pele — revisões sistemáticas no PubMed": "https://pubmed.ncbi.nlm.nih.gov/40324552/ ; https://pmc.ncbi.nlm.nih.gov/articles/PMC13370842/",
    "Calor, suor e evaporação — CDC/NIOSH": "https://www.cdc.gov/niosh/bulletin/2011/heat2.html",
    "Microplásticos e lacunas de evidência — OMS": "https://www.who.int/publications/i/item/9789240054608",
    "Bioluminescência marinha — NOAA Ocean Exploration": "https://oceanexplorer.noaa.gov/ocean-fact/bioluminescence/",
    "Memória reconstrutiva e falsas lembranças — revisão no PubMed": "https://pubmed.ncbi.nlm.nih.gov/22827854/",
    "Efeitos da microgravidade no corpo — NASA": "https://www.nasa.gov/humans-in-space/the-human-body-in-space/",
    "Limites da previsão de terremotos — USGS": "https://www.usgs.gov/faqs/can-you-predict-earthquakes",
    "Raios podem atingir áreas abertas — National Weather Service": "https://www.weather.gov/source/zhu/ZHU_Training_Page/lightning_stuff/lightning2/lightning.html",
    "Como as vacinas funcionam — CDC": "https://www.cdc.gov/vaccines/basics/explaining-how-vaccines-work.html",
    "Resistência antimicrobiana — OMS": "https://www.who.int/news-room/fact-sheets/detail/antimicrobial-resistance",
    "Energia fotovoltaica — U.S. Department of Energy": "https://www.energy.gov/cmei/systems/solar-photovoltaic-technology-basics",
}
