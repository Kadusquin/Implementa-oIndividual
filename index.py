def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado.")
        return []
    except IOError:
        print(f"Erro ao ler o arquivo {nome_arquivo}.")
        return []

def escrever_arquivo(nome_arquivo, linhas):
    try:
        with open(nome_arquivo, 'w') as f:
            f.writelines(linhas)
    except IOError:
        print(f"Erro ao escrever no arquivo {nome_arquivo}.")

def ordenar_documentos_por_titulo(documentos):
    return sorted(documentos, key=lambda x: x['titulo'])

def adicionar_documento():
    titulo = input("Título do documento: ")
    data_producao = input("Data de produção: ")
    tema = input("Tema: ")
    contexto_historico = input("Contexto histórico: ")
    descricao = input("Descrição: ")
    autor = input("Autor: ")
    localizacao = input("Localização na biblioteca: ")

    documento = f"{titulo};{data_producao};{tema};{contexto_historico};{descricao};{autor};{localizacao}\n"
    escrever_arquivo('documentos.txt', ler_arquivo('documentos.txt') + [documento])

def listar_documentos():
    documentos = ler_arquivo('documentos.txt')
    documentos_formatados = []
    for documento in documentos:
        partes = documento.strip()
        documentos_formatados.append({
            'titulo': partes[0],
            'data_producao': partes[1],
            'tema': partes[2],
            'contexto_historico': partes[3],
            'descricao': partes[4],
            'autor': partes[5],
            'localizacao': partes[6]
        })

    documentos_ordenados = ordenar_documentos_por_titulo(documentos_formatados)
    for doc in documentos_ordenados:
        print(f"Título: {doc['titulo']}, Data de Produção: {doc['data_producao']}, Tema: {doc['tema']}, "
              f"Contexto Histórico: {doc['contexto_historico']}, Descrição: {doc['descricao']}, "
              f"Autor: {doc['autor']}, Localização: {doc['localizacao']}")

def main():
    while True:
        print("\nMenu da Biblioteca de História")
        print("1. Adicionar Documento")
        print("2. Listar Documentos")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            adicionar_documento()
        elif opcao == '2':
            listar_documentos()
        elif opcao == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
