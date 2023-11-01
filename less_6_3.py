class Build_Errors(Exception):
    def __str__(self):
        return f"з цією кількістю цегли будинок пободувати не можна!!!!"

def perevirka (kilkict, limit):
    if kilkict>limit:
        return "цегли вистача"
    else:
        raise Build_Errors(kilkict)

cegla = 1001
perevirka(cegla,1000)