import random
import time

class entity:
    def __init__(self, name, hp, dmg, max_hp, base_dmg, passiva=None):
        self.name = name
        self.health = hp
        self.max_health = max_hp
        self.damage = dmg
        self.base_damage = base_dmg
        self.passiva=passiva
        if passiva is None:
            self.passiva = []
        else:
            self.passiva = passiva
    def atacar(self, target):
        target.health -= self.damage
        if "vampirico" in self.passiva:
            curavampirica=int(self.damage * 0.05)
            self.health = min(self.max_health, self.health + curavampirica)
    def afiar(self):
        self.damage += random.randint(1, 5)
    def curar(self):
        quantidade_cura = random.randint(10, 30)
        self.health = min(self.max_health, self.health + quantidade_cura)
    def ultra_ataque(self, target):
        chance = random.randint(1, 100)
        if chance <= 10:
            target.health -= target.health
        else:
            target.health -= 0
            self.health -= self.health
            
guerreiro_passiva=[]
guerreiro = entity("Guerreiro", 100, 30, 100, 30, guerreiro_passiva)

inimigos= [
entity("demonio", 60, 30, 60, 30),
entity("cão infernal",90, 25, 90, 25),
entity("vampiro",200,40,999,40, ["vampirico"])
]
inimigoatual=0

turnos=1

almas = 0

print(f"você achou um demonio, ele tem {inimigos[inimigoatual].health} de vida e {inimigos[inimigoatual].damage} de dano")
time.sleep(2)
print(f"seu dano é {guerreiro.damage}")
time.sleep(2)

while True:
    print(f"estamos no turno {turnos}, você tem {guerreiro.health} de vida e seu inimigo tem {inimigos[inimigoatual].health} de vida")
    time.sleep(1)
    acao = input("Digite 'atacar' para atacar, 'afiar' para afiar sua arma, 'curar' para se curar \n ou 'ultra_ataque' para usar o ataque especial, \n ele tem 10% de chance de matar instantaneamente \n mas caso erre você morre instantaniamente ").lower().strip()
    while acao not in ["atacar", "afiar", "curar", "ultra_ataque"]:
        acao = input("Ação inválida, digite novamente: ").lower().strip()
    if acao == "atacar":
        guerreiro.atacar(inimigos[inimigoatual])
        print(f"você atacou o inimigo! agora ele tem {inimigos[inimigoatual].health} de vida")
        time.sleep(3)
    elif acao == "afiar":
        guerreiro.afiar()
        print(f"você afiou sua arma! agora seu dano é {guerreiro.damage}")
        time.sleep(3)
    elif acao == "curar":
        guerreiro.curar()
        print(f"você se curou! agora você tem {guerreiro.health} de vida")
        time.sleep(3)
    elif acao == "ultra_ataque":
        guerreiro.ultra_ataque(inimigos[inimigoatual])
        print(f"você usou o ataque especial! agora o inimigo tem {inimigos[inimigoatual].health} de vida")
        time.sleep(3)
    if inimigos[inimigoatual].health <= 0:
        recompensabatalha= random.randint(15, 25)
        almas += recompensabatalha
        inimigoatual += 1
        print(f"você venceu, ganhou {recompensabatalha} almas e subiu de nível!, \n  agora você tem {almas} almas \n escolha uma melhoria a seguir:")
        time.sleep(3)
        break
    if guerreiro.health <= 0:
            print("você perdeu...")
            exit()
    
    if inimigos[inimigoatual].health == inimigos[inimigoatual].max_health:
       acao_inimigo = random.choice(["atacar", "afiar"])
    else:
        acao_inimigo=random.choice(["atacar", "afiar", "curar"])

    if acao_inimigo == "atacar":
        inimigos[inimigoatual].atacar(guerreiro)
        print(f"o inimigo atacou você! agora você tem {guerreiro.health} de vida")
        time.sleep(3)
        turnos += 1
    elif acao_inimigo == "afiar":
        inimigos[inimigoatual].afiar()
        print(f"o inimigo afiou sua arma! agora o dano dele é {inimigos[inimigoatual].damage}")
        time.sleep(3)
        turnos += 1
    elif acao_inimigo == "curar":
        inimigos[inimigoatual].curar()
        print(f"o inimigo se curou! agora ele tem {inimigos[inimigoatual].health} de vida")
        time.sleep(3)
        turnos += 1
    if guerreiro.health <= 0:
        print("você perdeu...")
        exit()

melhoria = input("vida: aumenta sua vida maxima em 20 ou dano: \n aumenta seu dano maximo em 5 ").lower().strip()
while melhoria not in ["vida", "dano"]:
    melhoria=input("melhoria invalida digite novamente").lower().strip()

if melhoria == "vida":
    guerreiro.max_health += 20
    print(f"sua vida aumentou para {guerreiro.max_health}")
elif melhoria == "dano":
    guerreiro.base_damage += 5
    print(f"seu dano base aumentou para {guerreiro.base_damage}")

guerreiro.health = guerreiro.max_health
guerreiro.damage = guerreiro.base_damage
turnos=1
time.sleep(3)



