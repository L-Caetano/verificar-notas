#coding: UTF-8
import os
import re
import bs4
import getpass
from robobrowser import RoboBrowser
from time import sleep
os.system('cls' if os.name == 'nt' else 'clear')
username = str(input("Digite os 2 últimos números do seu login (matrícula): 2017112760"))
os.system('cls' if os.name == 'nt' else 'clear')
password = getpass.getpass("Digite a sua senha (ela ficará invisível): ")
br = RoboBrowser()
notas2 = True
os.system('cls' if os.name == 'nt' else 'clear')
print ("| 1 - Algoritmos  | 2 - Artes -  | 3 - Ed. Física             |")
print ("| 4 - Filosofia   | 5 - Física   | 6 - Fundamentos / Hardware |")
print ("| 7 - Geografia   | 8 - Inglês   | 9 - Português              |")
print ("| 10 - Matemática | 11 - Química | 12 - Redes de computadores |")
print ("| 13 - Sociologia |\n")
escolha = int(input("Digite a matéria desejada: "))
os.system('cls' if os.name == 'nt' else 'clear')
if escolha == 1:
    url = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070454"
    br.open(url)
    form = br.get_form()
    form['j_username'] = '2017112760%s' % username
    form['j_password'] = password
    br.submit_form(form)
    if br.url == "https://portal.ufsm.br/aluno/turmas/j_security_check":
        print ("Login e/ou senha estão errados!")
        input("\nPressione ENTER para fechar!")
        exit()
    src = str(br.parsed)
    soup = bs4.BeautifulSoup(src)
    totalPresencas = re.search (r'(class="icon-warning-sign ausente"></i> )(.*)', src)
    totalFaltasID = re.search (r'(id=")(.*)(_label">Total de faltas</span>)', src)
    totalFaltas = re.search (r'(%s" style="">)(.*)(</span>)' % (totalFaltasID.group (2)), src)
    minPresencaID = re.search (r'(id=")(.*)(_label">Mínimo de presenças</span>)', src)
    minPresencas = re.search (r'(%s" style="">)(.*)(</span>)' % (minPresencaID.group (2)), src)
    cargaHorariaID = re.search (r'(id=")(.*)(_label">Carga horária</span>)', src)
    cargaHoraria = re.search (r'(%s" style="">)(.*)(</span>)' % (cargaHorariaID.group (2)), src)
    print ("=========== ALGORITMOS ===========")
    print ("\n=========== NOTAS ===========\n")
    for nota in soup.findAll('span', attrs={'style': ''}):
        notas = re.search(r'<span class="" style="">(.*?)</span', str(nota))
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

if escolha == 2:
    url = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070452"
    br.open (url)
    form = br.get_form ()
    form['j_username'] = '2017112760%s' % username
    form['j_password'] = password
    br.submit_form (form)
    if br.url == "https://portal.ufsm.br/aluno/turmas/j_security_check":
        print ("Login e/ou senha estão errados!")
        input("\nPressione ENTER para fechar!")
        exit()
    src = str (br.parsed)
    soup = bs4.BeautifulSoup (src)
    totalPresencas = re.search (r'(class="icon-warning-sign ausente"></i> )(.*)', src)
    totalFaltasID = re.search (r'(id=")(.*)(_label">Total de faltas</span>)', src)
    totalFaltas = re.search (r'(%s" style="">)(.*)(</span>)' % (totalFaltasID.group (2)), src)
    minPresencaID = re.search (r'(id=")(.*)(_label">Mínimo de presenças</span>)', src)
    minPresencas = re.search (r'(%s" style="">)(.*)(</span>)' % (minPresencaID.group (2)), src)
    cargaHorariaID = re.search (r'(id=")(.*)(_label">Carga horária</span>)', src)
    cargaHoraria = re.search (r'(%s" style="">)(.*)(</span>)' % (cargaHorariaID.group (2)), src)
    print ("=========== ARTES ===========")
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

if escolha == 3:
    url = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070451"
    br.open (url)
    form = br.get_form ()
    form['j_username'] = '2017112760%s' % username
    form['j_password'] = password
    br.submit_form (form)
    if br.url == "https://portal.ufsm.br/aluno/turmas/j_security_check":
        print ("Login e/ou senha estão errados!")
        input("\nPressione ENTER para fechar!")
        exit()
    src = str (br.parsed)
    soup = bs4.BeautifulSoup (src)
    totalPresencas = re.search (r'(class="icon-warning-sign ausente"></i> )(.*)', src)
    totalFaltasID = re.search (r'(id=")(.*)(_label">Total de faltas</span>)', src)
    totalFaltas = re.search (r'(%s" style="">)(.*)(</span>)' % (totalFaltasID.group (2)), src)
    minPresencaID = re.search (r'(id=")(.*)(_label">Mínimo de presenças</span>)', src)
    minPresencas = re.search (r'(%s" style="">)(.*)(</span>)' % (minPresencaID.group (2)), src)
    cargaHorariaID = re.search (r'(id=")(.*)(_label">Carga horária</span>)', src)
    cargaHoraria = re.search (r'(%s" style="">)(.*)(</span>)' % (cargaHorariaID.group (2)), src)
    print ("=========== ED. FÍSICA ===========")
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

