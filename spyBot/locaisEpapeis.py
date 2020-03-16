import random
from copy import deepcopy

english = {'Airplane': ['1st Class Passenger','Air Marshal','Mechanic','Coach Passenger','Flight Attendant','Co-pilot','Captain','Spy'],
'Bank': ['Armored Car Driver','Bank Manager','Loan Consultant','Bank Robber','Customer','Security Guard','Bank Teller','Spy'],
'Beach' : ['Beach Bartender','Kite Surfer','Lifeguard','Thief','Beach Goer','Beach Photographer','Ice Cream Man','Spy'],
'Casino': ['Bartender','Head of Security','Bouncer','Pit Boss', 'Hustler','Dealer','Gambler','Spy'],
'Cathedral' : ['Priest', 'Beggar', 'Sinner', 'Parishioner','Tourist','Deacon','Choir Singer','Spy'],
'Circus': ['Acrobat','Animal Tamer','Magician','Audience Member','Fire Eater','Clown','Juggler','Spy'],
'Corporate': ['Entertainer', 'Manager', 'Party Crasher', 'CEO', 'Admin Assistant','Accountant','Delivery Boy','Spy'],
'Crusader': ['Monk','Imprisoned Arab', 'Servant', 'Bishop', 'Squire','Archer','Knight','Spy'],
'Day Spa': ['Customer','Stylist','Massage Tech', 'Manicurist','Makeup Artist','Dermatologist','Beautician','Spy'],
'Embassy': ['Security Guard', 'Admin Assistant', 'Ambassador','Government Official','Tourist','Refugee','Diplomat','Spy'],
'Hospital': ['Nurse','Doctor','Anesthesiologist','Intern','Patient','Therapist','Surgeon','Spy'],
'Hotel': ['Doorman','Security Guard','Hotel Manager','Housekeeper', 'Hotel Guest', 'Bartender','Valet','Spy'],
'Militar': ['Deserter','Colonel','Medic','Soldier','Sniper','Executive officer','Tank Commander','Spy'],
'Movie': ['Stuntman','Sound Engineer','Cameraman','Director','Costume Artist','Actor','Producer','Spy'],
'Ocean': ['Rich Passenger','Cook','Captain','Bartender','Musician','Waiter','Ship\'s Mechanic','Spy'],
'Train': ['Mechanic','Border Patrol','Chef', 'Engineer','Steward', 'Ticket Taker', 'Passenger','Spy'],
'Pirate': ['Cook','Sailor','Slave','Cannoner', 'Bound prisoner', 'Cabin boy','Pirate Captain', 'Spy'],
'Polar Station': ['Medic','Geologist','Expedition Leader','Biologist','Radioman','Hydrologist','Meteorologist','Spy'],
'Police': ['Detective', 'Lawyer','Journalist','Forensic Scientist','Evidence Archivist','Patrol Officer','Criminal','Spy'],
'Restaurant': ['Musician','Customer','Table Busser','Host','Head Chef','Food Critic','Server','Spy'],
'School': ['Gym Teacher','Student','Principal','Security Guard','Janitor','Lunch Lady','Maintenance Man','Spy'],
'Mechanic': ['Manager', 'Tire Specialist','Motorcyclist','Car Owner','Car Washer','Diagnostic Tech','Auto Mechanic','Spy'],
'Space': ['Engineer','Alien','Tourist','Pilot','Mission Commander','Scientist','Doctor','Spy'],
'Submarine': ['Cook','Captain','Sonar Operator','Weapons Technician','Sailor','Radioman','Navigator','Spy'],
'Supermarket': ['Customer','Cashier','Butcher','Janitor','Produce Manager','Food Sample Demo','Shelf Stocker','Spy'],
'Theater': ['Coat Check','Cue Card Prompter','Ticket Office Cashier','Theater Visitor','Director', 'Actor','Crewman', 'Spy'],
'University': ['Graduate Student','Professor','Dean','Psychologist','Maintenance Man','Student','Advisor','Spy']}

