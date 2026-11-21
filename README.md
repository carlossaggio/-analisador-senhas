# Analisador de Senhas em Python

Projeto de estudos em **cibersegurança** para identificar algumas características que podem tornar senhas mais previsíveis. O programa funciona no terminal, em português, e apresenta um indicador didático com recomendações.

## O que faz

- Analisa o tamanho da senha e a variedade de caracteres.
- Reconhece alguns exemplos de senhas comuns, sequências e repetições.
- Apresenta um nível de classificação e sugestões de melhoria.
- Usa entrada oculta no terminal, sem exibir a senha digitada.
- Funciona localmente, sem chamadas de rede ou gravação das senhas.

## Tecnologias

- Python 3.9 ou superior
- Bibliotecas padrão: `getpass`, `re` e `unittest`
- Sem dependências externas

## Como executar

1. Instale o Python 3.
2. Baixe o projeto e abra um terminal na pasta.
3. Execute:

```bash
python analisador_senhas.py
```

Digite apenas **senhas fictícias** para testar. O texto digitado não aparece na tela. Ao terminar, o programa apresenta um resultado e pergunta se você deseja testar outro exemplo.

### Executar testes

```bash
python -m unittest discover -v
```

## Organização

- `analisador_senhas.py`: análise e interface no terminal.
- `test_analisador_senhas.py`: testes automatizados.

## Limitações importantes

Este é um **projeto educacional**, não uma ferramenta profissional de auditoria. A pontuação é uma heurística simples; não mede com precisão o tempo necessário para descobrir uma senha e não consulta bancos de dados de credenciais vazadas. Uma classificação "Forte" **não garante** que a senha seja segura.

O programa não salva nem envia o conteúdo digitado. Ainda assim, a recomendação é usar apenas exemplos fictícios, especialmente ao executar ferramentas de estudo.

## O que aprendi com o projeto

O projeto foi organizado para praticar funções, estruturas condicionais, expressões regulares, validações e testes automatizados, aplicando esses conceitos a um problema de segurança da informação.

## Melhorias futuras

- Ampliar a detecção de padrões previsíveis.
- Investigar formas de avaliar frases-senha sem penalizar seu comprimento.
- Explorar bibliotecas especializadas e bases conhecidas de senhas comprometidas, considerando privacidade e segurança.
