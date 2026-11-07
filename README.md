# Quiz-10 — questões de Enfermagem para EBSERH

O pacote tem 15 questões autorais, no estilo de concurso, sobre conteúdos do cargo de Enfermeiro no edital EBSERH/Nacional 01/2024. Cada vídeo contém **uma pergunta** e três alternativas.

## Fluxo de cada vídeo

1. A voz do Quiz-10 lê o enunciado e as três alternativas.
2. A tela mostra a contagem regressiva de 3 segundos.
3. O vídeo marca a alternativa correta e a voz lê o gabarito.
4. Surge a página “COMENTÁRIO”, com a explicação escrita e narrada.

O visual segue a referência enviada: fundo amarelo, tema em faixa turquesa, cronômetro branco, texto preto e “Juh Quiz” pequeno no canto inferior. Três variações discretas de layout se alternam a cada três vídeos. A voz é `pt-BR-AntonioNeural`, +10%, igual ao Quiz-10.

As perguntas são inéditas e foram elaboradas com base nos conteúdos do edital; não são transcrições de questões oficiais.

## Arquivos

- `dados_quiz.py`: 15 perguntas, alternativas, gabaritos, explicações e legendas.
- `gerar_quiz.py`: telas, narração, vídeos MP4 e envio ao Drive.
- `.github/workflows/gerar-quiz.yml`: botão de geração pelo GitHub Actions.
- `requirements.txt`: dependências Python.
- `FONTES.txt`: edital e documentos oficiais consultados.

## Configurar o Drive

No repositório, abra **Settings → Secrets and variables → Actions → New repository secret**. O nome do Secret é `RCLONE_DRIVE_TOKEN`; use o JSON completo da autorização do Drive já utilizada no Quiz-10. Não coloque o token nos arquivos.

O workflow envia MP4 e TXT para `saida/Juh-Quiz-10/execucao-NÚMERO` na pasta do Drive já configurada no projeto.

## Gerar no GitHub

1. Envie o conteúdo do ZIP para a raiz do repositório Quiz-10, incluindo a pasta oculta `.github`.
2. Abra **Actions → Gerar Juh Quiz e salvar no Drive → Run workflow**.
3. Para conferir, use início `1` e quantidade `1`. Para gerar as 15 questões, use início `1` e quantidade `15`.

## Gerar localmente

Instale Python 3.11, FFmpeg e DejaVu Sans Bold. Rode:

```bash
pip install -r requirements.txt
python gerar_quiz.py --inicio 1 --quantidade 1 --lote teste
```

Para enviar localmente, acrescente `--enviar-drive` e configure o rclone com um remote chamado `destino`.