portuguese = {'Avião':['Passageiro de Primeira Classe','Marechal Aéreo','Mecânico','Passageiro de Ônibus','Comissário de Bordo','Co-piloto','Capitão','Espião'],
'Banco':['Motorista de Carro Blindado','Gerente de Banco','Consultor de Empréstimos','Assaltante de Banco','Cliente','Agente de Segurança','Caixa de Banco','Espião'],
'Praia':['Vendedor','Surfista','Salva-vidas','Ladrão','Frequentador da Praia','Fotógrafo','Homem do Sorvete','Espião'],
'Cassino':['Barman','Chefe de Segurança','Segurança','Idoso','Meretriz','Dealer das cartas','Apostador','Espião'],
'Catedral':['Padre','Mendigo','Pecador','Paroquiano','Turista','Diácono','Coro','Espião'],
'Circo':['Acrobata','Domador de Animais','Mágico','Membro da Platéia','Devorador de Fogo','Palhaço','Malabarista','Espião'],
'Empresa':['Alegra-festa','Gerente','Crasher de Festas','CEO','Assistente de Administração','Contador','Entregador','Espião'],
'Exército de Cruzados':['Monge','Árabe Encarcerado','Servo','Bispo','Escudeiro','Arqueiro','Cavaleiro','Espião'],
'Day Spa':['Cliente','Estilista','Massagista','Manicure','Maquiador','Dermatologista','Esteticista','Espião'],
'Embaixada':['Guarda de Segurança','Assistente Administrativo','Embaixador','Funcionário do Governo','Turista','Refugiado','Diplomata','Espião'],
'Hospital':['Enfermeira','Médico','Anestesiologista','Estagiário','Paciente','Terapeuta','Cirurgião','Espião'],
'Hotel':['Porteiro','Guarda de Segurança','Gerente do Hotel','Governanta','Hóspede','Barman','Manobrista','Espião'],
'Base Militar':['Desertor','Coronel','Médico','Soldado','Sniper','Oficial Executivo','Comandante de Tanques','Espião'],
'Set de Filmagem':['Dublê','Engenheiro de Som','Cameraman','Diretor','Figurinista','Ator','Produtor','Espião'],
'Transatlântico':['Passageiro Rico','Cozinheiro','Capitão','Barman','Músico','Garçom','Mecânico de Navios','Espião'],
'Trem de Passageiros':['Mecânico','Patrulha Fronteiriça','Chefe de Cozinha','Engenheiro','Comissário de Bordo','Bilheteira','Passageiro','Espião'],
'Navio Pirata':['Cozinheiro','Marinheiro','Escravo','Canhão','Prisioneiro Amarrado','Camaroteiro','Capitão','Espião'],
'Estação Polar':['Médico','Geólogo','Líder da Expedição','Biólogo','Radioman','Hidrologista','Meteorologista','Espião'],
'Base da Polícia':['Detetive','Advogado','Jornalista','Cientista Forense','Arquivista de Provas','Oficial de Patrulha','Criminoso','Espião'],
'Restaurante':['Músico','Cliente','Garçom','Anfitrião','Chefe de Cozinha','Crítico de Comida','Servidor','Espião'],
'Escola':['Professor de Ginástica','Estudante','Diretor','Guarda de Segurança','Zelador','Tia do Almoço','Homem da Manutenção','Espião'],
'Mecânica':['Gerente','Especialista em Pneus','Motociclista','Proprietário de Carro','Lavador de Carros','Técnico de Diagnóstico','Mecânico de Automóveis','Espião'],
'Base Espacial':['Engenheiro','Alienígena','Turista','Piloto','Comandante da Missão','Cientista','Médico','Espião'],
'Submarino':['Cozinheiro','Capitão','Operador de Sonar','Técnico Em Armas','Marinheiro','Radioman','Navegador','Espião'],
'Supermercado':['Cliente','Caixa','Açougueiro','Zelador','Gerente de Produtos','Demonstração de Amostras de Alimentos','Prateleira','Espião'],
'Teatro':['Figurinista','Prompter de Cartão de Sinalização','Caixa da Bilheteria','Visitante de Teatro','Diretor','Ator','Tripulante','Espião'],
'Universidade':['Estudante de Pós-graduação','Professor','Reitor','Psicólogo','Manutenção','Estudante','Orientador','Espião']}

def getLista(lang='pt'):
    if lang=='en':
        return deepcopy(english)
    elif lang=="pt":
        return deepcopy(portuguese)
    else:
        print("Error: Language not supported.")
        return None

def getLocationList():
    return list(getLista().keys())

def getPrintableLocationList():
    lista = getLocationList()
    lista.sort()
    pretty = ""
    while len(lista) > 0:
        pretty += f"{lista[0]}{(14-len(lista[0]))*' '}\t{lista[1]}{(20-len(lista[1]))*' '}\t{lista[2]}\n"
        del lista[0:3]
    return pretty

def getLocation():
    return random.choice(getLocationList()) 

def choiceAndPop(lista):
    if len(lista) == 8: #max 8 roles and spy being the last
        item = lista.pop() #spy
    elif len(lista) > 0:
        item = random.choice(lista)
        lista.remove(item)
    else:
        print("Erro: itens insuficientes na lista de roles para escolher.")
        return
    return item

def getNroles(numplayers: int, location: str):
    nPlayers = int(numplayers)
    if nPlayers == None:
        return
    if nPlayers < 3 or nPlayers > 8:
        print("Número de jogadores não permitido. (Min:3) (Máx: 8)")
    else:
        #location = getLocation()
        lista = getLista()[location]   
        #print(f'{location}:{lista}') 
        roles = []      
        while nPlayers > 0:            
            roles.append(choiceAndPop(lista))
            nPlayers-=1
        return roles



        
