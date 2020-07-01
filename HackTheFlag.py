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
	elif opcao1 == "6":
		exit()		
	elif opcao1 == "q":
		exit(1)
	else:
		ComandoNaoEncontrado()

		Menu1()

def Permissao():
	Apresentacao()
	os.system("ls | grep HackTheFlag.py ")
	sleep(3)
	print("\n Pronto, permissões aplicadas.")
	sleep(3)
	os.system("chmod +x HackTheFlag.py")
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
	elif opcao1 == "q":
		Menu1()
	else:
		ComandoNaoEncontrado()
		MudarPara()

def Instalacao():
	def ArchDerivados():
		print("⟫═── Instalando as dependencias...\n")
		sleep(3)
		os.system("sudo pacman -S --noconfirm sl curl lolcat")
		print("    ⟫═── Instalado com sucesso.")
		input("⟫═── Press " + R+ "q" +C+ " To Return")
		Menu1()
	def DebianDerivados():
		print("⟫═── Instalando as dependencias...\n")
		sleep(3)
		os.system("sudo apt install -y sl curl")
		print("")
		os.system("gem install lolcat")
		print("    ⟫═── Instalado com sucesso.")
		input("⟫═── Press " + R+ "q" +C+" To Return")
		Menu1()
	Apresentacao()
	print('''

  Option ⟫═── Escolha sua distribuição
╔══════════════════════════════════════════════════════════════─────
│	1 ⟫═── Debian & Derivados
│	2 ⟫═── Arch Linux & Derivados
│	3 ⟫═── Return
│	4 ⟫═── exit()
╚════════════════════════════════════════════════════════════════════════════─────
''')
	opcao1 = input("─══█ Option ⟫═──")
	if opcao1 == "1":
		DebianDerivados()
	elif opcao1 == "2":
		ArchDerivados()
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
			q = "60662b74c6a43cbb2f3d4826c3910ba8faf72717a2b9e12d8cdba1c741ca7fc09b5e48a1875ef2de88d3990c8afe4ecd50dd381993dead6aed7c061d4ac407ff"
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
	p = True
	q = False
	Apresentacao()
	print('''
╔════──══█ ''' + R + '''LEVEL 05''' + W + ''' █═══──═════════════════════════──══█''' + R + ''' WORDLIST''' + W + ''' █═══─────
╚════════════════════════════════════════════════════════════════════════════──────	
╔══════════════════════════════════════════════════════════════─────

 _________________________________________________
|                                                 |
|Robert D. Hack                                   |
|Namorada: Ketty                                  |
|Estilo de música: Eletronica                     |
|Cidade: Nova York                                |
|Nome da mãe: Marta                               |
|Nome do pai: Peterson                            |
|Coordenadas geográficas: 43,010354, -88,076145   |
|Telefone: 414-557-3179                           |
|Codigo da cidade: 55                	         |
|Data de nascimento: 20 de julho, 1982            |
|Idade: 39 anos                                   |
|Signo: Leão                                      |
|Endereço de e-mail: hackingnapratica@gmail.com   |
|Nome de usuário: CHEv10                          |
|MasterCard: 5151 6656 3798 1026                  |
|Vence em: 6/2020                                 |
|Nome do cachorro: paulinho                       |
|Empresa: Tec Solution                            |
|Ocupação: Hacking                                |
|Altura: 1,75                                     |
|Peso: 78 Kg                                      |
|Tipo sanguíneo: B+                               |
|Cor favorita: Verde                              |
|Veículo: Ninja H2R                               |
|_________________________________________________|
                 	
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
			q = "72b55c4b25245415fde7a75ae5b65425493613719fe843dfde750c09f51dc4057af5ea678a34b1c6668e63b26f020331f27ef6f946beaee996619551c62dd178"
			if p != q:
				print("─══█ ⟫═── Acess Danied.")
				input("─══█ Try again ⟫═── Press ENTER...")
				Bloco5()
		print("─══█ ⟫═── Acess Granted... ")
		print('''
╔══════════════════════════════════════════════════════════════─────
│  Esta consulta iria resetar o valor da coluna password de cada usuário,
│  porque 1 é sempre igual a 1!.  				
╚════════════════════════════════════════════════════════════════════════════─────
		''')
		input(" ⟫═── press ENTER to continue...  ")
		Bloco6()
	elif opcao1 == "2":
		Bloco6()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("─══█ ⟫═── Press ENTER... ")
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
   █ Nome do Programa: [ Hack The Flag ]                                           █
   █ Data de Criação: [ 27/5/2020 ]-[ 03/06/2020 ]                                █
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
│                          	
│    
╚──────────────────══█ Consegue desactivar a backdoor??? █═══──────────────
╔───═════════════──══█                                   █═══──══════════════╗                           
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
			system("curl https://github.com/a-legiao-the-hacker-security/CTF-2020/Level13.sh | bash")
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
		Bloco20()
	elif opcao1 == "2":
		Bloco20()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("─══█ ⟫═── Press ENTER... ")
		Bloco18()

def Bloco19():
	p = True
	q = False
	Apresentacao()
	print('''
╔════──══█ ''' + R + '''LEVEL 19''' + W + ''' █═══──═════════════════════════──══█''' + R + ''' ANALISE ''' + W + '''█═══─────
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
				Bloco19()
		print("─══█ ⟫═── Resposta correta! ")
		print('''
╔══════════════════════════════════════════════════════════════─────
│  
│    				
╚════════════════════════════════════════════════════════════════════════════─────
		''')
		input(" ⟫═── press ENTER to continue...  ")
		Bloco20()
	elif opcao1 == "2":
		Bloco20()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("─══█ ⟫═── Press ENTER... ")
		Bloco19()


def Bloco20():
	p = True
	q = False
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
		FimDoDesafio()
	elif opcao1 == "2":
		FimDoDesafio()
	elif opcao1 == "3":
		exit(1)
	else:
		ComandoNaoEncontrado()
		input("─══█ ⟫═── Press ENTER... ")
		Bloco20()

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
		input(" ⟫═── press ENTER to continue...  ")
	except:
		exit(1)

Menu1()
