# Dados do Quiz — Arquitetura e Engenharia Civil para concursos EBSERH
# Questões autorais ou adaptadas dos temas das provas EBSERH/IBFC 2023.
# Cada vídeo contém uma pergunta.

CAPA_SEGUNDOS = 2

QUIZZES = {
    "arquitetura_ebserh": [
        {
            "pergunta": "Em um projeto arquitetônico, qual documento organiza os ambientes necessários, suas atividades e relações funcionais antes do desenvolvimento do projeto?",
            "alternativas": ['Programa de necessidades', 'Memorial de cálculo estrutural', 'Cronograma físico-financeiro'],
            "correta": 0,
            "explicacao": "O programa de necessidades reúne os ambientes e requisitos funcionais que orientarão o projeto, como atividades previstas, relações entre setores e necessidades dos usuários.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Edital 04, Arquiteto, questão sobre programa de necessidades para arquitetura (tema adaptado).",
        },
        {
            "pergunta": "Na escala 1:200, uma parede representada com 4 cm no desenho corresponde a qual comprimento real?",
            "alternativas": ['2 m', '8 m', '80 m'],
            "correta": 1,
            "explicacao": "Na escala 1:200, cada centímetro no desenho representa 200 cm na realidade. Assim, 4 × 200 = 800 cm, equivalentes a 8 m.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Edital 04, Arquiteto, questão sobre escala e representação gráfica (tema adaptado).",
        },
        {
            "pergunta": "Ao projetar a sinalização de um hospital, qual característica torna um pictograma mais eficaz para orientar diferentes usuários?",
            "alternativas": ['Depender apenas de texto técnico extenso', 'Mudar de significado entre setores', 'Ser simples, reconhecível e usado de forma consistente'],
            "correta": 2,
            "explicacao": "Pictogramas simples e consistentes facilitam o reconhecimento rápido e apoiam a orientação de usuários com diferentes níveis de alfabetização e familiaridade com o hospital.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Edital 04, Arquiteto, questão sobre pictogramas do sistema de sinalização hospitalar (tema adaptado).",
        },
        {
            "pergunta": "Qual norma sanitária estabelece requisitos para análise, avaliação e aprovação de projetos físicos de estabelecimentos de saúde?",
            "alternativas": ['RDC Anvisa nº 509/2021', 'RDC Anvisa nº 51/2011', 'NR-10'],
            "correta": 1,
            "explicacao": "A RDC nº 51/2011 dispõe sobre requisitos mínimos para análise, avaliação e aprovação dos projetos físicos de estabelecimentos de saúde no Sistema Nacional de Vigilância Sanitária.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Edital 04, Arquiteto; Anvisa, RDC nº 51/2011.",
        },
        {
            "pergunta": "Em um hospital, separar fluxos limpos e contaminados durante o planejamento dos ambientes ajuda principalmente a quê?",
            "alternativas": ['Aumentar o percurso de materiais sem benefício', 'Substituir protocolos de limpeza', 'Reduzir cruzamentos e apoiar o controle de infecções'],
            "correta": 2,
            "explicacao": "O planejamento de fluxos compatíveis com as atividades reduz cruzamentos indesejáveis entre pessoas, materiais limpos e resíduos, contribuindo para a segurança e o controle de infecções.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Edital 04, Arquiteto, conteúdos de projeto de estabelecimentos assistenciais de saúde; Anvisa, RDC nº 50/2002 (tema adaptado).",
        },
        {
            "pergunta": "Qual é a finalidade principal de um Relatório de Requalificação Ambiental (RRA) em projetos e intervenções?",
            "alternativas": ['Avaliar aspectos e medidas de requalificação ambiental', 'Substituir o projeto arquitetônico executivo', 'Registrar somente o custo de mobiliário'],
            "correta": 0,
            "explicacao": "O relatório reúne avaliação e diretrizes relacionadas à requalificação ambiental da área ou edificação, considerando condições existentes e medidas previstas no escopo aplicável.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Edital 04, Arquiteto, questão sobre Relatório de Requalificação Ambiental (tema adaptado).",
        },
        {
            "pergunta": "Qual recurso ajuda a verificar se uma rota acessível em um edifício pode ser usada por pessoas com mobilidade reduzida?",
            "alternativas": ['Avaliar somente a cor do piso', 'Considerar apenas a largura da porta principal', 'Conferir dimensões, inclinações, áreas de manobra e obstáculos'],
            "correta": 2,
            "explicacao": "A rota acessível deve ser avaliada como um percurso contínuo, incluindo dimensões, inclinações, áreas de manobra, desníveis e obstáculos, conforme os requisitos de acessibilidade aplicáveis.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Edital 04, Arquiteto, conteúdo de acessibilidade e representação arquitetônica; ABNT NBR 9050 (tema autoral).",
        },
        {
            "pergunta": "Na elaboração de um projeto de reforma hospitalar, por que é importante levantar e registrar as condições existentes antes de detalhar a intervenção?",
            "alternativas": ['Para compatibilizar a proposta com a edificação e reduzir incompatibilidades', 'Para dispensar a verificação das instalações', 'Para evitar consulta aos setores usuários'],
            "correta": 0,
            "explicacao": "O levantamento das condições existentes permite compatibilizar arquitetura, estrutura e instalações, identificar restrições e planejar a obra com menor risco de interferências.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Edital 04, Arquiteto, conteúdos de projeto, levantamento e representação (questão autoral sobre o tema).",
        },
    ],
    "engenheiro_civil_ebserh": [
        {
            "pergunta": "Em orçamento de obras, o que representa o BDI aplicado sobre custos diretos para formar o preço de venda?",
            "alternativas": ['Somente o custo de materiais', 'Despesas indiretas, tributos e lucro', 'Apenas a quantidade de horas trabalhadas'],
            "correta": 1,
            "explicacao": "BDI significa Benefícios e Despesas Indiretas. Em orçamento, a taxa considera parcelas indiretas, tributos e lucro, conforme a metodologia e os critérios aplicáveis ao empreendimento.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Edital 04, Engenheiro Civil, questão sobre BDI; Diretrizes para Contratação e Fiscalização de Obras da Rede Ebserh, Volume I (tema adaptado).",
        },
        {
            "pergunta": "Segundo a RDC Anvisa nº 51/2011, a que se refere a expressão 'estabelecimento assistencial de saúde'?",
            "alternativas": ['Local destinado à realização de ações ou serviços de saúde', 'Somente hospital com internação', 'Apenas unidade pública de alta complexidade'],
            "correta": 0,
            "explicacao": "A definição abrange local destinado à realização de ações e/ou serviços de saúde, coletivos ou individuais, independentemente do porte ou nível de complexidade.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Edital 04, Engenheiro Civil, questão sobre normas e legislações; Anvisa, RDC nº 51/2011 (tema adaptado).",
        },
        {
            "pergunta": "Em um cronograma de obra, o caminho crítico é formado pelas atividades que: ",
            "alternativas": ['Podem atrasar sem afetar a entrega', 'São sempre as atividades de menor custo', 'Determinam a duração total e não têm folga disponível'],
            "correta": 2,
            "explicacao": "As atividades do caminho crítico têm folga total nula ou mínima conforme o método adotado. Atrasos nelas podem atrasar a data final do projeto.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Edital 04, Engenheiro Civil, conteúdos de planejamento e controle de obras (questão autoral sobre o tema).",
        },
        {
            "pergunta": "Uma laje retangular mede 5 m por 4 m e terá 0,12 m de espessura. Qual volume geométrico de concreto será necessário, sem considerar perdas?",
            "alternativas": ['9 m³', '2,4 m³', '24 m³'],
            "correta": 1,
            "explicacao": "O volume é comprimento × largura × espessura: 5 × 4 × 0,12 = 2,4 m³. O orçamento pode prever perdas conforme os critérios do projeto e da execução.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Edital 04, Engenheiro Civil, temas de orçamento e planejamento de obras (questão autoral).",
        },
        {
            "pergunta": "Qual é uma finalidade importante do controle tecnológico do concreto durante a execução da obra?",
            "alternativas": ['Alterar o projeto estrutural sem autorização', 'Verificar se o material atende aos requisitos especificados', 'Substituir a inspeção da execução'],
            "correta": 1,
            "explicacao": "O controle tecnológico verifica características e conformidade do concreto com as especificações do projeto e das normas, apoiando a qualidade e a segurança da estrutura.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Edital 04, Engenheiro Civil, conteúdos de estruturas, edificações e fiscalização de obras (questão autoral).",
        },
        {
            "pergunta": "Na fiscalização de uma obra hospitalar, qual procedimento ajuda a comprovar que o serviço foi executado conforme o projeto e as especificações?",
            "alternativas": ['Inspecionar, registrar evidências e documentar não conformidades', 'Aceitar o serviço apenas por informação verbal', 'Verificar somente o pagamento da medição'],
            "correta": 0,
            "explicacao": "A fiscalização deve comparar a execução com projetos, especificações e critérios de aceitação, registrar evidências e acompanhar a correção de eventuais não conformidades.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Edital 04, Engenheiro Civil, temas de planejamento, fiscalização e controle de obras (questão autoral).",
        },
        {
            "pergunta": "Por que as instalações prediais devem ser compatibilizadas com os projetos de arquitetura e estrutura antes da execução?",
            "alternativas": ['Para aumentar o número de furos em vigas', 'Para dispensar desenhos e memoriais', 'Para prevenir interferências e retrabalho na obra'],
            "correta": 2,
            "explicacao": "A compatibilização identifica conflitos entre tubulações, dutos, elementos estruturais e espaços arquitetônicos antes da obra, reduzindo retrabalho, atrasos e riscos à edificação.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Edital 04, Engenheiro Civil, temas de instalações, edificações e planejamento de obras (questão autoral).",
        },
    ],
}

LEGENDAS = {
    "arquitetura_ebserh": "Questão de Arquitetura para concurso EBSERH. Responda antes da explicação. #JuhQuiz #EBSERH #Arquitetura #Concursos",
    "engenheiro_civil_ebserh": "Questão de Engenharia Civil para concurso EBSERH. Responda antes da explicação. #JuhQuiz #EBSERH #EngenhariaCivil #Concursos",
}
