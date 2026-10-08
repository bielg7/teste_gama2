class Documento:
    def __init__(self, titulo, conteudo, tipo):
        self.__titulo = titulo
        self.__conteudo = conteudo
        self.__tipo = tipo


    def get_titulo(self):
        return self.__titulo

    def get_conteudo(self):
        return self.__conteudo

    def get_tipo(self):
        return self.__tipo

class Impressora:
    def imprimir(self, documento):
        print("\n" + "="*30)
        print("  IMPRIMINDO DOCUMENTO ")
        print("="*30)
        print(f"Título: {documento.get_titulo()}")
        print(f"Tipo: {documento.get_tipo().capitalize()}")
        print("-" * 30)
        print(f"Conteúdo:\n{documento.get_conteudo()}")
        print("="*30 + "\n")

def main():
    impressora = Impressora()
    documentos = []

    while True:
        print("=== MENU PRINCIPAL ===")
        print("1 - Criar documento")
        print("2 - Imprimir documento")
        print("0 - Encerrar o programa")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo = input("Digite o título: ")
            tipo = input("Digite o tipo (ex: relatório, carta, artigo): ")
            conteudo = input("Digite o conteúdo: ")
            documentos.append(Documento(titulo, conteudo, tipo))
            print("Documento criado com sucesso!\n")

        elif opcao == '2':
            if not documentos:
                print("Nenhum documento criado ainda.\n")
                continue
            for i, doc in enumerate(documentos, start=1):
                print(f"{i} - {doc.get_titulo()} ({doc.get_tipo()})")
            escolha = input("Número do documento: ")
            if escolha.isdigit() and 1 <= int(escolha) <= len(documentos):
                impressora.imprimir(documentos[int(escolha) - 1])
            else:
                print("Documento inválido.\n")

        elif opcao == '0':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()