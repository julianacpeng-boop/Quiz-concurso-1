# -*- coding: utf-8 -*-
"""15 questões autorais de Química com referência a provas de concursos."""

CAPA_SEGUNDOS = 2

QUIZZES = {
    'Modelo atômico de Rutherford': [{
        'pergunta': 'No experimento da lâmina metálica, a maioria das partículas alfa atravessou sem desvio, mas algumas foram muito desviadas. Qual conclusão explica esse resultado?',
        'alternativas': ['O átomo tem um núcleo pequeno e positivo e é, em grande parte, espaço vazio', 'A carga positiva ocupa uniformemente todo o átomo', 'Os elétrons concentram quase toda a massa no centro'],
        'correta': 0,
        'explicacao': 'A maioria das partículas atravessava a lâmina porque o átomo é majoritariamente espaço vazio. Os grandes desvios indicavam um núcleo muito pequeno, denso e positivo.',
        'fonte': 'Fonte: CBM/PA, Cebraspe 2023, questão 31 (questão autoral inspirada no conteúdo)'
    }],
    'Eletronegatividade': [{
        'pergunta': 'Em uma ligação química, um átomo com baixa eletronegatividade tende a:',
        'alternativas': ['Ceder elétrons com maior facilidade', 'Atrair com mais força os elétrons da ligação', 'Formar apenas ligações covalentes apolares'],
        'correta': 0,
        'explicacao': 'Elementos pouco eletronegativos, em especial muitos metais, tendem a ceder elétrons e formar cátions. A tendência depende do elemento e do contexto químico.',
        'fonte': 'Fonte: CBM/PA, Cebraspe 2023, questão 32 (questão autoral inspirada no conteúdo)'
    }],
    'Número de oxidação do hidrogênio': [{
        'pergunta': 'Qual é o número de oxidação do hidrogênio em HCl e em NaH, nessa ordem?',
        'alternativas': ['+1 e −1', '−1 e +1', '+1 e +1'],
        'correta': 0,
        'explicacao': 'Com não metais, como o cloro, o hidrogênio geralmente tem Nox +1. Nos hidretos metálicos, como NaH, tem Nox −1.',
        'fonte': 'Fonte: CBM/PA, Cebraspe 2023, questão 33 (questão autoral inspirada no conteúdo)'
    }],
    'Oxidação e redução': [{
        'pergunta': 'Em uma reação de oxirredução, uma espécie que perde elétrons sofre:',
        'alternativas': ['Oxidação e aumento do número de oxidação', 'Redução e aumento do número de oxidação', 'Oxidação e diminuição do número de oxidação'],
        'correta': 0,
        'explicacao': 'Oxidação é a perda de elétrons e corresponde ao aumento do número de oxidação. Redução é o ganho de elétrons.',
        'fonte': 'Fonte: CBM/PA, Cebraspe 2023, questão 34 (questão autoral inspirada no conteúdo)'
    }],
    'Ligações no hidróxido de sódio': [{
        'pergunta': 'No hidróxido de sódio (NaOH), que tipos de ligação aparecem?',
        'alternativas': ['Ligação iônica entre Na⁺ e OH⁻ e covalente entre O e H', 'Somente ligações covalentes', 'Somente ligações metálicas'],
        'correta': 0,
        'explicacao': 'O composto é formado por íons Na⁺ e OH⁻, atraídos por ligação iônica. Dentro do íon hidróxido, oxigênio e hidrogênio compartilham elétrons por ligação covalente.',
        'fonte': 'Fonte: CBM/PA, Cebraspe 2023, questão 35 (questão autoral inspirada no conteúdo)'
    }],
    'Energia de ionização': [{
        'pergunta': 'Considerando a tendência geral da tabela periódica, qual elemento tende a ter menor primeira energia de ionização: sódio (Na), magnésio (Mg) ou cloro (Cl), todos no terceiro período?',
        'alternativas': ['Sódio (Na)', 'Magnésio (Mg)', 'Cloro (Cl)'],
        'correta': 0,
        'explicacao': 'Em geral, a primeira energia de ionização aumenta da esquerda para a direita em um período. Entre esses três elementos, o sódio está mais à esquerda e tende a perder um elétron com maior facilidade.',
        'fonte': 'Fonte: CBMPA, Cebraspe 2023, questão 40 (questão autoral inspirada no conteúdo)'
    }],
    'Nox do carbono': [{
        'pergunta': 'Qual é o número de oxidação do carbono no dióxido de carbono (CO₂)?',
        'alternativas': ['+4', '+2', '−4'],
        'correta': 0,
        'explicacao': 'Cada oxigênio tem Nox −2. Como a molécula é neutra, x + 2(−2) = 0; portanto, o carbono tem Nox +4.',
        'fonte': 'Fonte: CBMPA, Cebraspe 2023, questão 41 (questão autoral inspirada no conteúdo)'
    }],
    'Ligação dupla': [{
        'pergunta': 'Uma ligação dupla entre dois átomos é composta por:',
        'alternativas': ['Uma ligação sigma e uma ligação pi', 'Duas ligações pi', 'Duas ligações sigma'],
        'correta': 0,
        'explicacao': 'Uma ligação dupla é formada por uma ligação sigma, resultante de sobreposição frontal, e uma ligação pi, resultante de sobreposição lateral de orbitais.',
        'fonte': 'Fonte: CBMPA, Cebraspe 2023, questão 42 (questão autoral inspirada no conteúdo)'
    }],
    'Isótopos e nêutrons': [{
        'pergunta': 'O cloro-37 e o potássio-39 têm o mesmo número de nêutrons. Como são chamados átomos de elementos diferentes com igual número de nêutrons?',
        'alternativas': ['Isótonos', 'Isótopos', 'Isóbaros'],
        'correta': 0,
        'explicacao': 'Cloro-37 tem 20 nêutrons (37 − 17) e potássio-39 também tem 20 (39 − 19). Átomos de elementos diferentes com igual número de nêutrons são isótonos.',
        'fonte': 'Fonte: CBMPA, Cebraspe 2023, questão 43 (questão autoral inspirada no conteúdo)'
    }],
    'Números quânticos': [{
        'pergunta': 'Qual conjunto de números quânticos é permitido para um elétron?',
        'alternativas': ['n = 3, l = 2, mₗ = −1, mₛ = +1/2', 'n = 2, l = 2, mₗ = 0, mₛ = −1/2', 'n = 1, l = 0, mₗ = 1, mₛ = +1/2'],
        'correta': 0,
        'explicacao': 'Para n = 3, l pode ser 0, 1 ou 2; para l = 2, mₗ pode variar de −2 a +2; e mₛ pode ser +1/2 ou −1/2. As outras opções violam esses limites.',
        'fonte': 'Fonte: CBMPA, Cebraspe 2023, questão 44 (questão autoral inspirada no conteúdo)'
    }],
    'Série isoeletrônica': [{
        'pergunta': 'Qual afirmação sobre os íons K⁺, Ca²⁺ e Cl⁻ é correta?',
        'alternativas': ['Os três têm 18 elétrons', 'Os três têm 19 elétrons', 'Somente K⁺ e Cl⁻ têm o mesmo número de elétrons'],
        'correta': 0,
        'explicacao': 'K⁺ tem 19 − 1 = 18 elétrons; Ca²⁺ tem 20 − 2 = 18; Cl⁻ tem 17 + 1 = 18. São espécies isoeletrônicas.',
        'fonte': 'Fonte: CBMPA, Cebraspe 2023, questão 45 (questão autoral inspirada no conteúdo)'
    }],
    'Força dos oxiácidos': [{
        'pergunta': 'Qual é a ordem decrescente de força dos oxiácidos do bromo?',
        'alternativas': ['HBrO₄ > HBrO₃ > HBrO₂ > HBrO', 'HBrO > HBrO₂ > HBrO₃ > HBrO₄', 'HBrO₃ > HBrO₂ > HBrO₄ > HBrO'],
        'correta': 0,
        'explicacao': 'Para oxiácidos do mesmo elemento central, em geral, maior número de oxigênios está associado a maior força ácida. Assim, HBrO₄ é o mais forte e HBrO, o mais fraco.',
        'fonte': 'Fonte: CBMPA, Cebraspe 2023, questão 46 (questão autoral inspirada no conteúdo)'
    }],
    'Geometria da amônia': [{
        'pergunta': 'Qual é a geometria molecular da amônia (NH₃)?',
        'alternativas': ['Piramidal trigonal', 'Linear', 'Trigonal plana'],
        'correta': 0,
        'explicacao': 'O nitrogênio tem três pares ligantes e um par de elétrons não ligante. A geometria eletrônica é tetraédrica, mas a geometria molecular é piramidal trigonal.',
        'fonte': 'Fonte: UDESC, Cebraspe 2026, questão 87 (questão autoral inspirada no conteúdo)'
    }],
    'Polaridade do dióxido de carbono': [{
        'pergunta': 'As ligações C=O do CO₂ são polares. Ainda assim, a molécula inteira é apolar porque:',
        'alternativas': ['A geometria linear faz os dipolos se cancelarem', 'O carbono não compartilha elétrons', 'Os oxigênios não atraem elétrons'],
        'correta': 0,
        'explicacao': 'O CO₂ é linear e simétrico. Os dois dipolos das ligações C=O têm mesma intensidade e sentidos opostos, resultando em momento dipolar total nulo.',
        'fonte': 'Fonte: UDESC, Cebraspe 2026, questão 88 (questão autoral inspirada no conteúdo)'
    }],
    'Absorbância e transmitância': [{
        'pergunta': 'Uma amostra apresenta transmitância de 1% em uma análise UV-Vis. Qual é sua absorbância, sabendo que A = −log₁₀(T) e que T deve ser usada como fração?',
        'alternativas': ['2', '1', '0,01'],
        'correta': 0,
        'explicacao': '1% em forma de fração é 0,01. Logo, A = −log₁₀(0,01) = 2.',
        'fonte': 'Fonte: UDESC, Cebraspe 2026, questão 77 (questão autoral inspirada no conteúdo)'
    }],
}

LEGENDAS = {
    tema: f'Questão de Química: responda e confira a explicação.\n#JuhQuiz #Quimica #Concursos #Estudos'
    for tema in QUIZZES
}
