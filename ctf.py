#!/usr/bin/env python
#coding: utf-8

# Bold
BR="\033[1;31m"         # Red
BG="\033[1;32m"       # Green
BY="\033[1;33m"      # Yellow
BB="\033[1;34m"        # Blue
BP="\033[1;35m"      # Purple
BC="\033[1;36m"        # Cyan
BW="\033[1;37m"       # White

# Regular Colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray


"""
	[ A LEGIAO THE HACKER SECURITY ]
          [ 2020 - CAPTURE THE FLAG ]
"""

from time import *
import hashlib
import getpass
import sys
import os
from os import system
from platform import python_version

Limpar = "clear"

os.system(Limpar)

if sys.version_info[0] < 3:
	versao = python_version()
	print(R+"┌═════════════════════════════════════════════════════════════════════════════┐")
	print("  Você está usando o python na versão %s ela é inferior ao python3. " %(versao))
	print("  Por favor rode o CTF com a versão superior ao python2. ")
	print("└═════════════════════════════════════════════════════════════════════════════┘")
	exit(1)
print(R + """
	┌═════════════════════════════════════════════════════════════════════════════┐
	█                       ╔──────────────────────────────╗                      █
	█                       │   HACK THE FLAG - CTF 2020   │                      █ 
	█                       ╚──────────────────────────────╝                      █
	└═════════════════════════════════════════════════════════════════════════════┘ 
 
	┌═════════════════════════════════════════════════════════════════════════════┐
	█                       ╔──────────────────────────────╗                      █
	█                       │ A Legiao The Hacker Security │                      █ 
	█                       ╚──────────────────────────────╝                      █
	└═════════════════════════════════════════════════════════════════════════════┘ 

""" + W)
try:
	print("┌══════════════════════════════════════────────────")	
	usuario = input("└───█ Username █══──── ").upper()
except:
	exit(1)

def Apresentacao():
	os.system(Limpar)
	print(R + """
   ╔════════════════════╗    ┌════════════════════════════════┐
   │██████ ██████ ██████│    █ ██████  ██████  ██████  ██████ █
─══████      ██   █████ ╚───██     ██  ██  ██      ██  ██  ██ █     ╔──────═╗
    ████     ██   ███▓ ╔──═╗ █ ██████  ██  ██  ██████  ██  ██ █▒────╝       │	 
─══▓▓▓▓▓▓▓   ▓▓   ▓▓ ╔─╝   ╚▓█ ▓▓      ▓▓  ▓▓  ▓▓      ▓▓  ▓▓ █             ╚─────═╗
   │▒▒▒▒▒▒   ▒▒   ▒▒ │       █ ▒▒▒▒▒   ▒▒▒▒▒▒  ▒▒▒▒▒   ▒▒▒▒▒▒ █                    │
   ╚═════════════════┘       └════════════════════════════════┘                    ╚──═╗  
                                                                                       ▓═┐ 
   ┌═════════════════════════════════════════════════════════════════════════════┐       ▒
─══█                       ╔──────────────────────────────╗                      █  ┌═┐  ▒
   █                       │ """+BC+"""A Legiao The Hacker Security"""+R+""" │                      █─═"""+C+"""███"""+R+"""══┘
─══█                       ╚──────────────────────────────╝                      █  └═┘
   └═════════════════════════════════════════════════════════════════════════════┘    														  
    
─══█▓▒──═══════════════════════════════════════════════───══█ """+C+"""User ▶"""+R+""" %s █═══─────═┐
   ╚════════════════════════════════════════════════════════════════════════════─────────┘
""" %(usuario)+C)

def Menu1():
	Apresentacao()
	print ('''
╔══════════════════════════════════════════════════════════════─────
│	1 ⟫═── Iniciar
│	2 ⟫═── Sobre
│	3 ⟫═── Dependências
│	4 ⟫═── Permissões
│	5 ⟫═── Níveis
│	6 ⟫═── Sair
╚════════════════════════════════════════════════════════════════════════════─────

''')
	opcao1 = input("─══█ option ⟫═── ")
	if opcao1 == "1":
		Bloco1()
	elif opcao1 == "2":
		Sobre()
	elif opcao1 == "3":
		Instalacao()
	elif opcao1 == "4":
		Permissao()
	elif opcao1 == "5":
		MudarPara()
	elif opcao1 == "q":
		exit(1)
	else:
		ComandoNaoEncontrado()

		Menu1()

def Permissao():
	Apresentacao()
	print("\n Arquivo a ser aplicado a permissão.\n")
	sleep(3)
	os.system("ls | grep spyquiz.py | lolcat")
	sleep(3)
	print("\n Pronto, permissões aplicadas.")
	sleep(3)
	os.system("chmod +x spyquiz.py")
	Menu1()

def MudarPara():
	Apresentacao()
	print("""
┌═══█ Nível ⟫═── Você deseja ir para que nível ?
█
█ Nível - 01 ⟫═── Descriptografia
█ Nível - 02 ⟫═── Esteganografia
█ Nível - 03 ⟫═── Engenharia Reversa
█ Nível - 04 ⟫═── Hexdump
█ Nível - 05 ⟫═── Coleta de Informações, Wordlist
█ Nível - 06 ⟫═── SqlInjection
█ Nível - 07 ⟫═── Leitura QRcode
█ Nível - 08 ⟫═── Base64 - crypt
█ Nível - 09 ⟫═── Binário
█ Nível - 10 ⟫═── Encrypted
█ Nível - 11 ⟫═── Reverter
█ Nível - 12 ⟫═── Engenharia Reversa
█ Nível - 13 ⟫═── A porta dos fundos
█ Nível - 14 ⟫═── Crypto Encrypted
█ Nível - 15 ⟫═── Análise Criminal
█ Nível - 16 ⟫═── Esteganografia 
█ Nível - 17 ⟫═── Análise de DLL
█ Nível - 18 ⟫═── Se vire Garoto
█ Nível - 19 ⟫═── Se vire
█ Nível - 20 ⟫═── Vasculhando
█ Nível - 21 ⟫═── Arabica2rs
█ Nível - 22 ⟫═── Tigo3fx
█ Nível - 24 ⟫═── Escuro
█ Nível - 25 ⟫═── Trabalhando e desencriptando
█ Nível - 26 ⟫═── <i>
█ Nível - 27 ⟫═── Nazca Lines
█ Nível - 28 ⟫═── Matrix
█ Nível - 29 ⟫═── Adam Smith
█ Nível - 30 ⟫═── The End
█
█─══█ Return ⟫═── Press """ + R+ """q"""+C+""" To Return 
└════════════════════════════════════════════════════════════════════════════─────
""")
	opcao1 = input("─══█ Nível ⟫═──")
	if opcao1 == "01":
		Bloco1()
	elif opcao1 == "02":
		Bloco2()
	elif opcao1 == "03":
		Bloco3()
	elif opcao1 == "04":
		Bloco4()
	elif opcao1 == "05":
		Bloco5()
	elif opcao1 == "06":
		Bloco6()
	elif opcao1 == "07":
		Bloco7()
	elif opcao1 == "08":
		Bloco8()
	elif opcao1 == "09":
		Bloco9()
	elif opcao1 == "10":
		Bloco10()
	elif opcao1 == "11":
		Bloco11()
	elif opcao1 == "12":
		Bloco12()
	elif opcao1 == "13":
		Bloco13()
	elif opcao1 == "14":
		Bloco14()
	elif opcao1 == "15":
		Bloco15()
	elif opcao1 == "16":
		Bloco16()
	elif opcao1 == "17":
		Bloco17()
	elif opcao1 == "18":
		Bloco18()
	elif opcao1 == "19":
		Bloco19()
	elif opcao1 == "20":
		Bloco20()
	elif opcao1 == "21":
		Bloco21()
	elif opcao1 == "22":
		Bloco22()
	elif opcao1 == "23":
		Bloco23()
	elif opcao1 == "24":
		Bloco24()
	elif opcao1 == "25":
		Bloco25()
	elif opcao1 == "26":
		Bloco26()
	elif opcao1 == "27":
		bloco27()
	elif opcao1 == "28":
		Bloco28()
	elif opcao1 == "29":
		Bloco29()
	elif opcao1 == "30":
		Bloco30()
	elif opcao1 == "q":
		Menu1()
	else:
		ComandoNaoEncontrado()
		MudarPara()

