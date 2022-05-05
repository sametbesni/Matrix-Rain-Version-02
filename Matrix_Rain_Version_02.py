import pygame, pygame.font
import random
import os
import sys
 
COLOR = (0, 200, 0)  
TICK = 30   # ekran yenileme hızı
CARPAN = 2.0    # harf yoğunluğu
IZBIRAK = True  # arkaplanın dolu veya boş olması
 
def getColor(fx,fy):
    defTemp=xHeads[fx]-fy
 
    if (maxCol>defTemp>0):
        return defTemp
    else:
        return maxCol-1

pygame.init()
temp = pygame.display.Info()
pygame.font.init()

# tam ekran kilitlenme sorunu için 
displLength = (temp.current_w-100, temp.current_h-50)
surface = pygame.display.set_mode(displLength, pygame.DOUBLEBUF)
 
# varsayılan yerine bu fontu indirip kullanabilirsiniz
# fontObj = pygame.font.Font(os.path.join("font_matrix\matrix code nfi.otf"), 14)
# fontObj = pygame.font.Font(os.path.join("font_matrix\Jaycons.ttf"), 14) 
# fontObj = pygame.font.Font(os.path.join("font_matrix\Aurebesh.otf"), 14) 
# fontObj = pygame.font.Font(os.path.join("font_matrix\SithAf-mLlyv.otf"), 14) 
# fontObj = pygame.font.Font(os.path.join("font_matrix\CINEMATIME.TTF"), 14) 
# fontObj = pygame.font.Font(os.path.join("font_matrix\Ciorheta_Font___Cosmic_Gem_by_ZBot9000.ttf"), 14)
# fontObj = pygame.font.Font(os.path.join("font_matrix\HIRAGANA.TTF"), 14)
# fontObj = pygame.font.Font(os.path.join("font_matrix\KATAKANA.TTF"), 14)
# fontObj = pygame.font.Font(os.path.join("font_matrix\RAFFH___.TTF"), 14)
fontObj = pygame.font.Font(os.path.join("font_matrix\MS Mincho.ttf"), 14)

# varsayılan font
# fontObj = pygame.font.Font(pygame.font.get_default_font(), 14)

sampleLetter = fontObj.render('_', False, (0, 111, 0))
letterSize = (sampleLetter.get_width(), sampleLetter.get_height())
lettersOnScreen = (int(displLength[0] / letterSize[0]), int(displLength[1] / letterSize[1]))
 
colorList = [(255, 255, 255)]
print(colorList)
primeColors = len(colorList)+1
R,G,B = COLOR
colorList += [(R+10, G+10, B+10)] * ((lettersOnScreen[1] - 10))
print(colorList)
endColors = len(colorList)
 
if IZBIRAK:
    kuyruk = (0,50,0) 
# izi bırakmak için      
else:
    kuyruk = (0, 0, 0)  
# izleri temizleme

colorList += [(20, 20, 20),(10, 10, 10),(4, 4, 4),kuyruk] 
endColors = len(colorList) - endColors+1
print(colorList) 
maxCol = len(colorList)
print(primeColors, endColors, maxCol);
letters = [[0 for _ in range(lettersOnScreen[1] + 1)] for _ in range(lettersOnScreen[0])]
char = chr(random.randint(32, 126))
 
for y in range(lettersOnScreen[1] + 1):
    for x in range(lettersOnScreen[0]):
        letters[x][y] = [fontObj.render(char, False, colorList[col]) for col in range(maxCol)]
        char = chr(random.randint(32, 126))
  
xHeads = [0 for _ in range(lettersOnScreen[0] + 1)]
notDone = True
ticksLeft = lettersOnScreen[1] + maxCol
strLen = int((lettersOnScreen[0] * CARPAN))
 
while notDone:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            notDone = False
        if event.type == pygame.KEYDOWN:
            notDone = False
    if random.randint(1, 2) == 1:
        randomInt = random.randint(0, lettersOnScreen[0])
        if xHeads[randomInt] <= 0:
            xHeads[randomInt] = 1
    for x in range(lettersOnScreen[0]):
        col = 0
        counter = xHeads[x]
        
        while (counter > 0) and (col < maxCol):
            if (counter < lettersOnScreen[1] + 2) and (col < primeColors or
                                    col > (maxCol - endColors)):
                surface.blit(letters[x][counter - 1][col], (x * letterSize[0],
                                                            (counter - 1) * letterSize[1]))
            col += 1
            counter -= 1
 
        randomInt = random.randint(1, maxCol - 1)
        charPosY = xHeads[x] - randomInt
 
        if (lettersOnScreen[1] - 1 > charPosY > 0):
            temp = letters[x][charPosY]
            randomX = random.randint(1, lettersOnScreen[0] - 1)
            randomY = random.randint(1,lettersOnScreen[1] - 1)
 
            surface.blit(letters[x][charPosY][maxCol - 1], (x * letterSize[0],
                                                            charPosY * letterSize[1]))
            surface.blit(letters[randomX][randomY][maxCol - 1], (randomX * letterSize[0],
                                                            randomY * letterSize[1]))

            letters[x][charPosY] = letters[randomX][randomY]
            letters[randomX][randomY] = temp
 
            surface.blit(letters[x][charPosY][randomInt], (x * letterSize[0], charPosY * letterSize[1]))
            surface.blit(letters[randomX][randomY][getColor(randomX,randomY)],
                         (randomX * letterSize[0], randomY * letterSize[1]))
 
        if xHeads[x] > 0:
            xHeads[x] += 1
        if xHeads[x] - maxCol > lettersOnScreen[1]:
            xHeads[x] = 0
 
    pygame.display.update()
    clock = pygame.time.Clock()
    clock.tick(TICK)
 
sys.exit()