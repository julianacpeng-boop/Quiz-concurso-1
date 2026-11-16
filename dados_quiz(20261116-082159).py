# Juh Quiz — Ciência, tecnologia e IA — lote novo de 15 questões
# Questões autorais, uma pergunta por vídeo.
# A fonte curta é exibida entre parênteses pelo gerar_quiz.py.

CAPA_SEGUNDOS = 2

QUIZZES = {
    "Ciência e IA — laboratório autônomo": [{
        "pergunta": "O que a plataforma AutoDNA demonstrou em um laboratório de biologia molecular?",
        "alternativas": ["Agentes de IA podem planejar e coordenar experimentos com instrumentos laboratoriais", "Um robô pode substituir todas as etapas de validação científica", "Uma máquina pode criar DNA sem materiais ou reagentes"],
        "correta": 0,
        "explicacao": "A AutoDNA é uma plataforma experimental em que agentes de IA coordenam instrumentos para executar operações biomoleculares, como síntese e sequenciamento de DNA. O trabalho ainda depende de pessoas para tarefas como manutenção e reposição de materiais.",
        "fonte": "Nature, AutoDNA",
    }],
    "Ciência e IA — caixa-preta": [{
        "pergunta": "O que tenta fazer a IA chamada de “mecânica” em uma pesquisa recente?",
        "alternativas": ["Consertar peças físicas de computadores", "Investigar e alterar partes internas de outra rede neural", "Traduzir códigos binários em idiomas humanos"],
        "correta": 1,
        "explicacao": "A pesquisa usa um modelo de IA para examinar padrões internos de outra rede neural e testar mudanças em seu funcionamento. É uma abordagem de interpretabilidade; não significa que todas as decisões de qualquer IA já possam ser explicadas perfeitamente.",
        "fonte": "Nature, IA mecânica",
    }],
    "Ciência e IA — testes de segurança": [{
        "pergunta": "O que os testes de segurança de uma inteligência artificial procuram avaliar?",
        "alternativas": ["Se o sistema sempre concorda com quem faz a pergunta", "Se a IA consegue substituir a supervisão humana", "Falhas, robustez e comportamento em diferentes condições de uso"],
        "correta": 2,
        "explicacao": "Testes, validação e avaliação ajudam a identificar falhas e verificar a confiabilidade de um sistema em condições variadas. O Inmetro debateu métodos e normas para comparar soluções e avaliar sua segurança.",
        "fonte": "Inmetro, testes de IA",
    }],
    "Ciência e tecnologia — interface cérebro-computador": [{
        "pergunta": "Como uma interface cérebro-computador pode ajudar uma pessoa com dificuldade de fala?",
        "alternativas": ["Decodificando sinais cerebrais relacionados à tentativa de comunicação", "Transformando pensamentos em voz sem captar sinais do cérebro", "Estimulando os músculos da língua para falar automaticamente"],
        "correta": 0,
        "explicacao": "Interfaces cérebro-computador registram atividade neural e usam algoritmos para interpretar padrões relacionados a movimentos ou tentativas de fala. Algumas tecnologias estão em estudos clínicos e não são soluções disponíveis para todas as pessoas.",
        "fonte": "Univ. Michigan, BCI",
    }],
    "Ciência e tecnologia — CRISPR in vivo": [{
        "pergunta": "Em uma terapia CRISPR “in vivo”, onde a edição genética é realizada?",
        "alternativas": ["Somente em uma placa de laboratório, sem células do paciente", "Dentro do organismo, levando o sistema de edição às células-alvo", "Em todas as células do corpo ao mesmo tempo"],
        "correta": 1,
        "explicacao": "In vivo significa que o sistema de edição é administrado para atuar dentro do organismo. Uma terapia experimental para angioedema hereditário teve seu pedido aceito para revisão prioritária pela FDA, com decisão prevista para 2027; ainda não estava aprovada na data desta questão.",
        "fonte": "NEJM, CRISPR in vivo",
    }],
    "Ciência e tecnologia — materiais autorreparáveis": [{
        "pergunta": "O que significa dizer que um material é autorreparável?",
        "alternativas": ["Que ele nunca sofre desgaste", "Que ele se recompõe sem qualquer limite ou condição", "Que pode recuperar parte de sua estrutura ou função após certos danos"],
        "correta": 2,
        "explicacao": "Materiais autorreparáveis são projetados para recuperar parte de sua estrutura ou desempenho depois de determinados danos. Em novos sensores flexíveis, essa propriedade ainda é estudada sob condições específicas e não torna o material indestrutível.",
        "fonte": "Estudo de materiais, 2026",
    }],
    "Ciência e IA — chip neuromórfico": [{
        "pergunta": "O que inspira o desenvolvimento de um chip neuromórfico?",
        "alternativas": ["A organização e alguns modos de processamento do cérebro", "A forma de armazenamento dos discos rígidos", "O funcionamento de uma bateria de lítio"],
        "correta": 0,
        "explicacao": "A computação neuromórfica busca reproduzir aspectos da organização e da dinâmica de redes neurais biológicas em hardware. É uma área de pesquisa que pode contribuir para sistemas mais eficientes, mas não cria um cérebro artificial completo.",
        "fonte": "MIT, chip neuromórfico",
    }],
    "Ciência e saúde — órgão-em-chip": [{
        "pergunta": "Para que pesquisadores usam dispositivos chamados “órgãos-em-chip”?",
        "alternativas": ["Para substituir órgãos humanos em transplantes", "Para reproduzir aspectos de órgãos em pequenos dispositivos com células", "Para armazenar órgãos doados em temperatura ambiente"],
        "correta": 1,
        "explicacao": "Órgãos-em-chip usam células humanas em dispositivos pequenos para imitar aspectos da estrutura ou função de órgãos, como pulmão, fígado ou coração. Eles ajudam na pesquisa e podem reduzir algumas necessidades de testes em animais, mas ainda têm limitações.",
        "fonte": "NIH, órgão-em-chip",
    }],
    "Ciência e tecnologia — bioimpressão 3D": [{
        "pergunta": "Por que imprimir um órgão completo para transplante ainda é um grande desafio?",
        "alternativas": ["Impressoras 3D não conseguem formar nenhuma estrutura biológica", "Células humanas não podem ser organizadas em camadas", "É difícil reproduzir vasos, vários tipos de tecido e funções complexas em escala"],
        "correta": 2,
        "explicacao": "A bioimpressão pode organizar células e biomateriais para formar tecidos, mas um órgão funcional exige estruturas complexas, circulação adequada e integração de diferentes células. Essas barreiras ainda limitam o uso de órgãos impressos completos em transplantes.",
        "fonte": "PubMed, bioimpressão 3D",
    }],
    "Ciência e tecnologia — baterias de sódio": [{
        "pergunta": "Qual íon se movimenta em uma bateria de íons de sódio durante seu funcionamento?",
        "alternativas": ["Íons de sódio", "Íons de lítio", "Íons de ferro"],
        "correta": 0,
        "explicacao": "Como o nome indica, baterias de íons de sódio movimentam íons de sódio entre os eletrodos durante os ciclos de carga e descarga. A tecnologia está em desenvolvimento e tem desafios próprios de desempenho, custo e durabilidade.",
        "fonte": "Nature, bateria de sódio",
    }],
    "Ciência e tecnologia — Wi-Fi como sensor": [{
        "pergunta": "Em pesquisas de sensoriamento por Wi-Fi, o que pode revelar a movimentação de uma pessoa?",
        "alternativas": ["A cor da rede Wi-Fi", "Mudanças nos sinais de rádio refletidos no ambiente", "O nome escolhido para o roteador"],
        "correta": 1,
        "explicacao": "Movimentos no ambiente podem alterar a propagação e a reflexão de sinais de rádio. Pesquisadores estudam se essas mudanças podem detectar movimento sem que a pessoa carregue um dispositivo; isso não significa que um roteador comum identifique qualquer pessoa ou leia pensamentos.",
        "fonte": "IEEE, Wi-Fi sensing",
    }],
    "Ciência e tecnologia — carne cultivada": [{
        "pergunta": "De onde vêm as células usadas para produzir carne cultivada?",
        "alternativas": ["De plantas modificadas para ter gosto de carne", "De fungos que são prensados em moldes", "De células animais cultivadas em condições controladas"],
        "correta": 2,
        "explicacao": "A carne cultivada é produzida a partir de células animais mantidas e multiplicadas em condições controladas. Tornar o processo seguro, acessível e capaz de produzir grandes volumes continua sendo um desafio tecnológico.",
        "fonte": "Nature, carne cultivada",
    }],
    "Ciência e tecnologia — robotáxis": [{
        "pergunta": "Como o sistema autônomo da Waymo combina sensores para perceber a rua?",
        "alternativas": ["Com câmeras, radar e lidar", "Somente com GPS e mapas impressos", "Com microfones e sensores de temperatura"],
        "correta": 0,
        "explicacao": "A Waymo informa que seu sistema usa câmeras, radar e lidar, que oferecem tipos diferentes de dados sobre o entorno. A combinação ajuda o veículo a perceber objetos e distâncias, mas não elimina a necessidade de validação e segurança operacional.",
        "fonte": "Waymo, sensores",
    }],
    "Ciência e energia — eletrólise do hidrogênio": [{
        "pergunta": "O que acontece na eletrólise da água para produzir hidrogênio?",
        "alternativas": ["A água é congelada até liberar hidrogênio", "A eletricidade separa a água em hidrogênio e oxigênio", "O hidrogênio é retirado do ar sem energia"],
        "correta": 1,
        "explicacao": "Um eletrolisador usa eletricidade para separar moléculas de água em hidrogênio e oxigênio. O impacto climático do hidrogênio produzido depende, entre outros fatores, da origem da eletricidade utilizada.",
        "fonte": "DOE, eletrólise",
    }],
    "Ciência e tecnologia — gêmeo digital": [{
        "pergunta": "O que diferencia um gêmeo digital de uma simulação estática?",
        "alternativas": ["É sempre uma imagem tridimensional de uma máquina", "É uma cópia física feita por impressão 3D", "É uma representação virtual conectada a dados do sistema real"],
        "correta": 2,
        "explicacao": "Um gêmeo digital representa um sistema físico e pode receber dados atualizados para acompanhar seu estado. Com isso, pesquisadores ou engenheiros podem monitorar, analisar e simular mudanças no sistema representado.",
        "fonte": "NIST, gêmeo digital",
    }],
}

