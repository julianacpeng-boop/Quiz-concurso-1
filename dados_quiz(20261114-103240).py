# Quiz Juh — Português para concursos (novo lote)
# 15 questões autorais, uma pergunta por vídeo.
# O gerar_quiz.py coloca a fonte entre parênteses na tela; não narrar a fonte.

CAPA_SEGUNDOS = 2

QUIZZES = {
    "Português — voz passiva": [{
        "pergunta": "Passe para a voz passiva: “A comissão divulgou o resultado.”",
        "alternativas": ["O resultado divulgou a comissão.", "O resultado foi divulgado pela comissão.", "A comissão foi divulgada pelo resultado."],
        "correta": 1,
        "explicacao": "Na voz passiva analítica, o objeto direto da voz ativa torna-se sujeito paciente. O verbo auxiliar ser acompanha o particípio: o resultado foi divulgado.",
        "fonte": "Cunha e Cintra, Nova Gramática, vozes verbais",
    }],
    "Português — transitividade verbal": [{
        "pergunta": "Na oração “A candidata precisa de apoio”, o verbo precisa é:",
        "alternativas": ["Transitivo indireto", "Transitivo direto", "Intransitivo"],
        "correta": 0,
        "explicacao": "No sentido de necessitar, precisar rege a preposição de. O complemento “de apoio” é objeto indireto.",
        "fonte": "Bechara, Moderna Gramática, regência verbal",
    }],
    "Português — tipos de predicado": [{
        "pergunta": "Em “A candidata saiu confiante da sala”, o predicado é:",
        "alternativas": ["Nominal", "Verbal", "Verbo-nominal"],
        "correta": 2,
        "explicacao": "O predicado apresenta uma ação expressa por saiu e uma característica da candidata, confiante. Por isso, é verbo-nominal.",
        "fonte": "Cunha e Cintra, Nova Gramática, predicação",
    }],
    "Português — pronome relativo": [{
        "pergunta": "Na frase “O edital que foi publicado ontem já está disponível”, a palavra “que” retoma:",
        "alternativas": ["Ontem", "Edital", "Disponível"],
        "correta": 1,
        "explicacao": "O pronome relativo que retoma o substantivo edital e introduz uma oração que acrescenta informação sobre ele.",
        "fonte": "Cunha e Cintra, Nova Gramática, pronomes relativos",
    }],
    "Português — oração adjetiva restritiva": [{
        "pergunta": "Em “Os candidatos que entregaram o documento receberam protocolo”, a oração destacada restringe:",
        "alternativas": ["O grupo de candidatos mencionado", "Todos os candidatos, sem distinção", "A palavra protocolo"],
        "correta": 0,
        "explicacao": "Sem vírgulas, a oração adjetiva é restritiva: especifica quais candidatos receberam protocolo, isto é, os que entregaram o documento.",
        "fonte": "Cunha e Cintra, Nova Gramática, orações adjetivas",
    }],
    "Português — oração condicional": [{
        "pergunta": "Em “Se o recurso for aceito, a banca revisará o resultado”, a oração iniciada por “se” expressa:",
        "alternativas": ["Causa", "Concessão", "Condição"],
        "correta": 2,
        "explicacao": "A conjunção se introduz uma condição para que a banca revise o resultado. A forma “for” está no futuro do subjuntivo.",
        "fonte": "Cunha e Cintra, Nova Gramática, orações condicionais",
    }],
    "Português — concordância partitiva": [{
        "pergunta": "Qual afirmação sobre a concordância em “A maioria dos candidatos compareceu” está correta?",
        "alternativas": ["Só se admite o verbo no plural", "Também pode ocorrer “compareceram”", "Só se admite o verbo no singular"],
        "correta": 1,
        "explicacao": "Com expressões partitivas como a maioria de, a concordância pode ser feita com o núcleo singular maioria ou com o termo plural candidatos.",
        "fonte": "Manual de Redação da Presidência, concordância",
    }],
    "Português — onde e aonde": [{
        "pergunta": "Complete: “______ a candidata pretende ir depois da prova?”",
        "alternativas": ["Onde", "Donde", "Aonde"],
        "correta": 2,
        "explicacao": "Aonde indica destino ou movimento e combina com a preposição a exigida por ir. Onde é usado, em geral, para indicar permanência ou localização.",
        "fonte": "Cunha e Cintra, Nova Gramática, advérbios de lugar",
    }],
    "Português — pronomes demonstrativos": [{
        "pergunta": "Leia: “O edital foi publicado ontem. Esse documento traz as regras da seleção.” “Esse” retoma:",
        "alternativas": ["O edital", "A seleção", "Ontem"],
        "correta": 0,
        "explicacao": "No texto, esse retoma um elemento já mencionado: edital. Esse emprego anafórico ajuda a conectar as frases.",
        "fonte": "FUNAG, Manual de Revisão, pronomes demonstrativos",
    }],
    "Português — hífen com prefixo": [{
        "pergunta": "Qual é a grafia correta segundo o Acordo Ortográfico?",
        "alternativas": ["antiinflamatório", "anti-inflamatório", "anti inflamatório"],
        "correta": 1,
        "explicacao": "Usa-se hífen quando o prefixo termina com a mesma vogal que inicia o segundo elemento: anti + inflamatório.",
        "fonte": "Acordo Ortográfico, Base XVI",
    }],
    "Português — plural de palavra composta": [{
        "pergunta": "Qual é o plural de “guarda-chuva”?",
        "alternativas": ["Guardas-chuva", "Guardas-chuvas", "Guarda-chuvas"],
        "correta": 2,
        "explicacao": "Em guarda-chuva, guarda é forma verbal e chuva é substantivo. Nesse tipo de composto, o substantivo varia: guarda-chuvas.",
        "fonte": "Cunha e Cintra, Nova Gramática, plural dos compostos",
    }],
    "Português — parônimos": [{
        "pergunta": "Complete: “A equipe agiu rapidamente diante do perigo ______.”",
        "alternativas": ["Iminente", "Eminente", "Eminecente"],
        "correta": 0,
        "explicacao": "Iminente significa prestes a acontecer. Eminente significa elevado ou de grande destaque.",
        "fonte": "Michaelis, Dicionário, verbetes eminente e iminente",
    }],
    "Português — ambiguidade": [{
        "pergunta": "Em “A servidora avisou à supervisora que seu relatório estava incompleto”, a ambiguidade está em:",
        "alternativas": ["A palavra supervisora estar no singular", "Não ficar claro de quem é o relatório", "A frase não apresentar verbo"],
        "correta": 1,
        "explicacao": "O possessivo seu pode se referir à servidora ou à supervisora. Reescrever a frase indicando a pessoa elimina a ambiguidade.",
        "fonte": "Manual de Redação da Presidência, ambiguidade",
    }],
    "Português — gênero textual notícia": [{
        "pergunta": "Qual é a finalidade mais comum de uma notícia?",
        "alternativas": ["Relatar um fato de interesse público", "Defender uma tese com argumentos", "Ensinar um procedimento passo a passo"],
        "correta": 0,
        "explicacao": "A notícia tem como propósito predominante informar sobre acontecimentos. Artigos de opinião defendem pontos de vista; textos instrucionais orientam procedimentos.",
        "fonte": "Marcuschi, Gêneros textuais: definição e funcionalidade",
    }],
    "Português — inferência textual": [{
        "pergunta": "Leia: “Após uma falha no sistema, a banca prorrogou o prazo de recursos para que todos pudessem enviar seus pedidos.” O texto permite concluir que a prorrogação:",
        "alternativas": ["Foi decidida antes da falha", "Cancelou a etapa de recursos", "Buscou evitar prejuízo aos candidatos"],
        "correta": 2,
        "explicacao": "A justificativa apresentada é a falha no sistema; ampliar o prazo permitiu que todos tivessem oportunidade de enviar os recursos.",
        "fonte": "Koch e Elias, Ler e compreender, leitura e inferência",
    }],
}

