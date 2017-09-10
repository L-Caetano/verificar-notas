#coding: UTF-8

def instalar_biblioteca(biblioteca):
    import importlib
    try:
        importlib.import_module(biblioteca)
    except ImportError:
        import pip
        pip.main(['install', biblioteca])
    finally:
        globals()[biblioteca] = importlib.import_module(biblioteca)

instalar_biblioteca('robobrowser')
instalar_biblioteca('bs4')

import os
import re
import bs4
import getpass
from robobrowser import RoboBrowser

os.system('cls' if os.name == 'nt' else 'clear')

br = RoboBrowser()
username = str(input("Digite os 2 últimos números do seu login (matrícula): 2017112760"))

os.system('cls' if os.name == 'nt' else 'clear')

password = getpass.getpass("Digite a sua senha (ela ficará invisível): ")
url = 'https://portal.ufsm.br/aluno/index.html'
br.open(url)
form = br.get_form()
form['j_username'] = '2017112760%s' % username
form['j_password'] = password
br.submit_form(form)
if br.url == "https://portal.ufsm.br/aluno/turmas/j_security_check":
    print ("Login e/ou senha estão errados!")
    input("\nPressione ENTER para fechar!")
    exit()
    
os.system('cls' if os.name == 'nt' else 'clear')      
    
print ("| 1 - Algoritmos  | 2 - Artes -  | 3 - Ed. Física             |")
print ("| 4 - Filosofia   | 5 - Física   | 6 - Fundamentos / Hardware |")
print ("| 7 - Geografia   | 8 - Inglês   | 9 - Português              |")
print ("| 10 - Matemática | 11 - Química | 12 - Redes de computadores |")
print ("| 13 - Sociologia |\n")
escolha = int(input("Digite a matéria desejada: "))

os.system('cls' if os.name == 'nt' else 'clear')
if escolha == 1:
    urlNota = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070454"
    print ("=========== ALGORITMOS ===========")

if escolha == 2:
    urlNota = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070452"
    print ("=========== ARTES ===========")

if escolha == 3:
    urlNota = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070451"
    print ("=========== ED. FÍSICA ===========")

if escolha == 4:
    urlNota = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070449"
    print ("=========== FILOSOFIA ===========")

if escolha == 5:
    urlNota = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070446"
    print ("=========== FÍSICA ===========")

if escolha == 6:
    urlNota = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070455"
    print ("=========== FUNDAMENTOS / HARDWARE ===========")

if escolha == 7:
    urlNota = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070450"
    print ("=========== GEOGRAFIA ===========")

if escolha == 8:
    urlNota = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070453"
    print ("=========== INGLÊS ===========")

if escolha == 9:
    urlNota = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070444"
    print ("=========== PORTUGUÊS ===========")

if escolha == 10:
    urlNota = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070447"
    print ("=========== MATEMÁTICA ===========")

if escolha == 11:
    urlNota = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070445"
    print ("=========== QUÍMICA ===========")

if escolha == 12:
    urlNota = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070456"
    print ("=========== REDES DE COMPUTADORES ===========")

if escolha == 13:
    urlNota = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070448"
    print ("=========== SOCIOLOGIA ===========")

br.open(urlNota)
codigo = str(br.parsed)   
notas2 = True
soup = bs4.BeautifulSoup (codigo)
totalPresencas = re.search(r'(class="icon-warning-sign ausente"></i> )(.*)', codigo)
totalFaltasID = re.search(r'(id=")(.*)(_label">Total de faltas</span>)', codigo)
totalFaltas = re.search(r'(%s" style="">)(.*)(</span>)' % (totalFaltasID.group (2)), codigo)
minPresencaID = re.search(r'(id=")(.*)(_label">Mínimo de presenças</span>)', codigo)
minPresencas = re.search(r'(%s" style="">)(.*)(</span>)' % (minPresencaID.group (2)), codigo)
cargaHorariaID = re.search(r'(id=")(.*)(_label">Carga horária</span>)', codigo)
cargaHoraria = re.search(r'(%s" style="">)(.*)(</span>)' % (cargaHorariaID.group (2)), codigo)

print ("\n=========== NOTAS ===========\n")
for nota in soup.findAll ('span', attrs={'style': ''}):
    notas = re.search (r'<span class="" style="">(.*?)</span', str (nota))
    if notas != None:
        if notas2 == True:
            print ("Nota 1: %s" % nota.text)
        if notas2 == False:
            print ("Nota 2: %s" % nota.text)
        notas2 = False
print ("\n=========== PRESENÇAS ===========\n")
print ("Carga horária: {}".format (cargaHoraria.group (2)))
print ("Mínimo de presenças: {}".format (minPresencas.group (2)))
print ("Total de presenças: {}".format (totalPresencas.group (2)))
print ("Total de faltas: {}".format (totalFaltas.group (2)))

input("\nPressione ENTER para fechar!")