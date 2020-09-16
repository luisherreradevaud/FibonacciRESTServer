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

    def calculaSuma(self,n):
        suma = 0
        n_int = int(n) + 1

        for n in range(0,n_int):
            suma = suma + n

        return suma

    def calculaMult(self,n):
        mult = 1
        n_int = int(n) + 1

        for n in range(2,n_int):
            mult = mult + n * n

        return mult


    def get(self,n):
        if(n.isnumeric()):
            respuestaPhi = self.calculaPhi(n)
            respuestaSuma = self.calculaSuma(n)
            respuestaMult = self.calculaMult(n)
        else:
            respuestaPhi = 'Solo enteros positivos.'
            respuestaSuma = 'Solo enteros positivos.'
            respuestaMult = 'Solo enteros positivos.'
        return {'respuestaPhi': respuestaPhi, 'respuestaSuma': respuestaSuma , 'respuestaMult': respuestaMult}