LEGENDAS = {
    tema: f"{tema}: teste seus conhecimentos de Português para concursos!\n\n#JuhQuiz #Portugues #Concursos #Quiz"
    for tema in QUIZZES
}

# Referências completas consultadas; fonte curta acima é a que aparece no vídeo.
FONTES_COMPLETAS = {
    "Acordo Ortográfico": "Decreto nº 6.583/2008 e Acordo Ortográfico, Bases XV e XVI — https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2008/decreto/d6583.htm",
    "Manual de Redação da Presidência": "3ª edição, 2018 — https://www4.planalto.gov.br/centrodeestudos/pages/assuntos/manual-de-redacao-da-presidencia-da-republica.html",
    "Manual de Revisão da FUNAG": "Pronomes demonstrativos e gramática — https://funag.gov.br/manual/index.php?title=Pronomes_demonstrativos",
    "VOLP da ABL": "Vocabulário Ortográfico da Língua Portuguesa — https://www.academia.org.br/nossa-lingua/busca-no-vocabulario",
    "Cunha e Cintra": "CUNHA, Celso; CINTRA, Lindley. Nova Gramática do Português Contemporâneo. 7ª ed. Lexikon.",
    "Bechara": "BECHARA, Evanildo. Moderna Gramática Portuguesa. Nova Fronteira.",
    "Michaelis": "Dicionário Brasileiro da Língua Portuguesa — https://michaelis.uol.com.br/moderno-portugues/",
    "Marcuschi": "MARCUSCHI, Luiz Antônio. Gêneros textuais: definição e funcionalidade. In: Gêneros textuais & ensino. Lucerna, 2002.",
    "Koch e Elias": "KOCH, Ingedore Villaça; ELIAS, Vanda Maria. Ler e compreender: os sentidos do texto. Contexto.",
}