if escolha == 4:
    url = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070449"
    br.open (url)
    form = br.get_form ()
    form['j_username'] = '2017112760%s' % username
    form['j_password'] = password
    br.submit_form (form)
    if br.url == "https://portal.ufsm.br/aluno/turmas/j_security_check":
        print ("Login e/ou senha estão errados!")
        input("\nPressione ENTER para fechar!")
        exit()
    src = str (br.parsed)
    soup = bs4.BeautifulSoup (src)
    totalPresencas = re.search (r'(class="icon-warning-sign ausente"></i> )(.*)', src)
    totalFaltasID = re.search (r'(id=")(.*)(_label">Total de faltas</span>)', src)
    totalFaltas = re.search (r'(%s" style="">)(.*)(</span>)' % (totalFaltasID.group (2)), src)
    minPresencaID = re.search (r'(id=")(.*)(_label">Mínimo de presenças</span>)', src)
    minPresencas = re.search (r'(%s" style="">)(.*)(</span>)' % (minPresencaID.group (2)), src)
    cargaHorariaID = re.search (r'(id=")(.*)(_label">Carga horária</span>)', src)
    cargaHoraria = re.search (r'(%s" style="">)(.*)(</span>)' % (cargaHorariaID.group (2)), src)
    print ("=========== FILOSOFIA ===========")
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

if escolha == 5:
    url = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070446"
    br.open (url)
    form = br.get_form ()
    form['j_username'] = '2017112760%s' % username
    form['j_password'] = password
    br.submit_form (form)
    if br.url == "https://portal.ufsm.br/aluno/turmas/j_security_check":
        print ("Login e/ou senha estão errados!")
        input("\nPressione ENTER para fechar!")
        exit()
    src = str (br.parsed)
    soup = bs4.BeautifulSoup (src)
    totalPresencas = re.search (r'(class="icon-warning-sign ausente"></i> )(.*)', src)
    totalFaltasID = re.search (r'(id=")(.*)(_label">Total de faltas</span>)', src)
    totalFaltas = re.search (r'(%s" style="">)(.*)(</span>)' % (totalFaltasID.group (2)), src)
    minPresencaID = re.search (r'(id=")(.*)(_label">Mínimo de presenças</span>)', src)
    minPresencas = re.search (r'(%s" style="">)(.*)(</span>)' % (minPresencaID.group (2)), src)
    cargaHorariaID = re.search (r'(id=")(.*)(_label">Carga horária</span>)', src)
    cargaHoraria = re.search (r'(%s" style="">)(.*)(</span>)' % (cargaHorariaID.group (2)), src)
    print ("=========== FÍSICA ===========")
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

if escolha == 6:
    url = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070455"
    br.open (url)
    form = br.get_form ()
    form['j_username'] = '2017112760%s' % username
    form['j_password'] = password
    br.submit_form (form)
    if br.url == "https://portal.ufsm.br/aluno/turmas/j_security_check":
        print ("Login e/ou senha estão errados!")
        input("\nPressione ENTER para fechar!")
        exit()
    src = str (br.parsed)
    soup = bs4.BeautifulSoup (src)
    totalPresencas = re.search (r'(class="icon-warning-sign ausente"></i> )(.*)', src)
    totalFaltasID = re.search (r'(id=")(.*)(_label">Total de faltas</span>)', src)
    totalFaltas = re.search (r'(%s" style="">)(.*)(</span>)' % (totalFaltasID.group (2)), src)
    minPresencaID = re.search (r'(id=")(.*)(_label">Mínimo de presenças</span>)', src)
    minPresencas = re.search (r'(%s" style="">)(.*)(</span>)' % (minPresencaID.group (2)), src)
    cargaHorariaID = re.search (r'(id=")(.*)(_label">Carga horária</span>)', src)
    cargaHoraria = re.search (r'(%s" style="">)(.*)(</span>)' % (cargaHorariaID.group (2)), src)
    print ("=========== FUNDAMENTOS / HARDWARE ===========")
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

