# Quiz de vestibular federal com questões adaptadas e resumidas.
# Cada vídeo contém uma pergunta. `correta`: 0 = A, 1 = B, 2 = C.

CAPA_SEGUNDOS = 2
TEMA = "Vestibulares federais — Física, Química e Geografia"

QUIZZES = {
    TEMA: [
        # FÍSICA (1–5)
        {
            "pergunta": "Uma atleta mantém uma pose parada sobre uma perna durante uma apresentação. Para permanecer em equilíbrio, o corpo precisa ter:",
            "alternativas": [
                "Força resultante e torque resultante iguais a zero.",
                "Velocidade crescente em todas as direções.",
                "Força peso igual a zero."
            ],
            "correta": 0,
            "explicacao": "No equilíbrio estático, a soma das forças e a soma dos torques sobre o corpo são nulas. Assim, ele não sofre aceleração linear nem tendência de rotação.",
            "fonte": "Vestibular Unificado UFSC/IFSC/IFC 2025, Física, prova amarela, questão 21 (adaptada; Leis de Newton e equilíbrio, em contexto de breaking)."
        },
        {
            "pergunta": "Uma bola é lançada obliquamente e o efeito do ar é desprezado. Durante o movimento, qual grandeza permanece constante?",
            "alternativas": [
                "A velocidade vertical.",
                "A componente horizontal da velocidade.",
                "A aceleração da gravidade, que passa a zero no ponto mais alto."
            ],
            "correta": 1,
            "explicacao": "Sem resistência do ar, não há força horizontal resultante, então a componente horizontal da velocidade permanece constante. A gravidade altera a componente vertical.",
            "fonte": "Vestibular Unificado UFSC/IFSC/IFC 2025, Física, prova amarela, questão 22 (adaptada; lançamento de projéteis, energia e quantidade de movimento)."
        },
        {
            "pergunta": "Uma nadadora fica parcialmente submersa em uma piscina. O empuxo sobre ela corresponde ao peso:",
            "alternativas": [
                "Do fluido deslocado pelo corpo.",
                "Da própria nadadora, em qualquer situação.",
                "Da água existente em toda a piscina."
            ],
            "correta": 0,
            "explicacao": "Pelo princípio de Arquimedes, o empuxo tem intensidade igual ao peso do fluido deslocado pelo corpo. Ele depende do volume submerso e da densidade do fluido.",
            "fonte": "Vestibular Unificado UFSC/IFSC/IFC 2025, Física, prova amarela, questão 23 (adaptada; empuxo, densidade e Leis de Newton, em contexto de nado artístico)."
        },
        {
            "pergunta": "Em um circuito simples com resistores ligados em série, qual afirmação é correta?",
            "alternativas": [
                "A corrente elétrica tem o mesmo valor em todos os resistores.",
                "A tensão é obrigatoriamente zero em cada resistor.",
                "A corrente se divide entre os resistores como em ligações paralelas."
            ],
            "correta": 0,
            "explicacao": "Em uma ligação em série há um único caminho para as cargas. Por isso, a corrente que atravessa cada componente tem o mesmo valor; a tensão se divide entre eles.",
            "fonte": "Vestibular Unificado UFSC/IFSC/IFC 2025, Física, prova amarela, questão 25 (adaptada; eletrodinâmica, em contexto de corrida de 100 metros)."
        },
        {
            "pergunta": "Um cubo de gelo está a −10 °C e será aquecido até derreter completamente. Qual etapa ocorre primeiro?",
            "alternativas": [
                "A água líquida congela a 0 °C.",
                "O gelo aquece até 0 °C antes de começar a fusão.",
                "O gelo vira vapor sem passar pelo estado líquido."
            ],
            "correta": 1,
            "explicacao": "Antes da fusão, o gelo precisa receber calor para elevar sua temperatura de −10 °C até 0 °C. Só depois começa a mudança de estado, que ocorre com temperatura constante enquanto a fusão acontece.",
            "fonte": "Vestibular Unificado UFSC/IFSC/IFC 2025, Física, prova amarela, questão 27 (adaptada; calorimetria e aquecimento do gelo no contexto de maratona)."
        },
        # QUÍMICA (6–10)
        {
            "pergunta": "A gasolina contém muitos hidrocarbonetos. Por que esses compostos se misturam pouco com água?",
            "alternativas": [
                "Porque são predominantemente apolares, enquanto a água é polar.",
                "Porque a água não forma ligações entre suas moléculas.",
                "Porque todos os hidrocarbonetos reagem imediatamente com água."
            ],
            "correta": 0,
            "explicacao": "A água é polar e os hidrocarbonetos são, em geral, apolares. A diferença de polaridade dificulta a mistura entre eles, como se observa na separação entre água e gasolina.",
            "fonte": "Vestibular Unificado UFSC/IFSC/IFC 2025, Química, prova amarela, questão 35 (adaptada; química orgânica, ligações e solubilidade)."
        },
        {
            "pergunta": "Na combustão completa do etanol, C₂H₅OH + O₂ → CO₂ + H₂O. Qual equação está balanceada?",
            "alternativas": [
                "C₂H₅OH + O₂ → CO₂ + H₂O.",
                "C₂H₅OH + 3 O₂ → 2 CO₂ + 3 H₂O.",
                "2 C₂H₅OH + O₂ → 2 CO₂ + H₂O."
            ],
            "correta": 1,
            "explicacao": "A equação balanceada conserva os átomos: 2 carbonos formam 2 CO₂; 6 hidrogênios formam 3 H₂O. No total, são 7 átomos de oxigênio nos produtos, correspondendo a 1 do etanol e 6 de 3 O₂.",
            "fonte": "Vestibular Unificado UFSC/IFSC/IFC 2025, Química, prova amarela, questão 36 (adaptada; combustão de etanol e estequiometria)."
        },
        {
            "pergunta": "Uma turbina eólica transforma a energia do vento em eletricidade. Qual característica descreve corretamente essa fonte?",
            "alternativas": [
                "Depende da queima de carvão dentro de cada turbina.",
                "Não pode ser usada para gerar energia elétrica.",
                "Usa o movimento do ar para acionar o gerador, sem combustão direta de combustível."
            ],
            "correta": 2,
            "explicacao": "O vento movimenta as pás e o sistema aciona um gerador elétrico. A geração eólica não envolve queima direta de combustível na turbina, embora sua implantação possa ter impactos ambientais e materiais associados.",
            "fonte": "Vestibular Unificado UFSC/IFSC/IFC 2025, Química, prova amarela, questão 38 (adaptada; fontes de energia e energia eólica)."
        },
        {
            "pergunta": "Ao adicionar água a uma solução sem perder soluto, o que acontece com sua concentração?",
            "alternativas": [
                "Diminui, porque a mesma quantidade de soluto fica distribuída em maior volume.",
                "Aumenta, porque a água se transforma em soluto.",
                "Permanece sempre igual, qualquer que seja a quantidade de água adicionada."
            ],
            "correta": 0,
            "explicacao": "Na diluição, acrescenta-se solvente e o volume aumenta, enquanto a quantidade de soluto permanece constante. Por isso, a concentração diminui.",
            "fonte": "Vestibular Unificado UFSC/IFSC/IFC 2025, Química, prova amarela, questão 39 (adaptada; soluções, ácido-base e diluição)."
        },
        {
            "pergunta": "Um material tem massa de 200 g e volume de 100 cm³. Qual é sua densidade?",
            "alternativas": [
                "0,5 g/cm³.",
                "2 g/cm³.",
                "100 g/cm³."
            ],
            "correta": 1,
            "explicacao": "A densidade é a razão entre massa e volume: d = 200 g ÷ 100 cm³ = 2 g/cm³.",
            "fonte": "Vestibular Unificado UFSC/IFSC/IFC 2025, Química, prova amarela, questão 40 (adaptada; conceito de densidade)."
        },
        # GEOGRAFIA (11–15)
        {
            "pergunta": "Ao representar a superfície curva da Terra em um mapa plano, por que algumas formas ou áreas podem parecer distorcidas?",
            "alternativas": [
                "Porque toda projeção cartográfica produz algum tipo de distorção.",
                "Porque mapas planos mostram a Terra sem escala.",
                "Porque os continentes mudam de tamanho conforme a estação do ano."
            ],
            "correta": 0,
            "explicacao": "É impossível transferir toda a superfície curva da Terra para um plano sem distorções. Cada projeção preserva melhor certas propriedades, como áreas, formas, distâncias ou direções, em detrimento de outras.",
            "fonte": "Vestibular Unificado UFSC/IFSC/IFC 2025, Geografia, prova amarela, questão 08 (adaptada; cartografia e projeções)."
        },
        {
            "pergunta": "A maior parte da água existente na superfície terrestre está armazenada: ",
            "alternativas": [
                "Nos rios de água doce.",
                "Nos oceanos, como água salgada.",
                "Na atmosfera, em forma de vapor."
            ],
            "correta": 1,
            "explicacao": "A maior parcela da água do planeta está nos oceanos e é salgada. A água doce representa uma fração menor e está concentrada principalmente em geleiras, calotas polares e águas subterrâneas.",
            "fonte": "Vestibular Unificado UFSC/IFSC/IFC 2025, Geografia, prova amarela, questão 09 (adaptada; hidrosfera e distribuição da água)."
        },
        {
            "pergunta": "O uso intenso de pesticidas na agricultura pode gerar qual consequência socioambiental?",
            "alternativas": [
                "Eliminar toda a necessidade de monitorar a qualidade da água.",
                "Impedir que substâncias alcancem o solo e os cursos d’água.",
                "Contaminar o ambiente e aumentar riscos à saúde dependendo da exposição."
            ],
            "correta": 2,
            "explicacao": "Pesticidas podem alcançar o solo e a água e afetar organismos não alvo. Os riscos à saúde dependem de fatores como substância, dose, duração e via de exposição.",
            "fonte": "Vestibular Unificado UFSC/IFSC/IFC 2025, Geografia, prova amarela, questão 11 (adaptada; espaço agrário, pesticidas, saúde e ambiente)."
        },
        {
            "pergunta": "Por que os impactos de um evento climático extremo tendem a ser maiores em áreas com moradias precárias e pouca infraestrutura?",
            "alternativas": [
                "Porque o risco também depende da exposição e da vulnerabilidade da população.",
                "Porque eventos climáticos atingem apenas cidades sem rios.",
                "Porque a infraestrutura urbana não altera a capacidade de resposta."
            ],
            "correta": 0,
            "explicacao": "O desastre não é determinado apenas pelo fenômeno natural. A exposição de pessoas e bens, a vulnerabilidade social e a capacidade de prevenção e resposta influenciam a dimensão dos danos.",
            "fonte": "Vestibular Unificado UFSC/IFSC/IFC 2025, Geografia, prova amarela, questão 12 (adaptada; mudanças climáticas e fatores humanos nos desastres)."
        },
        {
            "pergunta": "Para que serve principalmente um censo demográfico?",
            "alternativas": [
                "Medir somente a produção industrial de cada município.",
                "Levantar informações sobre população e suas condições de vida para orientar políticas públicas.",
                "Registrar exclusivamente os limites entre países."
            ],
            "correta": 1,
            "explicacao": "O censo reúne dados sobre população, domicílios e características sociais e demográficas. Essas informações ajudam a conhecer as necessidades da sociedade e a planejar políticas e serviços.",
            "fonte": "Vestibular Unificado UFSC/IFSC/IFC 2025, Geografia, prova amarela, questão 14 (adaptada; Censo Demográfico 2022, demografia e problemas urbanos)."
        }
    ]
}

LEGENDAS = {
    TEMA: "15 questões adaptadas de vestibular federal: Física, Química e Geografia. Responda antes da explicação!\n\n#JuhQuiz #Vestibular #Estudos #Conhecimento"
}


# Distribui as respostas corretas entre A, B e C ao longo dos 15 vídeos.
# A ordem das alternativas é ajustada sem alterar o conteúdo ou a explicação.
for _indice, _questao in enumerate(QUIZZES[TEMA]):
    _destino = _indice % 3
    _resposta = _questao["alternativas"].pop(_questao["correta"])
    _questao["alternativas"].insert(_destino, _resposta)
    _questao["correta"] = _destino
del _indice, _questao, _destino, _resposta
