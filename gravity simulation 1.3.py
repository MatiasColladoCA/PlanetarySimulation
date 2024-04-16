#como asignar un color a cada planeta HECHO
#retocar aceleracion en funcion de su masa HECHO
#poner pausa HECHO
#apoyar mouse y mostrar masa CASI HECHO
#Mostrar nombre HECHO
#mostrar posicion truncada a entero HECHO
#generacion infinita de planetas HECHO DESDE USUARIO
#mostrar rastro en color del planeta (cada 20 puntos, va a quitar un punto de una lista guardada y va a añadir uno nuevo) NO HACE FALTA
#retocar masa en relacion a su radio HECHO
#moverme a traves de la pantalla (pero no se va a poder con pantallar de asteroid)
#buscar rango de colores bonitos NO HACE FALTA
#tamaño aumenta linealmente, masa aumenta exponencialmente HECHO
#Necesito ver que pasa con las posiciones de los planetas por lo que voy a colocar una letra para que al pulsarla me aparezca en cada planeta su posición en la terminal se muestre la posicion mas el nombre del planeta del que estoy hablando. Para eso voy a crear una lista de nombres que se muestren sobre el planeta si pulso la tecla, y se muestren en el terminal, usando una lista y quitandolos cada vez que use uno. HECHO
#(luego de crear funcion creacion de planetas por usuario), si el usuario crea mas nombres que planetas disponibles, o avisar q no se puede y continuar, o reiniciar lista de nombres. CASI
#mostrar caracteristicas segun presiono tecla HECHO
#tiempo mas lento
#fusionar planetas
#pantalla infinita
#agrandar pantalla
#pantalla de asteroidIinfinita) reparar error (seguro puedo con que si la ultima distancia hasta un borde no es mayor a la anterior(implicando que desapareció el planeta), lo redibuje del lado contrario)
#Podria hacer una pantalla a parte que muestre en funciones como se comportan los planetas y sus caracteristicas...
#Va a ser mejor cuando existan agujeros negros, colisiones con perdida de masa y particulas, y fusionamiento de astros.
#Mostrar grafica con radio y masa de cada planeta en pantalla.
#si los planetas no llegan al centro del que los está atrayendo, no saldran disparados
#disfrutar la vida implica aceptar el hecho de que todo puede salir mal y aun asi animarse
from turtle import update
import pygame,math,random
pygame.init()
G=0.01
h=600
w=1000
disp= pygame.display.set_mode((w,h))
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

names = ["Aken","Nejen","Amenhotep","Am-Heh","Ammyt","Amón","Amonet","AnaT","Anhur","Anubis","Anuke","Apofis","Atón","Baal","Baaltis","Bat","Bennu","Beset","Daumutef","Geb","Heqet","Hesat","Horus","Isis","Jepri","Jonsu","Meret","Montu","Nefertum","Neftis","Nejbet","Neit","Nun","Osiris","Qudshu","Qebehut","Ra","Reshef","Sah","Sed","Seret","Seth","Sia","Sopdu","Tefnut","Thot","Yam"]

def giveName(listaP):
    for i in range(len(listaP)):
        listaP[i].name = names.pop(random.randint(0,len(names)-1))
        
planets=list()

class planet():#aca ocurre la creacion del planeta
    def __init__(self,x,y,mass,radius,re,g,b,name):
        self.name = name
        self.x=x
        self.y=y
        self.m=mass
        self.r=radius
        self.dx=0
        self.dy=0
        self.re = re
        self.g = g
        self.b = b
        self.orbit = []
        
    def draw(self,re,g,b):
        #TANTOS DETALLES ME DEJARON EL CÓDIGO HORRIBLE
        # self.x+=self.dx
        # self.y+=self.dy
        # #18.36 asteroid speed coding. El:(800,600) yo:(1000,600)
        # self.newX = self.x+self.dx
        # self.newY = h-self.y+self.dy
        
        # if self.newX > w-self.r:
        #     self.newX -= w
        # elif self.newX < 0+self.r:
        #     self.newX += w
        # if self.newY > h-self.r:
        #     self.newY -= h
        # elif self.newY < 0+self.r:
        #     self.newY += h
        
        #ERA ASÍ DE SENCILLO
        self.x += self.dx
        self.y += self.dy
        
        # Verificar si el objeto sale del borde derecho o izquierdo
        if self.x > w + self.r:
            self.x = 0 - self.r # Aparecer en el lado izquierdo
        elif self.x < 0 - self.r:
            self.x = w + self.r # Aparecer en el lado derecho
        
        # Verificar si el objeto sale del borde inferior o superior
        if self.y > h + self.r:
            self.y = 0 - self.r # Aparecer en la parte superior
        elif self.y < 0 - self.r:
            self.y = h + self.r # Aparecer en la parte inferior
            
        self.color=(re,g,b)
        global cont
        
        pygame.draw.circle(disp,self.color,(self.x,self.y),self.r,0)
        # print("x" + str(self.newX))
        # print("y" + str(self.newY))
        # if self.newX % 0.25 == 0:
        
        if cont % 2 == 0:
            # if math.trunc(self.newY) % 2 == 0:
            self.orbit.append((self.x,self.y))
            
