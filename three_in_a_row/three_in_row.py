import os
path = "C:/Users/misak/Desktop/python/three_in_a_row"
os.chdir(path)


import pyglet
import random

#from game import State
krizek = []
kolecko = []
kolecko_vyber = [(1, 1), (4, 1), (7, 1), (4, 1), (4, 4), (4, 7), (7, 1), (7, 4), (7, 7) ]
vsechno = kolecko_vyber

def minus(a, b):
    return list(set(a) - set(b))

#rozpoznat viteznou kombinaci
def vitezstvi(pole):
    if minus([(1, 1), (4, 1), (7, 1)], pole)  == [] or minus([(1, 4), (4, 4), (7, 4)], pole)  == [] or minus([(1, 7), (4, 7), (7, 7)], pole)  == [] or minus([(1, 1), (4, 4), (7, 7)], pole)  == []  or  minus([(1, 7), (4, 4), (7, 1)], pole)  == []:
        return True
    else:
        return False

#minus([(1, 4), (4, 4), (7, 4)], [(7, 4)])

TILE_SIZE = 48
cross_image = pyglet.image.load('cross.png')
circle_image = pyglet.image.load('circle.png')

window = pyglet.window.Window()



@window.event
def on_draw():
    window.clear()
    for x, y in krizek:
        cross_image.blit(x * TILE_SIZE, y * TILE_SIZE, width=100, height=100)
    
    for x, y in kolecko:
        circle_image.blit(x * TILE_SIZE, y * TILE_SIZE, width=100, height=100)


#obsazene = []

#ovladani bude cislicemi
@window.event
def on_key_press( symbol, mod):

    #zjistime, zda policko jiz je obsazene:
    # obsazene = krizek + kolecko
    # volne = minus(vsechno, obsazene)
    
    if symbol == pyglet.window.key.NUM_1:
        krizek.append((1, 1))
        obsazene = krizek + kolecko
        volne = minus(vsechno, obsazene)


        if not len(volne) == 0:
            kolecko.append(random.choice(volne))
            obsazene = krizek + kolecko
            volne = minus(vsechno, obsazene)

        if (vitezstvi(krizek) or vitezstvi(kolecko)) == True:
            print("Konec hry")
            pyglet.app.exit()
                



    elif symbol == pyglet.window.key.NUM_2:
        krizek.append((4, 1))
        obsazene = krizek + kolecko
        volne = minus(vsechno, obsazene)


        if not len(volne) == 0:
            kolecko.append(random.choice(volne))
            obsazene = krizek + kolecko
            volne = minus(vsechno, obsazene)
       
        if (vitezstvi(krizek) or vitezstvi(kolecko)) == True:
            print("Konec hry")
            pyglet.app.exit()
                    

    elif symbol == pyglet.window.key.NUM_3:
        krizek.append((7, 1))
        obsazene = krizek + kolecko
        volne = minus(vsechno, obsazene)


        if not len(volne) == 0:
            kolecko.append(random.choice(volne))
            obsazene = krizek + kolecko
            volne = minus(vsechno, obsazene)

        if (vitezstvi(krizek) or vitezstvi(kolecko)) == True:
            print("Konec hry")
            pyglet.app.exit()
                

            
    elif symbol == pyglet.window.key.NUM_4:
        krizek.append((1, 4))
        obsazene = krizek + kolecko
        volne = minus(vsechno, obsazene)

        if not len(volne) == 0:
            kolecko.append(random.choice(volne))
            obsazene = krizek + kolecko
            volne = minus(vsechno, obsazene)

        if (vitezstvi(krizek) or vitezstvi(kolecko)) == True:
            print("Konec hry")
            pyglet.app.exit()
            



    elif symbol == pyglet.window.key.NUM_5:
        krizek.append((4, 4))
        obsazene = krizek + kolecko
        volne = minus(vsechno, obsazene)


        if not len(volne) == 0:
            kolecko.append(random.choice(volne))
            obsazene = krizek + kolecko
            volne = minus(vsechno, obsazene)

        if (vitezstvi(krizek) or vitezstvi(kolecko)) == True:
            print("Konec hry")
            pyglet.app.exit()
                



    elif symbol == pyglet.window.key.NUM_6:
        krizek.append((7, 4))
        obsazene = krizek + kolecko
        volne = minus(vsechno, obsazene)

        if not len(volne) == 0:
            kolecko.append(random.choice(volne))
            obsazene = krizek + kolecko
            volne = minus(vsechno, obsazene)

        if (vitezstvi(krizek) or vitezstvi(kolecko)) == True:
            print("Konec hry")
            pyglet.app.exit()
                



    elif symbol == pyglet.window.key.NUM_7:
        krizek.append((1, 7))
        obsazene = krizek + kolecko
        volne = minus(vsechno, obsazene)


        if not len(volne) == 0:
            kolecko.append(random.choice(volne))
            obsazene = krizek + kolecko
            volne = minus(vsechno, obsazene)

        if (vitezstvi(krizek) or vitezstvi(kolecko)) == True:
            print("Konec hry")
            pyglet.app.exit()
                



    elif symbol == pyglet.window.key.NUM_8:
        krizek.append((4, 7))
        obsazene = krizek + kolecko
        volne = minus(vsechno, obsazene)


        if not len(volne) == 0:
            kolecko.append(random.choice(volne))
            obsazene = krizek + kolecko
            volne = minus(vsechno, obsazene)

        if (vitezstvi(krizek) or vitezstvi(kolecko)) == True:
            print("Konec hry")
            pyglet.app.exit()
                



    elif symbol == pyglet.window.key.NUM_9:
        krizek.append((7, 7))
        obsazene = krizek + kolecko
        volne = minus(vsechno, obsazene)
        

        if not len(volne) == 0:
            kolecko.append(random.choice(volne))
            obsazene = krizek + kolecko
            volne = minus(vsechno, obsazene)

                
        if (vitezstvi(krizek) or vitezstvi(kolecko)) == True:
            print("Konec hry")
            pyglet.app.exit()
                
                

 
    

    
pyglet.app.run()


