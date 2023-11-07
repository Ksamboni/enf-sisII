class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if self.successor:
            self.successor.handle_request(request)

class ConcreteHandlerA(Handler):
    def handle_request(self, request):
        if request == 'A':
            print("ConcreteHandlerA: Manejó la solicitud 'A'.")
        else:
            super().handle_request(request)

class ConcreteHandlerB(Handler):
    def handle_request(self, request):
        if request == 'B':
            print("ConcreteHandlerB: Manejó la solicitud 'B'.")
        else:
            super().handle_request(request)

class ConcreteHandlerC(Handler):
    def handle_request(self, request):
        if request == 'C':
            print("ConcreteHandlerC: Manejó la solicitud 'C'.")
        else:
            print("Ningún manejador pudo manejar la solicitud.")

# Uso del patrón
if __name__ == "__main__":
    handlerA = ConcreteHandlerA()
    handlerB = ConcreteHandlerB()
    handlerC = ConcreteHandlerC()

    handlerA.successor = handlerB
    handlerB.successor = handlerC

    requests = ['A', 'B', 'C', 'D']
    for request in requests:
        handlerA.handle_request(request)
