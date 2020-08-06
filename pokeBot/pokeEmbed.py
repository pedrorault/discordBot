import discord 
from pokeBot.pokeObj import Pokemon

class PokeInfo():  
    def __init__(self, namePokemon):       
        self.embedVar = self.createEmbed(namePokemon)

    def createEmbed(self,namePokemon):
        poke = Pokemon(namePokemon=namePokemon)
        serebii = f'https://www.serebii.net/pokedex-sm/{poke.number:03}.shtml'
        icon = f'https://www.serebii.net/pokedex-sm/icon/{poke.number:03}.png'

        
        embedVar = discord.Embed(color=0x00ffff,type="rich") 
        embedVar.set_author(name=poke.name, url=serebii, icon_url=icon)   
        embedVar.set_image(
        url=f'https://assets.pokemon.com/assets/cms2/img/pokedex/detail/{poke.number:03}.png'
        )
        embedVar.add_field(name="Número", value=f'#{poke.number:03}', inline=True)
        embedVar.add_field(name="Tipo", value=" ".join(poke.types), inline=False)
        embedVar.add_field(name="Evolui de", value=poke.evolvesFrom,inline=True)
        embedVar.add_field(name="Evolui para", value=', '.join(poke.evolvesTo),inline=True)

        return embedVar 
