from App import *

# Função principal que executa o servidor
def main():
    app = App()  # Instanciando a classe App
    app.initialize()  # Inicializando o banco de dados e o Flask
    app.run()  # Inicia o servidor Flask

if __name__ == "__main__":
    main()