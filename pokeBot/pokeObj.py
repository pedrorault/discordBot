import pokepy
import collections
from anytree import Node

#TODO: Implement own Tree
class Pokemon():
    def __init__(self, idPokemon: str):
        client = pokepy.V2Client()
        
        self.__pokeApi = client.get_pokemon(idPokemon)
        self.__speciesApi = client.get_pokemon_species(idPokemon)
        namePokemon = self.__speciesApi.name
        self.name = namePokemon.capitalize()

        self.number = int(self.__pokeApi.id)

        idChain = self.__speciesApi.evolution_chain.url.split("/")[-2]
        self.__chainApi = client.get_evolution_chain(idChain).chain
        
        self.infoPage = f'https://www.serebii.net/pokedex-sm/{self.number:03}.shtml'
        self.iconUrl = f'https://www.serebii.net/pokedex-sm/icon/{self.number:03}.png'
        self.imageUrl = f'https://assets.pokemon.com/assets/cms2/img/pokedex/detail/{self.number:03}.png'
        
        self.types = list(map(lambda a: ( (a.type.name).capitalize() ), self.__pokeApi.types))
        self.evolvesFrom = self.__speciesApi.evolves_from_species.name.capitalize() if self.__speciesApi.evolves_from_species else "-"

        root = getEvolutionTree(self.__chainApi)
        evolutions = findEvolutions(root=root,name=namePokemon)
        self.evolvesTo = evolutions if evolutions else "-"
        
    def __repr__(self):
        return f'Pokemon({self.name!r})'

    def formatedInfo(self):
        infos = {
            "Número": '#{:03}'.format(self.number),
            "Tipo": ' '.join(self.types),
            "Evolui De" : self.evolvesFrom,
            "Evolui Para" : ', '.join(self.evolvesTo)
        }
        return infos

def getEvolutionTree(chain):
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
        return list(map(lambda x : x.name.capitalize(),root.children))
    else:
        for i in root.children:
            result = findEvolutions(i,name)
            if result:
                return result
