#como asignar un color a cada planeta HECHO
#retocar aceleracion en funcion de su masa HECHO
#poner pausa HECHO
#apoyar mouse y mostrar masa CASI HECHO
#Mostrar nombre HECHO
#mostrar posicion truncada a entero HECHO
#generacion infinita de planetas HECHO DESDE USUARIO
#mostrar rastro en color del planeta (cada 20 puntos, va a quitar un punto de una lista guardada y va a añadir uno nuevo) NO HACE FALTA
#retocar masa en relacion a su radio HECHO
#moverme a traves de la pantalla (pero no se va a poder con pantalla de asteroid)
#buscar rango de colores bonitos NO HACE FALTA
#relación radio-masa, masa aumenta exponencialmente HECHO
#Necesito ver que pasa con las posiciones de los planetas por lo que voy a colocar una letra para que al pulsarla me aparezca en cada planeta su posición en la terminal se muestre la posicion mas el nombre del planeta del que estoy hablando. Para eso voy a crear una lista de nombres que se muestren sobre el planeta si pulso la tecla, y se muestren en el terminal, usando una lista y quitandolos cada vez que use uno. HECHO
#(luego de crear funcion creacion de planetas por usuario), si el usuario crea mas nombres que planetas disponibles, o avisar q no se puede y continuar, o reiniciar lista de nombres. CASI
#mostrar caracteristicas segun presiono tecla HECHO
#tiempo mas lento
#fusionar planetas
#pantalla infinita
#agrandar pantalla
#mejorar colisiones con los bordes HECHO
#abstraer mas la función de distancia euclidiana HECHO
#mejorar lógica para secuencia de creación de planeta(radio y posicion) y vector (dirección y velocidad)
#permitir ver magnitud (velocidad) en la etapa de creación de vector
#en la creación de planetas, añadir vector que indique velocidad y direccion
#pantalla de asteroid Iinfinita) reparar error (seguro puedo con que si la ultima distancia hasta un borde no es mayor a la anterior(implicando que desapareció el planeta), lo redibuje del lado contrario)
#Podria hacer una pantalla a parte que muestre en funciones como se comportan los planetas y sus caracteristicas...
#Va a ser mejor cuando existan agujeros negros, colisiones con perdida de masa y particulas, y fusionamiento de astros.
#Mostrar grafica con radio y masa de cada planeta en pantalla.
#si los planetas no llegan al centro del que los está atrayendo, no saldran disparados, mejorar colisiones

from turtle import update
import pygame,math,random
pygame.init()
G=0.01
h=1000
w=2000
disp= pygame.display.set_mode((w,h))
pygame.display.update()
pygame.display.set_caption("Let's predict the Universe")
clock = pygame.time.Clock()
state = True

pygame.draw.circle(disp,(255,0,255),(400,300),5,0)


#FONDO
# fondo = pygame.image.load("fondo.png")
# fondoM = pygame.image.load("fondot.png")
# fondoM2 = pygame.image.load("fondot2.png")
# fondoM3 = pygame.image.load("fondot3.png")

disp.fill((0,0,0))
#pygame.draw.circle(disp,(255,255,255),[400,300],10,0)
pygame.display.update()


##Objeto
names = ["Aken","Nejen","Amenhotep","Am-Heh","Ammyt","Amón","Amonet","AnaT","Anhur","Anubis","Anuke","Apofis","Atón","Baal","Baaltis","Bat","Bennu","Beset","Daumutef","Geb","Heqet","Hesat","Horus","Isis","Jepri","Jonsu","Meret","Montu","Nefertum","Neftis","Nejbet","Neit","Nun","Osiris","Qudshu","Qebehut","Ra","Reshef","Sah","Sed","Seret","Seth","Sia","Sopdu","Tefnut","Thot","Yam"]

def giveName(listaP):
    for i in range(len(listaP)):
        listaP[i].name = names.pop(random.randint(0,len(names)-1))
        
planets=list()