# p1=planet(300,200,5000,10)
# p1.dx=-0.01
# p2=planet(200,300,5000,10)
# p2.dx=0.01
#
# planets.append(p1)
# planets.append(p2)

def truncar5(x): #Truncar a 5 decimales
    integer = int(x*(10**10))/(10**10)
    return float(integer)

def ds(p,q): #Calcular distancia al cuadrado
    distance_squared= (p.x-q.x)**2+(p.y-q.y)**2
    return distance_squared

def force(p,q): #Calcular fuerza
    distance=ds(p,q)
    force=-p.m*q.m*G/distance
    return force * 0.7

def acc(p,q): #Calcular aceleración
    f=force(p,q)
    acc=f/p.m
    acc = truncar5(acc)
    return acc

def angle(p,q): #Calcular ángulo
    if p.x==q.x and p.y>q.y:
        angle=math.pi/2
    elif p.x==q.x and p.y<q.y:
        angle=math.pi*3/2
    else:
        angle=math.atan((p.y-q.y)/(p.x-q.x))
    #print(angle)
    return angle

def comp(p,q):#Divide aceleración entre componentes c e y
    a=acc(p,q)
    if p.x<q.x:
        p.dx-=a*math.cos(angle(p,q))
        p.dy-=a*math.sin(angle(p,q))
    else:
        p.dx+=a*math.cos(angle(p,q))
        p.dy+=a*math.sin(angle(p,q))
        
font = pygame.font.Font("freesansbold.ttf",10)

def showMass(i): #Mostrar masa
    textMass = font.render("Mass: " + str(math.trunc(i.m)),True,(255,255,255))
    disp.blit(textMass,(i.newX,i.newY))
    
# def mayor(lista):
#     for i in range(len(lista)):
#         for j in range(len(lista)):
#             if lista[i].m > lista[j].m:
#                 mayor = lista[i]
#             else:
#                 mayor = lista[j]
#     mayor.m *= 1.4
#     mayor.m *= 1.4

text1 = font.render("Presionar 'Espacio' para pausar",True,(255,255,255))
text2 = font.render("Presionar 'm' para mostrar masa",True,(255,255,255))
text3 = font.render("Presionar 'n' para mostrar nombre",True,(255,255,255))
text4 = font.render("Presionar 'o' para mostrar orbita",True,(255,255,255))
text5 = font.render("Presionar p para mostrar posición",True,(255,255,255))
def showInfo():
    disp.blit(text1, (10, 10))
    disp.blit(text2, (10, 20))
    disp.blit(text3, (10, 30))
    disp.blit(text4, (10, 40))
    disp.blit(text5, (10, 50))
    
    
def showName(planet):
    textName = font.render(str(planet.name),True,(255,255,255))
    disp.blit(textName,(planet.newX,planet.newY+10))
updatedPoints = []

def showPath(planet):
    #si trunco las coordenadas a enteros, entonces las orbitas se dibujaran con cada cambio de x e y a otro entero.
    for i in range(len(planet.orbit)):
        pygame.draw.circle(disp,planet.color,(planet.orbit[i]),1,0)
    # print(planet.orbit)
    
def showPos(planet):
    posText = font.render("x: "+(str(math.trunc(planet.newX)))+", "+"y: "+ (str(math.trunc(planet.newY))),True,(255,255,255))
    disp.blit(posText,(planet.newX,planet.newY+20))
    
def drawTempPlanet(xDown,yDown,xStillDown,yStillDown):
    radio =math.sqrt((xDown-xStillDown)**2+(yDown-yStillDown)**2)#distancia entre primer click y mouse levantado
    p = planet(xDown,yDown,0,radio,255,255,255,"name")#crea un planeta sin masa y luego de finalizar este proceso, le añade masa y lo apendiza a la lista de planetas. del mismo modo dibuja un circulo que no será el planeta asi no es afectado por la gravedad de otros planetas mientras se dibuja.
    # ,names.pop(random.randint(0,len(names)-1))
    pygame.draw.circle(disp,(p.re,p.g,p.b),(xDown,yDown),radio,0)
    return xStillDown,yStillDown,radio,p.name #¿Funcion que retorna varias variables?o como

