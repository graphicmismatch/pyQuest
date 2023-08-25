print("created by graphicmismatch")

class Item:
    def __init__(self,nam,desc,effect):
        self.nam = nam
        self.desc = desc
        self.effect = effect
    def toString(self):
        return "Name: {0}\nDescription: {1}\nEffect: {2}".format(self.nam, self.desc, self.effect)
class Location:
    def __init__(self,nam,desc,items):
        self.nam = nam
        self.desc = desc
        self.items = items

    def toString(self, withItems):
        if withItems and len(self.items)>0:
            temp = ""
            for itm in self.items:
                if(itm != self.items[-1]):
                    temp += itm.nam + ", "
                    if(itm == self.items[-2]):
                        temp += "and "
                else:
                    temp += itm.nam
            return "{0}\n{1}\n\nIt has {2}".format(self.nam, self.desc,temp)
        else:
            return "{0}\n{1}".format(self.nam, self.desc)



isDead = False
loc = 0
locations = [
    Location("Home","a small house, it has a table, a chair, a bed and a washroom, all you need really.",[Item("sword","t","z"),Item("bottle","of cum","z"),Item("pp","of death","z"),Item("ur mom","so fat","she wakes up on both sides of the bed")])

    ]
inventory = []
def getArg(command, inp):
     return inp.replace(command+" ", "")

def pick(arg):
    iexist = False
    itmn = -1
    for itm in locations[loc].items:
        itmn+=1
        if arg == itm.nam:
            iexist = True
            break
    if(iexist):
      print("Picked up the following item:")
      print(locations[loc].items[itmn].toString())
      inventory.append(locations[loc].items[itmn])
      locations[loc].items.remove(locations[loc].items[itmn])
    else:
        print("no such item")
    return None

while (not isDead):
    #gameloop
    inp = input("What will you do?\n> ").lower()
    inputflush = 10+10
    print("")

    if inp in ["desc","describe","description","env","environment"]:
      print(locations[loc].toString(True))
    elif inp == "die":
        print("ok lol")
        isDead = True
    elif ("pick" in inp):
        pick(getArg("pick",inp))
    else:
        print("damn who asked bro")

    print("\n\n")
