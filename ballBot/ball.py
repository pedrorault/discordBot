import random
def randomResponse():
    answers = ["Sim","Não","Talvez","Impossível","Só uma vez","Sempre","Quantas vezes você imaginar",
    "Quantas vezes você quiser", "Pergunte de novo","Mais que uma, menos que três vezes", "Depende",
    "Dependa da lua","Se o Boulos quiser, sim","De máscara, sim","De máscara, não","Sim, se estiver virado",
    "Não, se estiver virado","Pode ser","Putz"]
    r = random.randint(0,len(answers)-1)
    return answers[r]

