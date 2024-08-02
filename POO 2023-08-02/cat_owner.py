from datetime import datetime
from datetime import date

#Classe do Dono
class Dono:
    def __init__(self, cpf, nome_dono, dt_nasc_dono, endereco, fone):
        self.__cpf = cpf
        self.__nome_dono = nome_dono
        self.__dt_nasc_dono = dt_nasc_dono
        self.__endereco = endereco
        self.__fone = fone
        self.__gato = None

    #Função para adotar um gato
    def adotar_Gato(self, gato):
        if type (gato) == Gato:
            idade = datetime.strptime(self.__dt_nasc_dono, "%d/%m/%Y").date()
            if date.today().year - idade.year< 16:
                print(f'O dono não pode adotar o gato, pois é menor de 16 anos...')
                return None
            else:
                if self.__gato == None:
                    self.__gato = gato
                    print('O gatinho foi adotado!')
                else:
                    print('O dono já possui um gato!')
        else:

            print('Isso não é um objeto... Tente novamente')
            return None


#Classe do Gato
class Gato:
    def __init__(self, codigo, nome_gato, dt_nasc, raca):
        self.__codigo = codigo
        self.__nome_gato = nome_gato
        self.__dt_nasc = dt_nasc
        self.__raca = raca


#Execução 1
Joao = Dono('0980980989','João','20/01/2000','rua 100', 86988761234)
Mimi = Gato(1,'Mimi','01/01/2023','SRD')

Joao.adotar_Gato(Mimi)


#Execução 2
Kati = Gato(2,'Kati','02/02/2021','SRD')
Joao.adotar_Gato(Kati)

#Execução 3
Lilian = Dono('87856947120','Lilian','10/02/2014','rua Dos Ipês', 86988751236)
Lilian.adotar_Gato(Kati)