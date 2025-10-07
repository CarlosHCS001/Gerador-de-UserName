import random
import string
import re
import sys


class GeradorCredenciais:
    def __init__(self):
        self.adjetivos = [
            'Rapido', 'Forte', 'Sabio', 'Bravo', 'Astuto', 'Veloz', 'Epico',
            'Lendario', 'Mistico', 'Sombrio', 'Brilhante', 'Feroz', 'Nobre'
        ]
        self.substantivos = [
            'Lobo', 'Aguia', 'Dragao', 'Tigre', 'Falcao', 'Leao', 'Fenix',
            'Guerreiro', 'Mago', 'Ninja', 'Samurai', 'Cavaleiro', 'Heroi'
        ]
        self.senhas_comuns = [
            '123456', 'password', '12345678', 'qwerty', '123456789',
            'abc123', 'password123', '111111', '123123'
        ]
        self.senhas_geradas = []

    def gerar_senha(self, comprimento=12, usar_maiusculas=True, usar_minusculas=True,
                    usar_numeros=True, usar_simbolos=True, evitar_ambiguos=False):
        if comprimento < 6:
            print("⚠️  Aviso: Comprimento mínimo recomendado é 6 caracteres")
            comprimento = 6

        caracteres = ''
        senha_obrigatoria = []
        ambiguos = '0O1lI'

        if usar_minusculas:
            minusculas = string.ascii_lowercase
            if evitar_ambiguos:
                minusculas = ''.join(c for c in minusculas if c not in ambiguos)
            caracteres += minusculas
            senha_obrigatoria.append(random.choice(minusculas))

        if usar_maiusculas:
            maiusculas = string.ascii_uppercase
            if evitar_ambiguos:
                maiusculas = ''.join(c for c in maiusculas if c not in ambiguos)
            caracteres += maiusculas
            senha_obrigatoria.append(random.choice(maiusculas))

        if usar_numeros:
            numeros = string.digits
            if evitar_ambiguos:
                numeros = ''.join(c for c in numeros if c not in ambiguos)
            caracteres += numeros
            senha_obrigatoria.append(random.choice(numeros))

        if usar_simbolos:
            simbolos = '!@#$%&*'
            caracteres += simbolos
            senha_obrigatoria.append(random.choice(simbolos))

        if not caracteres:
            raise ValueError("Pelo menos um tipo de caractere deve ser selecionado!")

        senha_restante = [random.choice(caracteres) for _ in range(comprimento - len(senha_obrigatoria))]

        senha_final = senha_obrigatoria + senha_restante
        random.shuffle(senha_final)
        senha = ''.join(senha_final)

        self.senhas_geradas.append(senha)
        return senha

    def validar_forca_senha(self, senha):
        pontuacao = 0
        feedback = []

        comprimento = len(senha)
        if comprimento >= 16:
            pontuacao += 30
            feedback.append("✓ Comprimento excelente")
        elif comprimento >= 12:
            pontuacao += 20
            feedback.append("✓ Comprimento bom")
        elif comprimento >= 8:
            pontuacao += 10
            feedback.append("⚠ Comprimento adequado, mas poderia ser maior")
        else:
            feedback.append("✗ Senha muito curta (mínimo 8 caracteres)")

        tem_minuscula = bool(re.search(r'[a-z]', senha))
        tem_maiuscula = bool(re.search(r'[A-Z]', senha))
        tem_numero = bool(re.search(r'\d', senha))
        tem_simbolo = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', senha))
        variedade = sum([tem_minuscula, tem_maiuscula, tem_numero, tem_simbolo])

        if variedade == 4:
            pontuacao += 30
            feedback.append("✓ Excelente variedade de caracteres")
        elif variedade == 3:
            pontuacao += 20
            feedback.append("✓ Boa variedade de caracteres")
        elif variedade == 2:
            pontuacao += 10
            feedback.append("⚠ Variedade limitada de caracteres")
        else:
            feedback.append("✗ Pouca variedade de caracteres")

        if senha.lower() in self.senhas_comuns:
            pontuacao -= 50
            feedback.append("✗ CRÍTICO: Senha muito comum!")
        else:
            pontuacao += 20
            feedback.append("✓ Não é uma senha comum")

        sequencias = ['123', '234', '345', '456', '567', '678', '789',
                      'abc', 'bcd', 'cde', 'def', 'efg', 'fgh']
        tem_sequencia = any(seq in senha.lower() for seq in sequencias)
        if tem_sequencia:
            pontuacao -= 10
            feedback.append("⚠ Contém sequências óbvias")
        else:
            pontuacao += 10
            feedback.append("✓ Sem sequências óbvias")

        tem_repeticao = bool(re.search(r'(.)\1{2,}', senha))
        if tem_repeticao:
            pontuacao -= 10
            feedback.append("⚠ Contém caracteres repetidos")
        else:
            pontuacao += 10
            feedback.append("✓ Sem repetições excessivas")

        if pontuacao >= 80:
            nivel = "MUITO FORTE 🛡️"
            cor = "verde"
        elif pontuacao >= 60:
            nivel = "FORTE 💪"
            cor = "azul"
        elif pontuacao >= 40:
            nivel = "MÉDIA ⚠️"
            cor = "amarelo"
        elif pontuacao >= 20:
            nivel = "FRACA ⚠️"
            cor = "laranja"
        else:
            nivel = "MUITO FRACA ❌"
            cor = "vermelho"

        return {
            'pontuacao': max(0, min(100, pontuacao)),
            'nivel': nivel,
            'cor': cor,
            'feedback': feedback
        }

    def comparar_senha_customizada(self, senha_usuario):
        print("\n" + "=" * 60)
        print("🔍 COMPARAÇÃO DE SENHA CUSTOMIZADA")
        print("=" * 60)

        validacao_usuario = self.validar_forca_senha(senha_usuario)

        print(f"\n📝 Sua senha: {senha_usuario}")
        print(f"📊 Força: {validacao_usuario['nivel']}")
        print(f"Pontuação: {validacao_usuario['pontuacao']}/100")

        if not self.senhas_geradas:
            print("\n⚠️  Nenhuma senha foi gerada ainda para comparação.")
            print("\n📋 Análise da sua senha:")
            for item in validacao_usuario['feedback']:
                print(f"  {item}")
            return

        print(f"\n🔄 Comparando com {len(self.senhas_geradas)} senha(s) gerada(s):\n")

        senhas_mais_fortes = 0
        senhas_mais_fracas = 0
        senhas_iguais = 0

        comparacoes = []
        for i, senha_gerada in enumerate(self.senhas_geradas, 1):
            validacao_gerada = self.validar_forca_senha(senha_gerada)
            diferenca = validacao_gerada['pontuacao'] - validacao_usuario['pontuacao']
            if diferenca > 0:
                senhas_mais_fortes += 1
                status = f"🔼 +{diferenca} pontos mais forte"
            elif diferenca < 0:
                senhas_mais_fracas += 1
                status = f"🔽 {diferenca} pontos mais fraca"
            else:
                senhas_iguais += 1
                status = "➡️  Mesma pontuação"

            comparacoes.append({
                'numero': i, 'senha': senha_gerada,
                'pontuacao': validacao_gerada['pontuacao'],
                'nivel': validacao_gerada['nivel'],
                'diferenca': diferenca,
                'status': status
            })

        comparacoes.sort(key=lambda x: x['pontuacao'], reverse=True)
        for comp in comparacoes:
            print(f"  Senha #{comp['numero']}: {comp['senha']}")
            print(f"    Força: {comp['nivel']} ({comp['pontuacao']}/100)")
            print(f"    {comp['status']}\n")

        print("=" * 60)
        print("📈 RESUMO DA COMPARAÇÃO:")
        print(f"  • Senhas geradas mais fortes que a sua: {senhas_mais_fortes}")
        print(f"  • Senhas geradas mais fracas que a sua: {senhas_mais_fracas}")
        print(f"  • Senhas com mesma força: {senhas_iguais}")

        print("\n💡 RECOMENDAÇÃO:")
        if validacao_usuario['pontuacao'] >= 80:
            print("  Sua senha é excelente! Está no nível ideal de segurança.")
        elif senhas_mais_fortes > 0:
            melhor_senha = comparacoes[0]
            print(f"  Considere usar uma senha mais forte.")
            print(f"  A melhor senha gerada tem {melhor_senha['pontuacao']} pontos.")
        else:
            print("  Sua senha é melhor que todas as geradas! Parabéns!")

        print("\n📋 Análise detalhada da sua senha:")
        for item in validacao_usuario['feedback']:
            print(f"  {item}")
        print("=" * 60)

    def gerar_usernames(self, quantidade=3, estilo='aleatorio', nome_base=None):
        usernames = []
        for _ in range(quantidade):
            if estilo == 'aleatorio':
                adjetivo = random.choice(self.adjetivos)
                substantivo = random.choice(self.substantivos)
                numero = random.randint(10, 999)
                formato = random.choice([
                    f"{adjetivo}{substantivo}{numero}",
                    f"{adjetivo}_{substantivo}{numero}",
                    f"{substantivo}{adjetivo}{numero}",
                    f"{adjetivo}{numero}{substantivo}"
                ])
                usernames.append(formato)
            elif estilo == 'nome_base' and nome_base:
                nome_limpo = re.sub(r'[^a-zA-Z]', '', nome_base).lower()
                sufixos = ['_pro', '_master', '_king', '_legend', '_gamer',
                           '_oficial', '_real', '_top', '_elite']
                numero = random.randint(10, 9999)
                formato = random.choice([
                    f"{nome_limpo}{numero}",
                    f"{nome_limpo}{random.choice(sufixos)}",
                    f"{nome_limpo}_{numero}",
                    f"{random.choice(self.adjetivos).lower()}_{nome_limpo}"
                ])
                usernames.append(formato)
            elif estilo == 'criativo':
                vogais = 'aeiou'
                consoantes = 'bcdfghjklmnpqrstvwxyz'
                username = ''
                for i in range(random.randint(6, 10)):
                    username += random.choice(consoantes if i % 2 == 0 else vogais)
                username += str(random.randint(10, 999))
                usernames.append(username.capitalize())
        return usernames

    def escolher_username(self, opcoes):
        if not opcoes:
            raise ValueError("Nenhuma opção de username fornecida.")

        print("\n👤 OPÇÕES DE USERNAME:")
        for i, u in enumerate(opcoes, 1):
            print(f"  {i}. {u}")

        while True:
            escolha = input("Escolha o username (1, 2 ou 3): ").strip()
            if escolha in {'1', '2', '3'} and 1 <= int(escolha) <= len(opcoes):
                return opcoes[int(escolha) - 1]
            print("Entrada inválida. Digite 1, 2 ou 3.")

    def exibir_resultado_senha(self, senha):
        print("\n" + "=" * 60)
        print("🔐 SENHA GERADA")
        print("=" * 60)
        print(f"\nSenha: {senha}")
        validacao = self.validar_forca_senha(senha)
        print(f"\n📊 Força da Senha: {validacao['nivel']}")
        print(f"Pontuação: {validacao['pontuacao']}/100")
        print("\n📋 Análise Detalhada:")
        for item in validacao['feedback']:
            print(f"  {item}")
        print("=" * 60)

    def limpar_historico(self):
        self.senhas_geradas = []
        print("✓ Histórico de senhas limpo!")

    def exibir_historico(self):
        if not self.senhas_geradas:
            print("\n⚠️  Nenhuma senha foi gerada ainda.")
            return
        print("\n" + "=" * 60)
        print(f"📜 HISTÓRICO DE SENHAS ({len(self.senhas_geradas)} senha(s))")
        print("=" * 60)
        for i, senha in enumerate(self.senhas_geradas, 1):
            validacao = self.validar_forca_senha(senha)
            print(f"\n{i}. {senha}")
            print(f"   Força: {validacao['nivel']} ({validacao['pontuacao']}/100)")
        print("=" * 60)


