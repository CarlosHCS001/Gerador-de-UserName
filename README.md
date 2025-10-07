# Gerador-de-UserName
Gerador CLI em Python para criar usernames e senhas com validação de força, comparação e fluxo interativo. Compatível com PyCharm (fallback de entrada de senha).

# Gerador de Usernames e Senhas (com Validação e Comparação)

Aplicação em Python para:
- Gerar usernames (3 opções) em diferentes estilos e permitir a escolha do usuário.
- Gerar senhas automaticamente (para referência).
- Permitir que o usuário digite sua própria senha.
- Validar a força da senha com pontuação e feedback detalhado.
- Comparar a senha digitada com as senhas geradas, exibindo um resumo e recomendações.
- Funciona bem no PyCharm com fallback de coleta de senha compatível.

## Funcionalidades

- Geração de usernames:
  - Estilos: aleatório, baseado em nome (nome_base) e criativo (pronunciável).
  - Exibe 3 opções e permite selecionar 1 (entrada 1/2/3).

- Geração de senhas:
  - Parâmetros: comprimento, uso de maiúsculas, minúsculas, números, símbolos e evitar caracteres ambíguos.
  - Garante ao menos 1 caractere de cada tipo selecionado.

- Validação de força da senha:
  - Pontuação de 0 a 100.
  - Critérios: comprimento, variedade de caracteres, presença em lista de senhas comuns, sequências óbvias e repetições.
  - Classificação: Muito Fraca, Fraca, Média, Forte, Muito Forte.
  - Feedback detalhado.

- Comparação de senhas:
  - Compara a senha digitada com todas as senhas geradas automaticamente.
  - Mostra diferenças de pontuação, ranking e resumo (mais fortes, mais fracas, iguais).
  - Recomendações com base na força.

- Compatibilidade com PyCharm:
  - Entrada de senha com função `coletar_senha()` que tenta `getpass` e faz fallback para `input()` caso o console não suporte TTY.

## Como usar

1. Requisitos
   - Python 3.8+
   - Sem dependências externas (usa apenas biblioteca padrão)

2. Executar
   - Via terminal:
     ```
     python gerador.py
     ```
   - No PyCharm:
     - Execute normalmente (Run). A função `coletar_senha()` garante compatibilidade.

3. Fluxo do programa
   - Escolha o estilo de username: `aleatorio`, `nome_base` ou `criativo`.
   - Se escolher `nome_base`, informe um nome (ex.: João Silva).
   - Selecione um dos 3 usernames sugeridos (1/2/3).
   - O programa gera 3 senhas automáticas para comparação e mostra o histórico.
   - Digite sua própria senha quando solicitado.
   - Veja a validação, comparação e as credenciais finais (Username + Senha).

## Estrutura principal do código

- Classe `GeradorCredenciais`
  - `gerar_senha(...)`: cria senha conforme regras.
  - `validar_forca_senha(senha)`: retorna pontuação, nível e feedbacks.
  - `comparar_senha_customizada(senha_usuario)`: compara com senhas geradas.
  - `gerar_usernames(quantidade, estilo, nome_base)`: cria sugestões de username.
  - `escolher_username(opcoes)`: permite escolher 1 dentre 3.
  - `exibir_historico()`: mostra senhas geradas com suas pontuações.
  - `limpar_historico()`: reseta histórico.

- Função `coletar_senha()`
  - Tenta ocultar a digitação com `getpass`.
  - Se o console não suportar, usa `input()` como fallback.

- Bloco `if __name__ == "__main__":`
  - Orquestra o fluxo de geração de usernames, senhas, coleta e comparação.
  - Exibe o pacote final de credenciais.

## Dicas de segurança

- Para ambientes de produção, prefira executar em terminal do sistema, onde `getpass` oculta a senha adequadamente.
- Evite reutilizar senhas e nunca use senhas comuns (ex.: 123456, qwerty).
- Prefira senhas com 12+ caracteres e variedade de tipos.

## Exemplo de uso (interação)

- Estilo de username: `aleatorio`
- Opções exibidas: `ForteLobo321`, `SombrioMago88`, `AstutoFenix574`
- Escolha: `2`
- Senhas geradas para comparação: 3 aleatórias
- Digite sua senha: `MinhaSenhaF0rte!`
- Saída: pontuação, feedbacks, resumo de comparação e credenciais finais:
  - Username: `SombrioMago88`
  - Senha: `MinhaSenhaF0rte!`

## Licença

Este projeto é fornecido "como está". Adapte livremente para uso pessoal ou educacional.
