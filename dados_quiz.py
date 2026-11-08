# Dados do Quiz — EBSERH: três cargos
# Cada vídeo contém uma pergunta. As questões foram adaptadas/autoriais,
# com fontes indicadas para estudo; não são transcrições integrais de prova.

CAPA_SEGUNDOS = 2

QUIZZES = {
    "tecnico_enfermagem_ebserh": [
        {
            "pergunta": "No pré-operatório, o período mediato compreende, em regra, o intervalo entre a indicação da cirurgia e as 24 horas que a antecedem. Como se chama esse período?",
            "alternativas": ["Pré-operatório mediato", "Pós-operatório imediato", "Período transoperatório"],
            "correta": 0,
            "explicacao": "O pré-operatório mediato começa quando a cirurgia é indicada e segue até as 24 horas anteriores ao procedimento. Nas últimas 24 horas, considera-se o pré-operatório imediato.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Técnico em Enfermagem, questão 42 (tema adaptado).",
        },
        {
            "pergunta": "Qual escala é usada para avaliar a recuperação do paciente após anestesia, considerando atividade, respiração, circulação, consciência e saturação de oxigênio?",
            "alternativas": ["Escala de Aldrete e Kroulik", "Escala de Braden", "Escala de Glasgow"],
            "correta": 0,
            "explicacao": "A escala de Aldrete e Kroulik avalia esses cinco parâmetros na recuperação pós-anestésica e auxilia a equipe na decisão sobre a alta da recuperação, conforme protocolo institucional.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Técnico em Enfermagem, questão 44 (tema adaptado).",
        },
        {
            "pergunta": "Qual é um dos cinco momentos para higienizar as mãos definidos pela Organização Mundial da Saúde?",
            "alternativas": ["Antes de tocar o paciente", "Somente ao terminar o plantão", "Apenas depois de retirar as luvas"],
            "correta": 0,
            "explicacao": "A higiene das mãos deve ocorrer antes de tocar o paciente, antes de procedimento limpo/asséptico, após risco de exposição a fluidos, após tocar o paciente e após tocar suas proximidades. Luvas não substituem a higiene.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Técnico em Enfermagem, questão 52; OMS, Meus 5 Momentos para Higiene das Mãos.",
        },
        {
            "pergunta": "Um paciente recebeu 1.500 mL de líquidos e eliminou 900 mL no período. Qual foi o balanço hídrico, considerando apenas esses valores?",
            "alternativas": ["Positivo em 600 mL", "Negativo em 600 mL", "Neutro"],
            "correta": 0,
            "explicacao": "O balanço é calculado subtraindo as saídas das entradas: 1.500 − 900 = 600 mL. Como as entradas foram maiores, o resultado é positivo.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Técnico em Enfermagem, questão 54 (tema adaptado).",
        },
        {
            "pergunta": "Antes de administrar um medicamento, qual prática ajuda a confirmar corretamente a identidade do paciente?",
            "alternativas": ["Conferir pelo menos dois identificadores", "Usar somente o número do leito", "Perguntar apenas o primeiro nome"],
            "correta": 0,
            "explicacao": "A identificação deve ser confirmada com pelo menos dois identificadores definidos no protocolo, como nome completo e data de nascimento. Número do leito ou localização não identifica o paciente.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Técnico em Enfermagem, questão 55 (tema adaptado); Protocolo de Identificação do Paciente, MS/Anvisa/Fiocruz.",
        },
    ],
    "tecnico_equipamentos_medicos_ebserh": [
        {
            "pergunta": "Ao receber um equipamento médico-hospitalar novo, qual ação favorece sua rastreabilidade durante todo o ciclo de vida?",
            "alternativas": ["Cadastrar identificação, localização e dados técnicos", "Guardar apenas a nota fiscal", "Aguardar a primeira falha para registrá-lo"],
            "correta": 0,
            "explicacao": "O gerenciamento requer identificação e registros que permitam acompanhar localização, intervenções, situação e histórico do equipamento desde a entrada até o destino final.",
            "fonte": "Anvisa, RDC nº 509/2021, arts. 1º e 2º; EBSERH, Norma Operacional de Gestão de Equipamentos Médico-Hospitalares.",
        },
        {
            "pergunta": "Qual é o objetivo principal da manutenção preventiva em um equipamento assistencial?",
            "alternativas": ["Reduzir falhas e preservar desempenho e segurança", "Substituir toda calibração", "Corrigir somente defeitos já ocorridos"],
            "correta": 0,
            "explicacao": "A manutenção preventiva é programada para reduzir a probabilidade de falhas e manter o equipamento em condições adequadas de desempenho e segurança. Ela não substitui calibrações ou ensaios quando aplicáveis.",
            "fonte": "EBSERH, Procedimentos Operacionais Padrão de Manutenção Preventiva, Calibração, Qualificação e Teste de Segurança Elétrica; Anvisa, RDC nº 509/2021.",
        },
        {
            "pergunta": "Quando o procedimento exigir calibração, qual evidência é essencial para avaliar o resultado metrológico?",
            "alternativas": ["Certificado ou relatório com resultados e rastreabilidade", "Apenas uma etiqueta com a data", "Uma anotação sem identificação do padrão"],
            "correta": 0,
            "explicacao": "O registro deve permitir verificar resultados, critérios de aceitação e rastreabilidade metrológica dos padrões utilizados, conforme o procedimento aplicável.",
            "fonte": "EBSERH, POP de Calibração de Equipamentos de Saúde; EBSERH, Norma Operacional de Gestão de Equipamentos Médico-Hospitalares.",
        },
        {
            "pergunta": "Após uma intervenção técnica em equipamento eletromédico, o que deve ocorrer antes de sua liberação para uso?",
            "alternativas": ["Verificações funcionais e de segurança previstas no procedimento", "Apenas limpar a parte externa", "Liberar imediatamente se o equipamento ligar"],
            "correta": 0,
            "explicacao": "A liberação depende de avaliação pós-intervenção, com testes funcionais e de segurança pertinentes ao equipamento e ao serviço executado, além do registro da intervenção.",
            "fonte": "EBSERH, POP de Teste de Segurança Elétrica e de Manutenção de Equipamentos de Saúde; Anvisa, RDC nº 509/2021.",
        },
        {
            "pergunta": "Para executar manutenção ou ensaio em um equipamento específico, qual referência técnica deve ser consultada primeiro?",
            "alternativas": ["Instruções do fabricante e procedimento institucional", "Uma configuração genérica de outro modelo", "Somente a lembrança de uma manutenção anterior"],
            "correta": 0,
            "explicacao": "Parâmetros e métodos podem variar entre modelos. As instruções do fabricante e os procedimentos institucionais orientam intervenções compatíveis com o equipamento e ajudam a preservar segurança e desempenho.",
            "fonte": "Anvisa, RDC nº 509/2021; EBSERH, Caderno de Processos e Práticas de Engenharia Clínica.",
        },
    ],
    "nutricionista_ebserh": [
        {
            "pergunta": "A deficiência de niacina (vitamina B3) está classicamente associada a qual doença?",
            "alternativas": ["Pelagra", "Beribéri", "Escorbuto"],
            "correta": 0,
            "explicacao": "A pelagra está associada à deficiência de niacina (B3) ou de seu precursor triptofano. Beribéri se relaciona à deficiência de tiamina (B1), e escorbuto à deficiência de vitamina C.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Nutricionista, questão de conhecimentos específicos sobre carências nutricionais (tema adaptado).",
        },
        {
            "pergunta": "Qual limitação é importante ao interpretar o índice de massa corporal (IMC) isoladamente?",
            "alternativas": ["Não distingue massa gorda de massa magra", "Mede diretamente a gordura visceral", "Substitui toda avaliação nutricional"],
            "correta": 0,
            "explicacao": "O IMC relaciona peso e estatura, mas não informa como o peso se distribui entre massa gorda e massa magra. Deve ser interpretado junto a outros dados clínicos e antropométricos.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Nutricionista, questão sobre avaliação antropométrica (tema adaptado).",
        },
        {
            "pergunta": "Para um paciente que necessita de nutrição enteral por período prolongado, qual acesso pode ser considerado pela equipe?",
            "alternativas": ["Gastrostomia", "Sonda orogástrica por tempo indefinido", "Acesso venoso periférico"],
            "correta": 0,
            "explicacao": "Quando há indicação de suporte enteral prolongado, a gastrostomia pode ser considerada pela equipe. A escolha depende da avaliação clínica, do trato gastrointestinal e do plano terapêutico.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Nutricionista, questão sobre terapia nutricional enteral (tema adaptado).",
        },
        {
            "pergunta": "A fermentação de fibras alimentares pela microbiota do cólon produz principalmente quais compostos?",
            "alternativas": ["Ácidos graxos de cadeia curta", "Aminoácidos essenciais em grande quantidade", "Vitamina B12 como produto principal"],
            "correta": 0,
            "explicacao": "A fermentação de fibras no cólon produz ácidos graxos de cadeia curta, como acetato, propionato e butirato, que podem ser utilizados pelas células intestinais e pelo organismo.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Nutricionista, questão sobre fibras e fermentação colônica (tema adaptado).",
        },
        {
            "pergunta": "Nas referências de ingestão dietética, o limite superior tolerável (UL) representa o quê?",
            "alternativas": ["Maior ingestão diária improvável de causar risco à saúde na população geral", "Necessidade média estimada para metade de um grupo", "Meta mínima obrigatória para todas as pessoas"],
            "correta": 0,
            "explicacao": "O UL é o maior nível de ingestão diária habitual que provavelmente não oferece risco de efeitos adversos à saúde para quase todos os indivíduos de um grupo. Não é uma meta de consumo.",
            "fonte": "EBSERH/IBFC, Concurso 01/2023, Nutricionista, questão sobre Dietary Reference Intakes (tema adaptado); National Academies, Dietary Reference Intakes.",
        },
    ],
}

LEGENDAS = {
    "tecnico_enfermagem_ebserh": "Questão de concurso para Técnico de Enfermagem EBSERH. Responda antes da explicação. #JuhQuiz #EBSERH #Enfermagem #Concursos",
    "tecnico_equipamentos_medicos_ebserh": "Desafio de conhecimentos em equipamentos médico-hospitalares. Responda antes da explicação. #JuhQuiz #EngenhariaClinica #EBSERH #Concursos",
    "nutricionista_ebserh": "Questão de concurso para Nutricionista EBSERH. Responda antes da explicação. #JuhQuiz #EBSERH #Nutricao #Concursos",
}
