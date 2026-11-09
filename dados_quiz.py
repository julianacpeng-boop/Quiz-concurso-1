# Dados do Quiz — Gravidez, menstruação e primeira vez
# 15 questões autorais: 5 de cada tema, uma pergunta por vídeo.

CAPA_SEGUNDOS = 2

QUIZZES = {
    "Gravidez — teste após atraso menstrual": [
        {
            "pergunta": "Segundo a orientação do Ministério da Saúde, atraso menstrual superior a 15 dias deve levar a pessoa a:",
            "alternativas": ["Procurar uma unidade de saúde para orientação sobre teste de gravidez", "Considerar a gravidez confirmada sem teste", "Esperar seis meses antes de procurar atendimento"],
            "correta": 0,
            "explicacao": "O Ministério da Saúde orienta que, diante de atraso menstrual superior a 15 dias, a equipe de saúde encaminhe para o Teste Imunológico de Gravidez (TIG), considerado sensível e confiável.",
            "fonte": "(Ministério da Saúde, “Gravidez”, orientação sobre atraso menstrual e TIG)",
        },
    ],
    "Gravidez — início do pré-natal": [
        {
            "pergunta": "Quando é recomendado iniciar o pré-natal após a confirmação da gravidez?",
            "alternativas": ["Somente no último trimestre", "O mais precocemente possível", "Apenas quando surgirem sintomas"],
            "correta": 1,
            "explicacao": "O Ministério da Saúde destaca a importância de iniciar o pré-natal o mais cedo possível e comparecer às consultas regularmente, para acompanhar a saúde da gestante e do bebê.",
            "fonte": "(Ministério da Saúde, “Gravidez”, acompanhamento pré-natal)",
        },
    ],
    "Gravidez — ácido fólico": [
        {
            "pergunta": "A suplementação de ácido fólico antes e durante a gestação pode ajudar a reduzir o risco de quê?",
            "alternativas": ["Todas as complicações possíveis da gravidez", "Infecções sexualmente transmissíveis", "Algumas anomalias congênitas, como defeitos do tubo neural"],
            "correta": 2,
            "explicacao": "A suplementação de ácido fólico no período pré-concepcional e durante a gestação reduz a chance de algumas anomalias congênitas, incluindo defeitos de fechamento do tubo neural. A orientação deve ser feita por profissional de saúde.",
            "fonte": "(Ministério da Saúde, FAQ “O ácido fólico pode prevenir anomalias congênitas?”, atualizado em 17/03/2026)",
        },
    ],
    "Gravidez — contracepção de emergência": [
        {
            "pergunta": "Após uma relação desprotegida ou falha do método, até quando pode ser considerada a contracepção oral de emergência?",
            "alternativas": ["Até cinco dias, com maior eficácia quanto antes for usada", "Somente até 12 horas", "Até 30 dias, com a mesma eficácia"],
            "correta": 0,
            "explicacao": "O protocolo do Ministério da Saúde prevê o uso da contracepção oral de emergência até cinco dias após a relação, com maior eficácia quanto mais cedo for utilizada. A equipe de saúde pode orientar sobre a opção adequada.",
            "fonte": "(Ministério da Saúde, PCDT para PEP, seção sobre anticoncepção de emergência, 2023)",
        },
    ],
    "Gravidez — risco na primeira relação": [
        {
            "pergunta": "Uma relação vaginal sem método contraceptivo pode causar gravidez mesmo sendo a primeira relação sexual?",
            "alternativas": ["Não; a primeira relação não causa gravidez", "Sim; pode haver gravidez desde a primeira relação", "Somente se houver sangramento"],
            "correta": 1,
            "explicacao": "A possibilidade de gravidez depende da exposição a espermatozoides e do período fértil, não de ser a primeira relação. Métodos contraceptivos podem ser discutidos com a equipe de saúde.",
            "fonte": "(Ministério da Saúde, “Contracepção” e “Use Preservativo”)",
        },
    ],
    "Menstruação — duração do ciclo": [
        {
            "pergunta": "Qual intervalo de duração do ciclo menstrual é apresentado pelo Ministério da Saúde como usual?",
            "alternativas": ["Sempre exatamente 28 dias", "Entre 60 e 90 dias", "Entre 21 e 35 dias"],
            "correta": 2,
            "explicacao": "O material do Programa Dignidade Menstrual informa que os ciclos variam entre as pessoas e costumam ocorrer em intervalos de 21 a 35 dias.",
            "fonte": "(Ministério da Saúde, Cartilha do Programa Dignidade Menstrual, 2025, glossário menstrual)",
        },
    ],
    "Menstruação — duração do fluxo": [
        {
            "pergunta": "De acordo com material do Ministério da Saúde, por quanto tempo costuma durar o sangramento menstrual?",
            "alternativas": ["De 3 a 7 dias", "De 10 a 15 dias em todos os ciclos", "Exatamente 24 horas"],
            "correta": 0,
            "explicacao": "O Ministério da Saúde informa que o fluxo menstrual geralmente dura de 3 a 7 dias, embora possa haver variações individuais.",
            "fonte": "(Ministério da Saúde, Cartilha do Programa Dignidade Menstrual, 2025, glossário menstrual)",
        },
    ],
    "Menstruação — por que ocorre o fluxo": [
        {
            "pergunta": "Quando não há fecundação e o endométrio descama, o que acontece?",
            "alternativas": ["A menstruação deixa de ocorrer para sempre", "O tecido é eliminado como fluxo menstrual", "A gravidez fica confirmada"],
            "correta": 1,
            "explicacao": "Quando não há gestação, o revestimento interno do útero (endométrio) descama e é eliminado pelo corpo como fluxo menstrual.",
            "fonte": "(Ministério da Saúde, “Série orienta mulheres sobre cuidados durante a menstruação”, Saúde Menstrual)",
        },
    ],
    "Menstruação — cólica intensa": [
        {
            "pergunta": "Se a dor menstrual é muito intensa ou interfere nas atividades diárias, o que é recomendado?",
            "alternativas": ["Considerar sempre normal e nunca buscar ajuda", "Suspender toda atividade física por tempo indeterminado", "Procurar avaliação de um serviço de saúde"],
            "correta": 2,
            "explicacao": "Cólicas podem ocorrer, mas dor muito intensa ou que interfere nas atividades merece avaliação profissional. A OMS orienta que dificuldades menstruais sejam ouvidas e avaliadas por trabalhadores da saúde.",
            "fonte": "(Organização Mundial da Saúde, “Menstrual health”, sinais que justificam cuidado)",
        },
    ],
    "Menstruação — mudanças importantes no ciclo": [
        {
            "pergunta": "Se houver mudanças importantes ou duradouras no ciclo ou no fluxo menstrual, qual deve ser a atitude?",
            "alternativas": ["Procurar uma unidade de saúde para avaliação", "Ignorar qualquer alteração por vários anos", "Tomar medicamento por conta própria"],
            "correta": 0,
            "explicacao": "A cartilha do Programa Dignidade Menstrual orienta procurar uma unidade de saúde quando são observadas alterações importantes ou mais duradouras no ciclo ou no fluxo.",
            "fonte": "(Ministério da Saúde, Cartilha do Programa Dignidade Menstrual, 2025, cuidados com a saúde)",
        },
    ],
    "Primeira vez — decisão sem pressão": [
        {
            "pergunta": "Qual afirmação sobre a decisão de ter a primeira relação sexual está de acordo com os direitos sexuais?",
            "alternativas": ["A pessoa deve aceitar se a parceria insistir", "A decisão deve ser livre, sem pressão ou imposição", "É obrigatório iniciar a vida sexual em determinada idade"],
            "correta": 1,
            "explicacao": "Os direitos sexuais incluem escolher se quer ou não ter relação sexual e viver a sexualidade sem violência, discriminação ou imposições.",
            "fonte": "(Ministério da Saúde, “Direitos sexuais, direitos reprodutivos e métodos anticoncepcionais”, direitos sexuais)",
        },
    ],
    "Primeira vez — sangramento": [
        {
            "pergunta": "É obrigatório haver sangramento na primeira relação sexual vaginal?",
            "alternativas": ["Sim; isso acontece com todas as pessoas", "Sim; a ausência sempre indica um problema", "Não; pode não haver sangramento"],
            "correta": 2,
            "explicacao": "Não é obrigatório sangrar na primeira relação. A anatomia varia, e a presença ou ausência de sangramento não comprova histórico sexual.",
            "fonte": "(Ministério da Saúde, BVS, publicação “Prevenir”, orientação sobre a primeira relação)",
        },
    ],
    "Primeira vez — hímen e histórico sexual": [
        {
            "pergunta": "A aparência do hímen consegue comprovar se uma pessoa já teve relação sexual?",
            "alternativas": ["Não; a aparência não é um indicador confiável e não há exame que prove esse histórico", "Sim; basta observar se há uma abertura", "Sim; um exame sempre identifica a primeira relação"],
            "correta": 0,
            "explicacao": "A OMS afirma que a aparência do hímen não é um indicador confiável de relação sexual e que não existe exame capaz de provar histórico de relação vaginal.",
            "fonte": "(OMS, UN Human Rights e UN Women, “Eliminating virginity testing”, declaração interagências, 2018)",
        },
    ],
    "Primeira vez — dor e desconforto": [
        {
            "pergunta": "Se houver dor ou desconforto durante a primeira relação, qual atitude respeita a saúde e os limites da pessoa?",
            "alternativas": ["Continuar para não decepcionar a parceria", "Pausar ou parar e conversar; ninguém é obrigado a continuar", "Ignorar a dor em todas as situações"],
            "correta": 1,
            "explicacao": "Uma experiência sexual deve ser segura e livre de coerção. A pessoa pode pausar ou parar; dor intensa ou persistente merece orientação de um serviço de saúde.",
            "fonte": "(OMS, “Sexual health”; Ministério da Saúde, direitos sexuais e reprodutivos)",
        },
    ],
    "Primeira vez — informação e planejamento": [
        {
            "pergunta": "Se a pessoa quer evitar uma gravidez antes da primeira relação, qual atitude ajuda a fazer uma escolha consciente?",
            "alternativas": ["Confiar apenas em comentários de redes sociais", "Não se informar porque será apenas a primeira vez", "Buscar informação confiável e conversar com a equipe de saúde sobre métodos"],
            "correta": 2,
            "explicacao": "O Ministério da Saúde orienta que a pessoa tenha acesso a informações confiáveis sobre os métodos contraceptivos e possa conversar com a equipe de saúde para escolher de forma consciente.",
            "fonte": "(Ministério da Saúde, “Contracepção”, planejamento reprodutivo)",
        },
    ],
}

