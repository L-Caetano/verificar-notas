#coding: UTF-8
import os
import re
import bs4
from robobrowser import RoboBrowser
from time import sleep
username = str(input("Digite o seu login (matricula): "))
password = str(input("Digite a sua senha: "))
br = RoboBrowser()
notas2 = True
print ("1 - Algoritmos  | 2 - Artes -  | 3 - Ed. Física")
print ("4 - Filosofia   | 5 - Física   | 6 - Fundamentos / Hardware")
print ("7 - Geografia   | 8 - Inglês   | 9 - Português")
print ("10 - Matemática | 11 - Química | 12 - Redes de computadores")
print ("13 - Sociologia |")
escolha = int(input("Digite a matéria desejada: "))
os.system('cls' if os.name == 'nt' else 'clear')
if escolha == 1:
    url = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070454"
    br.open(url)
    form = br.get_form()
    form['j_username'] = username
    form['j_password'] = password
    br.submit_form(form)
    print (br.url)
    if br.url == "https://portal.ufsm.br/aluno/turmas/j_security_check":
        print ("Login e/ou senha estão errados!")
        input("\nPressione ENTER para fechar!")
        exit()
    src = str(br.parsed)
    soup = bs4.BeautifulSoup(src)
    print ("Algoritmos!")
    for nota in soup.findAll('span', attrs={'style': ''}):
        notas = re.search(r'<span class="" style="">(.*?)</span', str(nota))
        if notas != None:
            if notas2 == True:
                print ("Nota 1: %s" % nota.text)
            if notas2 == False:
                print ("Nota 2: %s" % nota.text)
            notas2 = False
if escolha == 2:
    url = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070452"
    br.open (url)
    form = br.get_form ()
    form['j_username'] = username
    form['j_password'] = password
    br.submit_form (form)
    if br.url == "https://portal.ufsm.br/aluno/turmas/j_security_check":
        print ("Login e/ou senha estão errados!")
        input("\nPressione ENTER para fechar!")
        exit()
    src = str (br.parsed)
    soup = bs4.BeautifulSoup (src)
    print ("Artes!")
    for nota in soup.findAll ('span', attrs={'style': ''}):
        notas = re.search (r'<span class="" style="">(.*?)</span', str (nota))
        if notas != None:
            if notas2 == True:
                print ("Nota 1: %s" % nota.text)
            if notas2 == False:
                print ("Nota 2: %s" % nota.text)
            notas2 = False
if escolha == 3:
    url = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070451"
    br.open (url)
    form = br.get_form ()
    form['j_username'] = username
    form['j_password'] = password
    br.submit_form (form)
    if br.url == "https://portal.ufsm.br/aluno/turmas/j_security_check":
        print ("Login e/ou senha estão errados!")
        input("\nPressione ENTER para fechar!")
        exit()
    src = str (br.parsed)
    soup = bs4.BeautifulSoup (src)
    print ("Educação física!")
    for nota in soup.findAll ('span', attrs={'style': ''}):
        notas = re.search (r'<span class="" style="">(.*?)</span', str (nota))
        if notas != None:
            if notas2 == True:
                print ("Nota 1: %s" % nota.text)
            if notas2 == False:
                print ("Nota 2: %s" % nota.text)
            notas2 = False
if escolha == 4:
    url = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070449"
    br.open (url)
    form = br.get_form ()
    form['j_username'] = username
    form['j_password'] = password
    br.submit_form (form)
    if br.url == "https://portal.ufsm.br/aluno/turmas/j_security_check":
        print ("Login e/ou senha estão errados!")
        input("\nPressione ENTER para fechar!")
        exit()
    src = str (br.parsed)
    soup = bs4.BeautifulSoup (src)
    print ("Filosofia!")
    for nota in soup.findAll ('span', attrs={'style': ''}):
        notas = re.search (r'<span class="" style="">(.*?)</span', str (nota))
        if notas != None:
            if notas2 == True:
                print ("Nota 1: %s" % nota.text)
            if notas2 == False:
                print ("Nota 2: %s" % nota.text)
            notas2 = False
if escolha == 5:
    url = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070446"
    br.open (url)
    form = br.get_form ()
    form['j_username'] = username
    form['j_password'] = password
    br.submit_form (form)
    if br.url == "https://portal.ufsm.br/aluno/turmas/j_security_check":
        print ("Login e/ou senha estão errados!")
        input("\nPressione ENTER para fechar!")
        exit()
    src = str (br.parsed)
    soup = bs4.BeautifulSoup (src)
    print ("Física!")
    for nota in soup.findAll ('span', attrs={'style': ''}):
        notas = re.search (r'<span class="" style="">(.*?)</span', str (nota))
        if notas != None:
            if notas2 == True:
                print ("Nota 1: %s" % nota.text)
            if notas2 == False:
                print ("Nota 2: %s" % nota.text)
            notas2 = False
if escolha == 6:
    url = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070455"
    br.open (url)
    form = br.get_form ()
    form['j_username'] = username
    form['j_password'] = password
    br.submit_form (form)
    if br.url == "https://portal.ufsm.br/aluno/turmas/j_security_check":
        print ("Login e/ou senha estão errados!")
        input("\nPressione ENTER para fechar!")
        exit()
    src = str (br.parsed)
    soup = bs4.BeautifulSoup (src)
    print ("Fundamentos / Hardware!")
    for nota in soup.findAll ('span', attrs={'style': ''}):
        notas = re.search (r'<span class="" style="">(.*?)</span', str (nota))
        if notas != None:
            if notas2 == True:
                print ("Nota 1: %s" % nota.text)
            if notas2 == False:
                print ("Nota 2: %s" % nota.text)
            notas2 = False