print(f"você achou um cão infernal extremamente agressivo")
time.sleep(2)
print(f"ele tem {inimigos[inimigoatual].health} de vida e {inimigos[inimigoatual].damage} de ataque")
time.sleep(2)
print(f"você tem {guerreiro.damage} de dano")

while True:
    print(f"estamos no turno {turnos}, você tem {guerreiro.health} de vida e seu inimigo tem {inimigos[inimigoatual].health} de vida")
    time.sleep(1)
    acao = input("Digite 'atacar' para atacar, 'afiar' para afiar sua arma, 'curar' para se curar \n ou 'ultra_ataque' para usar o ataque especial, \n ele tem 10% de chance de matar instantaneamente \n mas caso erre você morre instantaniamente ").lower().strip()
    while acao not in ["atacar", "afiar", "curar", "ultra_ataque"]:
        acao = input("Ação inválida, digite novamente: ").lower().strip()
    if acao == "atacar":
        guerreiro.atacar(inimigos[inimigoatual])
        print(f"você atacou o inimigo! agora ele tem {inimigos[inimigoatual].health} de vida")
        time.sleep(3)
    elif acao == "afiar":
        guerreiro.afiar()
        print(f"você afiou sua arma! agora seu dano é {guerreiro.damage}")
        time.sleep(3)
    elif acao == "curar":
        guerreiro.curar()
        print(f"você se curou! agora você tem {guerreiro.health} de vida")
        time.sleep(3)
    elif acao == "ultra_ataque":
        guerreiro.ultra_ataque(inimigos[inimigoatual])
        print(f"você usou o ataque especial! agora o inimigo tem {inimigos[inimigoatual].health} de vida")
        time.sleep(3)
    if inimigos[inimigoatual].health <= 0:
        recompensabatalha= random.randint(50, 75)
        almas += recompensabatalha
        inimigoatual += 1
        print(f"você venceu, a coleira dele tinha um colar estranho \n ao pega-lo ele se destruir e virou {recompensabatalha} almas")
        time.sleep(3)
        break
    if guerreiro.health <= 0:
            print("você perdeu...")
            exit()
    
    if inimigos[inimigoatual].health == inimigos[inimigoatual].max_health:
       acao_inimigo = random.choice(["atacar", "afiar"])
    else:
        acao_inimigo=random.choice(["atacar", "afiar", "curar"])

    if acao_inimigo == "atacar":
        inimigos[inimigoatual].atacar(guerreiro)
        print(f"o inimigo atacou você! agora você tem {guerreiro.health} de vida")
        time.sleep(3)
        turnos += 1
    elif acao_inimigo == "afiar":
        inimigos[inimigoatual].afiar()
        print(f"o inimigo afiou seus dentes! agora o dano dele é {inimigos[inimigoatual].damage}")
        time.sleep(3)
        turnos += 1
    elif acao_inimigo == "curar":
        inimigos[inimigoatual].curar()
        print(f"o inimigo se curou! agora ele tem {inimigos[inimigoatual].health} de vida")
        time.sleep(3)
        turnos += 1
    if guerreiro.health <= 0:
        print("você perdeu...")
        exit()
guerreiro.damage = guerreiro.base_damage
guerreiro.health = guerreiro.max_health
turnos = 1

print("andando depois de enfrentar o cão infernal, você encontrou uma loja")
time.sleep(0.5)
entrar=input("deseja entrar? ").lower().strip()
while entrar != "sim" and entrar != "não":
     entrar=input("ação invalida, digite novamente: ")

if entrar == "sim":
    print("você entrou na loja, o atendente é um esqueleto com centenas de almas no peito \n ele olha para você e te atende")
    time.sleep(1)
    print("olá, você parece estar sujo de sangue, porque não fica aqui um pouco?")
    time.sleep(2)
    print(f"então, vejo que tem {almas} almas certo? porque não compra algo?")
    p_pocvamp=80
    p_espachif=40
    p_armalmas=60
    pocestoque=1
    espachifestoque=1
    armaalmasestoque=1
    while True:
        escolha = input("as suas opções são: \n poção vampirica: eu achei ela em um calabouço, não sei ao certo oque faz... \n custa 80 almas \n espada de chifre: forgei com os chifres de um demonio, aumenta seu dano em 10 \n custa 40 almas, \n armadura de almas: feita de almas puras, aumenta sua vida maxima em 20 \n custa 60 almas \n oque gostaria de comprar? digite sair para sair").lower().strip()
        while "poção vampirica" not in escolha and "espada de chifre" not in escolha and "armadura de almas" not in escolha and "sair" not in escolha:
            escolha = input("perdão? eu não vendo isso, fale outra coisa").lower().strip()
        if escolha=="sair":
            print("ja está de saida? volte sempre")
            break
        if escolha=="poção vampirica":
            if p_pocvamp <= almas and pocestoque >=1:
                almas -= p_pocvamp
                pocestoque -= 1
                guerreiro_passiva.append("vampirico")
                print("escolha exotica em? quem sou eu para julgar, pegue")
                time.sleep(2)
                print("*você bebe a poção, ela tem um gosto agoniante de sangue...*")
                time.sleep(2)
                print("*derrepente o gosto de sangue parece muito mais apetitoso para você*")
                time.sleep(1)
                print("agora você ganhou a passiva vampirico! seu ataque normal agora possui roubo de vida")
                time.sleep(3)
            elif pocestoque == 0:
                print("você comprou todos, esqueceu?")
            else:
                print("você não tem almas o suficiente")
        if escolha=="espada de chifre":
            if p_espachif<=almas and espachifestoque>=1:
                espachifestoque -=1
                almas -= p_espachif
                print("esses chifres são bem afiados, cortaria aço com facilidade")
                time.sleep(1)
                print("*seu dano aumentou em 10*")
                guerreiro.base_damage += 10
                time.sleep(1)
            elif almas<p_espachif:
                print("você não tem almas o suficiente para isso")
            else:
                print("estoque esgotado")
        if escolha == "armadura de almas":
            if p_armalmas <= almas and armaalmasestoque != 0:
                guerreiro.max_health += 20
                print("boa escolha, uma dessas é bem rara, principalmente nesse preço")
                time.sleep (1)
                print("*seu hp maximo aumentou em 20*")
            elif p_armalmas>almas:
                print("você não tem almas o suficiente")
            else:
                print("estoque esgotado")
        print(f"você tem {almas} almas")
        time.sleep(1)