class planet():#aca ocurre la creacion del planeta
    def __init__(self,x,y,mass,radius,re,g,b,name, dx=0, dy=0):
        self.name = name
        self.x=x
        self.y=y
        self.m=mass
        self.r=radius
        self.dx=dx #componentes de la velocidad
        self.dy=dy #componentes de la velocidad
        self.re = re
        self.g = g
        self.b = b
        self.orbit = []
        
    def draw(self,re,g,b):
        
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
        
        if cont % 2 == 0:
            # if math.trunc(self.y) % 2 == 0:
            self.orbit.append((self.x,self.y))



##Funciones
# def draw_vector(surface, start_pos, angle, magnitude, color):
#     # Calcular el punto final del vector
#     end_pos = (
#         start_pos[0] + magnitude * math.cos(math.radians(angle)),
#         start_pos[1] + magnitude * math.sin(math.radians(angle))
#     )
#     pygame.draw.line(surface, color, start_pos, end_pos, 3)  # Grosor de 3 para el vector


def truncar5(x): #Truncar a 5 decimales
    integer = int(x*(10**10))/(10**10)
    return float(integer)

#Llamada por force
def dist_euc(px,py,qx,qy): #Calcular distancia al cuadrado
    distance_squared= (px-qx)**2+(py-qy)**2
    return distance_squared

#Llamada por acc
def force(p,q): #Calcular fuerza
    distance=dist_euc(p.x,p.y,q.x,q.y)
    force=-p.m*q.m*G/distance
    return force * 0.7

#Llamada por comp
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

def showVector(x_centro, y_centro, x_final, y_final):
    pygame.draw.line(disp,(50,50,255),(x_centro,y_centro),(x_final,y_final),2)

def showVectorCalculation(i):
    #Tomo las componentes del elemento y formo el vector y lo dibujo como linea desde el radio
    # modulo = (i.dx**2 + dy**2)**0.05
    
    x_centro = i.x
    y_centro = i.y
    
    dx = i.dx
    dy = i.dy
    
    x_final = x_centro - dx
    y_final = y_centro - dy
    
    draw_vector(x_centro, y_centro, x_final, y_final)

def showMass(i): #Mostrar masa
    textMass = font.render("Mass: " + str(math.trunc(i.m)),True,(255,255,255))
    disp.blit(textMass,(i.x,i.y))

text1 = font.render("Presionar 'Espacio' para pausar",True,(255,255,255))
text2 = font.render("Presionar 'm' para mostrar masa",True,(255,255,255))
text3 = font.render("Presionar 'n' para mostrar nombre",True,(255,255,255))
text4 = font.render("Presionar 'o' para mostrar orbita",True,(255,255,255))
text5 = font.render("Presionar p para mostrar posición",True,(255,255,255))
text6 = font.render("Arrastar click para crear el radio del planeta y el próximo click definirá dirección y velocidad",True,(255,255,255))
def showInfo():
    disp.blit(text1, (10, 10))
    disp.blit(text2, (10, 20))
    disp.blit(text3, (10, 30))
    disp.blit(text4, (10, 40))
    disp.blit(text5, (10, 50))
    disp.blit(text6, (10, 60))
    
    
def showName(planet):
    textName = font.render(str(planet.name),True,(255,255,255))
    disp.blit(textName,(planet.x,planet.y+10))
updatedPoints = []

def showPath(planet):
    #si trunco las coordenadas a enteros, entonces las orbitas se dibujaran con cada cambio de x e y a otro entero.
    for i in range(len(planet.orbit)):
        pygame.draw.circle(disp,planet.color,(planet.orbit[i]),1,0)
    # print(planet.orbit)
    
def showPos(planet):
    posText = font.render("x: "+(str(math.trunc(planet.x)))+", "+"y: "+ (str(math.trunc(planet.y))),True,(255,255,255))
    disp.blit(posText,(planet.x,planet.y+20))
    
def drawTempPlanet(xDown,yDown,xStillDown,yStillDown):
    radio =math.sqrt((xDown-xStillDown)**2+(yDown-yStillDown)**2)#distancia entre primer click y mouse levantado
    p = planet(xDown,yDown,0,radio,255,255,255,"name")#crea un planeta sin masa y luego de finalizar este proceso, le añade masa y lo apendiza a la lista de planetas. del mismo modo dibuja un circulo que no será el planeta asi no es afectado por la gravedad de otros planetas mientras se dibuja.
    # ,names.pop(random.randint(0,len(names)-1))
    pygame.draw.circle(disp,(p.re,p.g,p.b),(xDown,yDown),radio,0)
    return xStillDown,yStillDown,radio,p.name #¿Funcion que retorna varias variables?o como