def coletar_senha():
    try:
        import getpass
        if not sys.stdin.isatty():
            raise RuntimeError("Sem TTY para getpass, usando input().")
        s = getpass.getpass("Senha (entrada oculta): ").strip()
        if not s:
            print("Você não digitou nada.")
            s = getpass.getpass("Senha (entrada oculta): ").strip()
        return s
    except Exception:
        return input("Senha (atenção: será exibida enquanto digita): ").strip()


if __name__ == "__main__":
    gerador = GeradorCredenciais()
    print("🎯 GERADOR DE CREDENCIAIS\n")

    print("== GERADOR DE USERNAME ==")
    estilo = None
    while estilo not in {"aleatorio", "nome_base", "criativo"}:
        estilo = input("Escolha o estilo (aleatorio / nome_base / criativo): ").strip().lower()

    nome_base = None
    if estilo == "nome_base":
        nome_base = input("Informe um nome base (ex: João Silva): ").strip()

    opcoes_usernames = gerador.gerar_usernames(quantidade=3, estilo=estilo, nome_base=nome_base)
    username_escolhido = gerador.escolher_username(opcoes_usernames)
    print(f"\n✅ Username escolhido: {username_escolhido}")

    print("\n== GERANDO 3 SENHAS AUTOMÁTICAS PARA COMPARAÇÃO ==")
    senha1 = gerador.gerar_senha(comprimento=12)
    print(f"1. {senha1}")
    senha2 = gerador.gerar_senha(comprimento=14, usar_simbolos=False)
    print(f"2. {senha2}")
    senha3 = gerador.gerar_senha(comprimento=16, evitar_ambiguos=True)
    print(f"3. {senha3}")
    gerador.exibir_historico()

    print("\n== SUA SENHA ==")
    print("Digite sua própria senha para comparar com as geradas.")
    print("Dica: use pelo menos 12 caracteres com maiúsculas, minúsculas, números e símbolos.\n")

    senha_usuario = coletar_senha()

    if not senha_usuario:
        print("⚠️ Nenhuma senha informada. Encerrando.")
        exit(0)

    gerador.comparar_senha_customizada(senha_usuario)

    print("\n" + "=" * 60)
    print("✅ CREDENCIAIS FINAIS")
    print("=" * 60)
    print(f"👤 Username: {username_escolhido}")
    print(f"🔐 Senha:    {senha_usuario}")
    print("=" * 60)