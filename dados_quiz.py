# Juh Quiz — Corpo humano: curiosidades que surpreendem — Parte 2
# Questões autorais de curiosidades científicas, uma pergunta por vídeo.
# A fonte curta é exibida entre parênteses pelo gerar_quiz.py.

CAPA_SEGUNDOS = 2

QUIZZES = {
    "Corpo humano — dor no cérebro": [{
        "pergunta": "Qual parte não sente dor diretamente, embora estruturas ao redor possam causar dor de cabeça?",
        "alternativas": ["O próprio tecido cerebral", "As meninges", "Os nervos do couro cabeludo"],
        "correta": 0,
        "explicacao": "O tecido cerebral não possui terminações sensíveis à dor. A dor de cabeça pode surgir quando estruturas ao redor, como meninges e vasos, ativam nervos sensíveis à dor.",
        "fonte": "NINDS/NIH, dor de cabeça",
    }],
    "Corpo humano — esmalte dos dentes": [{
        "pergunta": "Qual é a substância mais dura do corpo humano?",
        "alternativas": ["A dentina", "O esmalte dentário", "O osso do fêmur"],
        "correta": 1,
        "explicacao": "O esmalte é a camada externa que cobre a coroa do dente. Seu alto conteúdo mineral faz dele a substância mais dura do corpo humano.",
        "fonte": "NCBI Bookshelf, dente",
    }],
    "Corpo humano — pupila": [{
        "pergunta": "A pupila é uma estrutura sólida ou uma abertura?",
        "alternativas": ["Uma lente transparente", "Uma parte colorida do olho", "Uma abertura no centro da íris"],
        "correta": 2,
        "explicacao": "A pupila é uma abertura por onde a luz entra no olho. A íris, que é a parte colorida, muda o tamanho dessa abertura para controlar a entrada de luz.",
        "fonte": "NEI/NIH, visão",
    }],
    "Corpo humano — pulmão esquerdo": [{
        "pergunta": "Por que o pulmão esquerdo é um pouco menor que o direito?",
        "alternativas": ["Para deixar espaço para o coração", "Porque tem menos alvéolos em todas as pessoas", "Porque recebe menos sangue"],
        "correta": 0,
        "explicacao": "O coração ocupa parte do espaço no lado esquerdo do tórax. Por isso, o pulmão esquerdo é ligeiramente menor e tem dois lobos, enquanto o direito tem três.",
        "fonte": "NHLBI/NIH, pulmões",
    }],
    "Corpo humano — nariz e respiração": [{
        "pergunta": "O que a cavidade nasal faz com o ar que inspiramos?",
        "alternativas": ["Retira todo o oxigênio do ar", "Ajuda a aquecer e umidificar o ar", "Transforma o ar em gás carbônico"],
        "correta": 1,
        "explicacao": "Ao passar pela cavidade nasal, o ar é aquecido e umidificado. Isso ajuda a preparar o ar antes de ele seguir pelas vias respiratórias.",
        "fonte": "NCBI Bookshelf, nariz",
    }],
    "Corpo humano — bile": [{
        "pergunta": "Qual alternativa descreve corretamente a relação entre fígado e vesícula biliar?",
        "alternativas": ["A vesícula produz bile e o fígado a armazena", "Os dois órgãos produzem insulina", "O fígado produz bile e a vesícula a armazena"],
        "correta": 2,
        "explicacao": "O fígado produz a bile, que ajuda na digestão das gorduras. A vesícula biliar guarda essa secreção entre as refeições e a libera quando necessário.",
        "fonte": "NIDDK/NIH, digestão",
    }],
    "Corpo humano — pâncreas": [{
        "pergunta": "O pâncreas participa de quais duas funções?",
        "alternativas": ["Produzir enzimas digestivas e hormônios", "Filtrar o sangue e armazenar bile", "Produzir lágrimas e células sanguíneas"],
        "correta": 0,
        "explicacao": "O pâncreas produz enzimas que ajudam a digerir alimentos e hormônios, como a insulina, que participa do controle da glicose no sangue.",
        "fonte": "NIDDK/NIH, pâncreas",
    }],
    "Corpo humano — medula óssea": [{
        "pergunta": "O que a medula óssea produz?",
        "alternativas": ["Somente cálcio para os ossos", "Células do sangue, como hemácias, leucócitos e plaquetas", "A bile usada na digestão"],
        "correta": 1,
        "explicacao": "A medula óssea é um tecido dentro de alguns ossos que produz diferentes células do sangue, incluindo glóbulos vermelhos, glóbulos brancos e plaquetas.",
        "fonte": "MedlinePlus/NIH, medula",
    }],
    "Corpo humano — baço": [{
        "pergunta": "Qual é uma das funções do baço?",
        "alternativas": ["Produzir o ar que chega aos pulmões", "Bombear o sangue para o corpo", "Filtrar o sangue e remover hemácias envelhecidas"],
        "correta": 2,
        "explicacao": "O baço filtra o sangue, ajuda a remover hemácias antigas e participa da defesa do organismo. Ele também pode armazenar algumas células sanguíneas.",
        "fonte": "MedlinePlus/NIH, baço",
    }],
    "Corpo humano — veias azuis": [{
        "pergunta": "O sangue dentro das veias é realmente azul?",
        "alternativas": ["Não. Ele é vermelho, embora possa parecer azulado sob a pele", "Sim, porque não contém hemoglobina", "Só fica azul quando chega aos pulmões"],
        "correta": 0,
        "explicacao": "O sangue das veias é vermelho mais escuro, não azul. As veias podem parecer azuladas através da pele por causa da forma como a luz atravessa e retorna dos tecidos.",
        "fonte": "Cleveland Clinic, veias",
    }],
    "Corpo humano — suor": [{
        "pergunta": "Como a evaporação do suor ajuda a resfriar o corpo?",
        "alternativas": ["O suor vira sangue e reduz o calor", "A evaporação retira calor da superfície do corpo", "O suor bloqueia a circulação na pele"],
        "correta": 1,
        "explicacao": "Quando o suor evapora, ele leva energia térmica da superfície do corpo para o ambiente. Se o suor apenas escorre sem evaporar, o resfriamento é menor.",
        "fonte": "NCBI Bookshelf, temperatura",
    }],
    "Corpo humano — paralisia do sono": [{
        "pergunta": "O que pode acontecer durante a paralisia do sono?",
        "alternativas": ["A pessoa perde a audição por alguns segundos", "O coração para durante o sono", "A consciência retorna enquanto a imobilidade do sono REM persiste"],
        "correta": 2,
        "explicacao": "Na paralisia do sono, a pessoa pode recuperar a consciência enquanto a atonia muscular típica do sono REM ainda persiste. Por isso, fica temporariamente sem conseguir se mover ou falar.",
        "fonte": "NCBI Bookshelf, sono",
    }],
    "Corpo humano — piscar": [{
        "pergunta": "O que acontece com a superfície do olho quando piscamos?",
        "alternativas": ["Uma fina película de lágrimas se espalha sobre a córnea", "A pupila é coberta por uma camada de pele", "O cristalino produz lágrimas"],
        "correta": 0,
        "explicacao": "Cada piscada espalha uma fina película de lágrimas sobre a córnea. Essa camada ajuda a manter a superfície do olho úmida e protegida.",
        "fonte": "NEI/NIH, lágrimas",
    }],
    "Corpo humano — tremores de frio": [{
        "pergunta": "Por que o corpo pode tremer quando sente frio?",
        "alternativas": ["Para reduzir a temperatura dos músculos", "Contrações musculares involuntárias ajudam a produzir calor", "Para impedir que o sangue chegue à pele"],
        "correta": 1,
        "explicacao": "Os tremores são contrações musculares involuntárias e repetidas. A atividade dos músculos libera calor e ajuda o corpo a responder ao frio.",
        "fonte": "NCBI Bookshelf, tremores",
    }],
    "Corpo humano — ouvido e pressão": [{
        "pergunta": "Qual estrutura ajuda a equilibrar a pressão dos dois lados do tímpano?",
        "alternativas": ["A cóclea", "O nervo auditivo", "A tuba de Eustáquio"],
        "correta": 2,
        "explicacao": "A tuba de Eustáquio conecta o ouvido médio à região posterior do nariz e da garganta. Ela ajuda a equilibrar a pressão ao redor do tímpano, como pode acontecer ao bocejar ou engolir.",
        "fonte": "MedlinePlus/NIH, ouvido",
    }],
}

