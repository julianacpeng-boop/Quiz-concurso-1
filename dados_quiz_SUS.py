# Quiz Juh — Saúde e SUS
# 15 questões autorais, uma pergunta por vídeo.
# A fonte fica no campo "fonte" para aparecer na tela sem ser narrada.

CAPA_SEGUNDOS = 2

QUIZZES = {
    "SUS — saúde como direito": [
        {
            "pergunta": "Segundo a Constituição Federal, a saúde é:",
            "alternativas": ["Direito de todos e dever do Estado", "Benefício restrito a quem contribui para a Previdência", "Responsabilidade exclusiva dos municípios"],
            "correta": 0,
            "explicacao": "O artigo 196 da Constituição define a saúde como direito de todos e dever do Estado, garantida por políticas sociais e econômicas e pelo acesso universal e igualitário.",
            "fonte": "(Constituição Federal de 1988, art. 196 — Planalto: https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm)",
        },
    ],
    "SUS — universalidade": [
        {
            "pergunta": "No SUS, o princípio da universalidade assegura:",
            "alternativas": ["Atendimento apenas a pessoas sem plano de saúde", "Acesso aos serviços de saúde a todas as pessoas", "Atendimento somente em situações de urgência"],
            "correta": 1,
            "explicacao": "A Lei nº 8.080/1990 estabelece a universalidade de acesso aos serviços de saúde em todos os níveis de assistência.",
            "fonte": "(Lei nº 8.080/1990, art. 7º, I — Planalto: https://www.planalto.gov.br/ccivil_03/leis/l8080.htm)",
        },
    ],
    "SUS — integralidade": [
        {
            "pergunta": "O princípio da integralidade propõe:",
            "alternativas": ["Priorizar somente consultas médicas", "Oferecer apenas ações preventivas", "Articular ações preventivas e curativas, individuais e coletivas"],
            "correta": 2,
            "explicacao": "A integralidade reúne ações e serviços preventivos e curativos, individuais e coletivos, conforme as necessidades de cada caso e em diferentes níveis de complexidade.",
            "fonte": "(Lei nº 8.080/1990, art. 7º, II — Planalto: https://www.planalto.gov.br/ccivil_03/leis/l8080.htm)",
        },
    ],
    "SUS — equidade": [
        {
            "pergunta": "Na saúde, aplicar a equidade significa:",
            "alternativas": ["Considerar necessidades diferentes para reduzir desigualdades", "Oferecer exatamente o mesmo atendimento em qualquer situação", "Atender primeiro quem chegou acompanhado"],
            "correta": 0,
            "explicacao": "Equidade considera necessidades e desigualdades para direcionar cuidado e recursos de forma justa, buscando reduzir barreiras de acesso.",
            "fonte": "(Ministério da Saúde, O que é Equidade: https://www.gov.br/saude/pt-br/composicao/saps/equidade/o-que-e-equidade)",
        },
    ],
    "SUS — descentralização": [
        {
            "pergunta": "A descentralização político-administrativa do SUS organiza responsabilidades entre:",
            "alternativas": ["Somente o Ministério da Saúde e hospitais privados", "União, estados, Distrito Federal e municípios", "Apenas estados e municípios"],
            "correta": 1,
            "explicacao": "A Lei nº 8.080 prevê direção única em cada esfera de governo e descentralização, com ênfase na municipalização dos serviços.",
            "fonte": "(Lei nº 8.080/1990, art. 7º, IX — Planalto: https://www.planalto.gov.br/ccivil_03/leis/l8080.htm)",
        },
    ],
    "SUS — regionalização e hierarquização": [
        {
            "pergunta": "A regionalização e a hierarquização ajudam a:",
            "alternativas": ["Concentrar todo atendimento em hospitais federais", "Impedir encaminhamentos entre serviços", "Organizar os serviços em rede e por níveis de atenção"],
            "correta": 2,
            "explicacao": "A rede regionalizada e hierarquizada organiza os pontos de atenção e os fluxos de cuidado conforme a necessidade de saúde e a complexidade do atendimento.",
            "fonte": "(Constituição Federal, art. 198; Lei nº 8.080/1990, art. 7º, IX — Planalto)",
        },
    ],
    "SUS — participação social": [
        {
            "pergunta": "Qual alternativa apresenta as instâncias colegiadas de participação social previstas no SUS?",
            "alternativas": ["Conselho de Saúde e Conferência de Saúde", "Ouvidoria e hospital universitário", "Secretaria de Saúde e unidade básica"],
            "correta": 0,
            "explicacao": "A Lei nº 8.142/1990 prevê, em cada esfera de governo, a Conferência de Saúde e o Conselho de Saúde como instâncias colegiadas.",
            "fonte": "(Lei nº 8.142/1990, art. 1º — Planalto: https://www.planalto.gov.br/ccivil_03/leis/l8142.htm)",
        },
    ],
    "SUS — Conselho de Saúde": [
        {
            "pergunta": "Uma característica do Conselho de Saúde é ser um órgão:",
            "alternativas": ["Temporário e formado apenas por gestores", "Permanente e deliberativo, com participação de diferentes segmentos", "Consultivo e composto somente por profissionais de saúde"],
            "correta": 1,
            "explicacao": "A Lei nº 8.142 define o Conselho de Saúde como permanente e deliberativo, com representantes do governo, prestadores, profissionais de saúde e usuários.",
            "fonte": "(Lei nº 8.142/1990, art. 1º, § 2º — Planalto: https://www.planalto.gov.br/ccivil_03/leis/l8142.htm)",
        },
    ],
    "SUS — Conferência de Saúde": [
        {
            "pergunta": "De acordo com a Lei nº 8.142/1990, a Conferência de Saúde reúne-se ordinariamente a cada:",
            "alternativas": ["Dois anos", "Seis anos", "Quatro anos"],
            "correta": 2,
            "explicacao": "A Conferência de Saúde reúne representantes de vários segmentos sociais a cada quatro anos para avaliar a situação de saúde e propor diretrizes.",
            "fonte": "(Lei nº 8.142/1990, art. 1º, § 1º — Planalto: https://www.planalto.gov.br/ccivil_03/leis/l8142.htm)",
        },
    ],
    "SUS — Atenção Primária": [
        {
            "pergunta": "No SUS, a Atenção Primária à Saúde é considerada:",
            "alternativas": ["A principal porta de entrada e centro de comunicação da rede", "Um serviço usado somente após internação", "Uma modalidade exclusiva de atendimento domiciliar"],
            "correta": 0,
            "explicacao": "O Ministério da Saúde descreve a Atenção Primária como principal porta de entrada do SUS e centro de comunicação com a Rede de Atenção à Saúde.",
            "fonte": "(Ministério da Saúde, Atenção Primária: https://www.gov.br/saude/pt-br/composicao/saps/atencao-primaria)",
        },
    ],
    "SUS — Estratégia Saúde da Família": [
        {
            "pergunta": "A Estratégia Saúde da Família busca principalmente:",
            "alternativas": ["Substituir todos os serviços especializados", "Reorganizar e fortalecer a Atenção Primária", "Atender somente pessoas com doenças crônicas"],
            "correta": 1,
            "explicacao": "A Estratégia Saúde da Família é um modelo prioritário para reorganizar a Atenção Primária e ampliar a continuidade do cuidado no território.",
            "fonte": "(Ministério da Saúde, Estratégia Saúde da Família: https://www.gov.br/saude/pt-br/composicao/saps/esf)",
        },
    ],
    "SUS — vacinação e PNI": [
        {
            "pergunta": "Qual programa coordena a política de vacinação no SUS?",
            "alternativas": ["Programa Saúde na Escola", "Sistema Nacional de Transplantes", "Programa Nacional de Imunizações (PNI)"],
            "correta": 2,
            "explicacao": "O Programa Nacional de Imunizações coordena a vacinação no país. O calendário e as recomendações são definidos pelo Ministério da Saúde e podem variar por idade e condição de saúde.",
            "fonte": "(Ministério da Saúde, Programa Nacional de Imunizações: https://www.gov.br/saude/pt-br/composicao/svsa/pni)",
        },
    ],
    "SUS — vigilância epidemiológica": [
        {
            "pergunta": "A epidemiologia é usada no SUS, entre outras finalidades, para:",
            "alternativas": ["Definir prioridades e orientar a alocação de recursos", "Substituir a avaliação clínica individual", "Restringir o acesso a ações preventivas"],
            "correta": 0,
            "explicacao": "A Lei nº 8.080 prevê o uso da epidemiologia para estabelecer prioridades, alocar recursos e orientar a programação das ações de saúde.",
            "fonte": "(Lei nº 8.080/1990, art. 7º, VII — Planalto: https://www.planalto.gov.br/ccivil_03/leis/l8080.htm)",
        },
    ],
    "SUS — vigilância sanitária": [
        {
            "pergunta": "A vigilância sanitária atua principalmente para:",
            "alternativas": ["Realizar apenas consultas e exames", "Prevenir e reduzir riscos relacionados a produtos e serviços de interesse da saúde", "Substituir a vigilância epidemiológica em surtos"],
            "correta": 1,
            "explicacao": "A Lei nº 8.080 define vigilância sanitária como ações capazes de eliminar, diminuir ou prevenir riscos à saúde e intervir em problemas sanitários relacionados ao ambiente, produtos e serviços.",
            "fonte": "(Lei nº 8.080/1990, art. 6º, § 1º — Planalto: https://www.planalto.gov.br/ccivil_03/leis/l8080.htm)",
        },
    ],
    "SUS — saúde mental e CAPS": [
        {
            "pergunta": "Os Centros de Atenção Psicossocial (CAPS) são serviços voltados a:",
            "alternativas": ["Acolher e acompanhar pessoas em intenso sofrimento psíquico na comunidade", "Atender exclusivamente emergências cirúrgicas", "Substituir todas as unidades básicas de saúde"],
            "correta": 0,
            "explicacao": "Os CAPS são serviços públicos comunitários de saúde mental que oferecem acolhimento, acompanhamento multiprofissional e articulação com outros pontos da rede.",
            "fonte": "(Ministério da Saúde, Centros de Atenção Psicossocial: https://www.gov.br/saude/pt-br/composicao/saes/desmad/raps/caps/caps)",
        },
    ],
}

LEGENDAS = {
    tema: f"{tema}: teste seus conhecimentos sobre saúde e SUS!\n\n#JuhQuiz #SUS #Saude #Quiz"
    for tema in QUIZZES
}

# Gabaritos distribuídos entre A, B e C para evitar repetição de alternativa.
