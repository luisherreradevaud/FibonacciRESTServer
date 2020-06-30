from flask_restful import Resource

class Phi(Resource):

    def calculaPhi(self,n):
        n_int = int(n)
        anterior = 0
        ant_anterior = 1
        suma = 0

        for n in range(0,n_int):
            suma = anterior + ant_anterior
            ant_anterior = anterior
            anterior = suma

        return suma

    def get(self,n):
        if(n.isnumeric()):
            respuesta = self.calculaPhi(n)
        else:
            respuesta = 'Solo enteros positivos.'
        return {'n': respuesta}
