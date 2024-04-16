import pygame,math,random
pygame.init()
G=0.000011
height=600
width=1000
disp= pygame.display.set_mode((width,height))
pygame.display.update()
pygame.display.set_caption("Let's predict the Universe")
clock = pygame.time.Clock()
state = True

pygame.draw.circle(disp,(255,0,255),(400,300),5,0)

#FONDO
fondo = pygame.image.load("fondo.png")
fondoM = pygame.image.load("fondot.png")
fondoM2 = pygame.image.load("fondot2.png")
fondoM3 = pygame.image.load("fondot3.png")

disp.fill((0,0,0))
#pygame.draw.circle(disp,(255,255,255),[400,300],10,0)
pygame.display.update()


planets=list()

font = pygame.font.Font("freesansbold.ttf",10)

names = ["Aken","Nejen","Amenhotep","Am-Heh","Ammyt","Amón","Amonet","AnaT","Anhur","Anubis","Anuke","Apofis","Atón","Baal","Baaltis","Bat","Bennu","Beset","Daumutef","Geb","Heqet","Hesat","Horus","Isis","Jepri","Jonsu","Meret","Montu","Nefertum","Neftis","Nejbet","Neit","Nun","Osiris","Qudshu","Qebehut","Ra","Reshef","Sah","Sed","Seret","Seth","Sia","Sopdu","Tefnut","Thot","Yam"]

cont = 0

class planet():#aca ocurre la creacion del planeta
    def __init__(self,x,y,m,r,name,re,g,b):
        self.vx = 0
        self.vy = 0
        self.x = x
        self.y = y
        self.m = m
        self.r = r
        self.name = name
        self.re = re
        self.g = g
        self.b = b
        self.color = (re,g,b)
        self.orbit = []
    def showName(self):
        textName = font.render(str(self.name),True,(255,255,255))
        disp.blit(textName,(self.x,self.y))
    updatedPoints = []
    def showPath(self):
        for i in range(len(self.orbit)):
            pygame.draw.circle(disp,self.color,(self.orbit[i]),1,0)   
    def showMass(self):
        textMass = font.render("Mass: " + str(math.trunc(self.m)),True,(255,255,255))
        disp.blit(textMass,(self.x,self.y + 10))
    def showPos(self):
        posText = font.render("x: "+(str(math.trunc(self.x)))+", "+"y: "+ (str(math.trunc(self.y))),True,(255,255,255))
        disp.blit(posText,(self.x,self.y+20))
    
    
        
for i in range(5):
    r = random.randint(1,20)
    re = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    name = names.pop(random.randint(0,len(names)-1))
    p = planet(random.randint(0,1000),random.randint(0,600),math.pow(2,r),r,name,re,g,b)
    planets.append(p)
    

pause = False
nameKey = False
massKey = False
pathKey = False
posKey = False
createKeyDown = False
xMouseUp = 0
yMouseUp = 0
mouseIsPar = False
while state:
    disp.fill((0,0,0))
    cont += 1
    if cont == 100:
        cont = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False
        elif event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause #LO QUE ANDABA BUSCANDO!!!!
                #una especie de interruptor que cambia el signo de la variable/proposición
            if event.key == pygame.K_m:
                massKey = not massKey
            if event.key == pygame.K_n:
                nameKey = not nameKey
            if event.key == pygame.K_p:
                posKey = not posKey
            if event.key == pygame.K_o:
                pathKey = not pathKey
    if  pause == True:
        continue
        print(pause)        
    for rp in planets:
        pygame.draw.circle(disp,rp.color,(rp.x,rp.y),rp.r,0)
        
        fx = 0
        fy = 0
        for p in planets:
            if rp != p:
                g = -0.000000000001
                dx = rp.x-p.x
                dy = rp.y-p.y
                dist = math.sqrt(dx*dx+dy*dy)
                if dist > 0:
                    F = g * rp.m*p.m/dist
                    fx += (F * dx)
                    fy += (F * dy)
        rp.vx += fx*0.7
        rp.vy += fy*0.7
        rp.x += rp.vx
        rp.y += rp.vy
        if rp.x > 1000:
            rp.x -=999
        elif rp.x < 0:
            rp.x +=999
        if rp.y > 600:
            rp.y -= 599
        elif rp.y < 0:
            rp.y += 599
        if cont % 2 == 0:
            rp.orbit.append((rp.x,rp.y))
        if massKey:
            rp.showMass()
        if nameKey:
            rp.showName()
        if posKey:
            rp.showPos()
        if pathKey:
            rp.showPath()
    #mayor(planets) 
    
    pygame.display.update()
    # clock.tick(100)
pygame.quit()