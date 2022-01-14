
#TODO: Implement own Tree
import requests

class Pokemon():
    def __init__(self, idPokemon: str):

        poke = self.queryPokemon(idPokemon)

        self.name = poke["species"].capitalize()
        self.number = int(idPokemon)
        self.infoPage = f'https://www.serebii.net/pokedex-sm/{self.number:03}.shtml'
        self.iconUrl = f'https://www.serebii.net/pokedex-sm/icon/{self.number:03}.png'
        self.imageUrl = f'https://assets.pokemon.com/assets/cms2/img/pokedex/detail/{self.number:03}.png'

        self.types = ", ".join(poke["types"])
        self.evolvesFrom = ", ".join( x["species"].capitalize() for x in poke["preevolutions"]) if poke["preevolutions"] else "-"
        self.evolvesTo = ", ".join([x["species"].capitalize() for x in poke["evolutions"]]) if poke["evolutions"] else "-"

    def __repr__(self):
        return f'Pokemon({self.name!r})'

    def formatedInfo(self):
        infos = {
            "Número": '#{:03}'.format(self.number),
            "Tipo": self.types,
            "Evolui De" : self.evolvesFrom,
            "Evolui Para" : self.evolvesTo
        }
        return infos

    def queryPokemon(self, id):
        url = "https://graphqlpokemon.favware.tech/"
        query = """
            query($pokedex: Int!){
                getPokemonByDexNumber(number: $pokedex){
                    species
                    types
                    evolutions {
                    species
                    }
                    preevolutions{
                    species
                    }
                }
            }"""
        variables = {"pokedex":int(id)}
        r = requests.post(url, json={"query": query, "variables": variables})
        return r.json()["data"]["getPokemonByDexNumber"]

if __name__ == "__main__":
    a = Pokemon("13")
    print(a.formatedInfo())