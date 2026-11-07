# -*- coding: utf-8 -*-
"""15 questões autorais de Enfermagem no estilo do concurso EBSERH."""

CAPA_SEGUNDOS = 2

QUIZZES = {
    'SUS — princípios e acesso': [{
        'pergunta': 'No SUS, qual princípio garante que todas as pessoas tenham acesso às ações e aos serviços de saúde, em todos os níveis de atenção?',
        'alternativas': ['Equidade', 'Universalidade', 'Regionalização'],
        'correta': 1,
        'explicacao': 'A universalidade assegura o acesso de todas as pessoas às ações e aos serviços de saúde. Equidade significa considerar necessidades diferentes para reduzir desigualdades; regionalização organiza os serviços por territórios.'
    }],
    'SUS — controle social': [{
        'pergunta': 'De acordo com a Lei nº 8.142/1990, como se caracteriza o Conselho de Saúde?',
        'alternativas': ['Órgão temporário e apenas consultivo', 'Órgão permanente e deliberativo', 'Reunião que ocorre somente a cada quatro anos'],
        'correta': 1,
        'explicacao': 'A Lei nº 8.142/1990 define o Conselho de Saúde como permanente e deliberativo. A Conferência de Saúde, por sua vez, reúne-se a cada quatro anos para avaliar a situação de saúde e propor diretrizes.'
    }],
    'Processo de Enfermagem — etapas': [{
        'pergunta': 'Conforme a Resolução Cofen nº 736/2024, qual sequência apresenta as cinco etapas do Processo de Enfermagem?',
        'alternativas': ['Coleta, prescrição médica, execução, alta e auditoria', 'Avaliação, diagnóstico, planejamento, implementação e evolução', 'Triagem, hipótese clínica, tratamento, encaminhamento e alta'],
        'correta': 1,
        'explicacao': 'A resolução organiza o Processo de Enfermagem em avaliação, diagnóstico, planejamento, implementação e evolução. As etapas são inter-relacionadas, interdependentes, recorrentes e cíclicas.'
    }],
    'Processo de Enfermagem — atribuições': [{
        'pergunta': 'Segundo a Resolução Cofen nº 736/2024, quais atividades do Processo de Enfermagem são privativas do enfermeiro?',
        'alternativas': ['Anotação e checagem dos cuidados executados', 'Diagnóstico e prescrição de Enfermagem', 'Aferição de sinais vitais e coleta de dados'],
        'correta': 1,
        'explicacao': 'A resolução estabelece que o diagnóstico e a prescrição de Enfermagem cabem privativamente ao enfermeiro. Técnicos e auxiliares participam da implementação e fazem anotações e checagens sob supervisão e orientação do enfermeiro.'
    }],
    'Segurança do paciente — identificação': [{
        'pergunta': 'Antes de administrar um medicamento, qual conduta contribui para confirmar corretamente a identidade do paciente?',
        'alternativas': ['Conferir somente o número do leito', 'Usar pelo menos dois identificadores e compará-los com a prescrição', 'Perguntar o nome apenas ao acompanhante, sem conferir a pulseira'],
        'correta': 1,
        'explicacao': 'A identificação deve usar pelo menos dois identificadores confiáveis, conferidos antes do cuidado com os registros ou a prescrição. O número do leito não é identificador seguro, pois pode mudar.'
    }],
    'Prevenção de infecções — higiene das mãos': [{
        'pergunta': 'Em qual momento a higiene das mãos é indicada segundo os cinco momentos da assistência?',
        'alternativas': ['Antes de procedimento limpo ou asséptico', 'Somente ao final do plantão', 'Apenas quando as mãos estiverem visivelmente sujas'],
        'correta': 0,
        'explicacao': 'A higiene das mãos deve ser realizada antes de procedimento limpo ou asséptico, além de outros momentos da assistência, como antes do contato com o paciente e após risco de exposição a fluidos.'
    }],
    'Biossegurança — precaução-padrão': [{
        'pergunta': 'A quem se aplicam as precauções-padrão nos serviços de saúde?',
        'alternativas': ['Somente a pacientes com infecção confirmada', 'A todos os pacientes, independentemente do diagnóstico', 'Somente a pacientes internados em isolamento'],
        'correta': 1,
        'explicacao': 'As precauções-padrão são aplicadas no cuidado de todos os pacientes, independentemente de diagnóstico conhecido. Incluem higiene das mãos e uso de equipamentos de proteção conforme o risco de exposição.'
    }],
    'Tuberculose — proteção respiratória': [{
        'pergunta': 'Na assistência a paciente com suspeita de tuberculose pulmonar transmissível, qual medida de proteção respiratória é adequada?',
        'alternativas': ['Profissional usa PFF2 ou N95; paciente usa máscara cirúrgica durante transporte', 'Profissional usa somente luvas; paciente permanece sem máscara', 'Profissional usa máscara de tecido; paciente usa PFF2 durante transporte'],
        'correta': 0,
        'explicacao': 'Na precaução para aerossóis, o profissional utiliza respirador PFF2 ou N95 ao entrar no ambiente indicado. Quando o transporte for necessário, o paciente deve usar máscara cirúrgica.'
    }],
    'Centro cirúrgico — cirurgia segura': [{
        'pergunta': 'Na lista de verificação de cirurgia segura, em que momento a equipe confirma verbalmente paciente, procedimento e local da cirurgia antes da incisão?',
        'alternativas': ['Durante a confirmação antes da incisão', 'Somente depois que o paciente deixa a sala', 'Apenas na admissão hospitalar'],
        'correta': 0,
        'explicacao': 'A confirmação verbal da identidade do paciente, do procedimento e do local cirúrgico ocorre antes da incisão. A lista também inclui verificações antes da indução anestésica e antes da saída da sala.'
    }],
    'Hemoterapia — reação transfusional': [{
        'pergunta': 'Durante uma transfusão, o paciente apresenta sinais que levantam suspeita de reação transfusional. Qual é a primeira conduta?',
        'alternativas': ['Diminuir a velocidade e aguardar melhora', 'Interromper imediatamente a transfusão e comunicar a equipe responsável', 'Descartar a bolsa e reiniciar a transfusão em outro acesso'],
        'correta': 1,
        'explicacao': 'Na suspeita de reação, a transfusão deve ser interrompida imediatamente. A equipe deve manter o acesso venoso, avaliar o paciente, conferir as identificações e comunicar o médico e o serviço de hemoterapia.'
    }],
    'Imunização — rede de frio': [{
        'pergunta': 'Na rotina de conservação de vacinas refrigeradas na sala de vacinação, qual faixa de temperatura deve ser mantida no equipamento?',
        'alternativas': ['De +2 °C a +8 °C', 'De −10 °C a −2 °C', 'De +10 °C a +18 °C'],
        'correta': 0,
        'explicacao': 'Para os imunobiológicos que devem permanecer refrigerados, a faixa de conservação indicada é de +2 °C a +8 °C. A equipe monitora e registra a temperatura conforme as normas da rede de frio.'
    }],
    'Farmacologia — cálculo de dose': [{
        'pergunta': 'Foi prescrita uma dose de 750 mg. A apresentação disponível contém 500 mg em 2 mL. Qual volume corresponde à dose prescrita?',
        'alternativas': ['2 mL', '3 mL', '4 mL'],
        'correta': 1,
        'explicacao': 'A concentração é 250 mg por mL, pois 500 mg estão em 2 mL. Para administrar 750 mg, são necessários 750 ÷ 250 = 3 mL.'
    }],
    'Segurança do paciente — prevenção de quedas': [{
        'pergunta': 'Qual ação é adequada para prevenir quedas durante a internação?',
        'alternativas': ['Aplicar a mesma medida a todos, sem avaliar riscos', 'Avaliar o risco e definir medidas preventivas individualizadas', 'Reavaliar o risco somente após a alta'],
        'correta': 1,
        'explicacao': 'A prevenção começa com a avaliação do risco e a escolha de medidas adequadas a cada paciente. O risco deve ser reavaliado quando houver mudança clínica, transferência ou outro fator relevante.'
    }],
    'Gerenciamento de resíduos — perfurocortantes': [{
        'pergunta': 'Após o uso, onde deve ser descartada uma agulha contaminada?',
        'alternativas': ['Em recipiente rígido, resistente à punctura e identificado para perfurocortantes', 'No lixo comum, depois de recolocar o protetor', 'Em saco branco, misturada a gazes usadas'],
        'correta': 0,
        'explicacao': 'Agulhas e outros perfurocortantes devem ser descartados no recipiente apropriado, rígido, resistente à punctura e identificado. Não se deve reencapar a agulha nem descartá-la no lixo comum.'
    }],
    'Saúde mental — CAPS': [{
        'pergunta': 'Qual característica corresponde à atuação dos Centros de Atenção Psicossocial, os CAPS?',
        'alternativas': ['Cuidado psicossocial comunitário e multiprofissional', 'Atendimento exclusivamente hospitalar e de longa permanência', 'Serviço restrito a consultas médicas, sem articulação com a rede'],
        'correta': 0,
        'explicacao': 'Os CAPS oferecem cuidado psicossocial comunitário e multiprofissional, articulado à rede de atenção. A proposta prioriza cuidado em liberdade e atenção no território, conforme as necessidades da pessoa.'
    }],
}

LEGENDAS = {
    tema: f'{tema}: responda à questão e confira a explicação.\n#JuhQuiz #EBSERH #Enfermagem #Concursos'
    for tema in QUIZZES
}
