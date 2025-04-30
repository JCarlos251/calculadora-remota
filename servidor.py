import Pyro5.api

# Antes de rodar o servidor, deve-se rodar o serviço de nomes com o comando:
# python -m Pyro5.nameserver --host=[IP]

# Decorador para expor a classe para ser acessada remotamente
@Pyro5.api.expose
# Define a classe/interface remota que será acessada
class CalculadoraRemota:
    def soma(self, n1, n2):
        return n1 + n2

    def subtrai(self, n1, n2):
        return n1 - n2

    def multiplica(self, n1, n2):
        return n1 * n2

    def divide(self, n1, n2):
        if n2 == 0:
            return "Erro: Divisão por zero!"
        return n1 / n2

    def raiz_quadrada(self, n1):
        return n1 ** 0.5

    def exponencia(self, b, e):
        return b ** e

def main():
    # endereço IP do servidor
    ip_servidor = '192.168.15.8'

    # daemon para escutar requisições nesse IP
    daemon = Pyro5.api.Daemon(host=ip_servidor)

    # localiza o serviço de nomes no IP informado
    ns = Pyro5.api.locate_ns(host=ip_servidor)

    # registra a classe CalculadoraRemota no daemon e obtem o URI
    uri = daemon.register(CalculadoraRemota())

    # registra o uri no serviço de nomes com o nome "calculadora_remota"
    ns.register("calculadora_remota", uri)

    print("Servidor pronto. Aguardando:")
    # daemon aguardando requisições
    daemon.requestLoop()

if __name__ == "__main__":
    main()
