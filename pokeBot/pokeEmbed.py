from discord import Embed
from pokeBot.pokeObj import Pokemon

class PokeInfo(Embed):  
    def __init__(self, namePokemon):       
        super().__init__()
        poke = Pokemon(namePokemon)

        self.color = 0x00ffff
        self.type = "rich"
        self.set_author(name=poke.name, url=poke.infoPage, icon_url=poke.iconUrl)
        self.set_image(url=poke.imageUrl)

        for field, value in poke.formatedInfo().items():
            isInline = False if field == "Tipo" else True
            self.add_field(name=field, value=value,inline=isInline)


    def createEmbed(self,namePokemon):
        poke = Pokemon(namePokemon=namePokemon)
        serebii = f'https://www.serebii.net/pokedex-sm/{poke.number:03}.shtml'
        icon = f'https://www.serebii.net/pokedex-sm/icon/{poke.number:03}.png'

        
        embedVar.set_author(name=poke.name, url=serebii, icon_url=icon)   
        embedVar.set_image(
        url=f'https://assets.pokemon.com/assets/cms2/img/pokedex/detail/{poke.number:03}.png'
        )
        embedVar.add_field(name="Número", value=f'#{poke.number:03}', inline=True)
        embedVar.add_field(name="Tipo", value=" ".join(poke.types), inline=False)
        embedVar.add_field(name="Evolui de", value=poke.evolvesFrom,inline=True)
        embedVar.add_field(name="Evolui para", value=', '.join(poke.evolvesTo),inline=True)

        return embedVar 
