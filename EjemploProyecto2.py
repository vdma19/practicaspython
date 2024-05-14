class Cocina:
    def __init__(self,cubiertos,ollas,platos,vasos):
        self.cubiertos=cubiertos
        self.ollas=ollas
        self.vasos=vasos
        self.platos=platos

    def cantidad_cosas(self):
        suma=self.cubiertos+self.ollas+self.vasos+self.platos
        if  suma < 50:
            return "Tienes {} utencilios de cocina.".format(suma)
        elif suma > 100:
            return "Tienes {} utencilios, hay que hacer una limpia".format(suma)
    
cubiertos=int(input("Ingrese la cantidad de cubiertos: "))
ollas=int(input("Ingrese la cantidad de ollas: "))
platos=int(input("Ingrese la cantidad de platos: "))
vasos= int(input("Ingrese la cantidad de vasos: "))

micocina=Cocina(cubiertos,ollas,platos,vasos)

print(micocina.cantidad_cosas())