for i in range(8):
    re = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    radio = random.randint(3,13)
    p=planet(random.randint(250,750),random.randint(150,450),math.pow(1.2,radio),radio,re,g,b,giveName(planets))
    planets.append(p)

cont = 0
pause = False
nameKey = False
massKey = False
pathKey = False
posKey = False
createKeyDown = False
xMouseUp = 0
yMouseUp = 0
mouseIsPar = False #si el mouse está levantado, esto cambia de signo. comienza con False. luego de un click completo, cambia designo.
def movContMouse(cant):
    x,y = pygame.mouse.get_pos()
    posX = -100
    posY = -60
    x = posX - x*cant
    y = posY - y*cant
    return x,y
while state:
    disp.fill((0,0,0))
    # disp.blit(fondo,(0,0))
    
    x,y = movContMouse(0.008)
    # disp.blit(fondoM,(x,y))
    # 
    x,y = movContMouse(0.02)
    # disp.blit(fondoM2,(x,y))
    # 
    x,y = movContMouse(0.05)
    # disp.blit(fondoM3,(x,y))
    # 
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
            if event.key == pygame.K_o:
                pathKey = not pathKey
            if event.key == pygame.K_p:
                posKey = not posKey
        
        #CREACIÓN DE PLANETA A MANO
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     createKeyDown = not createKeyDown
        #     xMouseDown,yMouseDown = pygame.mouse.get_pos()
        # if createKeyDown:
        #     xMouseStillDown,yMouseStillDown = pygame.mouse.get_pos()
        #     radio = math.sqrt((xMouseDown-xMouseStillDown)**2+(yMouseDown-yMouseStillDown)**2)
        #     pygame.draw.circle(disp,(255,255,255),(xMouseDown,yMouseDown),radio,0)
        # if event.type == pygame.MOUSEBUTTONUP:
        #     createKeyDown = not createKeyDown
        #     # xMouseUp,yMouseUp = pygame.mouse.get_pos()
        #     # mouseIsPar = not mouseIsPar
        #     p=planet(xMouseDown,h-yMouseDown,math.pow(1.2,radio),radio,random.randint(0,255),random.randint(0,255),random.randint(0,255),names[random.randint(0,len(names)-1)])
        #     planets.append(p)
        ##
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not createKeyDown:
                createKeyDown = True
                xMouseDown, yMouseDown = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            if createKeyDown:
                createKeyDown = False
                xMouseUp, yMouseUp = pygame.mouse.get_pos()
                radius = math.sqrt((xMouseDown - xMouseUp)**2 + (yMouseDown - yMouseUp)**2)
                new_planet = planet(xMouseDown, yMouseDown, math.pow(1.2,radius), int(radius), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), names[random.randint(0,len(names)-1)])
                planets.append(new_planet)
                
        
            
    if  pause == True:
        continue
        print(pause)        
    for rp in planets:
        for p in planets:
            if rp != p:
                comp(rp,p)
        rp.draw(rp.re,rp.g,rp.b)
        if massKey:
            showMass(rp)
        if nameKey:
            showName(rp)
        if pathKey:
            showPath(rp)
        if posKey:
            showPos(rp)
    
    #mayor(planets) 
    # if createKeyDown:
            # x,y,radio,name = drawTempPlanet(xMouseDown,yMouseDown,xMouseStillDown,yMouseStillDown)
    
    if createKeyDown:
        xMouseStillDown, yMouseStillDown = pygame.mouse.get_pos()
        # radius = int(math.sqrt((xMouseDown - xMouseStillDown)**2 + (yMouseDown - yMouseStillDown)**2))
        # pygame.draw.circle(window, (255, 255, 255), (xMouseDown, yMouseDown), radius, 1)
        x,y,radio,name = drawTempPlanet(xMouseDown,yMouseDown,xMouseStillDown,yMouseStillDown)
     
    else:
        if mouseIsPar:
            re = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            p=planet(xMouseDown,yMouseDown,round(math.pow(3.5,radio)),radio,re,g,b,"name")
            planets.append(p)
            
            # radioUser = (xMouseDown-xMouseUp)**2+(yMouseDown-yMouseUp)**2       
            # names.pop(random.randint(0,len(names)-1))

    
    showInfo()
    pygame.display.flip()
    pygame.display.update()
    #clock.tick(120)
pygame.quit()