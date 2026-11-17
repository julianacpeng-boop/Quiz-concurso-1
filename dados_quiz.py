# Quiz com 15 questões adaptadas do ENEM 2026: Biologia e História.
# Cada item é pensado para um vídeo independente; enunciados e alternativas
# foram reescritos e resumidos para o formato curto.
# `correta`: 0 = A, 1 = B, 2 = C.

CAPA_SEGUNDOS = 2
TEMA = "ENEM 2026 — Biologia e História"

QUIZZES = {
    TEMA: [
        {
            "pergunta": "No milho, a inserção do gene Bt, originado de uma bactéria, ajuda a controlar lagartas que atacam a lavoura. Qual benefício pode resultar dessa técnica?",
            "alternativas": [
                "Menores perdas e maior produtividade do milho.",
                "Transformação das lagartas em polinizadoras.",
                "Eliminação da necessidade de água na plantação."
            ],
            "correta": 0,
            "explicacao": "O gene Bt permite que a planta produza uma proteína que afeta determinadas lagartas-praga. Com menos danos às plantas, a lavoura pode ter menos perdas e maior produtividade.",
            "fonte": "ENEM 2026, Biologia, questão 103 (adaptada)"
        },
        {
            "pergunta": "Para avaliar metais pesados em um manguezal, qual organismo pode funcionar como bom indicador ambiental?",
            "alternativas": [
                "Uma ave que sobrevoa a região.",
                "Um sururu que filtra a água e retém partículas.",
                "Um peixe predador que visita vários ambientes."
            ],
            "correta": 1,
            "explicacao": "O sururu filtra a água do manguezal e pode acumular contaminantes em seus tecidos. Por isso, sua análise ajuda a revelar a qualidade ambiental do local onde vive.",
            "fonte": "ENEM 2026, Biologia, questão 107 (adaptada)"
        },
        {
            "pergunta": "A seleção natural atua sobre indivíduos que já apresentam diferenças em uma população. Essas diferenças são chamadas de:",
            "alternativas": [
                "Características adquiridas por esforço individual.",
                "Mudanças que surgem porque o ambiente precisa delas.",
                "Variações entre os indivíduos da população."
            ],
            "correta": 2,
            "explicacao": "A seleção natural não cria as características de que a espécie precisa. Ela favorece algumas variações que já existem; indivíduos com características vantajosas podem sobreviver e deixar mais descendentes.",
            "fonte": "ENEM 2026, Biologia, questão 109 (adaptada)"
        },
        {
            "pergunta": "Corredores treinam em locais de altitude, onde há menos oxigênio disponível. Se o condicionamento favorece a respiração aeróbica, o teste de esforço pode indicar:",
            "alternativas": [
                "Aumento do lactato no sangue.",
                "Redução do lactato produzido durante o esforço.",
                "Desaparecimento das hemácias."
            ],
            "correta": 1,
            "explicacao": "Com melhor adaptação ao uso de oxigênio, os músculos conseguem obter mais energia pela respiração aeróbica. Isso reduz a dependência da via anaeróbica, que produz lactato, e tende a diminuir seus níveis no sangue durante o esforço.",
            "fonte": "ENEM 2026, Biologia, questão 120 (adaptada)"
        },
        {
            "pergunta": "Em uma flor, o gene A permite formar pigmento rosa; o gene B transforma esse pigmento em vermelho. Quando o gene A está em aa, nenhum pigmento é produzido; em bb, a transformação em vermelho não ocorre. Qual genótipo pode gerar flor rosa?",
            "alternativas": [
                "AaBB.",
                "aaBb.",
                "Aabb."
            ],
            "correta": 2,
            "explicacao": "Para formar o pigmento rosa, a planta precisa ter pelo menos um alelo A dominante. Para não convertê-lo em vermelho, precisa ser bb. Assim, Aabb pode produzir flor rosa.",
            "fonte": "ENEM 2026, Biologia, questão 123 (adaptada)"
        },
        {
            "pergunta": "Lagartas comem somente a gema apical de plantas jovens. Ao perder essa ponta do caule, o que tende a acontecer com as plantas?",
            "alternativas": [
                "As gemas laterais começam a crescer, formando ramos.",
                "Todas as raízes param imediatamente de absorver água.",
                "Uma nova gema apical surge no mesmo ponto."
            ],
            "correta": 0,
            "explicacao": "A gema apical produz auxina, que inibe o crescimento das gemas laterais. Quando a ponta é removida, essa inibição diminui e os ramos laterais podem se desenvolver.",
            "fonte": "ENEM 2026, Biologia, questão 124 (adaptada)"
        },
        {
            "pergunta": "Uma comunidade limita a pesca do pirarucu durante o período reprodutivo. Qual é a finalidade ambiental dessa medida?",
            "alternativas": [
                "Impedir que os peixes se reproduzam nos rios.",
                "Permitir a reprodução e ajudar a recuperar o estoque de peixes.",
                "Substituir as espécies nativas por espécies criadas em cativeiro."
            ],
            "correta": 1,
            "explicacao": "O período de defeso protege os peixes enquanto se reproduzem. Com mais indivíduos chegando à fase reprodutiva, a população pode se recuperar e a pesca pode continuar de forma mais sustentável.",
            "fonte": "ENEM 2026, Biologia, questão 128 (adaptada)"
        },
        {
            "pergunta": "No Brasil colonial, um religioso criticou senhores que separavam casais escravizados e negligenciavam sua instrução religiosa. O texto expõe principalmente:",
            "alternativas": [
                "A igualdade de direitos entre senhores e escravizados.",
                "O fim do trabalho forçado nos engenhos.",
                "A condição da cultura cristã dentro da relação de dominação."
            ],
            "correta": 2,
            "explicacao": "A crítica mostra a contradição entre a prática cristã defendida pelos senhores e o tratamento imposto às pessoas escravizadas. O contexto de dominação limitava até a vida familiar e religiosa dos cativos.",
            "fonte": "ENEM 2026, História, questão 58 (adaptada)"
        },
        {
            "pergunta": "No início do século XX, um anúncio apresenta uma mulher médica atendendo clientes; outra publicação associa o papel feminino ao casamento e à família. Que contraste aparece?",
            "alternativas": [
                "Atuação profissional no espaço público e ideal doméstico no privado.",
                "Participação política e serviço militar.",
                "Vida religiosa e educação universitária."
            ],
            "correta": 0,
            "explicacao": "O anúncio mostra uma mulher trabalhando e atendendo o público, enquanto a revista reforça expectativas ligadas ao lar, ao casamento e à família. O contraste é entre as esferas pública e privada.",
            "fonte": "ENEM 2026, História, questão 60 (adaptada)"
        },
        {
            "pergunta": "Canções brasileiras do fim dos anos 1970 celebravam a volta de pessoas que haviam deixado o país durante a ditadura. Esse contexto se relaciona à luta pelo retorno de:",
            "alternativas": [
                "Imigrantes que buscavam trabalho nas cidades.",
                "Exilados políticos, durante a abertura e a campanha pela anistia.",
                "Soldados brasileiros que voltavam da Segunda Guerra."
            ],
            "correta": 1,
            "explicacao": "As canções remetem à campanha pela anistia e ao desejo de retorno de brasileiros exilados pela ditadura. Em 1979, a Lei da Anistia permitiu que muitos voltassem ao país.",
            "fonte": "ENEM 2026, História, questão 65 (adaptada)"
        },
        {
            "pergunta": "Dois relatos, sobre tradições indígenas na América do Sul e na América do Norte, descrevem rituais que prometiam renovação e abundância. O ponto em comum é:",
            "alternativas": [
                "A adoção de costumes impostos por colonizadores.",
                "A substituição das identidades de diferentes povos.",
                "A valorização de práticas e crenças originárias."
            ],
            "correta": 2,
            "explicacao": "Apesar de pertencerem a povos e épocas diferentes, os relatos mostram tradições religiosas próprias, ligadas à esperança de renovação. Essas práticas originárias também expressavam resistência em contextos de pressão colonial.",
            "fonte": "ENEM 2026, História, questão 66 (adaptada)"
        },
        {
            "pergunta": "No século XIX, um gabinete de leitura emprestava livros, mas também promovia debates, saraus e encontros. O que o diferenciava de uma biblioteca comum?",
            "alternativas": [
                "Também funcionava como espaço de convivência e debate público.",
                "Era dedicado apenas à guarda de documentos religiosos.",
                "Proibia a circulação de jornais e revistas."
            ],
            "correta": 0,
            "explicacao": "Além do empréstimo de livros, o gabinete organizava debates e eventos sociais. Por isso, tinha uma atuação mais ampla do que a de uma biblioteca voltada principalmente ao acervo e à leitura.",
            "fonte": "ENEM 2026, História, questão 68 (adaptada)"
        },
        {
            "pergunta": "Em mosteiros medievais, pessoas nobres podiam ocupar posições privilegiadas, enquanto pessoas pobres eram admitidas em condições inferiores. Isso indica que os mosteiros:",
            "alternativas": [
                "Eliminavam as diferenças sociais da época.",
                "Reproduziam hierarquias presentes na sociedade.",
                "Eram espaços sem relação com a vida social."
            ],
            "correta": 1,
            "explicacao": "Embora fossem instituições religiosas, os mosteiros também refletiam desigualdades do mundo exterior: a origem social influenciava o lugar ocupado por cada pessoa.",
            "fonte": "ENEM 2026, História, questão 78 (adaptada)"
        },
        {
            "pergunta": "A construção de uma ferrovia e a exploração de madeira no Sul do Brasil, no início do século XX, avançaram sobre terras ocupadas por comunidades locais. Que consequência esse modelo gerou?",
            "alternativas": [
                "Distribuição igualitária das terras entre os moradores.",
                "Redução dos conflitos por meio da preservação das comunidades.",
                "Modernização econômica acompanhada de expulsões e conflitos locais."
            ],
            "correta": 2,
            "explicacao": "A expansão ferroviária e a exploração econômica foram apresentadas como progresso, mas também concentraram terras e expulsaram moradores. Esse processo contribuiu para tensões sociais ligadas à Guerra do Contestado.",
            "fonte": "ENEM 2026, História, questão 81 (adaptada)"
        },
        {
            "pergunta": "O crescimento econômico acelerado do Brasil no início dos anos 1970 foi seguido por recessão e inflação na década seguinte. Um fator que contribuiu para a crise foi:",
            "alternativas": [
                "O aumento da dívida externa e dos juros internacionais.",
                "A falta de empresas estatais no período.",
                "A redução dos empréstimos feitos no exterior."
            ],
            "correta": 0,
            "explicacao": "Parte do crescimento foi financiada por empréstimos externos. Com a elevação dos juros internacionais e as crises do petróleo, o custo da dívida aumentou, pressionando a economia e contribuindo para a crise dos anos 1980.",
            "fonte": "ENEM 2026, História, questão 82 (adaptada)"
        }
    ]
}

LEGENDAS = {
    TEMA: "Biologia e História em questões adaptadas do ENEM 2026. Responda antes da explicação!\n\n#JuhQuiz #ENEM #Biologia #História"
}