if escolha == 7:
    url = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070450"
    br.open (url)
    form = br.get_form ()
    form['j_username'] = '2017112760%s' % username
    form['j_password'] = password
    br.submit_form (form)
    if br.url == "https://portal.ufsm.br/aluno/turmas/j_security_check":
        print ("Login e/ou senha estão errados!")
        input("\nPressione ENTER para fechar!")
        exit()
    src = str (br.parsed)
    soup = bs4.BeautifulSoup (src)
    totalPresencas = re.search (r'(class="icon-warning-sign ausente"></i> )(.*)', src)
    totalFaltasID = re.search (r'(id=")(.*)(_label">Total de faltas</span>)', src)
    totalFaltas = re.search (r'(%s" style="">)(.*)(</span>)' % (totalFaltasID.group (2)), src)
    minPresencaID = re.search (r'(id=")(.*)(_label">Mínimo de presenças</span>)', src)
    minPresencas = re.search (r'(%s" style="">)(.*)(</span>)' % (minPresencaID.group (2)), src)
    cargaHorariaID = re.search (r'(id=")(.*)(_label">Carga horária</span>)', src)
    cargaHoraria = re.search (r'(%s" style="">)(.*)(</span>)' % (cargaHorariaID.group (2)), src)
    print ("=========== GEOGRAFIA ===========")
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

if escolha == 8:
    url = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070453"
    br.open (url)
    form = br.get_form ()
    form['j_username'] = '2017112760%s' % username
    form['j_password'] = password
    br.submit_form (form)
    if br.url == "https://portal.ufsm.br/aluno/turmas/j_security_check":
        print ("Login e/ou senha estão errados!")
        input("\nPressione ENTER para fechar!")
        exit()
    src = str (br.parsed)
    soup = bs4.BeautifulSoup (src)
    totalPresencas = re.search (r'(class="icon-warning-sign ausente"></i> )(.*)', src)
    totalFaltasID = re.search (r'(id=")(.*)(_label">Total de faltas</span>)', src)
    totalFaltas = re.search (r'(%s" style="">)(.*)(</span>)' % (totalFaltasID.group (2)), src)
    minPresencaID = re.search (r'(id=")(.*)(_label">Mínimo de presenças</span>)', src)
    minPresencas = re.search (r'(%s" style="">)(.*)(</span>)' % (minPresencaID.group (2)), src)
    cargaHorariaID = re.search (r'(id=")(.*)(_label">Carga horária</span>)', src)
    cargaHoraria = re.search (r'(%s" style="">)(.*)(</span>)' % (cargaHorariaID.group (2)), src)
    print ("=========== INGLÊS ===========")
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

if escolha == 9:
    url = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070444"
    br.open (url)
    form = br.get_form ()
    form['j_username'] = '2017112760%s' % username
    form['j_password'] = password
    br.submit_form (form)
    if br.url == "https://portal.ufsm.br/aluno/turmas/j_security_check":
        print ("Login e/ou senha estão errados!")
        input("\nPressione ENTER para fechar!")
        exit()
    src = str (br.parsed)
    soup = bs4.BeautifulSoup (src)
    totalPresencas = re.search (r'(class="icon-warning-sign ausente"></i> )(.*)', src)
    totalFaltasID = re.search (r'(id=")(.*)(_label">Total de faltas</span>)', src)
    totalFaltas = re.search (r'(%s" style="">)(.*)(</span>)' % (totalFaltasID.group (2)), src)
    minPresencaID = re.search (r'(id=")(.*)(_label">Mínimo de presenças</span>)', src)
    minPresencas = re.search (r'(%s" style="">)(.*)(</span>)' % (minPresencaID.group (2)), src)
    cargaHorariaID = re.search (r'(id=")(.*)(_label">Carga horária</span>)', src)
    cargaHoraria = re.search (r'(%s" style="">)(.*)(</span>)' % (cargaHorariaID.group (2)), src)
    print ("=========== PORTUGUÊS ===========")
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

if escolha == 10:
    url = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070447"
    br.open (url)
    form = br.get_form ()
    form['j_username'] = '2017112760%s' % username
    form['j_password'] = password
    br.submit_form (form)
    if br.url == "https://portal.ufsm.br/aluno/turmas/j_security_check":
        print ("Login e/ou senha estão errados!")
        input("\nPressione ENTER para fechar!")
        exit()
    src = str (br.parsed)
    soup = bs4.BeautifulSoup (src)
    totalPresencas = re.search (r'(class="icon-warning-sign ausente"></i> )(.*)', src)
    totalFaltasID = re.search (r'(id=")(.*)(_label">Total de faltas</span>)', src)
    totalFaltas = re.search (r'(%s" style="">)(.*)(</span>)' % (totalFaltasID.group (2)), src)
    minPresencaID = re.search (r'(id=")(.*)(_label">Mínimo de presenças</span>)', src)
    minPresencas = re.search (r'(%s" style="">)(.*)(</span>)' % (minPresencaID.group (2)), src)
    cargaHorariaID = re.search (r'(id=")(.*)(_label">Carga horária</span>)', src)
    cargaHoraria = re.search (r'(%s" style="">)(.*)(</span>)' % (cargaHorariaID.group (2)), src)
    print ("=========== MATEMÁTICA ===========")
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

