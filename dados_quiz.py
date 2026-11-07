# -*- coding: utf-8 -*-
"""15 questões autorais de Biologia baseadas em assuntos de provas públicas.

As fontes identificam concursos e itens que cobraram os assuntos usados como
referência. Os enunciados e alternativas deste arquivo são autorais.
"""

CAPA_SEGUNDOS = 2

QUIZZES = {
    'Trocas gasosas': [{
        'pergunta': 'Em qual estrutura dos pulmões ocorre principalmente a passagem de oxigênio e gás carbônico entre o ar e o sangue?',
        'alternativas': ['Alvéolos pulmonares', 'Brônquios principais', 'Laringe'],
        'correta': 0,
        'explicacao': 'As trocas gasosas ocorrem principalmente nos alvéolos, que têm paredes finas e são envolvidos por capilares. O oxigênio passa para o sangue e o gás carbônico segue do sangue para o ar alveolar.',
        'fonte': 'Base: CBMPA CFO, Cebraspe 2023, questão 26 (autoral)'
    }],
    'Coagulação sanguínea': [{
        'pergunta': 'Qual proteína solúvel do plasma é convertida em fibrina durante a coagulação do sangue?',
        'alternativas': ['Fibrinogênio', 'Hemoglobina', 'Albumina'],
        'correta': 0,
        'explicacao': 'Na coagulação, a trombina transforma o fibrinogênio solúvel em fibrina. Os filamentos de fibrina ajudam a formar a rede que estabiliza o coágulo.',
        'fonte': 'Base: CBMPA CFO, Cebraspe 2023, questão 27 (autoral)'
    }],
    'Mosquito Aedes': [{
        'pergunta': 'Quais doenças podem ser transmitidas pelo mosquito Aedes aegypti?',
        'alternativas': ['Dengue, zika e chikungunya', 'Malária, doença de Chagas e leishmaniose', 'Hepatite B, tétano e tuberculose'],
        'correta': 0,
        'explicacao': 'O Aedes aegypti pode transmitir dengue, zika e chikungunya. A prevenção inclui eliminar recipientes com água parada, onde o mosquito pode se reproduzir.',
        'fonte': 'Base: CBMPA CFO, Cebraspe 2023, questão 28 (autoral)'
    }],
    'Sistema digestório': [{
        'pergunta': 'Qual é uma das principais funções do intestino delgado?',
        'alternativas': ['Absorver a maior parte dos nutrientes', 'Produzir bile para digerir gorduras', 'Armazenar fezes antes da eliminação'],
        'correta': 0,
        'explicacao': 'O intestino delgado realiza a maior parte da digestão química e da absorção de nutrientes. A bile é produzida pelo fígado, e o armazenamento final das fezes ocorre no reto.',
        'fonte': 'Base: CBMPA CFO, Cebraspe 2023, questão 29 (autoral)'
    }],
    'Eutrofização': [{
        'pergunta': 'O que pode acontecer quando um lago recebe excesso de nutrientes, como nitratos e fosfatos?',
        'alternativas': ['Proliferação de algas e redução do oxigênio dissolvido', 'Aumento permanente do oxigênio e da transparência da água', 'Desaparecimento da matéria orgânica e dos decompositores'],
        'correta': 0,
        'explicacao': 'O excesso de nutrientes pode causar proliferação de algas. Quando essa biomassa morre e é decomposta, o consumo de oxigênio aumenta e pode formar áreas com pouco oxigênio, prejudicando a vida aquática.',
        'fonte': 'Base: Embrapa Analista, Cebraspe 2024, questão 41 (autoral)'
    }],
    'Produtividade primária': [{
        'pergunta': 'Qual conjunto reúne fatores que podem influenciar a produtividade primária de um ecossistema?',
        'alternativas': ['Luz, temperatura e disponibilidade de nutrientes', 'Somente o número de predadores', 'Apenas a quantidade de consumidores terciários'],
        'correta': 0,
        'explicacao': 'A produtividade primária depende da atividade dos produtores e de condições como luz, temperatura, água e nutrientes. Esses fatores variam entre ambientes terrestres e aquáticos.',
        'fonte': 'Base: Embrapa Analista, Cebraspe 2024, questão 42 (autoral)'
    }],
    'Proteínas recombinantes': [{
        'pergunta': 'Por que bactérias como Escherichia coli são usadas na produção de algumas proteínas recombinantes?',
        'alternativas': ['Porque crescem rapidamente e podem receber genes de interesse', 'Porque realizam todas as modificações celulares humanas', 'Porque não precisam de material genético para produzir proteínas'],
        'correta': 0,
        'explicacao': 'E. coli pode ser modificada para carregar um gene de interesse e produzir a proteína correspondente. Como é uma bactéria, porém, não realiza certas modificações pós-traducionais próprias de células humanas, como a glicosilação complexa.',
        'fonte': 'Base: Embrapa Analista, Cebraspe 2024, questão 44 (autoral)'
    }],
    'Peroxissomos': [{
        'pergunta': 'Qual alternativa descreve corretamente uma função dos peroxissomos?',
        'alternativas': ['Participam da oxidação de ácidos graxos e da degradação de substâncias', 'Produzem ATP por respiração celular como função exclusiva', 'Fabricam autonomamente todas as suas proteínas'],
        'correta': 0,
        'explicacao': 'Peroxissomos contêm enzimas envolvidas, entre outras funções, na oxidação de ácidos graxos e na degradação de peróxido de hidrogênio. Eles não possuem sistema próprio para fabricar todas as suas proteínas.',
        'fonte': 'Base: Embrapa Analista, Cebraspe 2024, questão 47 (autoral)'
    }],
    'Metilação do DNA': [{
        'pergunta': 'A metilação do DNA pode influenciar a atividade de um gene sem alterar qual elemento?',
        'alternativas': ['A sequência de nucleotídeos do DNA', 'O número de cromossomos da espécie', 'A identidade química das bases nitrogenadas'],
        'correta': 0,
        'explicacao': 'A metilação é uma marca epigenética que pode alterar a expressão gênica sem modificar a sequência de nucleotídeos. Em regiões regulatórias, costuma estar associada à redução da transcrição.',
        'fonte': 'Base: Embrapa Analista, Cebraspe 2024, questão 49 (autoral)'
    }],
    'Biomagnificação': [{
        'pergunta': 'Em uma cadeia alimentar, em quais organismos tende a ser maior a concentração de um poluente persistente que sofre biomagnificação?',
        'alternativas': ['Nos predadores do topo da cadeia', 'Nos produtores, sempre e em qualquer situação', 'Nos decompositores, independentemente do ambiente'],
        'correta': 0,
        'explicacao': 'Na biomagnificação, a concentração de certos poluentes persistentes aumenta nos níveis tróficos mais altos. Predadores de topo podem acumular substâncias ingeridas por muitas presas.',
        'fonte': 'Base: Embrapa Analista, Cebraspe 2024, questão 51 (autoral)'
    }],
    'Biogeografia de ilhas': [{
        'pergunta': 'Segundo a teoria da biogeografia de ilhas, qual ilha tende a abrigar mais espécies, considerando condições semelhantes?',
        'alternativas': ['Uma ilha maior e mais próxima do continente', 'Uma ilha menor e mais distante do continente', 'Uma ilha menor, independentemente da distância'],
        'correta': 0,
        'explicacao': 'Ilhas maiores tendem a oferecer mais habitats e menores taxas de extinção. Ilhas mais próximas do continente costumam receber mais colonizadores, o que favorece a riqueza de espécies.',
        'fonte': 'Base: Embrapa Analista, Cebraspe 2024, questão 53 (autoral)'
    }],
    'Síndrome de Klinefelter': [{
        'pergunta': 'Qual cariótipo está associado à síndrome de Klinefelter?',
        'alternativas': ['47, XXY', '45, X', '47, XXX'],
        'correta': 0,
        'explicacao': 'A síndrome de Klinefelter está associada, mais frequentemente, ao cariótipo 47, XXY, que corresponde à presença de um cromossomo X adicional em indivíduos do sexo masculino.',
        'fonte': 'Base: FUB, Cebraspe 2025, questão 78 (autoral)'
    }],
    'Processamento do RNA': [{
        'pergunta': 'Qual processo ocorre no amadurecimento do RNA mensageiro de células eucarióticas?',
        'alternativas': ['Remoção de íntrons e união de éxons', 'Duplicação do RNA para formar dois cromossomos', 'Tradução dos códons dentro do núcleo'],
        'correta': 0,
        'explicacao': 'No processamento do pré-RNA mensageiro eucariótico, os íntrons são removidos e os éxons unidos. Também podem ser adicionados o cap na extremidade 5’ e a cauda poli-A na extremidade 3’.',
        'fonte': 'Base: FUB, Cebraspe 2025, questão 79 (autoral)'
    }],
    'RNA transportador': [{
        'pergunta': 'Qual é a função do RNA transportador durante a síntese de proteínas?',
        'alternativas': ['Levar aminoácidos ao ribossomo e reconhecer códons pelo anticódon', 'Copiar todo o DNA antes da divisão celular', 'Formar a membrana que envolve o núcleo'],
        'correta': 0,
        'explicacao': 'Cada RNA transportador carrega um aminoácido e possui um anticódon que se pareia com o códon correspondente do RNA mensageiro no ribossomo.',
        'fonte': 'Base: FUB, Cebraspe 2025, questão 82 (autoral)'
    }],
    'Produtores': [{
        'pergunta': 'Qual é o papel dos produtores em uma cadeia alimentar iniciada por vegetais?',
        'alternativas': ['Converter energia luminosa em energia química por fotossíntese', 'Obter toda a energia consumindo outros animais', 'Transformar energia química em luz para os consumidores'],
        'correta': 0,
        'explicacao': 'Produtores, como plantas e algas, captam energia luminosa e a convertem em energia química durante a fotossíntese. Essa matéria orgânica sustenta os demais níveis da cadeia alimentar.',
        'fonte': 'Base: FUB, Cebraspe 2025, questão 100 (autoral)'
    }],
}

LEGENDAS = {
    tema: f'Questão de Biologia para concurso: responda e confira a explicação.\n#JuhQuiz #Biologia #Concursos #ConcursoPublico'
    for tema in QUIZZES
}
