# -*- coding: utf-8 -*-
"""15 questões autorais de Fisioterapia com referências ao concurso EBSERH."""

CAPA_SEGUNDOS = 2

QUIZZES = {
    'Fragilidade em idosos': [{
        'pergunta': 'Pelo fenótipo de fragilidade de Fried, quantos critérios positivos classificam o idoso como frágil?',
        'alternativas': ['Três ou mais', 'Apenas um', 'Todos os cinco obrigatoriamente'],
        'correta': 0,
        'explicacao': 'O fenótipo de Fried considera perda de peso não intencional, exaustão, baixa força de preensão, lentidão da marcha e baixo nível de atividade física. A presença de três ou mais critérios caracteriza fragilidade.',
        'fonte': 'Fonte: EBSERH, IBFC, Concurso Nacional 01/2023, Fisioterapeuta, questão 42 (pergunta autoral sobre o tema)'
    }],
    'Recursos térmicos': [{
        'pergunta': 'Antes de aplicar calor terapêutico, qual cuidado é essencial?',
        'alternativas': [
            'Verificar sensibilidade e condição da pele',
            'Aplicar calor intenso sobre qualquer lesão recente',
            'Manter o recurso até a pele ficar muito vermelha'
        ],
        'correta': 0,
        'explicacao': 'A avaliação da sensibilidade e da pele ajuda a reduzir o risco de queimaduras. Calor terapêutico também exige cautela em inflamação aguda, alterações circulatórias e outras contraindicações clínicas.',
        'fonte': 'Fonte: EBSERH, IBFC, Concurso Nacional 01/2023, Fisioterapeuta, questão 44 (pergunta autoral sobre o tema)'
    }],
    'TENS convencional': [{
        'pergunta': 'Na TENS convencional, qual padrão é geralmente utilizado para modular a dor?',
        'alternativas': [
            'Frequência alta e intensidade sensorial confortável',
            'Frequência baixa e intensidade que provoque dor',
            'Corrente contínua sem percepção sensorial'
        ],
        'correta': 0,
        'explicacao': 'A TENS convencional costuma usar frequência alta e intensidade sensorial confortável, buscando estimular fibras aferentes de maior diâmetro e modular a transmissão da dor. Os parâmetros devem ser ajustados à pessoa e ao objetivo clínico.',
        'fonte': 'Fonte: EBSERH, IBFC, Concurso Nacional 01/2023, Fisioterapeuta, questão 45 (pergunta autoral sobre o tema)'
    }],
    'Alongamento estático': [{
        'pergunta': 'Quando o tecido é levado ao alongamento e mantido por um período sem movimentos repetidos, trata-se de:',
        'alternativas': ['Alongamento estático', 'Alongamento balístico', 'Contração isométrica'],
        'correta': 0,
        'explicacao': 'No alongamento estático, a posição de alongamento é sustentada por um tempo, com força controlada e sem impulsos repetidos. A intensidade deve respeitar a tolerância e as condições clínicas.',
        'fonte': 'Fonte: EBSERH, IBFC, Concurso Nacional 01/2023, Fisioterapeuta, questão 46 (pergunta autoral sobre o tema)'
    }],
    'Reabilitação após artroplastia do quadril': [{
        'pergunta': 'Na reabilitação após artroplastia total do quadril, qual conduta costuma integrar o início do plano, conforme avaliação e protocolo cirúrgico?',
        'alternativas': [
            'Mobilização precoce e exercícios circulatórios',
            'Repouso absoluto por várias semanas',
            'Exercícios máximos de impacto no primeiro dia'
        ],
        'correta': 0,
        'explicacao': 'A mobilização precoce e exercícios circulatórios, como bombas de tornozelo, podem fazer parte da recuperação e da prevenção de complicações. Progressão e precauções dependem da abordagem cirúrgica, do estado clínico e da orientação da equipe.',
        'fonte': 'Fonte: EBSERH, IBFC, Concurso Nacional 01/2023, Fisioterapeuta, questão 47 (pergunta autoral sobre o tema)'
    }],
    'Reabilitação após acromioplastia': [{
        'pergunta': 'Após acromioplastia, a reabilitação deve buscar principalmente:',
        'alternativas': [
            'Controlar sintomas e recuperar gradualmente a função do ombro',
            'Manter o ombro imobilizado por tempo indefinido',
            'Iniciar arremessos máximos logo após a cirurgia'
        ],
        'correta': 0,
        'explicacao': 'A recuperação é progressiva: pode envolver controle da dor, mobilidade orientada e fortalecimento conforme a cicatrização e o protocolo cirúrgico. A carga é aumentada de acordo com a resposta clínica.',
        'fonte': 'Fonte: EBSERH, IBFC, Concurso Nacional 01/2023, Fisioterapeuta, questão 48 (pergunta autoral sobre o tema)'
    }],
    'Articulação do ombro': [{
        'pergunta': 'Quais estruturas ósseas formam a articulação glenoumeral?',
        'alternativas': [
            'Cabeça do úmero e cavidade glenoidal da escápula',
            'Clavícula e acrômio',
            'Esterno e extremidade medial da clavícula'
        ],
        'correta': 0,
        'explicacao': 'A articulação glenoumeral é formada pela cabeça do úmero e pela cavidade glenoidal da escápula. A cápsula, o lábio glenoidal e os músculos contribuem para sua estabilidade.',
        'fonte': 'Fonte: EBSERH, IBFC, Concurso Nacional 01/2023, Fisioterapeuta, questão 50 (pergunta autoral sobre o tema)'
    }],
    'Articulação do tornozelo': [{
        'pergunta': 'A articulação talocrural é formada principalmente por quais ossos?',
        'alternativas': [
            'Tálus, tíbia e fíbula',
            'Calcâneo, navicular e cuboide',
            'Patela, tíbia e fíbula'
        ],
        'correta': 0,
        'explicacao': 'A articulação talocrural, ou do tornozelo, envolve a tróclea do tálus dentro da pinça formada pelas extremidades distais da tíbia e da fíbula. Ela participa dos movimentos de dorsiflexão e flexão plantar.',
        'fonte': 'Fonte: EBSERH, IBFC, Concurso Nacional 01/2023, Fisioterapeuta, questão 51 (pergunta autoral sobre o tema)'
    }],
    'Síndrome do túnel do carpo': [{
        'pergunta': 'No teste de Phalen, qual posição é mantida para investigar sintomas do túnel do carpo?',
        'alternativas': [
            'Flexão dos punhos, aproximando o dorso das mãos',
            'Extensão dos cotovelos com os punhos neutros',
            'Desvio ulnar dos punhos com os dedos estendidos'
        ],
        'correta': 0,
        'explicacao': 'No teste de Phalen, os punhos são mantidos em flexão, geralmente com o dorso das mãos aproximado. A reprodução de parestesias na distribuição do nervo mediano pode indicar irritação, mas o teste não confirma o diagnóstico sozinho.',
        'fonte': 'Fonte: EBSERH, IBFC, Concurso Nacional 01/2023, Fisioterapeuta, questão 52 (pergunta autoral sobre o tema)'
    }],
    'Sinal de Babinski': [{
        'pergunta': 'Em um adulto, o que pode indicar a resposta extensora do hálux no sinal de Babinski?',
        'alternativas': [
            'Alteração da via corticoespinal',
            'Lesão isolada do nervo mediano',
            'Encurtamento dos músculos isquiotibiais'
        ],
        'correta': 0,
        'explicacao': 'A extensão do hálux, por vezes acompanhada da abertura dos outros dedos, é uma resposta plantar extensora. Em adultos, pode sugerir comprometimento da via corticoespinal e precisa ser interpretada no contexto do exame neurológico.',
        'fonte': 'Fonte: EBSERH, IBFC, Concurso Nacional 01/2023, Fisioterapeuta, questão 54 (pergunta autoral sobre o tema)'
    }],
    'Marcha e controle do joelho': [{
        'pergunta': 'Durante a fase final do balanço da marcha, qual grupo muscular ajuda a desacelerar a extensão do joelho?',
        'alternativas': ['Isquiotibiais', 'Flexores dos dedos do pé', 'Músculos intrínsecos da mão'],
        'correta': 0,
        'explicacao': 'Os isquiotibiais ajudam a controlar e desacelerar a extensão do joelho no balanço terminal, preparando o membro para o contato inicial. A marcha depende da ação coordenada de vários grupos musculares.',
        'fonte': 'Fonte: EBSERH, IBFC, Concurso Nacional 01/2023, Fisioterapeuta, questão 55 (pergunta autoral sobre o tema)'
    }],
    'Teste de força muscular': [{
        'pergunta': 'Na graduação manual de força muscular, o grau 3 geralmente significa que a pessoa consegue:',
        'alternativas': [
            'Completar a amplitude contra a gravidade, sem resistência adicional',
            'Mover o segmento apenas com a gravidade eliminada',
            'Manter a posição contra resistência máxima'
        ],
        'correta': 0,
        'explicacao': 'No grau 3 da escala manual, o movimento percorre a amplitude disponível contra a gravidade, mas não tolera resistência manual adicional. A escala deve ser aplicada com posicionamento e estabilização adequados.',
        'fonte': 'Fonte: EBSERH, IBFC, Concurso Nacional 01/2023, Fisioterapeuta, questão 56 (pergunta autoral sobre o tema)'
    }],
    'Respiração diafragmática': [{
        'pergunta': 'Na respiração diafragmática, qual movimento é enfatizado durante a inspiração?',
        'alternativas': [
            'Expansão abdominal pelo movimento do diafragma',
            'Elevação máxima dos ombros',
            'Contração sustentada dos músculos do pescoço'
        ],
        'correta': 0,
        'explicacao': 'Na respiração diafragmática, a descida do diafragma favorece a expansão abdominal durante a inspiração. A técnica deve ser adaptada ao quadro e ao objetivo terapêutico.',
        'fonte': 'Fonte: EBSERH, IBFC, Concurso Nacional 01/2023, Fisioterapeuta, questão 57 (pergunta autoral sobre o tema)'
    }],
    'Fisioterapia aquática e flutuação': [{
        'pergunta': 'Na fisioterapia aquática, qual efeito da flutuação pode facilitar exercícios com menor descarga de peso?',
        'alternativas': [
            'Redução da carga aparente sobre as articulações',
            'Aumento obrigatório do impacto em cada passo',
            'Impedimento de qualquer movimento contra a água'
        ],
        'correta': 0,
        'explicacao': 'A força de empuxo atua para cima e pode reduzir a carga aparente suportada pelos membros. O efeito varia com a profundidade e a posição do corpo, permitindo ajustar o exercício.',
        'fonte': 'Fonte: EBSERH, IBFC, Concurso Nacional 01/2023, Fisioterapeuta, questão 58 (pergunta autoral sobre o tema)'
    }],
    'Segurança na fisioterapia aquática': [{
        'pergunta': 'Qual situação exige interromper a atividade aquática e avaliação clínica antes de retomar o exercício?',
        'alternativas': [
            'Crise de angina ou dor torácica aguda',
            'Dor muscular leve após exercício anterior',
            'Uso de roupa de banho confortável'
        ],
        'correta': 0,
        'explicacao': 'Dor torácica aguda ou crise de angina exige interrupção da atividade e avaliação imediata. A segurança na piscina depende de triagem clínica e consideração das contraindicações individuais.',
        'fonte': 'Fonte: EBSERH, IBFC, Concurso Nacional 01/2023, Fisioterapeuta, questão 59 (pergunta autoral sobre o tema)'
    }],
}

LEGENDAS = {
    tema: f'Questão de Fisioterapia para concurso EBSERH: responda e confira a explicação.\n#JuhQuiz #Fisioterapia #EBSERH #Concursos'
    for tema in QUIZZES
}
