import pytz
import datetime
import json
FILENAME = "./dayBot/db.json"
TZ =  pytz.timezone('America/Sao_Paulo')



#write date object as dataObject.toordinal()
#read date as datetime.date.fromordinal(xxxx)

def readData():
    data = None
    with open(FILENAME,"r") as f:
        data = json.load(f)
    return data

def writeData(guild,tag,newEntry):
    data = readData()

    guildList = data.keys()
    data[guild] = data[guild] if guild in guildList else dict()
    entries = data[guild]

    if tag not in entries:
        entries[tag] = newEntry
        with open(FILENAME,"w") as f:
            json.dump(data,f)
        return f"Tag {tag} inserida"
    else:
        return f"Já existe a Tag {tag}"

def isEmpty(value):
    if value != None and value.strip() != "":
        return False
    return True


def createMemo(tag,frase,date,guild):
    if isEmpty(tag) or isEmpty(frase):
        return "Não há tag ou frase"
    entry = {
        "prefix":"Estamos há",
        "sufix" : frase,
        "date" : date.toordinal(),
        }
    return writeData(guild,tag,entry)

def getMemo(tag,guild):
    data = readData()
    if guild not in data.keys():
        return None
    else:
        if tag in data[guild]:
            return data[guild][tag]
        else:
            return None

def resetMemo(tag,guild):
    memo = getMemo(tag,guild)
    if memo:
        dateAtual = datetime.datetime.now(TZ).date()
        memo["date"] = dateAtual.toordinal()
        writeData(guild,tag,memo)
        return getMessage(tag,guild)
    else:
        return "Tag não encontrada..."
        
def removeMemo(tag,guild):
    data = readData()
    if guild in data.keys():
        if tag in data[guild]:
            del data[guild][tag]
            with open(FILENAME,"w") as f:
                json.dump(data,f)
            return f"Lembrete com a tag {tag} removido"
    return f"Tag {tag} não encontrada"

def getMessage(tag,guild):
    memo = getMemo(tag,guild)
    if not memo:
        return "Tag não encontrada..."
    else:
        dateAtual = datetime.datetime.now(TZ).date()
        diasPassados = dateAtual - datetime.date.fromordinal(memo["date"])
        diaSufix = "dias" if diasPassados != 1 else "dia"
        msg = f'{memo["prefix"]} {diasPassados.days} {diaSufix} {memo["sufix"]}'
        return msg


    