LEGENDAS = {
    tema: f"{tema}: mais uma curiosidade do corpo humano!\n\n#JuhQuiz #CorpoHumano #Curiosidades #Quiz"
    for tema in QUIZZES
}

FONTES_COMPLETAS = {
    "Dor no cérebro — NINDS/NIH, Headache": "https://www.ninds.nih.gov/sites/default/files/2025-07/NINDS_Headache_Booklet_Digital_508c%20%281%29.pdf",
    "Esmalte dentário — NCBI Bookshelf, Physiology, Tooth": "https://www.ncbi.nlm.nih.gov/books/NBK538475/",
    "Pupila — National Eye Institute, About the Eye": "https://www.nei.nih.gov/eye-health-information/healthy-vision/nei-for-kids/about-eye",
    "Pulmão esquerdo — NHLBI/NIH, How the Lungs Work": "https://www.nhlbi.nih.gov/health/lungs/respiratory-system",
    "Nariz — NCBI Bookshelf, Anatomy, Head and Neck, Nasal Cavity": "https://www.ncbi.nlm.nih.gov/books/NBK544232/",
    "Bile — NIDDK/NIH, Your Digestive System & How It Works": "https://www.niddk.nih.gov/health-information/digestive-diseases/digestive-system-how-it-works",
    "Pâncreas — NIDDK/NIH, Definition & Facts for Pancreatitis": "https://www.niddk.nih.gov/health-information/digestive-diseases/pancreatitis/definition-facts",
    "Medula óssea — MedlinePlus, Bone Marrow Tests": "https://medlineplus.gov/lab-tests/bone-marrow-tests/",
    "Baço — MedlinePlus, Splenomegaly": "https://medlineplus.gov/ency/article/003276.htm",
    "Cor das veias — Cleveland Clinic, Veins: Anatomy and Function": "https://my.clevelandclinic.org/health/body/23360-veins",
    "Evaporação e temperatura — NCBI Bookshelf, Physiology, Temperature Regulation": "https://www.ncbi.nlm.nih.gov/books/NBK507838/",
    "Paralisia do sono — NCBI Bookshelf, Sleep Paralysis": "https://www.ncbi.nlm.nih.gov/books/NBK562322/",
    "Piscada e película lacrimal — National Eye Institute, How Tears Work": "https://www.nei.nih.gov/eye-health-information/healthy-vision/how-eyes-work/how-tears-work",
    "Tremores e produção de calor — NCBI Bookshelf, Biochemistry, Heat and Calories": "https://www.ncbi.nlm.nih.gov/books/NBK538294/",
    "Tuba de Eustáquio — MedlinePlus, Ear: Blocked at High Altitudes": "https://medlineplus.gov/ency/article/002077.htm",
}