LEGENDAS = {
    "Gravidez — teste após atraso menstrual": "Atraso menstrual: quando testar? #JuhQuiz #Gravidez #Saude #Estudos",
    "Gravidez — início do pré-natal": "Pré-natal: quando começar? #JuhQuiz #Gravidez #Saude #Estudos",
    "Gravidez — ácido fólico": "Ácido fólico e gestação. #JuhQuiz #Gravidez #Saude #Estudos",
    "Gravidez — contracepção de emergência": "Contracepção de emergência: até quando? #JuhQuiz #Gravidez #Saude #Estudos",
    "Gravidez — risco na primeira relação": "A primeira relação pode causar gravidez? #JuhQuiz #Gravidez #Saude #Estudos",
    "Menstruação — duração do ciclo": "Quanto dura o ciclo menstrual? #JuhQuiz #Menstruacao #Saude #Estudos",
    "Menstruação — duração do fluxo": "Quanto tempo dura o fluxo menstrual? #JuhQuiz #Menstruacao #Saude #Estudos",
    "Menstruação — por que ocorre o fluxo": "Você sabe por que ocorre a menstruação? #JuhQuiz #Menstruacao #Saude #Estudos",
    "Menstruação — cólica intensa": "Cólica intensa merece atenção. #JuhQuiz #Menstruacao #Saude #Estudos",
    "Menstruação — mudanças importantes no ciclo": "Mudanças no ciclo: quando procurar ajuda? #JuhQuiz #Menstruacao #Saude #Estudos",
    "Primeira vez — decisão sem pressão": "A primeira vez tem que ser sem pressão. #JuhQuiz #PrimeiraVez #Saude #Estudos",
    "Primeira vez — sangramento": "É obrigatório sangrar na primeira vez? #JuhQuiz #PrimeiraVez #Saude #Estudos",
    "Primeira vez — hímen e histórico sexual": "O hímen comprova histórico sexual? #JuhQuiz #PrimeiraVez #Saude #Estudos",
    "Primeira vez — dor e desconforto": "Dor não significa que precisa continuar. #JuhQuiz #PrimeiraVez #Saude #Estudos",
    "Primeira vez — informação e planejamento": "Informação ajuda a decidir com segurança. #JuhQuiz #PrimeiraVez #Saude #Estudos",
}
