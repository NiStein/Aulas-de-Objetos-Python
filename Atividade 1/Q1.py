# Minha primeira classe/objeto
# 1.A classe tem que ter pelo menos um atributo mutável.
# 2. Os métodos devem ter relação com algum atributo mutável.

# Classe
class video_game():
    # Atributos da classe
    marca = None
    nome = None
    tipo = None
    modelo = None
    cor = None
    estado = 'desligado'
    jogo = 'sem jogo'
    verfica_jogo = False
    biblioteca = ['Okami', 'New Super Mario', 'NFS MW', 'Spider-Man 2', 'Pokemon Y', 'Kirby', 'Gears of War', 'Halo', 'Resident Evil 4', 'Crash Bandicoot', 'Marvel Spider-Man2', 'Hi-Fi Rush', 'Red Dead Redemption 2', 'Zelda']
    gameplay = 'não rodando'

    #Métodos da Classe

    #Método para ligar o console
    def ligar(self):
        if self.estado == 'ligado':
            print(f'O {self.nome} já se encontra {self.estado}')
        else:
            self.estado = 'ligado'
            print(f'O {self.nome} está {self.estado}')

    #Método para desligar o console
    def desligar(self):
        if self.estado == 'desligado':
            print(f'O {self.nome} já está {self.estado}!')
        else:
            self.estado = 'desligado'
            print(f'O {self.nome} está {self.estado}')

    #Método para inserir um jogo
    def inserir_jogo(self,jogo):
        if self.estado == 'ligado':
            if self.verfica_jogo:
                print('Já existe um jogo no console!\nRetire ele primeiro')
            else:
                if jogo in self.biblioteca:
                    self.jogo = jogo
                    self.verfica_jogo = True
                    print(f'O {jogo} foi selecionado!')
                else:
                    print(f'o {jogo} não está na sua biblioteca!\nBaixe ele antes de jogar')
        else:
            print('Lige o console primeiro!')

    #Método para tirar um jogo
    def tirar_jogo(self):
        if self.estado == 'ligado':
            if not self.verfica_jogo:
                print(f'O {self.nome} já se encontra {self.jogo}!')
            else:
                self.jogo = 'sem jogo'
                self.verfica_jogo = False
                print(f'O {self.nome} está {self.jogo}')
        else:
            print('Lige o console primeiro!')
  
    #Método para baixar jogos
    def baixar_jogos(self, baixar):
        if self.estado == 'ligado':
            if baixar in self.biblioteca:
                print(f'O jogo {baixar} já foi baixado!')
            else:
                self.biblioteca.insert(1,baixar)
                print(f'{baixar} adicionado a biblioteca!')
        else:
            print('Lige o console primeiro!')

    #Método para listar jogos
    def listar_jogos(self):
        if self.estado == 'ligado':
            for jogo in self.biblioteca:
               print(f'{jogo}')
        else:
            print('Lige o console primeiro!')             

    #Método para jogar os jogos
    def gaming(self):
        if self.estado == 'ligado':
            if not self.verfica_jogo:
                print(f'Primeiro insira um jogo, gamplay {self.gameplay}!')
            else:
                self.gameplay = 'rodando'
                print(f'O {self.nome} está {self.gameplay} o jogo {self.jogo}')
        else:
            print('Lige o console primeiro!')        

def main():
    #Criando um console!
    console = video_game()
    console.marca = 'Xbox'
    console.nome = 'Xbox-360'
    console.tipo = 'Mesa'
    console.modelo = '360 Fat 1-Gen'
    console.cor = 'Branca'

    #Utilizando o console!
    console.ligar()

    #Verifica se está ligado
    console.ligar()

    #Listando bibliloteca
    console.listar_jogos()

    #Baixando um jogo
    console.baixar_jogos('Call of Duty: Black-Ops II')

    #Baixar um jogo que já existe
    console.baixar_jogos('Resident Evil 4')

    #Jogando sem jogo
    console.gaming()

    #Insira um jogo não existe
    console.inserir_jogo('Gears of War 3')

    #Inserindo um jogo que existe
    console.inserir_jogo('Gears of War')

    #Jogando um jogo
    console.gaming()

    #Tentando colocar mais um jogo
    console.inserir_jogo('Halo')

    #Retirando um jogo
    console.tirar_jogo()

    #Retirando um jogo sem jogos
    console.tirar_jogo()

    #Desligando o video-game
    console.desligar()

    #Tentando desligar de novo
    console.desligar()

    #Validação para ligar o console primeiro
    console.gaming()

if __name__ == "__main__":
    main()