# Questões de vestibular federal reescritas para vídeos curtos.
# Todos os itens abaixo são adaptações, não transcrições literais.
# Cada vídeo contém uma pergunta. `correta`: 0 = A, 1 = B, 2 = C.

CAPA_SEGUNDOS = 2
TEMA = "Vestibulares federais — Biologia, Matemática e História"

QUIZZES = {
    TEMA: [
        # BIOLOGIA (1–5)
        {
            "pergunta": "A luz de telas à noite pode interferir no relógio biológico. Qual processo pode ser afetado pela exposição luminosa no período noturno?",
            "alternativas": [
                "A produção de melatonina, hormônio ligado ao sono.",
                "A formação de hemácias na medula óssea.",
                "A digestão de proteínas no estômago."
            ],
            "correta": 0,
            "explicacao": "A luz à noite pode reduzir ou atrasar a liberação de melatonina, hormônio que participa da regulação do ciclo sono-vigília. Esse efeito pode dificultar o início do sono.",
            "fonte": "Vestibular Unificado UFSC/IFSC/IFC 2025, Biologia, prova amarela, questão 31 (adaptada; tema de ritmos circadianos)."
        },
        {
            "pergunta": "Após uma queimada, uma área pode voltar a ser ocupada por diferentes espécies ao longo do tempo. Como se chama esse processo de mudança na comunidade?",
            "alternativas": [
                "Eutrofização artificial.",
                "Sucessão ecológica.",
                "Seleção sexual."
            ],
            "correta": 1,
            "explicacao": "A sucessão ecológica é a mudança gradual na composição das comunidades de uma área. Depois de um distúrbio, como o fogo, espécies pioneiras podem colonizar o local e abrir caminho para outras.",
            "fonte": "Vestibular Unificado UFSC/IFSC/IFC 2025, Biologia, prova amarela, questões 31–40 (adaptada; contexto de queimadas indicado no relatório da banca)."
        },
        {
            "pergunta": "Na esclerose múltipla, o sistema imune pode atacar estruturas do próprio organismo. Qual estrutura é afetada principalmente?",
            "alternativas": [
                "A mielina que reveste fibras nervosas.",
                "A parede celular dos neurônios.",
                "A hemoglobina dentro das hemácias."
            ],
            "correta": 0,
            "explicacao": "Na esclerose múltipla, ocorre um processo autoimune que danifica a mielina do sistema nervoso central. A perda dessa camada prejudica a condução dos impulsos nervosos.",
            "fonte": "Vestibular Unificado UFSC/IFSC/IFC 2025, Biologia, prova amarela, questões 31–40 (adaptada; pesquisa sobre esclerose múltipla citada no relatório da banca)."
        },
        {
            "pergunta": "Uma doença autoimune ocorre quando o sistema imunológico: ",
            "alternativas": [
                "Deixa de reconhecer qualquer microrganismo.",
                "Ataca células ou tecidos do próprio corpo.",
                "Produz apenas anticorpos contra vacinas."
            ],
            "correta": 1,
            "explicacao": "Nas doenças autoimunes, mecanismos de defesa passam a reagir contra componentes do próprio organismo. O tecido afetado varia conforme a doença.",
            "fonte": "Vestibular Unificado UFSC/IFSC/IFC 2025, Biologia, prova amarela, questões 31–40 (adaptada; tema de doenças autoimunes citado no relatório da banca)."
        },
        {
            "pergunta": "O uso prolongado de telas, especialmente à noite, pode alterar hábitos de descanso. Qual atitude ajuda a reduzir a interferência da luz no sono?",
            "alternativas": [
                "Aumentar o brilho da tela antes de dormir.",
                "Usar o celular deitado no escuro até adormecer.",
                "Diminuir a exposição à tela no período que antecede o sono."
            ],
            "correta": 2,
            "explicacao": "Reduzir o tempo de exposição à luz de telas antes de dormir pode ajudar a preservar o ritmo sono-vigília. A questão relaciona um hábito cotidiano aos ritmos circadianos.",
            "fonte": "Vestibular Unificado UFSC/IFSC/IFC 2025, Biologia, prova amarela, questões 31–40 (adaptada; uso excessivo de telas e ritmos circadianos abordados no relatório da banca)."
        },
        # MATEMÁTICA (6–10)
        {
            "pergunta": "Uma taxa de inscrição de R$ 80 recebeu desconto de 15%. Qual é o valor final?",
            "alternativas": [
                "R$ 68.",
                "R$ 72.",
                "R$ 65."
            ],
            "correta": 0,
            "explicacao": "Quinze por cento de R$ 80 são R$ 12. Subtraindo o desconto: R$ 80 − R$ 12 = R$ 68.",
            "fonte": "Vestibular Unificado UFSC/IFSC/IFC 2025, Matemática, prova amarela, questões 21–30 (adaptada; conteúdo de porcentagem e proporcionalidade)."
        },
        {
            "pergunta": "Um capital de R$ 1.000 é aplicado a juros compostos de 10% ao ano por 2 anos. Qual será o montante?",
            "alternativas": [
                "R$ 1.200.",
                "R$ 1.210.",
                "R$ 1.100."
            ],
            "correta": 1,
            "explicacao": "Nos juros compostos, os juros de cada período incidem sobre o montante acumulado. Após dois anos: 1.000 × 1,10² = R$ 1.210.",
            "fonte": "Vestibular Unificado UFSC/IFSC/IFC 2025, Matemática, prova amarela, questões 21–30 (adaptada; juros compostos citados no relatório da banca)."
        },
        {
            "pergunta": "Uma função é dada por f(x) = 2x + 3. Quanto vale f(4)?",
            "alternativas": [
                "8.",
                "10.",
                "11."
            ],
            "correta": 2,
            "explicacao": "Substituindo x por 4: f(4) = 2 × 4 + 3 = 8 + 3 = 11.",
            "fonte": "Vestibular Unificado UFSC/IFSC/IFC 2025, Matemática, prova amarela, questões 21–30 (adaptada; conteúdo de funções)."
        },
        {
            "pergunta": "Uma caixa tem 3 bolas vermelhas e 2 azuis. Ao retirar uma bola ao acaso, qual é a probabilidade de ela ser azul?",
            "alternativas": [
                "2/5.",
                "3/5.",
                "1/2."
            ],
            "correta": 0,
            "explicacao": "Há 5 bolas ao todo e 2 são azuis. Assim, a probabilidade é 2/5, ou 40%.",
            "fonte": "Vestibular Unificado UFSC/IFSC/IFC 2025, Matemática, prova amarela, questões 21–30 (adaptada; conteúdo de probabilidade)."
        },
        {
            "pergunta": "Uma sala retangular mede 8 m por 5 m. Quantos metros quadrados de piso são necessários para cobrir o chão?",
            "alternativas": [
                "13 m².",
                "40 m².",
                "26 m²."
            ],
            "correta": 1,
            "explicacao": "A área de um retângulo é comprimento × largura. Portanto, 8 × 5 = 40 m².",
            "fonte": "Vestibular Unificado UFSC/IFSC/IFC 2025, Matemática, prova amarela, questões 21–30 (adaptada; geometria plana e resolução contextualizada)."
        },
        # HISTÓRIA (11–15)
        {
            "pergunta": "Na Revolução Industrial, o crescimento das fábricas alterou profundamente o trabalho. Qual transformação marcou esse processo?",
            "alternativas": [
                "A expansão do trabalho assalariado e da produção mecanizada.",
                "O retorno predominante à produção artesanal doméstica.",
                "O fim das diferenças entre proprietários e trabalhadores."
            ],
            "correta": 0,
            "explicacao": "A industrialização ampliou a produção mecanizada e consolidou o trabalho assalariado nas fábricas. Também fortaleceu a formação de uma classe trabalhadora urbana.",
            "fonte": "Vestibular Unificado UFSC/IFSC/IFC 2025, História, prova amarela, questão 1 (adaptada; Revolução Industrial e classe trabalhadora)."
        },
        {
            "pergunta": "A rotina nas fábricas durante a Revolução Industrial passou a ser organizada por horários rígidos. O que isso evidencia?",
            "alternativas": [
                "A autonomia total dos trabalhadores sobre o ritmo de produção.",
                "O controle do tempo de trabalho pela disciplina fabril.",
                "A ausência de divisão de tarefas nas fábricas."
            ],
            "correta": 1,
            "explicacao": "A fábrica organizava o trabalho por horários, supervisão e ritmo de produção. Essa disciplina diferenciava a experiência fabril de muitas formas de trabalho anteriores.",
            "fonte": "Vestibular Unificado UFSC/IFSC/IFC 2025, História, prova amarela, questão 1 (adaptada; impactos sociais da Revolução Industrial)."
        },
        {
            "pergunta": "A industrialização inglesa contribuiu para o crescimento das cidades e da classe operária. Qual grupo era formado principalmente por trabalhadores que vendiam sua força de trabalho?",
            "alternativas": [
                "A nobreza proprietária de terras.",
                "A burguesia industrial.",
                "O proletariado."
            ],
            "correta": 2,
            "explicacao": "O proletariado é composto por trabalhadores que, sem controlar os meios de produção, vendem sua força de trabalho em troca de salário. A classe operária cresceu com a expansão das fábricas.",
            "fonte": "Vestibular Unificado UFSC/IFSC/IFC 2025, História, prova amarela, questão 1 (adaptada; formação da classe operária)."
        },
        {
            "pergunta": "A Lei do Ventre Livre, aprovada no Brasil em 1871, declarou livres os filhos de mulheres escravizadas nascidos a partir daquela data. O que limitava essa liberdade na prática?",
            "alternativas": [
                "A escravidão foi abolida imediatamente para toda a população.",
                "A lei manteve formas de tutela e dependência durante a infância.",
                "As crianças passaram a receber terras do governo."
            ],
            "correta": 1,
            "explicacao": "Embora declarasse livres essas crianças, a lei previa que permanecessem sob autoridade dos senhores das mães por muitos anos, com alternativas legais de tutela e prestação de serviços. Por isso, a liberdade era limitada na prática.",
            "fonte": "Vestibular Unificado UFSC/IFSC/IFC 2025, História, prova amarela, questão 2 (adaptada; Lei do Ventre Livre e limites da liberdade)."
        },
        {
            "pergunta": "Por que a Lei do Ventre Livre não significou o fim imediato da escravidão no Brasil?",
            "alternativas": [
                "Porque manteve a escravidão de pessoas adultas e não extinguiu de imediato as relações de exploração.",
                "Porque proibiu a liberdade de todos os filhos de mulheres escravizadas.",
                "Porque restaurou oficialmente o tráfico transatlântico."
            ],
            "correta": 0,
            "explicacao": "A lei de 1871 foi uma medida gradual e não libertou imediatamente as pessoas adultas escravizadas. Além disso, a situação das crianças declaradas livres permaneceu condicionada por mecanismos de tutela e trabalho.",
            "fonte": "Vestibular Unificado UFSC/IFSC/IFC 2025, História, prova amarela, questão 2 (adaptada; debate sobre a Lei do Ventre Livre)."
        }
    ]
}

LEGENDAS = {
    TEMA: "15 questões adaptadas de vestibular federal: Biologia, Matemática e História. Responda antes da explicação!\n\n#JuhQuiz #Vestibular #Estudos #Conhecimento"
}
