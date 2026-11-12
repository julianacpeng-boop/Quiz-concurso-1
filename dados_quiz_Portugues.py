# Quiz Juh — Português para concursos
# 15 questões autorais; uma pergunta por vídeo.
# A fonte está no campo "fonte" e não precisa ser narrada.

CAPA_SEGUNDOS = 2

QUIZZES = {
    "Português — acentuação de ideia": [{
        "pergunta": "De acordo com a ortografia vigente, qual é a grafia correta?",
        "alternativas": ["idéia", "ideia", "idéía"],
        "correta": 1,
        "explicacao": "A palavra ideia não recebe acento gráfico. O Acordo Ortográfico retirou o acento dos ditongos abertos ei e oi em palavras paroxítonas.",
        "fonte": "(Acordo Ortográfico da Língua Portuguesa, Base IX; Decreto nº 6.583/2008 — https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2008/decreto/d6583.htm)",
    }],
    "Português — ortografia oficial": [{
        "pergunta": "Assinale a palavra escrita corretamente segundo a ortografia oficial.",
        "alternativas": ["excessão", "exceção", "escessão"],
        "correta": 1,
        "explicacao": "A grafia registrada é exceção, com ç depois de ex.",
        "fonte": "(Academia Brasileira de Letras, Vocabulário Ortográfico da Língua Portuguesa — https://www.academia.org.br/nossa-lingua/busca-no-vocabulario)",
    }],
    "Português — classe gramatical": [{
        "pergunta": "Na frase “A candidata respondeu cuidadosamente”, a palavra “cuidadosamente” é:",
        "alternativas": ["Advérbio", "Adjetivo", "Substantivo"],
        "correta": 0,
        "explicacao": "Cuidadosamente modifica o verbo respondeu, indicando o modo como a ação foi realizada; por isso, é advérbio de modo.",
        "fonte": "(CUNHA, Celso; CINTRA, Lindley. Nova Gramática do Português Contemporâneo, capítulo sobre advérbio.)",
    }],
    "Português — emprego da crase": [{
        "pergunta": "Qual frase emprega corretamente o acento indicativo de crase?",
        "alternativas": ["A candidata dirigiu-se à sala de prova.", "A candidata dirigiu-se á sala de prova.", "A candidata dirigiu-se a à sala de prova."],
        "correta": 0,
        "explicacao": "O verbo dirigir-se rege a preposição a; diante do substantivo feminino sala, ocorre a combinação da preposição com o artigo: a + a = à.",
        "fonte": "(Manual de Revisão da FUNAG, Noções básicas de gramática; Manual de Redação da Presidência da República — https://funag.gov.br/manual/index.php?title=No%C3%A7%C3%B5es_b%C3%A1sicas_de_gram%C3%A1tica_da_l%C3%ADngua_portuguesa)",
    }],
    "Português — vocativo e vírgula": [{
        "pergunta": "Em qual alternativa a vírgula está corretamente usada para separar o vocativo?",
        "alternativas": ["Candidatos leiam, as instruções.", "Candidatos, leiam as instruções.", "Candidatos leiam as, instruções."],
        "correta": 1,
        "explicacao": "Candidatos é vocativo, pois chama os interlocutores. O vocativo deve ser separado por vírgula.",
        "fonte": "(Manual de Revisão da FUNAG, Pontuação — https://funag.gov.br/manual/index.php?title=Pontua%C3%A7%C3%A3o)",
    }],
    "Português — concordância com fazer": [{
        "pergunta": "Assinale a frase correta segundo a concordância verbal.",
        "alternativas": ["Fazem três anos que ela tomou posse.", "Faz três anos que ela tomou posse.", "Faziam três anos que ela tomou posse, desde ontem."],
        "correta": 1,
        "explicacao": "Quando indica tempo decorrido, o verbo fazer é impessoal e fica na terceira pessoa do singular: faz três anos.",
        "fonte": "(Manual de Redação da Presidência da República, seção de concordância; Manual de Revisão da FUNAG — https://funag.gov.br/manual/index.php?title=Concord%C3%A2ncia_verbal)",
    }],
    "Português — verbo haver impessoal": [{
        "pergunta": "Qual alternativa está correta na norma-padrão?",
        "alternativas": ["Havia muitos candidatos aguardando.", "Haviam muitos candidatos aguardando.", "Houveram muitos candidatos aguardando."],
        "correta": 0,
        "explicacao": "Com sentido de existir, haver é impessoal e permanece no singular, inclusive quando acompanhado de complemento plural.",
        "fonte": "(Manual de Revisão da FUNAG, Concordância verbal — https://funag.gov.br/manual/index.php?title=Concord%C3%A2ncia_verbal)",
    }],
    "Português — colocação pronominal": [{
        "pergunta": "Assinale a frase adequada à colocação pronominal na norma-padrão.",
        "alternativas": ["Não esqueça-se do prazo.", "Não se esqueça do prazo.", "Não esqueça do prazo-se."],
        "correta": 1,
        "explicacao": "A palavra negativa não atrai o pronome oblíquo para antes do verbo: não se esqueça.",
        "fonte": "(Manual de Revisão da FUNAG, Colocação pronominal — https://funag.gov.br/manual/index.php?title=Coloca%C3%A7%C3%A3o_pronominal)",
    }],
    "Português — uso dos porquês": [{
        "pergunta": "Complete corretamente: “A comissão explicou ______ o resultado foi alterado.”",
        "alternativas": ["por que", "porque", "porquê"],
        "correta": 0,
        "explicacao": "Usa-se por que em uma pergunta indireta, com sentido de “por qual motivo”: explicou por que o resultado foi alterado.",
        "fonte": "(Manual de Revisão da FUNAG, Uso do por que/por quê/porque/porquê — https://funag.gov.br/manual/index.php?title=Uso_do_por_que%2Fpor_qu%C3%AA%2Fporque%2Fporqu%C3%AA)",
    }],
    "Português — regência verbal": [{
        "pergunta": "Qual frase está de acordo com a regência do verbo obedecer?",
        "alternativas": ["O servidor obedeceu o regulamento.", "O servidor obedeceu ao regulamento.", "O servidor obedeceu no regulamento."],
        "correta": 1,
        "explicacao": "Na norma-padrão, obedecer é verbo transitivo indireto e rege a preposição a: obedecer ao regulamento.",
        "fonte": "(BECHARA, Evanildo. Moderna Gramática Portuguesa, regência verbal; Manual de Redação da Presidência da República.)",
    }],
    "Português — retificar e ratificar": [{
        "pergunta": "Em um comunicado, a banca precisou corrigir um erro no horário da prova. O verbo adequado é:",
        "alternativas": ["Ratificar o horário", "Retificar o horário", "Retardar o horário"],
        "correta": 1,
        "explicacao": "Retificar significa corrigir ou tornar exato. Ratificar significa confirmar ou validar.",
        "fonte": "(Academia Brasileira de Letras, Vocabulário Ortográfico da Língua Portuguesa — https://www.academia.org.br/nossa-lingua/busca-no-vocabulario)",
    }],
    "Português — futuro do subjuntivo": [{
        "pergunta": "Complete corretamente: “Se o fiscal ______ no procedimento, a equipe deverá registrar a ocorrência.”",
        "alternativas": ["intervir", "intervier", "intervia"],
        "correta": 1,
        "explicacao": "O futuro do subjuntivo do verbo intervir é intervier. Esse verbo segue a conjugação de vir: se vier, se intervier.",
        "fonte": "(Manual de Revisão da FUNAG, Vocabulário — verbete “futuro do subjuntivo”: https://funag.gov.br/manual/index.php?title=Vocabul%C3%A1rio)",
    }],
    "Português — conjunção concessiva": [{
        "pergunta": "Na frase “Embora estivesse cansada, a candidata concluiu a prova”, a palavra “embora” expressa ideia de:",
        "alternativas": ["Concessão", "Conclusão", "Finalidade"],
        "correta": 0,
        "explicacao": "Embora introduz uma oração subordinada adverbial concessiva: apresenta um fato que poderia contrariar a ação principal, mas não a impede.",
        "fonte": "(CUNHA, Celso; CINTRA, Lindley. Nova Gramática do Português Contemporâneo, orações subordinadas adverbiais.)",
    }],
    "Português — figura de linguagem": [{
        "pergunta": "Em “A cidade acordou cedo para receber os candidatos”, ocorre:",
        "alternativas": ["Eufemismo", "Prosopopeia ou personificação", "Ironia"],
        "correta": 1,
        "explicacao": "Atribui-se à cidade uma ação própria de seres vivos: acordar. Esse recurso é chamado prosopopeia ou personificação.",
        "fonte": "(CUNHA, Celso; CINTRA, Lindley. Nova Gramática do Português Contemporâneo, recursos expressivos.)",
    }],
    "Português — referência pronominal": [{
        "pergunta": "Leia: “A comissão publicou o resultado. Ela também divulgou o prazo para recursos.” A palavra “ela” retoma:",
        "alternativas": ["O resultado", "O prazo", "A comissão"],
        "correta": 2,
        "explicacao": "O pronome ela retoma o termo feminino singular comissão, mantendo a continuidade do referente entre as frases.",
        "fonte": "(KOCH, Ingedore Villaça. A coesão textual. São Paulo: Contexto.)",
    }],
}

LEGENDAS = {
    tema: f"{tema}: teste seus conhecimentos de Português para concursos!\n\n#JuhQuiz #Portugues #Concursos #Quiz"
    for tema in QUIZZES
}
