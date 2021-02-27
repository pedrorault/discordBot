# discordBot
My personal discord bot, using [discord.py](https://github.com/Rapptz/discord.py) and [pokepy](https://github.com/PokeAPI/pokepy)
### Features
1. **SpyBot**: Creates a Spyfall game to be played in discord. Send messages to Channels, DMs and read reactions.
3. **PokeBot**: 
    - .poke: Get and sends a random pokemon fusion image as a file.
    - .poke intA intB: Get and sends the specified poke fusion.
    - .poke {name or id}: Sends an embed message containing the name, evolutions, number, image, icon and serebii link to the pokemon.
    - .poke {mispelledName}: Tries to guess which pokemon is being mispelled. If it only has one close match, acts the same as the previous item. Otherwise, sends a list that matches parts of the name being mismatched.