for i in range(1):
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
showVectorKey = False
createKey = False
vectorCreatingKey = False
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
            if event.key == pygame.K_v:
                showVectorKey = not showVectorKey
        
        
        elif event.type == pygame.MOUSEBUTTONDOWN: #Si pulso el click y !createKey
            if not createKey and not vectorCreatingKey: #Este bloque debe estar acá porque almacena el primer click
                createKey = True #En el primer click creayeKey es False y se activa y se guarda la información de la posición inicial del mouse
                xMouseDown, yMouseDown = pygame.mouse.get_pos()
            
            elif not createKey and vectorCreatingKey: #Si hacemos click y está vector activado
                vectorCreatingKey = False
                #Si estoy creando el vector (es decir que createKey == False and vectorCreatingKey == True)
                # vectorCreatingKey = False
                xMouseUp, yMouseUp = xMouseStillDown, yMouseStillDown #Estas componentes corresponden al proceso de creación del radio/planeta
                module = dist_euc(xMouseDown, yMouseDown, vectorxMouseStillDown, vectoryMouseStillDown)#Estas componentes corresponden al proceso de creación del vector
                
                # Calcular la diferencia en coordenadas
                dx = (xMouseUp - vectorxMouseStillDown)
                dy = (yMouseUp - vectoryMouseStillDown)

                # Calcular el ángulo utilizando math.atan2
                angleVar = math.atan2(dx, dy)
                #corrección de angulo
                angleVar = angleVar + math.pi if angleVar >= 0 else angleVar-math.pi
                
                
                # print(angle)
                
                #calculo componentes de velocidad
                dx = math.cos(angleVar) * module * 0.001
                dy = math.sin(angleVar) * module * 0.001
                
                # dx = dx + vx
                # dy = dy + vy
                
                radius = math.sqrt((xMouseDown - xMouseUp)**2 + (yMouseDown - yMouseUp)**2)
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                
                new_planet = planet(xMouseDown, yMouseDown, math.pow(1.2,radius), int(radius), r, g, b, names[random.randint(0,len(names)-1)], dy, dx)
                planets.append(new_planet)
                    
                

        elif event.type == pygame.MOUSEBUTTONUP: #Si suelto el click
            if createKey: #si createKey == True se desactiva y almaceno la ultima posición del mouse
                createKey = False #impide volver a entrar a este bloque una vez que se suelte el click
                vectorCreatingKey = True #Luego de crear el planeta se activa la creación del vector
                xMouseUp, yMouseUp = pygame.mouse.get_pos()
                    
            
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
        if showVectorKey:
            showVectorCalculation(p)

    
    if createKey:
        xMouseStillDown, yMouseStillDown = pygame.mouse.get_pos()
        # radius = int(math.sqrt((xMouseDown - xMouseStillDown)**2 + (yMouseDown - yMouseStillDown)**2))
        # pygame.draw.circle(window, (255, 255, 255), (xMouseDown, yMouseDown), radius, 1)
        x,y,radio,name = drawTempPlanet(xMouseDown,yMouseDown,xMouseStillDown,yMouseStillDown)
        
    if vectorCreatingKey:
        x,y,radio,name = drawTempPlanet(xMouseDown,yMouseDown,xMouseStillDown,yMouseStillDown) #Dibujo el planeta con tamaño fijo que creayeKey ya no puede dibujar
        
        vectorxMouseStillDown, vectoryMouseStillDown = pygame.mouse.get_pos() #posición de la punta del vector
        pygame.draw.line(disp, (50,50,255), (xMouseDown, yMouseDown), (vectorxMouseStillDown, vectoryMouseStillDown), 2)
        moduleNumber = dist_euc(xMouseDown,yMouseDown,vectorxMouseStillDown,vectoryMouseStillDown)
        moduleText = font.render(str(moduleNumber),True,(255,255,255))
        disp.blit(moduleText, (vectorxMouseStillDown+20, vectoryMouseStillDown+20))

    
    
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