LEGENDAS = {
    tema: f"{tema}: teste seus conhecimentos de ciência e tecnologia!\n\n#JuhQuiz #Ciencia #Tecnologia #IA"
    for tema in QUIZZES
}

FONTES_COMPLETAS = {
    "Laboratório AutoDNA com agentes de IA — Nature, 04/11/2026": "https://www.nature.com/articles/s41586-026-11228-6",
    "IA investiga a caixa-preta de redes neurais — Nature, 13/11/2026": "https://www.nature.com/articles/d41586-026-03679-8",
    "Segurança, avaliação e normas para IA — Inmetro, 04/11/2026": "https://www.gov.br/inmetro/pt-br/centrais-de-conteudo/noticias/2026/brasilia-sedia-forum-brasil-europa-sobre-testes-de-seguranca-para-a-inteligencia-artificial/",
    "Interface cérebro-computador em estudo clínico — University of Michigan, 17/06/2026": "https://medresearch.umich.edu/news-release/university-michigan-implants-first-human-paradromics-wireless-brain-computer-interface-designed",
    "Terapia CRISPR in vivo para angioedema hereditário — NEJM": "https://www.nejm.org/doi/full/10.1056/NEJMoa2600931 ; FDA review announcement: https://ir.intelliatx.com/news-releases/news-release-details/intellia-therapeutics-announces-fda-acceptance-biologics-license",
    "Material flexível autorreparável para sensores — Carbohydrate Polymers, 10/11/2026": "https://www.sciencedirect.com/science/article/pii/S0144861726011409",
    "Dispositivos neuromórficos — MIT News, 16/09/2026": "https://news.mit.edu/2026/nanoscale-mechanics-could-enable-brain-inspired-computing-0916",
    "Órgãos-em-chip para pesquisa — NIH/NCATS": "https://ncats.nih.gov/research/research-activities/tissue-chip",
    "Desafios da bioimpressão 3D de tecidos — revisão no PubMed": "https://pubmed.ncbi.nlm.nih.gov/40513614/",
    "Baterias de íons de sódio — Nature, 11/11/2026": "https://www.nature.com/articles/s44359-026-00234-6",
    "Detecção de pessoas por Wi-Fi comercial — IEEE, 2026": "https://ieeexplore.ieee.org/abstract/document/11477250",
    "Carne cultivada e desafios de escala — Nature Biotechnology, 10/11/2026": "https://www.nature.com/articles/s41587-026-03364-1",
    "Sensores da sexta geração do Waymo Driver — Waymo, 2026": "https://waymo.com/blog/2026/02/ro-on-6th-gen-waymo-driver/",
    "Produção de hidrogênio por eletrólise — U.S. Department of Energy": "https://www.energy.gov/cmei/fuels/hydrogen-production-electrolysis",
    "Definição e sincronização de gêmeos digitais — NIST": "https://www.nist.gov/digital-twins/essential-elements",
}
