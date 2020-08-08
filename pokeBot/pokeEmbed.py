from discord import Embed
from pokeBot.pokeObj import Pokemon

class PokeInfo(Embed):  
    def __init__(self, idPokemon):       
        super().__init__()
        poke = Pokemon(idPokemon)

        self.color = 0x00ffff
        self.type = "rich"
        self.set_author(name=poke.name, url=poke.infoPage, icon_url=poke.iconUrl)
        self.set_image(url=poke.imageUrl)

        for field, value in poke.formatedInfo().items():
            isInline = False if field == "Tipo" else True
            self.add_field(name=field, value=value,inline=isInline)