if escolha == 11:
    url = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070445"
    br.open (url)
    form = br.get_form ()
    form['j_username'] = '2017112760%s' % username
    form['j_password'] = password
    br.submit_form (form)
    if br.url == "https://portal.ufsm.br/aluno/turmas/j_security_check":
        print ("Login e/ou senha estão errados!")
        input("\nPressione ENTER para fechar!")
        exit()
    src = str (br.parsed)
    soup = bs4.BeautifulSoup (src)
    totalPresencas = re.search (r'(class="icon-warning-sign ausente"></i> )(.*)', src)
    totalFaltasID = re.search (r'(id=")(.*)(_label">Total de faltas</span>)', src)
    totalFaltas = re.search (r'(%s" style="">)(.*)(</span>)' % (totalFaltasID.group (2)), src)
    minPresencaID = re.search (r'(id=")(.*)(_label">Mínimo de presenças</span>)', src)
    minPresencas = re.search (r'(%s" style="">)(.*)(</span>)' % (minPresencaID.group (2)), src)
    cargaHorariaID = re.search (r'(id=")(.*)(_label">Carga horária</span>)', src)
    cargaHoraria = re.search (r'(%s" style="">)(.*)(</span>)' % (cargaHorariaID.group (2)), src)
    print ("=========== QUÍMICA ===========")
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

if escolha == 12:
    url = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070456"
    br.open (url)
    form = br.get_form ()
    form['j_username'] = '2017112760%s' % username
    form['j_password'] = password
    br.submit_form (form)
    if br.url == "https://portal.ufsm.br/aluno/turmas/j_security_check":
        print ("Login e/ou senha estão errados!")
        input("\nPressione ENTER para fechar!")
        exit()
    src = str (br.parsed)
    soup = bs4.BeautifulSoup (src)
    totalPresencas = re.search (r'(class="icon-warning-sign ausente"></i> )(.*)', src)
    totalFaltasID = re.search (r'(id=")(.*)(_label">Total de faltas</span>)', src)
    totalFaltas = re.search (r'(%s" style="">)(.*)(</span>)' % (totalFaltasID.group (2)), src)
    minPresencaID = re.search (r'(id=")(.*)(_label">Mínimo de presenças</span>)', src)
    minPresencas = re.search (r'(%s" style="">)(.*)(</span>)' % (minPresencaID.group (2)), src)
    cargaHorariaID = re.search (r'(id=")(.*)(_label">Carga horária</span>)', src)
    cargaHoraria = re.search (r'(%s" style="">)(.*)(</span>)' % (cargaHorariaID.group (2)), src)
    print ("=========== REDES DE COMPUTADORES ===========")
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

if escolha == 13:
    url = "https://portal.ufsm.br/aluno/turmas/turma.html?itemCurriculoAluno=11070448"
    br.open (url)
    form = br.get_form ()
    form['j_username'] = '2017112760%s' % username
    form['j_password'] = password
    br.submit_form (form)
    if br.url == "https://portal.ufsm.br/aluno/turmas/j_security_check":
        print ("Login e/ou senha estão errados!")
        input("\nPressione ENTER para fechar!")
        exit()
    src = str (br.parsed)
    soup = bs4.BeautifulSoup (src)
    totalPresencas = re.search (r'(class="icon-warning-sign ausente"></i> )(.*)', src)
    totalFaltasID = re.search (r'(id=")(.*)(_label">Total de faltas</span>)', src)
    totalFaltas = re.search (r'(%s" style="">)(.*)(</span>)' % (totalFaltasID.group (2)), src)
    minPresencaID = re.search (r'(id=")(.*)(_label">Mínimo de presenças</span>)', src)
    minPresencas = re.search (r'(%s" style="">)(.*)(</span>)' % (minPresencaID.group (2)), src)
    cargaHorariaID = re.search (r'(id=")(.*)(_label">Carga horária</span>)', src)
    cargaHoraria = re.search (r'(%s" style="">)(.*)(</span>)' % (cargaHorariaID.group (2)), src)
    print ("=========== SOCIOLOGIA ===========")
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