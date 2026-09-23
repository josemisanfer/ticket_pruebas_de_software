class RepositorioFake:
    def __init__(self):
        self.compras = []

    def guardar(self, usuario, cantidad):
        self.compras.append({
            'usuario': usuario,
            'cantidad': cantidad
        })

#test

#repositorio = RepositorioFake();
#repositorio.guardar("josemi", 3);
#print(repositorio.compras);