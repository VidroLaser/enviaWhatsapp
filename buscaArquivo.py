import os


def buscar_arquivo(diretorio, nome_arquivo):
    try:
        for raiz, _, arquivos in os.walk(diretorio):
            if nome_arquivo in arquivos:
                return os.path.join(raiz, nome_arquivo)
        return None
    except Exception as e:
        print(f"Erro ao buscar arquivo: {e}")
        return None


def set_dir(path):
    try:
        numero_pasta = int(path)
        diretorio = r"\\servidor\PEDIDOS"

        if 10000 <= numero_pasta < 19999:
            nome_pasta = os.path.join(diretorio, "10000 ao 19999")
        elif 20000 <= numero_pasta < 29999:
            nome_pasta = os.path.join(diretorio, "20000 ao 29999")
        elif 30000 <= numero_pasta < 39999:
            nome_pasta = os.path.join(diretorio, "30000 ao 39999")
        elif 40000 <= numero_pasta < 49999:
            nome_pasta = os.path.join(diretorio, "40000 ao 49999")
        elif 50000 <= numero_pasta < 59999:
            nome_pasta = os.path.join(diretorio, "50000 ao 59999")
        else:
            nome_pasta = diretorio

        return nome_pasta
    except ValueError:
        print(f"Erro: o valor '{path}' não é um número inteiro válido.")
        return None
    except Exception as e:
        print(f"Erro ao definir diretório: {e}")
        return None


def buscar_pasta_com_palavra(diretorio, palavra_chave):
    try:

        if not os.path.exists(diretorio):
            print(f"Diretório '{diretorio}' não encontrado.")
            return None

        for nome_pasta in os.listdir(diretorio):
            caminho_completo = os.path.join(diretorio, nome_pasta)

            if os.path.isdir(caminho_completo):

                if palavra_chave in nome_pasta:
                    return caminho_completo

        print(f"Nenhuma pasta encontrada com a palavra '{palavra_chave}' no nome.")
        return None

    except Exception as e:
        print(f"Erro ao encontrar pasta {palavra_chave}: {e}")