if escolha == 7:
    url = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070450"
    br.open (url)
    form = br.get_form ()
    form['j_username'] = username
    form['j_password'] = password
    br.submit_form (form)
    if br.url == "https://portal.ufsm.br/aluno/turmas/j_security_check":
        print ("Login e/ou senha estão errados!")
        input("\nPressione ENTER para fechar!")
        exit()
    src = str (br.parsed)
    soup = bs4.BeautifulSoup (src)
    print ("Geografia!")
    for nota in soup.findAll ('span', attrs={'style': ''}):
        notas = re.search (r'<span class="" style="">(.*?)</span', str (nota))
        if notas != None:
            if notas2 == True:
                print ("Nota 1: %s" % nota.text)
            if notas2 == False:
                print ("Nota 2: %s" % nota.text)
            notas2 = False
if escolha == 8:
    url = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070453"
    br.open (url)
    form = br.get_form ()
    form['j_username'] = username
    form['j_password'] = password
    br.submit_form (form)
    if br.url == "https://portal.ufsm.br/aluno/turmas/j_security_check":
        print ("Login e/ou senha estão errados!")
        input("\nPressione ENTER para fechar!")
        exit()
    src = str (br.parsed)
    soup = bs4.BeautifulSoup (src)
    print ("Inglês!")
    for nota in soup.findAll ('span', attrs={'style': ''}):
        notas = re.search (r'<span class="" style="">(.*?)</span', str (nota))
        if notas != None:
            if notas2 == True:
                print ("Nota 1: %s" % nota.text)
            if notas2 == False:
                print ("Nota 2: %s" % nota.text)
            notas2 = False
if escolha == 9:
    url = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070444"
    br.open (url)
    form = br.get_form ()
    form['j_username'] = username
    form['j_password'] = password
    br.submit_form (form)
    if br.url == "https://portal.ufsm.br/aluno/turmas/j_security_check":
        print ("Login e/ou senha estão errados!")
        input("\nPressione ENTER para fechar!")
        exit()
    src = str (br.parsed)
    soup = bs4.BeautifulSoup (src)
    print ("Português!")
    for nota in soup.findAll ('span', attrs={'style': ''}):
        notas = re.search (r'<span class="" style="">(.*?)</span', str (nota))
        if notas != None:
            if notas2 == True:
                print ("Nota 1: %s" % nota.text)
            if notas2 == False:
                print ("Nota 2: %s" % nota.text)
            notas2 = False
if escolha == 10:
    url = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070447"
    br.open (url)
    form = br.get_form ()
    form['j_username'] = username
    form['j_password'] = password
    br.submit_form (form)
    if br.url == "https://portal.ufsm.br/aluno/turmas/j_security_check":
        print ("Login e/ou senha estão errados!")
        input("\nPressione ENTER para fechar!")
        exit()
    src = str (br.parsed)
    soup = bs4.BeautifulSoup (src)
    print ("Matemática!")
    for nota in soup.findAll ('span', attrs={'style': ''}):
        notas = re.search (r'<span class="" style="">(.*?)</span', str (nota))
        if notas != None:
            if notas2 == True:
                print ("Nota 1: %s" % nota.text)
            if notas2 == False:
                print ("Nota 2: %s" % nota.text)
            notas2 = False
if escolha == 11:
    url = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070445"
    br.open (url)
    form = br.get_form ()
    form['j_username'] = username
    form['j_password'] = password
    br.submit_form (form)
    if br.url == "https://portal.ufsm.br/aluno/turmas/j_security_check":
        print ("Login e/ou senha estão errados!")
        input("\nPressione ENTER para fechar!")
        exit()
    src = str (br.parsed)
    soup = bs4.BeautifulSoup (src)
    print ("Química")
    for nota in soup.findAll ('span', attrs={'style': ''}):
        notas = re.search (r'<span class="" style="">(.*?)</span', str (nota))
        if notas != None:
            if notas2 == True:
                print ("Nota 1: %s" % nota.text)
            if notas2 == False:
                print ("Nota 2: %s" % nota.text)
            notas2 = False
if escolha == 12:
    url = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070456"
    br.open (url)
    form = br.get_form ()
    form['j_username'] = username
    form['j_password'] = password
    br.submit_form (form)
    if br.url == "https://portal.ufsm.br/aluno/turmas/j_security_check":
        print ("Login e/ou senha estão errados!")
        input("\nPressione ENTER para fechar!")
        exit()
    src = str (br.parsed)
    soup = bs4.BeautifulSoup (src)
    print ("Redes de computadores!")
    for nota in soup.findAll ('span', attrs={'style': ''}):
        notas = re.search (r'<span class="" style="">(.*?)</span', str (nota))
        if notas != None:
            if notas2 == True:
                print ("Nota 1: %s" % nota.text)
            if notas2 == False:
                print ("Nota 2: %s" % nota.text)
            notas2 = False
if escolha == 13:
    url = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070448"
    br.open (url)
    form = br.get_form ()
    form['j_username'] = username
    form['j_password'] = password
    br.submit_form (form)
    if br.url == "https://portal.ufsm.br/aluno/turmas/j_security_check":
        print ("Login e/ou senha estão errados!")
        input("\nPressione ENTER para fechar!")
        exit()
    src = str (br.parsed)
    soup = bs4.BeautifulSoup (src)
    print ("Sociologia!")
    for nota in soup.findAll ('span', attrs={'style': ''}):
        notas = re.search (r'<span class="" style="">(.*?)</span', str (nota))
        if notas != None:
            if notas2 == True:
                print ("Nota 1: %s" % nota.text)
            if notas2 == False:
                print ("Nota 2: %s" % nota.text)
            notas2 = False
input("\nPressione ENTER para fechar!")