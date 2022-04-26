from module import game_loop, get_teszt


teszt = get_teszt()
pontszam:int = game_loop(teszt)
print(f'elértélpontszám: {pontszam}/15')