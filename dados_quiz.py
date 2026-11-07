# -*- coding: utf-8 -*-
"""15 questões autorais de Direito Penal para concurso público."""

CAPA_SEGUNDOS = 2

QUIZZES = {
    'Princípio da legalidade': [{
        'pergunta': 'De acordo com o Código Penal, quando uma conduta pode ser considerada crime e receber uma pena?',
        'alternativas': ['Quando houver lei anterior que a defina e pena previamente prevista em lei', 'Quando a autoridade considerar a conduta prejudicial', 'Quando houver apenas costume social sobre a punição'],
        'correta': 0,
        'explicacao': 'O princípio da legalidade exige lei anterior que defina o crime e lei anterior que estabeleça a pena. A regra impede a criação de crimes ou penas por decisão da autoridade ou por costume.',
        'fonte': 'Código Penal, art. 1º'
    }],
    'Crime doloso': [{
        'pergunta': 'Para o Código Penal, age dolosamente quem:',
        'alternativas': ['Quer o resultado ou assume o risco de produzi-lo', 'Produz o resultado por imprudência, negligência ou imperícia', 'Não prevê um resultado que era impossível prever'],
        'correta': 0,
        'explicacao': 'O dolo ocorre quando a pessoa quis o resultado ou assumiu o risco de produzi-lo. O Código Penal distingue essa hipótese do crime culposo, ligado à imprudência, negligência ou imperícia.',
        'fonte': 'Código Penal, art. 18, inciso I'
    }],
    'Crime culposo': [{
        'pergunta': 'Qual conjunto de modalidades caracteriza o crime culposo no Código Penal?',
        'alternativas': ['Imprudência, negligência ou imperícia', 'Intenção, motivo ou finalidade', 'Coação, ameaça ou fraude'],
        'correta': 0,
        'explicacao': 'O crime é culposo quando o resultado decorre de imprudência, negligência ou imperícia. Em regra, só há punição por culpa quando a lei prevê expressamente essa modalidade.',
        'fonte': 'Código Penal, art. 18, inciso II e parágrafo único'
    }],
    'Tentativa': [{
        'pergunta': 'Quando há tentativa de crime, conforme o Código Penal?',
        'alternativas': ['A execução começa, mas o crime não se consuma por circunstâncias alheias à vontade do agente', 'A pessoa apenas pensa em cometer o crime, sem iniciar a execução', 'O agente consuma o crime e depois se arrepende'],
        'correta': 0,
        'explicacao': 'A tentativa pressupõe início da execução. O crime não se consuma por circunstâncias que não dependem da vontade do agente; atos preparatórios, por si sós, não bastam para caracterizá-la.',
        'fonte': 'Código Penal, art. 14, inciso II'
    }],
    'Desistência voluntária e arrependimento eficaz': [{
        'pergunta': 'O que ocorre quando o agente, voluntariamente, desiste de prosseguir na execução ou impede que o resultado aconteça?',
        'alternativas': ['Responde somente pelos atos já praticados', 'Responde sempre pelo crime consumado', 'Fica automaticamente isento de qualquer responsabilidade'],
        'correta': 0,
        'explicacao': 'Na desistência voluntária, o agente interrompe a execução; no arrependimento eficaz, impede que o resultado se produza. Em ambos os casos, responde pelos atos que já praticou, se eles constituírem infração penal.',
        'fonte': 'Código Penal, art. 15'
    }],
    'Arrependimento posterior': [{
        'pergunta': 'Em crime cometido sem violência ou grave ameaça à pessoa, qual conduta pode permitir a redução de pena prevista no arrependimento posterior?',
        'alternativas': ['Reparar o dano ou restituir a coisa até o recebimento da denúncia ou queixa', 'Confessar o crime somente depois do trânsito em julgado', 'Pedir desculpas à vítima depois de iniciada a execução'],
        'correta': 0,
        'explicacao': 'O Código Penal prevê redução de pena quando, em crime sem violência ou grave ameaça, o agente repara o dano ou restitui a coisa por ato voluntário até o recebimento da denúncia ou da queixa.',
        'fonte': 'Código Penal, art. 16'
    }],
    'Erro sobre a ilicitude do fato': [{
        'pergunta': 'Segundo o Código Penal, qual é o efeito do erro inevitável sobre a ilicitude do fato?',
        'alternativas': ['Isenta de pena', 'Aumenta a pena', 'Transforma automaticamente o crime doloso em culposo'],
        'correta': 0,
        'explicacao': 'O erro inevitável sobre a ilicitude do fato isenta de pena. Se o erro for evitável, a pena pode ser diminuída nos limites previstos no Código Penal.',
        'fonte': 'Código Penal, art. 21'
    }],
    'Estado de necessidade': [{
        'pergunta': 'Qual situação corresponde ao estado de necessidade previsto no Código Penal?',
        'alternativas': ['Praticar o fato para salvar direito próprio ou alheio de perigo atual, nas condições legais', 'Reagir a uma agressão passada para se vingar', 'Agir por conveniência, mesmo sem perigo a qualquer direito'],
        'correta': 0,
        'explicacao': 'O estado de necessidade exige perigo atual e a proteção de direito próprio ou alheio, observadas as demais condições legais. A reação a perigo passado por vingança não se enquadra nessa justificativa.',
        'fonte': 'Código Penal, art. 24'
    }],
    'Legítima defesa': [{
        'pergunta': 'Para caracterizar legítima defesa, a pessoa deve usar moderadamente os meios necessários para:',
        'alternativas': ['Repelir agressão injusta, atual ou iminente, a direito próprio ou de outra pessoa', 'Punir quem praticou uma agressão no passado', 'Evitar qualquer discussão, ainda que não exista agressão'],
        'correta': 0,
        'explicacao': 'A legítima defesa é a reação moderada, com os meios necessários, contra agressão injusta atual ou iminente a direito próprio ou alheio. Ela não autoriza vingança após a agressão terminar.',
        'fonte': 'Código Penal, art. 25'
    }],
    'Inimputabilidade por condição mental': [{
        'pergunta': 'Em que hipótese o Código Penal prevê isenção de pena por inimputabilidade relacionada à saúde mental?',
        'alternativas': ['Quando, ao tempo da ação ou omissão, a pessoa era inteiramente incapaz de entender o caráter ilícito do fato ou de determinar-se conforme esse entendimento', 'Sempre que a pessoa alegar sofrimento emocional', 'Quando a pessoa desconhecer a identidade da vítima'],
        'correta': 0,
        'explicacao': 'O art. 26 trata da incapacidade inteira, ao tempo da ação ou omissão, de entender a ilicitude do fato ou de agir conforme esse entendimento, em razão de doença mental ou desenvolvimento mental incompleto ou retardado. A avaliação depende dos requisitos legais.',
        'fonte': 'Código Penal, art. 26'
    }],
    'Menoridade penal': [{
        'pergunta': 'Para efeitos penais, como é considerada a pessoa que ainda não completou 18 anos na data do fato?',
        'alternativas': ['Inimputável, sujeita às normas da legislação especial', 'Imputável pelas mesmas regras aplicáveis a adultos', 'Imputável apenas se o crime for contra o patrimônio'],
        'correta': 0,
        'explicacao': 'O Código Penal estabelece que menores de 18 anos são penalmente inimputáveis e ficam sujeitos às normas da legislação especial, atualmente o Estatuto da Criança e do Adolescente.',
        'fonte': 'Código Penal, art. 27'
    }],
    'Concurso de pessoas': [{
        'pergunta': 'No concurso de pessoas, como regra, quem concorre para o crime responde:',
        'alternativas': ['Na medida de sua culpabilidade', 'Sempre com pena idêntica à de todos os demais envolvidos', 'Somente se tiver executado pessoalmente o verbo do crime'],
        'correta': 0,
        'explicacao': 'Quem concorre para o crime incide nas penas a ele cominadas, na medida de sua culpabilidade. A participação de cada pessoa deve ser avaliada conforme sua contribuição e responsabilidade.',
        'fonte': 'Código Penal, art. 29'
    }],
    'Furto': [{
        'pergunta': 'Qual conduta corresponde à definição básica de furto no Código Penal?',
        'alternativas': ['Subtrair, para si ou para outra pessoa, coisa alheia móvel', 'Obter vantagem induzindo alguém em erro por meio fraudulento', 'Subtrair coisa móvel mediante violência ou grave ameaça à pessoa'],
        'correta': 0,
        'explicacao': 'O furto consiste em subtrair coisa alheia móvel para si ou para outra pessoa. A violência ou grave ameaça contra a pessoa diferencia a definição básica do roubo.',
        'fonte': 'Código Penal, art. 155'
    }],
    'Roubo': [{
        'pergunta': 'Qual elemento diferencia a definição básica de roubo da definição básica de furto?',
        'alternativas': ['Violência ou grave ameaça à pessoa, ou redução da capacidade de resistência', 'A coisa subtraída precisa ser imóvel', 'A vítima precisa ser agente público'],
        'correta': 0,
        'explicacao': 'Na definição básica do roubo, a subtração ocorre mediante violência ou grave ameaça à pessoa, ou após a vítima ser reduzida à impossibilidade de resistência. No furto, esses elementos não integram a definição básica.',
        'fonte': 'Código Penal, arts. 155 e 157'
    }],
    'Peculato': [{
        'pergunta': 'Qual conduta descreve o peculato-apropriação previsto no Código Penal?',
        'alternativas': ['Apropriar-se de dinheiro, valor ou bem móvel que o funcionário público possui em razão do cargo', 'Subtrair bem móvel sem relação com cargo ou função pública', 'Receber vantagem para influenciar ato de outro funcionário'],
        'correta': 0,
        'explicacao': 'No peculato-apropriação, o funcionário público se apropria de dinheiro, valor ou bem móvel, público ou particular, cuja posse decorre do cargo, em proveito próprio ou alheio. O artigo também prevê a modalidade de desvio.',
        'fonte': 'Código Penal, art. 312'
    }],
}

LEGENDAS = {
    tema: f'{tema}: responda à questão e confira a explicação.\n#JuhQuiz #DireitoPenal #Concursos #ConcursoPublico'
    for tema in QUIZZES
}
