# -*- coding: utf-8 -*-
"""15 questões autorais de Física com referência a provas de concursos."""

CAPA_SEGUNDOS = 2

QUIZZES = {
    'Força e velocidade constante': [{
        'pergunta': 'Uma pessoa sobe por uma corda em velocidade constante. Se sua massa é 60 kg e g = 10 m/s², qual é a intensidade da força que ela exerce na corda?',
        'alternativas': ['600 N', '60 N', '6.000 N'],
        'correta': 0,
        'explicacao': 'Como a velocidade é constante, a aceleração é zero e a força resultante também é zero. A tensão equilibra o peso: T = mg = 60 × 10 = 600 N.',
        'fonte': 'Fonte: CBM/PA, Cebraspe 2023, questão 41 (questão autoral inspirada no conteúdo)'
    }],
    'Transformação de energia': [{
        'pergunta': 'Uma bola cai de uma altura de 5 m. Desprezando a resistência do ar e usando g = 10 m/s², qual será sua velocidade imediatamente antes de tocar o chão?',
        'alternativas': ['10 m/s', '5 m/s', '50 m/s'],
        'correta': 0,
        'explicacao': 'A energia potencial gravitacional transforma-se em energia cinética: mgh = mv²/2. Assim, v = √(2gh) = √(2 × 10 × 5) = 10 m/s.',
        'fonte': 'Fonte: CBM/PA, Cebraspe 2023, questão 42 (questão autoral inspirada no conteúdo)'
    }],
    'Pressão hidrostática': [{
        'pergunta': 'Qual é a pressão hidrostática exercida pela água a 4 m de profundidade? Considere densidade de 1.000 kg/m³ e g = 10 m/s².',
        'alternativas': ['40.000 Pa', '4.000 Pa', '400.000 Pa'],
        'correta': 0,
        'explicacao': 'A pressão hidrostática é p = ρgh. Portanto, p = 1.000 × 10 × 4 = 40.000 Pa, sem incluir a pressão atmosférica.',
        'fonte': 'Fonte: CBM/PA, Cebraspe 2023, questão 43 (questão autoral inspirada no conteúdo)'
    }],
    'Escalas termométricas': [{
        'pergunta': 'A que temperatura em Celsius corresponde 104 °F?',
        'alternativas': ['40 °C', '36 °C', '52 °C'],
        'correta': 0,
        'explicacao': 'Usamos C = (F − 32) × 5/9. Para 104 °F: (104 − 32) × 5/9 = 40 °C.',
        'fonte': 'Fonte: CBM/PA, Cebraspe 2023, questão 44 (questão autoral inspirada no conteúdo)'
    }],
    'Calor sensível': [{
        'pergunta': 'Quanto calor é necessário para aquecer 200 g de água de 20 °C para 50 °C? Use c = 1 cal/(g·°C).',
        'alternativas': ['6.000 cal', '600 cal', '30.000 cal'],
        'correta': 0,
        'explicacao': 'Pela fórmula Q = mcΔT, Q = 200 × 1 × (50 − 20) = 6.000 cal, ou 6 kcal.',
        'fonte': 'Fonte: CBM/PA, Cebraspe 2023, questão 45 (questão autoral inspirada no conteúdo)'
    }],
    'Dilatação térmica': [{
        'pergunta': 'Uma tampa de latão está muito presa em um pote de vidro. O latão se dilata mais que o vidro. O que tende a acontecer se a tampa for aquecida?',
        'alternativas': ['A tampa se dilata mais e tende a ficar mais fácil de abrir', 'O vidro se dilata mais e aperta a tampa', 'Tampa e pote sempre se dilatam exatamente na mesma proporção'],
        'correta': 0,
        'explicacao': 'Ao aquecer os dois materiais, ambos se dilatam, mas o latão tem coeficiente de dilatação maior. O diâmetro da tampa aumenta relativamente mais que o do pote.',
        'fonte': 'Fonte: CBM/PA, Cebraspe 2023, questão 46 (questão autoral inspirada no conteúdo)'
    }],
    'Lei dos gases ideais': [{
        'pergunta': 'Um gás ideal está em um recipiente rígido. Sua temperatura absoluta aumenta de 300 K para 450 K. Se a pressão inicial era 100 kPa, qual será a pressão final?',
        'alternativas': ['150 kPa', '100 kPa', '225 kPa'],
        'correta': 0,
        'explicacao': 'Em volume constante, P/T permanece constante. Assim, P₂ = 100 × (450/300) = 150 kPa.',
        'fonte': 'Fonte: CBM/PA, Cebraspe 2023, questão 47 (questão autoral inspirada no conteúdo)'
    }],
    'Rendimento de máquina térmica': [{
        'pergunta': 'Uma máquina térmica ideal opera entre uma fonte quente a 600 K e uma fonte fria a 300 K. Qual é o rendimento máximo teórico?',
        'alternativas': ['50%', '25%', '75%'],
        'correta': 0,
        'explicacao': 'O rendimento máximo de Carnot é η = 1 − Tf/Tq. Logo, η = 1 − 300/600 = 0,5, ou 50%.',
        'fonte': 'Fonte: CBM/PA, Cebraspe 2023, questão 48 (questão autoral inspirada no conteúdo)'
    }],
    'Descargas elétricas': [{
        'pergunta': 'O que permite que uma descarga elétrica atravesse o ar entre uma nuvem e o solo?',
        'alternativas': ['O campo elétrico supera a rigidez dielétrica do ar', 'A resistência elétrica do ar se torna infinita', 'As cargas elétricas deixam de existir na nuvem'],
        'correta': 0,
        'explicacao': 'Quando o campo elétrico fica suficientemente intenso para superar a rigidez dielétrica do ar, o ar se ioniza e pode conduzir a descarga elétrica.',
        'fonte': 'Fonte: CBM/PA, Cebraspe 2023, questão 49 (questão autoral inspirada no conteúdo)'
    }],
    'Movimento circular': [{
        'pergunta': 'Um carrinho de 2 kg percorre uma trajetória circular de raio 3 m a 6 m/s. Qual é a força centrípeta resultante?',
        'alternativas': ['24 N', '12 N', '36 N'],
        'correta': 0,
        'explicacao': 'A força centrípeta é Fc = mv²/r. Substituindo: Fc = 2 × 6² ÷ 3 = 24 N.',
        'fonte': 'Fonte: CBMPA, Cebraspe 2023, questão 33 (questão autoral inspirada no conteúdo)'
    }],
    'Lançamento horizontal': [{
        'pergunta': 'Uma bola é lançada horizontalmente a 10 m/s de uma altura de 20 m. Desprezando o ar e usando g = 10 m/s², a que distância horizontal ela cai?',
        'alternativas': ['20 m', '10 m', '40 m'],
        'correta': 0,
        'explicacao': 'O tempo de queda vem de h = gt²/2: 20 = 5t², então t = 2 s. No eixo horizontal, x = vt = 10 × 2 = 20 m.',
        'fonte': 'Fonte: CBMPA, Cebraspe 2023, questão 34 (questão autoral inspirada no conteúdo)'
    }],
    'Colisão inelástica': [{
        'pergunta': 'Um carrinho de 2 kg, a 10 m/s, colide e gruda em outro carrinho de 2 kg parado. Quanta energia cinética é dissipada na colisão?',
        'alternativas': ['50 J', '100 J', '25 J'],
        'correta': 0,
        'explicacao': 'A velocidade final é (2 × 10) ÷ 4 = 5 m/s. A energia inicial é 100 J e a final é (4 × 5²)/2 = 50 J. A diferença, 50 J, foi dissipada.',
        'fonte': 'Fonte: CBMPA, Cebraspe 2023, questão 35 (questão autoral inspirada no conteúdo)'
    }],
    'Primeira lei da termodinâmica': [{
        'pergunta': 'Um gás ideal monoatômico recebe 900 J de calor e realiza 300 J de trabalho sobre o ambiente. Qual é a variação de sua energia interna?',
        'alternativas': ['600 J', '1.200 J', '−600 J'],
        'correta': 0,
        'explicacao': 'Pela primeira lei da termodinâmica, ΔU = Q − W. Como o gás recebe 900 J e realiza 300 J de trabalho, ΔU = 900 − 300 = 600 J.',
        'fonte': 'Fonte: CBMPA, Cebraspe 2023, questão 36 (questão autoral inspirada no conteúdo)'
    }],
    'Potência elétrica e aquecimento': [{
        'pergunta': 'Um resistor de 20 Ω é ligado a uma fonte de 100 V durante 2 minutos. Qual energia elétrica é dissipada em calor?',
        'alternativas': ['60.000 J', '10.000 J', '120.000 J'],
        'correta': 0,
        'explicacao': 'A potência é P = V²/R = 100²/20 = 500 W. Em 120 s, a energia é E = Pt = 500 × 120 = 60.000 J.',
        'fonte': 'Fonte: CBMPA, Cebraspe 2023, questão 38 (questão autoral inspirada no conteúdo)'
    }],
    'Circuito em série': [{
        'pergunta': 'Dois resistores de 4 Ω e 8 Ω estão ligados em série a uma fonte de 24 V. Qual é a corrente no circuito?',
        'alternativas': ['2 A', '3 A', '6 A'],
        'correta': 0,
        'explicacao': 'Em série, a resistência equivalente é 4 + 8 = 12 Ω. Pela lei de Ohm, I = V/R = 24/12 = 2 A.',
        'fonte': 'Fonte: CBMPA, Cebraspe 2023, questão 39 (questão autoral inspirada no conteúdo)'
    }],
}

LEGENDAS = {
    tema: f'Questão de Física: responda e confira a explicação.\n#JuhQuiz #Fisica #Concursos #Estudos'
    for tema in QUIZZES
}
