#Classe do Gato
class Gato:
    def __init__(self, codigo, nome_gato, dt_nasc, raca):
        self.__codigo = codigo
        self.__nome_gato = nome_gato
        self.__dt_nasc = dt_nasc
        self.__raca = raca
        self.__dono = None

    #Função para cadastrar um dono
    def cadastrar_dono(self, pessoa):
        if  type(pessoa) == Pessoa:
            if self.__dono == None:
                self.__dono = pessoa
                print('O gatinho possui um dono agora!')
            else:
                print('O gatinho já tem um dono no momento....')
        else:
            print('Isso não é um objeto... Tente novamente')
            return None


#Classe do Dono
class Pessoa:
    def __init__(self, cpf, nome_dono, endereco, fone):
        self.__cpf = cpf
        self.__nome_dono = nome_dono
        self.__endereco = endereco
        self.__fone = fone

#Execução 1
Joao = Pessoa('0980980989','João','rua 100', 86988761234)
Mimi = Gato(1,'Mimi','01/01/2023','SRD')

Mimi.cadastrar_dono(Joao)

#Execução 2
Maria = Pessoa('05648936650','Maria','rua Lavanda', 8694523060)
Mimi.cadastrar_dono(Maria)