else:
    print("você ignorou a loja")
    chance=random.randint(1, 100)
    time.sleep(1)
    if chance <= 20:
        print("andando após a loja você acha um corpo com uma poção, após beber seu hp maximo aumentou em 30")
        guerreiro.max_health += 30
        time.sleep(1)
        print(f"agora seu hp maximo é {guerreiro.max_health}")

guerreiro.health = guerreiro.max_health
guerreiro.damage = guerreiro.base_damage

time.sleep(1)
print("depois de tudo, você encontra uma grande pilha de corpos")
time.sleep(1)
print("você sente algo atras de você")
time.sleep(2)
escolha=input("você deseja se virar? ")
print("antes que possa fazer algo você sente uma mordida profunda no seu pescoço")
time.sleep(2)
print("sua pele fica dormente na hora, quem te mordeu foi um vampiro, você contraiu uma infecção por causa da mordida")
time.sleep(2)
while True:
    print(f", você morrera no turno 12, estamos no turno {turnos}, você tem {guerreiro.health} de vida e seu inimigo tem {inimigos[inimigoatual].health} de vida")
    time.sleep(1)
    acao = input("Digite 'atacar' para atacar, 'afiar' para afiar sua arma, 'curar' para se curar \n ou 'ultra_ataque' para usar o ataque especial, \n ele tem 10% de chance de matar instantaneamente \n mas caso erre você morre instantaniamente ").lower().strip()
    while acao not in ["atacar", "afiar", "curar", "ultra_ataque"]:
        acao = input("Ação inválida, digite novamente: ").lower().strip()
    if turnos == 12:
        print("você sente fraco e você sente que seu corpo não te obedece \n você cai no chão e morre convulcionando")
        exit()
    if acao == "atacar":
        guerreiro.atacar(inimigos[inimigoatual])
        print(f"você atacou o inimigo! agora ele tem {inimigos[inimigoatual].health} de vida")
        time.sleep(3)
    elif acao == "afiar":
        guerreiro.afiar()
        print(f"você afiou sua arma! agora seu dano é {guerreiro.damage}")
        time.sleep(3)
    elif acao == "curar":
        guerreiro.curar()
        print(f"você se curou! agora você tem {guerreiro.health} de vida")
        time.sleep(3)
    elif acao == "ultra_ataque":
        guerreiro.ultra_ataque(inimigos[inimigoatual])
        print(f"você usou o ataque especial! agora o inimigo tem {inimigos[inimigoatual].health} de vida")
        time.sleep(3)
    if inimigos[inimigoatual].health <= 0:
        recompensabatalha= random.randint(50, 75)
        almas += recompensabatalha
        inimigoatual += 1
        print(f"você venceu")
        break
    if guerreiro.health <= 0:
            print("você perdeu...")
            exit()
    
   
    acao_inimigo=random.choice(["atacar", "afiar"])

    if acao_inimigo == "atacar":
        inimigos[inimigoatual].atacar(guerreiro)
        print(f"o inimigo atacou você! agora você tem {guerreiro.health} de vida")
        time.sleep(3)
        turnos += 1
    elif acao_inimigo == "afiar":
        inimigos[inimigoatual].afiar()
        print(f"o inimigo afiou seus dentes! agora o dano dele é {inimigos[inimigoatual].damage}")
        time.sleep(3)
        turnos += 1
    
    if guerreiro.health <= 0:
        print("você perdeu...")
        exit()

time.sleep(3)
print("você matou ele, você consegue extrair a cura do sangue dele")
time.sleep(1)
print("você finalmente sai desse inferno(literalmente)")