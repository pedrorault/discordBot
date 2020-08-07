import pokepy
import collections
from anytree import Node, RenderTree

#TODO: Implement own Tree
client = pokepy.V2Client()
class Pokemon():
    def __init__(self, namePokemon: str):
        self.name = namePokemon.capitalize()
        self.number = requestNumber(namePokemon)
        self.types = map(lambda x : x.capitalize(),requestTypes(namePokemon))
        self.evolvesFrom = requestEvolvesFrom(namePokemon).capitalize()

        evolutions = findEvolutions(root=getEvolutionTree(namePokemon),name=namePokemon)
        if evolutions:
            self.evolvesTo = map(lambda x: x.capitalize(), evolutions)
        else:
            self.evolvesTo = "-"

    def __repr__(self):
        return f'Pokemon({self.name!r})'

def requestNumber(name: str):
    stats = client.get_pokemon(name)
    number = stats.id
    return int(number)

def getEvolutionTree(name: str):
    # client = pokepy.V2Client() #TODO: Remove this V2Client() call
    species = client.get_pokemon_species(name)
    idChain = species.evolution_chain.url.split("/")[-2]

    chain = client.get_evolution_chain(idChain).chain
    root = Node(chain.species.name)
    for evo1 in chain.evolves_to:
        firstEvo = Node(evo1.species.name,parent=root)
        for evo2 in evo1.evolves_to:
            Node(evo2.species.name,parent=firstEvo)
    return root

def findEvolutions(root, name):
    if not root:
        return None 
    if root.name == name:
        return list(map(lambda x : x.name,root.children))
    else:
        for i in root.children:
            result = findEvolutions(i,name)
            if result:
                return result

def requestTypes(name: str):
    # client = pokepy.V2Client()
    stats = client.get_pokemon(name)
    types = list(map(lambda a: ((a.type.name)),stats.types)) 
    return types

def requestEvolvesFrom(name: str):
    # client = pokepy.V2Client()
    species = client.get_pokemon_species(name)
    evolvesFrom = species.evolves_from_species.name if species.evolves_from_species else "-"
    return evolvesFrom
