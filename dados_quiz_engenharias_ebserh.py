# Dados do Quiz — Engenharias em concursos EBSERH
# Questões autorais/adaptadas de temas cobrados nas provas citadas nas fontes.
# Cada grupo contém cinco perguntas para vídeos individuais.

CAPA_SEGUNDOS = 2

QUIZZES = {
    "engenheiro_mecanico_ebserh": [
        {
            "pergunta": "Uma barra recebe força axial de 100 kN e tem área de 2 cm². Qual é a tensão normal média?",
            "alternativas": ['50 MPa', '500 MPa', '5 MPa'],
            "correta": 1,
            "explicacao": "A tensão normal é força dividida pela área. Convertendo 2 cm² para 0,0002 m²: 100.000 N ÷ 0,0002 m² = 500.000.000 Pa, ou 500 MPa.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Edital 04, Engenheiro Mecânico, questão sobre mecânica dos sólidos (tema adaptado).",
        },
        {
            "pergunta": "Na condução de calor em uma parede plana homogênea, o fluxo de calor aumenta quando aumenta qual grandeza, mantidas as demais constantes?",
            "alternativas": ['A espessura da parede', 'A resistência térmica da parede', 'A diferença de temperatura entre as faces'],
            "correta": 2,
            "explicacao": "Pela lei de Fourier para parede plana, o fluxo é proporcional à diferença de temperatura e à condutividade, e inversamente proporcional à espessura.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Edital 04, Engenheiro Mecânico, conteúdo de termodinâmica e transferência de calor (tema adaptado).",
        },
        {
            "pergunta": "Uma máquina frigorífica retira 3 kW de calor do ambiente refrigerado e consome 1 kW de potência. Qual é seu coeficiente de desempenho (COP)?",
            "alternativas": ['1/3', '3', '4'],
            "correta": 1,
            "explicacao": "Para refrigeração, COP é o calor retirado do ambiente frio dividido pelo trabalho fornecido: 3 kW ÷ 1 kW = 3.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Edital 04, Engenheiro Mecânico, conteúdo de sistemas termomecânicos (questão autoral sobre o tema).",
        },
        {
            "pergunta": "Em um escoamento permanente, incompressível e ideal, qual princípio relaciona pressão, velocidade e altura ao longo de uma linha de corrente?",
            "alternativas": ['Lei de Hooke', 'Lei de Fourier', 'Equação de Bernoulli'],
            "correta": 2,
            "explicacao": "A equação de Bernoulli expressa a conservação da energia mecânica do fluido ideal ao longo de uma linha de corrente, relacionando pressão, energia cinética e energia potencial por unidade de volume.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Edital 04, Engenheiro Mecânico, conteúdo de mecânica dos fluidos (questão autoral sobre o tema).",
        },
        {
            "pergunta": "Em um ensaio de tração dentro do regime elástico linear, qual relação descreve a lei de Hooke para tensão e deformação?",
            "alternativas": ['Tensão é igual ao módulo de elasticidade vezes a deformação', 'Tensão é igual à deformação dividida pela massa', 'Deformação é independente da tensão'],
            "correta": 0,
            "explicacao": "No regime elástico linear, a tensão normal é proporcional à deformação específica: σ = E·ε, em que E é o módulo de elasticidade.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Edital 04, Engenheiro Mecânico, conteúdo de materiais de construção mecânica e mecânica dos sólidos (tema adaptado).",
        },
    ],
    "engenheiro_clinico_ebserh": [
        {
            "pergunta": "Qual é o objetivo central do gerenciamento de tecnologias em saúde em um estabelecimento assistencial?",
            "alternativas": ['Registrar somente os equipamentos que falharam', 'Substituir as instruções do fabricante por um padrão único', 'Promover rastreabilidade, qualidade, eficácia e segurança'],
            "correta": 2,
            "explicacao": "O gerenciamento deve acompanhar a tecnologia desde a entrada até o destino final e contribuir para sua rastreabilidade, qualidade, eficácia, efetividade e segurança.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Edital 04, Engenheiro Clínico, tema de gestão de equipamentos; Anvisa, RDC nº 509/2021.",
        },
        {
            "pergunta": "Ao organizar o inventário de equipamentos médico-hospitalares, qual conjunto de informações é mais útil para rastrear cada bem?",
            "alternativas": ['Identificação única, localização e histórico de intervenções', 'Somente marca e cor', 'Somente o setor onde foi comprado'],
            "correta": 0,
            "explicacao": "Identificação única, localização e registros de manutenção, calibração e movimentação permitem acompanhar o equipamento e seu histórico durante o ciclo de vida.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Edital 04, Engenheiro Clínico, temas de estabelecimentos assistenciais e equipamentos biomédicos (adaptada).",
        },
        {
            "pergunta": "Qual atividade distingue principalmente a manutenção preventiva da manutenção corretiva?",
            "alternativas": ['Ocorre apenas depois que o equipamento para', 'É programada para reduzir a probabilidade de falha', 'Dispensa registro técnico'],
            "correta": 1,
            "explicacao": "A manutenção preventiva é planejada e executada em intervalos definidos ou conforme critérios técnicos para reduzir falhas e manter segurança e desempenho. A corretiva responde a uma falha identificada.",
            "fonte": "EBSERH, POP de Manutenção Preventiva de Equipamentos de Saúde; EBSERH/IBFC, Concurso 01/2023, Engenheiro Clínico, tema adaptado.",
        },
        {
            "pergunta": "Após manutenção de um equipamento eletromédico, o que deve ser feito antes de devolvê-lo ao setor assistencial?",
            "alternativas": ['Realizar os testes funcionais e de segurança pertinentes e registrar o serviço', 'Apenas confirmar que o painel acende', 'Liberar sem teste se a manutenção foi rápida'],
            "correta": 0,
            "explicacao": "A avaliação após a intervenção deve confirmar funcionamento e segurança conforme o tipo de equipamento e o serviço realizado. Os resultados e a liberação precisam ficar registrados.",
            "fonte": "EBSERH, POP de Teste de Segurança Elétrica e Manutenção; EBSERH/IBFC, Concurso 01/2023, Engenheiro Clínico, tema adaptado.",
        },
        {
            "pergunta": "Um aparelho foi projetado para uso domiciliar por leigos, sem necessidade de assistência profissional ou treinamento especializado. Como a Anvisa classifica esse tipo de dispositivo?",
            "alternativas": ['Dispositivo exclusivamente hospitalar', 'Acessório de infraestrutura predial', 'Dispositivo médico de uso pessoal'],
            "correta": 2,
            "explicacao": "Dispositivo médico de uso pessoal é aquele que, segundo a especificação do produto regularizado, não depende de assistência profissional ou treinamento especializado para ser utilizado.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Edital 04, Engenheiro Clínico, questão sobre dispositivos médicos de uso pessoal (tema adaptado); Anvisa.",
        },
    ],
    "engenheiro_eletrico_ebserh": [
        {
            "pergunta": "Em um circuito monofásico resistivo de 220 V e 10 A, qual é a potência ativa?",
            "alternativas": ['22 W', '2.200 W', '220 W'],
            "correta": 1,
            "explicacao": "Para carga resistiva, fator de potência é 1. A potência ativa é P = V·I = 220·10 = 2.200 W.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Edital 04, Engenheiro Eletricista, conteúdo de circuitos elétricos (questão autoral sobre o tema).",
        },
        {
            "pergunta": "Em um sistema trifásico equilibrado, qual expressão calcula a potência ativa usando tensão de linha e corrente de linha?",
            "alternativas": ['P = Vlinha ÷ Ilinha', 'P = √3 · Vlinha · Ilinha · fator de potência', 'P = 3 · Vlinha · Ilinha²'],
            "correta": 1,
            "explicacao": "Para um sistema trifásico equilibrado, P = √3·Vlinha·Ilinha·cosφ. O fator de potência corresponde ao cosseno do ângulo entre tensão e corrente.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Edital 04, Engenheiro Eletricista, conteúdo de circuitos elétricos e instalações (tema adaptado).",
        },
        {
            "pergunta": "Qual dispositivo é destinado a interromper automaticamente a corrente quando ocorre sobrecorrente, protegendo condutores e circuitos?",
            "alternativas": ['Disjuntor', 'Transformador de potencial', 'Banco de capacitores'],
            "correta": 0,
            "explicacao": "O disjuntor abre o circuito quando a corrente excede condições de operação definidas, como em sobrecarga ou curto-circuito, conforme sua especificação e coordenação com a instalação.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Edital 04, Engenheiro Eletricista, conteúdo de instalações elétricas e manutenção (questão autoral sobre o tema).",
        },
        {
            "pergunta": "Em uma instalação elétrica, qual é a função principal do condutor de proteção (PE)?",
            "alternativas": ['Conduzir a corrente normal da carga no lugar do neutro', 'Aumentar a tensão de alimentação', 'Conduzir corrente de falta e favorecer a atuação da proteção'],
            "correta": 2,
            "explicacao": "O condutor PE liga massas ao sistema de aterramento e fornece caminho para correntes de falta, favorecendo o desligamento automático pela proteção. Não deve ser usado como condutor de corrente normal da carga.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Edital 04, Engenheiro Eletricista, conteúdo de instalações elétricas; ABNT NBR 5410 (tema adaptado).",
        },
        {
            "pergunta": "Qual sequência corresponde a medidas essenciais para desenergização segura em serviços elétricos, conforme a NR-10?",
            "alternativas": ['Seccionar, impedir reenergização, constatar ausência de tensão, aterrar/equipotencializar e sinalizar', 'Desligar o disjuntor e iniciar o serviço sem verificação', 'Usar luvas e manter o circuito energizado'],
            "correta": 0,
            "explicacao": "A NR-10 prevê etapas de desenergização, incluindo seccionamento, impedimento de reenergização, constatação de ausência de tensão, aterramento temporário com equipotencialização quando aplicável e sinalização.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Edital 04, Engenheiro Eletricista; NR-10, item 10.5.1 (tema adaptado).",
        },
    ],
}

LEGENDAS = {
    "engenheiro_mecanico_ebserh": "Desafio para Engenheiro Mecânico de concurso EBSERH. Responda antes da explicação. #JuhQuiz #EBSERH #EngenhariaMecanica #Concursos",
    "engenheiro_clinico_ebserh": "Desafio para Engenheiro Clínico de concurso EBSERH. Responda antes da explicação. #JuhQuiz #EBSERH #EngenhariaClinica #Concursos",
    "engenheiro_eletrico_ebserh": "Desafio para Engenheiro Eletricista de concurso EBSERH. Responda antes da explicação. #JuhQuiz #EBSERH #EngenhariaEletrica #Concursos",
}