def Instalacao():
	def ArchDerivados():
		print("\n[\033[1;32m*\033[1;m] Aguarde em quanto instalamos as dependências...\n")
		sleep(3)
		os.system("sudo pacman -S --noconfirm sl curl lolcat")
		print("\n\n[\033[1;32m*\033[1;m] Instalado com sucesso.")
		input("\n\033[1;36mPressione ENTER para voltar...\033[1;m ")
		Menu1()
	def DebianDerivados():
		print("\n[\033[1;32m*\033[1;m] Aguarde em quanto instalamos as dependências...\n")
		sleep(3)
		os.system("sudo apt install -y sl curl")
		print("")
		os.system("gem install lolcat")
		print("\n\n[\033[1;32m*\033[1;m] Instalado com sucesso.")
		input("\n\033[1;36mPressione ENTER para voltar...\033[1;m ")
		Menu1()
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Escolha sua distribuição atual para a instalação dos requisítos.

\033[31m1\033[1;m) Arch Linux & Derivados
\033[31m2\033[1;m) Debian & Derivados
\033[31m3\033[1;m) Voltar
\033[31m4\033[1;m) Sair
''')
	opcao1 = input("─══█ Option ⟫═──")
	if opcao1 == "1":
		ArchDerivados()
	elif opcao1 == "2":
		DebianDerivados()
	elif opcao1 == "3":
		Menu1()
	elif opcao1 == "4":
		exit(1)
	else:
		ComandoNaoEncontrado()


def Bloco1():
	p = True
	q = False
	Apresentacao()
	print( W + '''
╔════──══█ ''' + R + '''LEVEL 01''' + W + ''' █═══──════════════════════════════════──══█''' + C + ''' CRIPTOGRAFIA''' + W + ''' █═══─────
╚════════════════════════════════════════════════════════════════════════════──────

		╔────────────────────────────────────────────╗
		│                                            │
		│      ''' + R + '''b078ffd28db767c502ac367053f6e0ac''' + W + '''      │
		│                                            │
		╚────────────────────────────────────────────╝

╔══════════════════════════════════════════════════════════════─────
│	1 ⟫═── Responder
│	2 ⟫═── Pular
│	3 ⟫═── Sair
╚════════════════════════════════════════════════════════════════════════════─────
''' + W )
	opcao1 = input("─══█ option ⟫═──")
	if opcao1 == "1":
		while p != q:
			p = input("─══█ ⟫═── Resposta: ")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "affb89447d5c8193b178f1f02126d6e3347ad25a772dc4a68227cdf1ce8984f1d9df367be450c8bfd19e23360ff3348b4f143e1135dd47d561b8920d0e7aaac9"
			if p != q:
				print("─══█ ⟫═── Resposta incorreta.")
				input("─══█ Try again ⟫═── Press ENTER...")
				Bloco1()
		print("─══█ ⟫═── Resposta correta! ")
		print('''
╔══════════════════════════════════════════════════════════════─────
│	WELCOME, WE ARE " A LEGIAO THE HACKER SECURITY "
│   WELCOME TO " HACK THE FLAG CTF-2020"				
╚════════════════════════════════════════════════════════════════════════════─────
		''')
		input(" ⟫═── press ENTER to continue...  ")
		Bloco2()
	elif opcao1 == "2":
		Bloco2()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("─══█ ⟫═── Press ENTER... ")
		Bloco1()

def Bloco2():
	p = True
	q = False
	Apresentacao()
	print('''
╔════──══█ ''' + R + '''LEVEL 02''' + W + ''' █═══──═════════════════════════──══█''' + R + ''' ESTEGANOGRAFIA''' + W + ''' █═══─────
╚════════════════════════════════════════════════════════════════════════════──────	
╔══════════════════════════════════════════════════════════════─────
│                  ──══█'''+R+''' Ache a senha dentro da imagem '''+W+'''█═══──
│    https://github.com/a-legiao-the-hacker-security/CTF-2020/Level02.png    │                  	
│                                                                            │
╚════════════════════════════════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════════════════─────
│	1 ⟫═── Responder
│	2 ⟫═── Pular
│	3 ⟫═── Sair
╚════════════════════════════════════════════════════════════════════════════─────
''')
	opcao1 = input("─══█ option ⟫═──")
	if opcao1 == "1":
		while p != q:
			p = input("─══█ ⟫═── Resposta: ")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "e08e73fb7514d2b021685d49fe5a8176dfdc24f23e3527df2e4ec126aad2202d3ddc7b7088ab5e16304537fe3ee82ddd99d723e583e4068b4357daec4d65346c"
			if p != q:
				print("─══█ ⟫═── Resposta incorreta.")
				input("─══█ Try again ⟫═── Press ENTER...")
				Bloco2()
		print("─══█ ⟫═── Resposta correta! ")
		print('''
╔══════════════════════════════════════════════════════════════─────
│	
│				
╚════════════════════════════════════════════════════════════════════════════─────
		''')
		input(" ⟫═── press ENTER to continue...  ")
		Bloco3()
	elif opcao1 == "2":
		Bloco3()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("─══█ ⟫═── Press ENTER... ")
		Bloco2()

def Bloco3():
	p = True
	q = False
	Apresentacao()
	print('''
╔════──══█ ''' + R + '''LEVEL 03''' + W + ''' █═══──═════════════════════════──══█''' + R + ''' E.Reversa''' + W + ''' █═══─────
╚════════════════════════════════════════════════════════════════════════════──────	
╔══════════════════════════════════════════════════════════════─────
│                  ──══█'''+R+''' Engenharia Reversa '''+W+'''█═══──
│    https://github.com/a-legiao-the-hacker-security/CTF-2020/Level03    │                  	
│                                                                            │
╚════════════════════════════════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════════════════─────
│	1 ⟫═── Responder
│	2 ⟫═── Pular
│	3 ⟫═── Sair
╚════════════════════════════════════════════════════════════════════════════─────
''')
	opcao1 = input("─══█ option ⟫═──")
	if opcao1 == "1":

		while p != q:
			p = input("─══█ ⟫═── Resposta: ")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "f26bd05f172b6a2eb8faebaf7820c4c9684d6a644aa958f7a141ccbab8bd84f671c7ff17112c2673742e8e146c8c58d57265a4fe0bc7bcac170cc512f9586566"
			if p != q:
				print("─══█ ⟫═── Resposta incorreta.")
				input("─══█ Try again ⟫═── Press ENTER...")
				Bloco3()
		print("─══█ ⟫═── Resposta correta! ")
		print('''
╔══════════════════════════════════════════════════════════════─────
│	A Engenharia Reversa e a arte de descobrir segredos,
│	Com ela voce pode saber como um software funciona; 			
╚════════════════════════════════════════════════════════════════════════════─────
		''')
		input("─══█ Continue ⟫═── Press ENTER... ")	
		Bloco4()
	elif opcao1 == "2":
		Bloco4()
	elif opcao1 == "3":
		Instalacao()
	elif opcao1 == "4":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("─══█ ⟫═── Press ENTER... ")
		Bloco3()

def ComandoNaoEncontrado():
	print ('''
   ┌═════════════════════════════════════════════════════════════════════════════┐
   █                       ╔──────────────────────────────╗                      █
─══█                       │ O comando nao foi encontrado │                      █ 
   █                       ╚──────────────────────────────╝                      █
   └═════════════════════════════════════════════════════════════════════════════┘ 
		''')

def Bloco4():
	p = True
	q = False
	Apresentacao()
	print('''
╔════──══█ ''' + R + '''LEVEL 04''' + W + ''' █═══──═════════════════════════──══█''' + R + ''' HEXDUMP''' + W + ''' █═══─────
╚════════════════════════════════════════════════════════════════════════════──────	
╔══════════════════════════════════════════════════════════════─────
│                  ──══█'''+R+''' Cade a Flag??? '''+W+'''█═══──
│    https://github.com/a-legiao-the-hacker-security/CTF-2020/Level04        │                  	
│                                                                            │
╚════════════════════════════════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════════════════─────
│	1 ⟫═── Responder
│	2 ⟫═── Pular
│	3 ⟫═── Sair
╚════════════════════════════════════════════════════════════════════════════─────
''')
	opcao1 = input("─══█ Option ⟫═── ")
	if opcao1 == "1":
		while p != q:
			p = input("─══█ ⟫═── Resposta: ")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "c226d6e0bd627b58aa625a5b2401a1040401fd8436f0e247ac0adac126b414fc2aee864c21c6579618d3ae41c5ef907ea7a93bdaacd485157906f2af8bf1df12"
			if p != q:
				print("─══█ ⟫═── Resposta incorreta.")
				input("─══█ Try again ⟫═── Press ENTER...")
				Bloco4()
		print("─══█ ⟫═── Resposta correta! ")
		print('''
╔══════════════════════════════════════════════════════════════─────
│	
│				
╚════════════════════════════════════════════════════════════════════════════─────
		''')
		input("─══█ Continue ⟫═── Press ENTER... ")
		Bloco5()
	elif opcao1 == "2":
		Bloco5()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("─══█ ⟫═── Press ENTER... ")
		Bloco4()

def Bloco5():
	Apresentacao()
	lista = []
	i = 1
	print('''
[\033[1;32m*\033[1;m] Nível - #5: Coleta de Informações, Wordlist
 _________________________________________________
|                                                 |
|Robert D. Baker                                  |
|Namorada: Ketty                                  |
|Estilo de música: Eletronica                     |
|Cidade: Nova York                                |
|Nome da mãe: Marta                               |
|Nome do pai: Peterson                            |
|Coordenadas geográficas: 43,010354, -88,076145   |
|Telefone: 414-557-3179                           |
|Codigo da cidade: 55                  	          |
|Data de nascimento: 20 de julho, 1982            |
|Idade: 34 anos                                   |
|Signo: Leão                                      |
|Endereço de e-mail: robertdbaker@gmail.com       |
|Nome de usuário: bakerdr                         |
|MasterCard: 5159 6656 3798 1026                  |
|Vence em: 6/2018                                 |
|Nome do cachorro: titicozito                     |
|Empresa: Robotic Solution                        |
|Ocupação: Robotica                               |
|Altura: 1,75                                     |
|Peso: 78 Kg                                      |
|Tipo sanguíneo: B+                               |
|Cor favorita: Verde                              |
|Veículo: Ninja H2R                               |
|_________________________________________________|

\033[31m1\033[1;m) Responder
\033[31m2\033[1;m) Pular
\033[31m3\033[1;m) Sair
''')
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "1":
		try:
			responder = int(input("\n\033[1;36mColoque a quantidade de senhas que você deseja importar a sua wordlist (ex: 5):\033[1;m "))
			print("\n")
			print("[\033[1;91m!\033[1;m] OBS: Digite as senhas que possa ser a da vitima, de acordo com os dados informados acima.\033[1;m")
		except:
			print("\n[\033[1;91m!\033[1;m] Valor errado!")
			sleep(2)
			return Bloco5()
		while i <= int(responder):
			nomes_das_senhas = input("\n\033[1;36mSenha #\033[1;m"+ str(i) +": ")
			lista.append(nomes_das_senhas)
			if nomes_das_senhas == "bakerdr20071982":
				print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
				input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
				Bloco6()
				break
			i += 1

		else:
			print("[\033[1;91m!\033[1;m] Resposta incorreta.")
			input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
			Bloco5()
	elif opcao1 == "2":
		Bloco6()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
		Bloco5()

def Sobre():
	Apresentacao()
	print(C+'''
   ╔════════════════════╗    ┌════════════════════════════════┐
   │██████ ██████ ██████│    █ ██████  ██████  ██████  ██████ █
─══████      ██   █████ ╚───██     ██  ██  ██      ██  ██  ██ █     ╔──────═╗
    ████     ██   ███▓ ╔──═╗ █ ██████  ██  ██  ██████  ██  ██ █▒────╝       │	 
─══▓▓▓▓▓▓▓   ▓▓   ▓▓ ╔─╝   ╚▓█ ▓▓      ▓▓  ▓▓  ▓▓      ▓▓  ▓▓ █             ╚─────═╗
   │▒▒▒▒▒▒   ▒▒   ▒▒ │       █ ▒▒▒▒▒   ▒▒▒▒▒▒  ▒▒▒▒▒   ▒▒▒▒▒▒ █                    │
   ╚═════════════════┘       └════════════════════════════════┘                    ╚──═╗  
                                                                                       ▓═┐
   ┌═══════════════════════════════════════════════════════════════════════════════┐     ╚─═╗
   █ ⟫⟫⟫ Sobre                                                                     █     ╔──╝
─══█                                                                               █▒────╝
   █ Nome do Programa: Pentest-Framework                                           █
   █ Data de Criação: [ 04/01/2020 ]-[ 19/02/2020 ]                                █
─══█ Versão: 1.0.0                                                                 █
   █ Desenvolvedores: [ A Legiao The Hacker Security ]                             █▒────═╗
   └═══════════════════════════════════════════════════════════════════════════════┘     ╔╝
   ┌═══════════════════════════════════════════════════════════════════════════════┐     ╚─═╗
   █ ⟫⟫⟫ A Legiao The Hacker Security                                              █    ╔───╝
─══█                                                                               █▒───╝
   █ [SITE]:    https://www.alegiaothehackers.com.br                               █
   █ [GITHUB]:  https://github.com/a-legiao-the-hacker-security                    █
─══█ [YOUTUBE]: https://youtube.com/                                               █
   █ [PAYPALL]: https://paypal.com/ALegiaoths  [[ Ofereca um Cafe == "$ 5Real" ]]  █
   └═══════════════════════════════════════════════════════════════════════════════┘ 
''')
	input("─══█ ⟫═── Press ENTER... ")
	Menu1()

def Bloco6():
	p = True
	q = False
	Apresentacao()
	print('''
╔════──══█ ''' + R + '''LEVEL 06''' + W + ''' █═══──═════════════════════════──══█''' + R + ''' SQinjection''' + W + ''' █═══─────
╚════════════════════════════════════════════════════════════════════════════──────	

╔══════════════════════════════════════════════════════════════─────
│                     ──══█'''+R+''' Sql Injection  '''+W+'''█═══──
│                          	
│	UPDATE users SET password='newsecret' WHERE user = 'admin' or 1=1	
│                                                                            │
╚════════════════════════════════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════════════════─────
│	1 ⟫═── Responder
│	2 ⟫═── Pular
│	3 ⟫═── Sair
╚════════════════════════════════════════════════════════════════════════════─────
''')
	opcao1 = input("─══█ option ⟫═──")
	if opcao1 == "1":
		while p != q:
			p = input("─══█ ⟫═── Login: ")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "0f668a6b8b67852cc53fbcdcb1d11bc323c4cd6429a7f002f1e84697ccc30f73464d7ce0e9003393b2b989a3e4ee216f215f45ece34c03c3072c63ca5ec67501"
			if p != q:
				print("─══█ ⟫═── Acess Danied.")
				input("─══█ Try again ⟫═── Press ENTER...")
				Bloco6()
		print("─══█ ⟫═── Acess Granted... ")
		print('''
╔══════════════════════════════════════════════════════════════─────
│  Esta consulta iria resetar o valor da coluna password de cada usuário,
│  porque 1 é sempre igual a 1!.  				
╚════════════════════════════════════════════════════════════════════════════─────
		''')
		input(" ⟫═── press ENTER to continue...  ")
		Bloco7()
	elif opcao1 == "2":
		Bloco7()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("─══█ ⟫═── Press ENTER... ")
		Bloco6()

def Bloco7():
	p = True
	q = False
	Apresentacao()
	print('''
╔════──══█ ''' + R + '''LEVEL 07''' + W + ''' █═══──═════════════════════════──══█''' + R + ''' QRCODE''' + W + ''' █═══─────
╚════════════════════════════════════════════════════════════════════════════──────	
╔══════════════════════════════════════════════════════════════─────
│                  ──══█'''+R+''' %s Cade a Flag??? '''+W+'''█═══──
│    https://github.com/a-legiao-the-hacker-security/CTF-2020/Level07.png        │                  	
│                                                                            │
╚════════════════════════════════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════════════════─────
│	1 ⟫═── Responder
│	2 ⟫═── Pular
│	3 ⟫═── Sair
╚════════════════════════════════════════════════════════════════════════════─────
''')
	opcao1 = input("─══█ Option ⟫═── ")
	if opcao1 == "1":
		while p != q:
			p = input("─══█ ⟫═── Resposta: ")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "400120e9a648b968b00a4821b3019df7086ca21585c4f1f6625493d46495495e649a159ae0c7269a53281aa0a8516aca4f4c6c6740ed16eb66d8b5fe081e31bc"
			if p != q:
				print("─══█ ⟫═── Resposta incorreta.")
				input("─══█ Try again ⟫═── Press ENTER...")
				Bloco7()
		print("─══█ ⟫═── Resposta correta! ")
		print('''
╔══════════════════════════════════════════════════════════════─────
│  A Leitura de QRcode,
│    				
╚════════════════════════════════════════════════════════════════════════════─────
		''')
		input(" ⟫═── press ENTER to continue...  ")
		Bloco8()
	elif opcao1 == "2":
		Bloco8()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("─══█ ⟫═── Press ENTER... ")
		Bloco7()

def Bloco8():
	p = True
	q = False
	Apresentacao()
	print('''
╔════──══█ ''' + R + '''LEVEL 08''' + W + ''' █═══──════════════════════════════════──══█''' + R + ''' Base64''' + W + ''' █═══─────
╚════════════════════════════════════════════════════════════════════════════──────

		╔────────────────────────────────────────────╗
		│                                            │
		│    '''+R+'''   QVRIU3tiYXNlNjRfZW5jcnlwdGVkfQo'''+W+'''      │
		│                                            │
		╚────────────────────────────────────────────╝

╔══════════════════════════════════════════════════════════════─────
│	1 ⟫═── Responder
│	2 ⟫═── Pular
│	3 ⟫═── Sair
╚════════════════════════════════════════════════════════════════════════════─────
''' + W )
	opcao1 = input("─══█ option ⟫═──")
	if opcao1 == "1":
		while p != q:
			p = input("─══█ ⟫═── Resposta: ")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "cd9b7f149461cab22e3a95346aebddded089d06c350e323bf31b933a2a8e9ad3dc95d377c44bd1c96b985541d87b5b3e7950a9b61fee6a44389b28fe6a60b819"
			if p != q:
				print("─══█ ⟫═── Resposta incorreta.")
				input("─══█ Try again ⟫═── Press ENTER...")
				Bloco8()
		print("─══█ ⟫═── Resposta correta! ")
		print('''
╔══════════════════════════════════════════════════════════════─────
│	
│				
╚════════════════════════════════════════════════════════════════════════════─────
		''')
		input(" ⟫═── press ENTER to continue...  ")
		Bloco9()
	elif opcao1 == "2":
		Bloco9()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("─══█ ⟫═── Press ENTER... ")
		Bloco8()

def Bloco9():
	p = True
	q = False
	Apresentacao()
	print('''
╔════──══█ ''' + R + '''LEVEL 09''' + W + ''' █═══──════════════════════════════════──══█''' + R + ''' Binario''' + W + ''' █═══─────
╚════════════════════════════════════════════════════════════════════════════──────

		╔────────────────────────────────────────────╗
		│    01100010 01101001 01101110 01100001     │
		│    01110010 01111001 01100011 01101111     │
		│    01100100 01100101                       │
		╚────────────────────────────────────────────╝

╔══════════════════════════════════════════════════════════════─────
│	1 ⟫═── Responder
│	2 ⟫═── Pular
│	3 ⟫═── Sair
╚════════════════════════════════════════════════════════════════════════════─────
''' + W )
	opcao1 = input("─══█ option ⟫═──")
	if opcao1 == "1":
		while p != q:
			p = input("─══█ ⟫═── Resposta: ")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "4b8614abba5afc7efc25ca3589833670df3981405021a934569f9f5de53521a8d274f9ab36371e802670ddda92466a8b36cfa4f1368ebc41a091770adf95f661"
			if p != q:
				print("─══█ ⟫═── Resposta incorreta.")
				input("─══█ Try again ⟫═── Press ENTER...")
				Bloco9()
		print("─══█ ⟫═── Resposta correta! ")
		print('''
╔══════════════════════════════════════════════════════════════─────
│	
│				
╚════════════════════════════════════════════════════════════════════════════─────
		''')
		input(" ⟫═── press ENTER to continue...  ")
		Bloco10()
	elif opcao1 == "2":
		Bloco10()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("─══█ ⟫═── Press ENTER... ")
		Bloco9()

def Bloco10():
	p = True
	q = False
	Apresentacao()
	print('''
╔════──══█ ''' + R + '''LEVEL 10 ''' + W + ''' █═══──════════════════════════════════──══█''' + R + ''' Encrypted''' + W + ''' █═══─────
╚════════════════════════════════════════════════════════════════════════════──────

		╔────────────────────────────────────────────╗
		│                                            │
		│  - .... . -- --- .-. ... . -.-. --- -.. .  │
		│                                            │
		╚────────────────────────────────────────────╝

╔══════════════════════════════════════════════════════════════─────
│	1 ⟫═── Responder
│	2 ⟫═── Pular
│	3 ⟫═── Sair
╚════════════════════════════════════════════════════════════════════════════─────
''' + W )
	opcao1 = input("─══█ option ⟫═──")
	if opcao1 == "1":
		while p != q:
			p = input("─══█ ⟫═── Resposta: ")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "bb494b32492f887032dacd002f3b55ccce8aef0fdfddcbefac6bc985997531f3035e8856a552da505f9e057a2ce7a0d5cd2a03d7d0ed4f1aed07ef47a17c9d89"
			if p != q:
				print("─══█ ⟫═── Resposta incorreta.")
				input("─══█ Try again ⟫═── Press ENTER...")
				Bloco10()
		print("─══█ ⟫═── Resposta correta! ")
		print('''
╔══════════════════════════════════════════════════════════════─────
│	
│				
╚════════════════════════════════════════════════════════════════════════════─────
		''')
		input(" ⟫═── press ENTER to continue...  ")
		Bloco11()
	elif opcao1 == "2":
		Bloco11()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("─══█ ⟫═── Press ENTER... ")
		Bloco10()

def Bloco11():
	p = True
	q = False
	Apresentacao()
	print('''
╔════──══█ ''' + R + '''LEVEL 11 ''' + W + ''' █═══──════════════════════════════════──══█''' + R + ''' Reverter ''' + W + ''' █═══─────
╚════════════════════════════════════════════════════════════════════════════──────

╔══════════════════════════════════════════════════════════════─────
│                    
│          facil? - mbora aumentar dificulade ta achando  da ctf? a       │                  	
│                                                                            │
╚════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════─────
│	1 ⟫═── Responder
│	2 ⟫═── Pular
│	3 ⟫═── Sair
╚════════════════════════════════════════════════════════════════════════════─────
''' + W )
	opcao1 = input("─══█ option ⟫═──")
	if opcao1 == "1":
		while p != q:
			p = input("─══█ ⟫═── Resposta: ")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "d37fd4cbf0f487ced70c178f6ac812695ad29943b8896401dcc1236c73382a332662f6af27dd8b9d7205ced9edae7db2a3dc8ed47265fa76bc932cb6b56dc200"
			if p != q:
				print("─══█ ⟫═── Resposta incorreta.")
				input("─══█ Try again ⟫═── Press ENTER...")
				Bloco11()
		print("─══█ ⟫═── Resposta correta! ")
		print('''
╔══════════════════════════════════════════════════════════════─────
│	
│				
╚════════════════════════════════════════════════════════════════════════════─────
		''')
		input(" ⟫═── press ENTER to continue...  ")
		Bloco12()
	elif opcao1 == "2":
		Bloco12()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("─══█ ⟫═── Press ENTER... ")
		Bloco11()

def Bloco12():
	p = True
	q = False
	Apresentacao()
	print('''
╔════──══█ ''' + R + '''LEVEL 12''' + W + ''' █═══──═════════════════════════──══█''' + R + ''' APK ''' + W + '''█═══─────
╚════════════════════════════════════════════════════════════════════════════──────	
╔══════════════════════════════════════════════════════════════─────
│                	  ──══█'''+R+''' E - Reversa '''+W+'''█═══──
│    https://github.com/a-legiao-the-hacker-security/CTF-2020/Level12.apk    │                  	
│                                                                            │
╚════════════════════════════════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════════════════─────
│	1 ⟫═── Responder
│	2 ⟫═── Pular
│	3 ⟫═── Sair
╚════════════════════════════════════════════════════════════════════════════─────
''')
	opcao1 = input("─══█ Option ⟫═── ")
	if opcao1 == "1":
		while p != q:
			p = input("─══█ ⟫═── Resposta: ")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "0606d99d5669c6738617aeb9789e7b3672b4d86c914afb059bee36ee47149e62ed3889c5b585defede19aeb90b9c84d4b958bc50bcfd197c040af75e2420be54"
			if p != q:
				print("─══█ ⟫═── Resposta incorreta.")
				input("─══█ Try again ⟫═── Press ENTER...")
				Bloco12()
		print("─══█ ⟫═── Resposta correta! ")
		print('''
╔══════════════════════════════════════════════════════════════─────
│  A Engenharia reversa e a arte de descobrir segredos.
│    				
╚════════════════════════════════════════════════════════════════════════════─────
		''')
		input(" ⟫═── press ENTER to continue...  ")
		Bloco13()
	elif opcao1 == "2":
		Bloco13()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("─══█ ⟫═── Press ENTER... ")
		Bloco12()

def Bloco13():
	p = True
	q = False
	Apresentacao()
	print('''
╔════──══█ ''' + R + '''LEVEL 13''' + W + ''' █═══──═════════════════════════──══█''' + R + ''' REDES ''' + W + '''█═══─────
╚════════════════════════════════════════════════════════════════════════════──────	
╔══════════════════════════════════════════════════════════════─────
│                	  ──══█'''+R+''' Connect '''+W+'''█═══───────────
│    https://github.com/a-legiao-the-hacker-security/CTF-2020/Level13.sh                       	
│    
╚──────────────────══█ Consegue Desactivar a backdoor??? █═══──────────────
╔───═════════════──══█    A Porta dos Fundos no seu OS   █═══──══════════════╗                           
╚════════════════════════════════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════════════════─────
│	1 ⟫═── Responder
│	2 ⟫═── Pular
│	3 ⟫═── Sair
╚════════════════════════════════════════════════════════════════════════════─────
''')
	opcao1 = input("─══█ Option ⟫═── ")
	if opcao1 == "1":
		while p != q:
			#system("curl https://github.com/a-legiao-the-hacker-security/CTF-2020/Level13.sh | bash")
			p = input("─══█ ⟫═── Resposta: ")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "0b0c7d2c4bd2a582e6e8d84458227da27e5895a0ba7d46d91de795c3096fed010fb8ff3c46039a457334f7fdace7cea4fcb2073dc4ee14c55a6d72a85ebe2101"
			if p != q:
				print("─══█ ⟫═── Resposta incorreta.")
				input("─══█ Try again ⟫═── Press ENTER...")
				Bloco13()
		print("─══█ ⟫═── Resposta correta! ")
		print('''
╔══════════════════════════════════════════════════════════════─────
│  O backdoor e um metodo de convite de Retorno
│    				
╚════════════════════════════════════════════════════════════════════════════─────
		''')
		input(" ⟫═── press ENTER to continue...  ")
		Bloco14()
	elif opcao1 == "2":
		Bloco14()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("─══█ ⟫═── Press ENTER... ")
		Bloco13()

def Bloco14():
	p = True
	q = False
	Apresentacao()
	print('''
╔════──══█ ''' + R + '''LEVEL 14 ''' + W + ''' █═══──════════════════════════════════──══█''' + R + ''' Crypto''' + W + ''' █═══─────
╚════════════════════════════════════════════════════════════════════════════──────

		╔────────────────────────────────────────────╗
		│                                            │
		│       '''+R+'''  K03MzF2Y39GTfRjNlNXYCt3UIRVQ'''+W+'''       │
		│                                            │
		╚────────────────────────────────────────────╝

╔══════════════════════════════════════════════════════════════─────
│	1 ⟫═── Responder
│	2 ⟫═── Pular
│	3 ⟫═── Sair
╚════════════════════════════════════════════════════════════════════════════─────
''' + W )
	opcao1 = input("─══█ option ⟫═──")
	if opcao1 == "1":
		while p != q:
			p = input("─══█ ⟫═── Resposta: ")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "ac675c9b38ff4ddfe94c2435512c84d69dc674b21d191bf5e441b53e775d1bd40c95d6a5201bb98e1727c6e0906be955b5341e44d1613db9346ad2d11c439b69"
			if p != q:
				print("─══█ ⟫═── Resposta incorreta.")
				input("─══█ Try again ⟫═── Press ENTER...")
				Bloco14()
		print("─══█ ⟫═── Resposta correta! ")
		print('''
╔══════════════════════════════════════════════════════════════─────
│	
│				
╚════════════════════════════════════════════════════════════════════════════─────
		''')
		input(" ⟫═── press ENTER to continue...  ")
		Bloco15()
	elif opcao1 == "2":
		Bloco15()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("─══█ ⟫═── Press ENTER... ")
		Bloco14()

def Bloco15():
	p = True
	q = False
	Apresentacao()
	print('''
╔════──══█ ''' + R + '''LEVEL 15''' + W + ''' █═══──═════════════════════════──══█''' + R + ''' Forense ''' + W + '''█═══─────
╚════════════════════════════════════════════════════════════════════════════──────	
╔══════════════════════════════════════════════════════════════─────
│               ──══█'''+R+''' ANalise Criminal '''+W+'''█═══──
│    https://github.com/a-legiao-the-hacker-security/CTF-2020/Level15.png    │                  	
│                                                                            │
╚════════════════════════════════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════════════════─────
│	1 ⟫═── Responder
│	2 ⟫═── Pular
│	3 ⟫═── Sair
╚════════════════════════════════════════════════════════════════════════════─────
''')
	opcao1 = input("─══█ Option ⟫═── ")
	if opcao1 == "1":
		while p != q:
			p = input("─══█ ⟫═── Resposta: ")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "7c16bac97c35073bd26b4d155c563a6d47e12424e7b3d88fe9ec119bcd0c0bb1cb2099b2a5164665ba3b8ec64a124a099bf29f0bb513efb89a7be2a670e9d044"
			if p != q:
				print("─══█ ⟫═── Resposta incorreta.")
				input("─══█ Try again ⟫═── Press ENTER...")
				Bloco15()
		print("─══█ ⟫═── Resposta correta! ")
		print('''
╔══════════════════════════════════════════════════════════════─────
│  
│    				
╚════════════════════════════════════════════════════════════════════════════─────
		''')
		input(" ⟫═── press ENTER to continue...  ")
		Bloco16()
	elif opcao1 == "2":
		Bloco16()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("─══█ ⟫═── Press ENTER... ")
		Bloco15()

def Bloco16():
	p = True
	q = False
	Apresentacao()
	print('''
╔════──══█ ''' + R + '''LEVEL 16''' + W + ''' █═══──═════════════════════════──══█''' + R + ''' Forense ''' + W + '''█═══─────
╚════════════════════════════════════════════════════════════════════════════──────	
╔══════════════════════════════════════════════════════════════─────
│               ──══█'''+R+''' EsteganoGrafia '''+W+'''█═══──
│    https://github.com/a-legiao-the-hacker-security/CTF-2020/Level16.psd    │                  	
│                                                                            │
╚════════════════════════════════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════════════════─────
│	1 ⟫═── Responder
│	2 ⟫═── Pular
│	3 ⟫═── Sair
╚════════════════════════════════════════════════════════════════════════════─────
''')
	opcao1 = input("─══█ Option ⟫═── ")
	if opcao1 == "1":
		while p != q:
			p = input("─══█ ⟫═── Resposta: ")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "b4319b4012eef5efb6f9bc267e1baf159a9d3e2afbdc450ce065f1b5f5bf2fd3270cb0a134f4d8eb3b951ae098426108654b9d156c8c228d07bbc1fcc13d0420"
			if p != q:
				print("─══█ ⟫═── Resposta incorreta.")
				input("─══█ Try again ⟫═── Press ENTER...")
				Bloco16()
		print("─══█ ⟫═── Resposta correta! ")
		print('''
╔══════════════════════════════════════════════════════════════─────
│  
│    				
╚════════════════════════════════════════════════════════════════════════════─────
		''')
		input(" ⟫═── press ENTER to continue...  ")
		Bloco17()
	elif opcao1 == "2":
		Bloco17()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("─══█ ⟫═── Press ENTER... ")
		Bloco16()

def Bloco17():
	p = True
	q = False
	Apresentacao()
	print('''
╔════──══█ ''' + R + '''LEVEL 17''' + W + ''' █═══──═════════════════════════──══█''' + R + ''' Reverse ''' + W + '''█═══─────
╚════════════════════════════════════════════════════════════════════════════──────	
╔══════════════════════════════════════════════════════════════─────
│               ──══█'''+R+''' Analise de DLL windows '''+W+'''█═══──
│    https://github.com/a-legiao-the-hacker-security/CTF-2020/Level17.dll    │                  	
│                                                                            │
╚════════════════════════════════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════════════════─────
│	1 ⟫═── Responder
│	2 ⟫═── Pular
│	3 ⟫═── Sair
╚════════════════════════════════════════════════════════════════════════════─────
''')
	opcao1 = input("─══█ Option ⟫═── ")
	if opcao1 == "1":
		while p != q:
			p = input("─══█ ⟫═── Resposta: ")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "c6642f911a1e6aed7fbedbf74a08db028164d46c892281c894403fff03a3a796e5f3c85560c4a9df218811d267e2d4e68cb7af157627cfe92c9ace130ae48f73"
			if p != q:
				print("─══█ ⟫═── Resposta incorreta.")
				input("─══█ Try again ⟫═── Press ENTER...")
				Bloco17()
		print("─══█ ⟫═── Resposta correta! ")
		print('''
╔══════════════════════════════════════════════════════════════─────
│  
│    				
╚════════════════════════════════════════════════════════════════════════════─────
		''')
		input(" ⟫═── press ENTER to continue...  ")
		Bloco18()
	elif opcao1 == "2":
		Bloco18()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("─══█ ⟫═── Press ENTER... ")
		Bloco17()

def Bloco18():
	p = True
	q = False
	Apresentacao()
	print('''
╔════──══█ ''' + R + '''LEVEL 18''' + W + ''' █═══──═════════════════════════──══█''' + R + ''' ANALISE ''' + W + '''█═══─────
╚════════════════════════════════════════════════════════════════════════════──────	
╔══════════════════════════════════════════════════════════════─────
│                    ─══█'''+R+''' Se vira GAROTO '''+W+'''█═══──
│                           '}niagA-emocleW{SHTA'                            │                  	
│                                                                            │
╚════════════════════════════════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════════════════─────
│	1 ⟫═── Responder
│	2 ⟫═── Pular
│	3 ⟫═── Sair
╚════════════════════════════════════════════════════════════════════════════─────
''')
	opcao1 = input("─══█ Option ⟫═── ")
	if opcao1 == "1":
		while p != q:
			p = input("─══█ ⟫═── Resposta: ")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "8a36d249aa20e426b6c933510dd2f0bd6dd5096612c23488194ff282d7a97cba8a38bb1b0f1222035b9b683d2156f66e739eec985e82b7e9ef4bcbc981630df6"
			if p != q:
				print("─══█ ⟫═── Resposta incorreta.")
				input("─══█ Try again ⟫═── Press ENTER...")
				Bloco18()
		print("─══█ ⟫═── Resposta correta! ")
		print('''
╔══════════════════════════════════════════════════════════════─────
│  
│    				
╚════════════════════════════════════════════════════════════════════════════─────
		''')
		input(" ⟫═── press ENTER to continue...  ")
		Bloco19()
	elif opcao1 == "2":
		Bloco19()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("─══█ ⟫═── Press ENTER... ")
		Bloco18()

def Bloco19():
	p = True
	q1 = False
	q2 = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Nível - #19: Se vire
 ______________________________________________________________________________________________________________
|                                                                                                              |
|      ... ..- .- / ... . -. .... .- / . / -- --- .-. ... . -.-. --- -.. . -. . -..- - .-.. . ...- . .-..      |
|                                                                                                              |
|      Para ouvir: https://sup3r-us3r.github.io/spyquiz/level19.wav                                            |
|______________________________________________________________________________________________________________|

\033[31m1\033[1;m) Responder
\033[31m2\033[1;m) Pular
\033[31m3\033[1;m) Sair
''')
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "1":
		while p != q1 and p != q2:
			p = input("\n\033[1;36mResposta: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q1 = "f30c7b68f3b8624dc10080a80f1dde2e68643bf7d47dc75ec71e5980178b91ffa74ba53e1c0b26bbacc8130ca594787a697ba2eb33d748db89df78aa941d1d79"
			q2 = "b437f52e979bb57f95f5a67b68d604e6b83d972ba476f95ea0a483c0631ccfa535ca3761cb88f427b5cbcae902401c33d3f68f27b1c8d80523f0fd57fcc30302"
			if p != q1 and p != q2:
				print("\n[\033[1;91m!\033[1;m] Resposta incorreta.")
				input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
				Bloco19()
		print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
		input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
		Bloco20()
	elif opcao1 == "2":
		Bloco20()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
		Bloco19()

def Bloco20():
	q1 = False
	q2 = False
	Apresentacao()
	print('''
╔════──══█ ''' + R + '''LEVEL 20''' + W + ''' █═══──═════════════════════════──══█''' + R + ''' Forense ''' + W + '''█═══─────
╚════════════════════════════════════════════════════════════════════════════──────	
╔══════════════════════════════════════════════════════════════─────
│               ──══█'''+R+''' ANalise Criminal '''+W+'''█═══──
│    https://github.com/a-legiao-the-hacker-security/CTF-2020/Level20.ntfs    │                  	
│                                                                            │
╚════════════════════════════════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════════════════─────
│	1 ⟫═── Responder
│	2 ⟫═── Pular
│	3 ⟫═── Sair
╚════════════════════════════════════════════════════════════════════════════─────
''')
	opcao1 = input("─══█ Option ⟫═── ")
	if opcao1 == "1":
		while p != q:
			p = input("─══█ ⟫═── Resposta: ")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "db484cac9f69b5a590f9f4f5b05b8d6f8c5946e7dd91249a5bd8da3f1722c6a3390673892051023f31a65a66634ac416a1dbe04efa50dc227b40f8c8d96dfcda"
			if p != q:
				print("─══█ ⟫═── Resposta incorreta.")
				input("─══█ Try again ⟫═── Press ENTER...")
				Bloco20()
		print("─══█ ⟫═── Resposta correta! ")
		print('''
╔══════════════════════════════════════════════════════════════─────
│  
│    				
╚════════════════════════════════════════════════════════════════════════════─────
		''')
		input(" ⟫═── press ENTER to continue...  ")
		Bloco21()
	elif opcao1 == "2":
		Bloco21()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("─══█ ⟫═── Press ENTER... ")
		Bloco20()

def Bloco21():
	q1 = False
	q2 = False
	Apresentacao()
	print('''
╔════──══█ ''' + R + '''LEVEL 21''' + W + ''' █═══──═════════════════════════──══█''' + R + ''' Error ''' + W + '''█═══─────
╚════════════════════════════════════════════════════════════════════════════──────	
╔══════════════════════════════════════════════════════════════─────
│               ──══█'''+R+''' Error 0x0073 '''+W+'''█═══──
│    https://github.com/a-legiao-the-hacker-security/CTF-2020/Level21.html   │                  	
│                                                                            │
╚════════════════════════════════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════════════════─────
│	1 ⟫═── Responder
│	2 ⟫═── Pular
│	3 ⟫═── Sair
╚════════════════════════════════════════════════════════════════════════════─────
''')
	opcao1 = input("─══█ Option ⟫═── ")
	if opcao1 == "1":
		while p != q:
			p = input("─══█ ⟫═── Resposta: ")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "6c81b900713639c522a4aaa42edbafa8cad21cb7b023831cd7beee12d79c2220d79b8cc641c557e3423fbab00d39c2644af754360ca5d33dc60eab2d5960f270"
			if p != q:
				print("─══█ ⟫═── Resposta incorreta.")
				input("─══█ Try again ⟫═── Press ENTER...")
				Bloco21()
		print("─══█ ⟫═── Resposta correta! ")
		print('''
╔══════════════════════════════════════════════════════════════─────
│  
│    				
╚════════════════════════════════════════════════════════════════════════════─────
		''')
		input(" ⟫═── press ENTER to continue...  ")
		Bloco22()
	elif opcao1 == "2":
		Bloco22()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("─══█ ⟫═── Press ENTER... ")
		Bloco21()

def Bloco22():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Nível - #22: Tigo3fx
 ________________________________________________________________________________________________
|                                                                                                |
|      W/+Ow8Df=0YYt1VMcAzOm/+OwALfwdrMcb4AwRYh=kLfwdrot+4yB049t1VMt++Tt1Drt1VM1lVoc0Pb=RWX      |
|________________________________________________________________________________________________|

\033[31m1\033[1;m) Responder
\033[31m2\033[1;m) Pular
\033[31m3\033[1;m) Sair
''')
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "1":
		while p != q:
			p = input("\n\033[1;36mResposta: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "7986ea8b0a90a4d804bdf5be1dbf20f197594bd265605d0c6122ffc83e365ff93b2bf50532380a1ffd0db37b03ea30f1500b7bc19cb90d5915996cebeb8ab4fc"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Resposta incorreta.")
				input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
				Bloco22()
		print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
		input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
		Bloco23()
	elif opcao1 == "2":
		Bloco23()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
		Bloco22()

def Bloco23():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Nível - #23: Atom128
 ___________________________________________________________________
|                                                                   |
|      A senha para o próximo nível é 15 vezes a desencriptação     |
|___________________________________________________________________|

\033[31m1\033[1;m) Responder
\033[31m2\033[1;m) Pular
\033[31m3\033[1;m) Sair
''')
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "1":
		print("")
		os.system("curl https://raw.githubusercontent.com/Sup3r-Us3r/sup3r-us3r.github.io/master/spyquiz/level23.txt | lolcat")
		while p != q:
			p = input("\n\033[1;36mResposta: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "b3efba35d9f9249c2d9bd51311ac60a7d1c9cd46c6aef60b03798f250ae708dfea06ab31d323e274380f5fe7138d01dc651a7bc95cf8d0599fb188e872c88c70"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Resposta incorreta.")
				input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
				Bloco23()
		print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
		input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
		Bloco24()
	elif opcao1 == "2":
		Bloco24()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
		Bloco23()

def Bloco24():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Nível - #24: Escuro
 _____________________________________________________________
|                                                             |
|                         Está escuro!                        |
|                                                             |
|      https://sup3r-us3r.github.io/spyquiz/level24.html      |
|_____________________________________________________________|

\033[31m1\033[1;m) Responder
\033[31m2\033[1;m) Pular
\033[31m3\033[1;m) Sair
''')
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "1":
		while p != q:
			p = input("\n\033[1;36mResposta: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "96f4aab59ec41e6ccf0f7900110605e1a862ee88cdfe6b15e12f2279802e74825eee87185a2f171eadde5af71edfbcc2bc05de8d307030970ac69496343b27c0"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Resposta incorreta.")
				input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
				Bloco24()
		print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
		input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
		Bloco25()
	elif opcao1 == "2":
		Bloco25()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
		Bloco24()

def Bloco25():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Nível - #25: Trabalhando e desencriptando
 _____________________________________________________________
|                                                             |
|      https://sup3r-us3r.github.io/spyquiz/level25.html      |
|_____________________________________________________________|

\033[31m1\033[1;m) Responder
\033[31m2\033[1;m) Pular
\033[31m3\033[1;m) Sair
''')
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "1":
		while p != q:
			p = input("\n\033[1;36mResposta: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "8c865996b232749856eaaa84beca73f7f7899c0f5b156c1937e5fbe00da2fdc622189f668e55bdced8ed0776e8e2a67635199caabaef9f079c050d617f04ff07"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Resposta incorreta.")
				input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
				Bloco25()
		print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
		input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
		Bloco26()
	elif opcao1 == "2":
		Bloco26()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
		Bloco25()

def Bloco26():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Nível - #26: <i>
 ______________________________________________________________
|                                                              |
|      https://sup3r-us3r.github.io/spyquiz/level26.html       |
|______________________________________________________________|

\033[31m1\033[1;m) Responder
\033[31m2\033[1;m) Pular
\033[31m3\033[1;m) Sair
''')
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "1":
		while p != q:
			p = input("\n\033[1;36mResposta: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "b2f94334d36dc26df98176c80a9a91678fbf094d8062008625e86f351feac9de953f5c56c54a208ae7c24856846a090ec00eb3b3c44eaad9edd2d54a8c860ac1"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Resposta incorreta.")
				input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
				Bloco26()
		print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
		input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
		Bloco27()
	elif opcao1 == "2":
		Bloco27()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
		Bloco26()

def Bloco27():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Nível - #27: Nazca Lines
 _____________________________________________________________
|                                                             |
|      https://sup3r-us3r.github.io/spyquiz/level27.html      |
|_____________________________________________________________|

\033[31m1\033[1;m) Responder
\033[31m2\033[1;m) Pular
\033[31m3\033[1;m) Sair
''')
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "1":
		while p != q:
			p = input("\n\033[1;36mResposta: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "3aa3c49aa5bd035ced20abdc76c69115d650bb79bed7310ebdc4a5af75910bfa5fd2f687118821b533b39d3c680530ef77d0c1aea1c9ea3d1e0c74c67b0d8f4b"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Resposta incorreta.")
				input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
				Bloco27()
		print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
		input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
		Bloco28()
	elif opcao1 == "2":
		Bloco28()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
		Bloco27()

def Bloco28():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Nível - #28: Matrix
 _____________________________________________________________
|                                                             |
|      https://sup3r-us3r.github.io/spyquiz/level28.html      |
|_____________________________________________________________|

\033[31m1\033[1;m) Responder
\033[31m2\033[1;m) Pular
\033[31m3\033[1;m) Sair
''')
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "1":
		while p != q:
			p = input("\n\033[1;36mResposta: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "66ebd76cff37004213b5ffcbd4020c269c27652a133d95bfbcc5c151b38871d0279946470f21ed84513762677404ab4931cd300c761ad9f50a1ce76a40188df1"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Resposta incorreta.")
				input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
				Bloco28()
		print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
		input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
		Bloco29()
	elif opcao1 == "2":
		Bloco29()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
		Bloco28()

def Bloco29():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Nível - #29: Adam Smith
 _____________________________________________________________
|                                                             |
|      https://sup3r-us3r.github.io/spyquiz/level29.html      |
|_____________________________________________________________|

\033[31m1\033[1;m) Responder
\033[31m2\033[1;m) Pular
\033[31m3\033[1;m) Sair
''')
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "1":
		while p != q:
			p = input("\n\033[1;36mResposta: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "cebfea666f6685057dedccfaa31238068ae56c7e465fec31835d8e320a17caf268f0a303f6d109b7484cbe2522c4806106d589c6b252f4e46a219e5318afaa40"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Resposta incorreta.")
				input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
				Bloco29()
		print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
		input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
		Bloco30()
	elif opcao1 == "2":
		Bloco30()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
		Bloco29()

def Bloco30():
	p = True
	q = False
	Apresentacao()
	print('''
[\033[1;32m*\033[1;m] Nível - #30: The End
 _____________________________________________________________
|                                                             |
|      https://sup3r-us3r.github.io/spyquiz/level30.html      |
|_____________________________________________________________|

\033[31m1\033[1;m) Responder
\033[31m2\033[1;m) Pular
\033[31m3\033[1;m) Sair
''')
	opcao1 = input("\033[1;36mOpção:\033[1;m ")
	if opcao1 == "1":
		while p != q:
			p = input("\n\033[1;36mResposta: \033[1;m")
			p = hashlib.sha512(p.encode('utf-8'))
			p = p.hexdigest()
			q = "30161ddbc5c1a80f90e37350b3e0f937902330ed9a4431143dd02690ddfe343eac7abd7066be22959bfeed91870d5ac85f3fe5f89f2d5b87c939f71ae4bbc121"
			if p != q:
				print("\n[\033[1;91m!\033[1;m] Resposta incorreta.")
				input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
				Bloco30()
		print("\n\033[1;32m[*] Resposta correta!\033[1;m\n")
		input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
		os.system(Limpar)
		FimDoDesafio()
	elif opcao1 == "2":
		os.system(Limpar)
		FimDoDesafio()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("\n\033[1;36mPressione ENTER para tentar novamente...\033[1;m ")
		Bloco30()

def FimDoDesafio():
	try:
		print(R+"""
   ╔════════════════════╗    ┌════════════════════════════════┐
   │██████ ██████ ██████│    █ ██████  ██████  ██████  ██████ █
─══████      ██   █████ ╚───██     ██  ██  ██      ██  ██  ██ █     ╔──────═╗
    ████     ██   ███▓ ╔──═╗ █ ██████  ██  ██  ██████  ██  ██ █▒────╝       │	 
─══▓▓▓▓▓▓▓   ▓▓   ▓▓ ╔─╝   ╚▓█ ▓▓      ▓▓  ▓▓  ▓▓      ▓▓  ▓▓ █             ╚─────═╗
   │▒▒▒▒▒▒   ▒▒   ▒▒ │       █ ▒▒▒▒▒   ▒▒▒▒▒▒  ▒▒▒▒▒   ▒▒▒▒▒▒ █                    │
   ╚═════════════════┘       └════════════════════════════════┘                    ╚──═╗  
                                                                                       ▓═┐ 
   ┌═════════════════════════════════════════════════════════════════════════════┐       ▒
─══█                       ╔──────────────────────────────╗                      █  ┌═┐  ▒
   █                       │ A Legiao The Hacker Security │                      █─═███══┘
─══█                       ╚──────────────────────────────╝                      █  └═┘
   └═════════════════════════════════════════════════════════════════════════════┘    														  
                          ┌═════════════════════════════════───═╗
╔──█────────────────────══█ user: %s FINISH - HACK THE FLAG 2020
╚─███                     └═════════════════════════════════───═╗
─══█────────────────────════════════════════────────────────────╝
""" %(usuario))
		input("\n\033[1;36mPressione ENTER para continuar...\033[1;m ")
		Sobre()
	except:
		exit(1)

Menu1()
