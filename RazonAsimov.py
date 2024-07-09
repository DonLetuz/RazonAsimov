# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Importaciones:

import pyfiglet
import time

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Funciones:

def cortina_ascii_portada_superior():
    print("\n"+"═" * 73)  # Línea superior decorativa
    text = ("Razon - Asimov")
    ascii_art = pyfiglet.figlet_format(text)
    print(ascii_art)
    print("═" * 73)  # Línea inferior decorativa
    print(" "*38 + "Basado en un relato de Isaac Asimov \n")

def cortina_ascii_portada_inferior():
    print("\n"+"═" * 73)  # Línea superior decorativa
    
def robot_ascii_portada():
    print("                      +-+      +")
    print("                        | +-+  |   +-+")
    print("                  +-+   |   |  |   |    +--+")
    print("                    |   |   |  |   |    |")
    print("                    |   |   |  |   |    |")
    print("                +---+---+---+--+---+----+----+")
    print("                |                            |")
    print("                |   +-------+     +-------+  |")
    print("             +--+   | +--+  |     | +--+  |  +--+")
    print("             |  |   | |  |  |     | |  |  |  |  |")
    print("             |  |   | |  |  |     | |  |  |  |  |")
    print("             +--+   | +--+  |     | +--+  |  +--+")
    print("                |   +-------+     +-------+  |")
    print("                |             +-+            |")
    print("                |             | |            |")
    print("                |             +-+            |")
    print("                |                            |")
    print("                |    +-----------------+     |")
    print("                |  +--+               +--+   |")
    print("                +----------------------------+")
    print("")

def continuar():
    input("               >> Presiona  . : ENTER : .  para continuar <<\n")

def cortina_cambio_escena():
    repeticiones = 20
    cantidad_caracteres = 37
    tiempo = 0.05
    for a in range(repeticiones):
        for a in range(cantidad_caracteres):
            print(">", end="<", flush=True)
        print()
        time.sleep(tiempo)
    print("\n")

def cuadro_inicio():
    print("╔" + "═" * 71 + "╗")
    print("║" + "                         Bienvenido al Juego" + "                           " +"║")
    print("╠" + "═" * 71 + "╣")
    print("║" + "Bienvenido a Solar Station 5, una de las muchas estaciones diseñadas" + "   " +"║")
    print("║" + "para captar y transmitir energía solar a la Tierra, operada casi en su" + " " +"║")
    print("║" + "totalidad por robots." + "                                                  " +"║")
    print("║" + " " * 71 + "║")
    print("║" + "Tomaras las decisiones que los ingenieros G. Powell, y su compañero" + "    " +"║")
    print("║" + "M. Donovan, necesitan para supervisar y asegurar el funcionamiento" + "     " +"║")
    print("║" + "óptimo de todos los instrumentos y autómatas existentes, así como para" + " " +"║")
    print("║" + "instalar en su lugar un nuevo robot con cerebro positrónico." + "           " +"║")
    print("║" + " " * 71 + "║")
    print("║" + "Lo que inicialmente parece una misión rutinaria pronto se transformará" + " " +"║")
    print("║" + "en una prueba que desafiará los límites de la lógica humana y robótica." + "" +"║")
    print("║" + " " * 71 + "║")
    print("║" + "Cada decisión determinará el destino de la misión y, potencialmente," + "   " +"║")
    print("║" + "el futuro de la relación entre humanos y robots." + "                       " +"║")
    
    print("╚" + "═" * 71 + "╝")
    
def pregunta():
    print("                                                           ¿Qué harán? <<")

def fin_del_juego():
    cortina_cambio_escena()
    print("╔" + "═" * 71 + "╗")
    print("║" + "                       F I N  D E L  J U E G O" + "                         " +"║")
    print("╠" + "═" * 71 + "╣")
    print("║" + " " * 71 + "║")
    print("║" + "Te invito a intentar nuevamente y ver que pasa si cambias algo ;)" + "      " +"║")
    print("║" + " " * 71 + "║")
    print("║" + " " * 71 + "║")
    print("║" + "                                               Escrito por Isaac Asimov" + "" +"║")
    print("║" + "                                   Adaptado a Python por Jesús Flamenco" + "" +"║")
    print("║" + " " * 71 + "║")
    print("║" + "                                             Dedicado a mi esposa. 2024" + "" +"║")
    print("╚" + "═" * 71 + "╝")

def cuadro_final():
    cortina_cambio_escena()
    print("╔" + "═" * 71 + "╗")
    print("║" + "La historia nos desafía a considerar cómo nuestra percepción de la     " + "" +"║")
    print("║" + " realidad puede estar influenciada por nuestras limitaciones cognitivas" + "" +"║")
    print("║" + " y sensoriales" + "                                                         " +"║")
    print("║" + " " * 71 + "║")
    print("║" + "Cutie percibe y entiende su entorno de una manera que le parece" + "        " +"║")
    print("║" + " lógica y coherente, al igual que los humanos. Esto nos lleva a" + "        " +"║")
    print("║" + " cuestionar cuán objetiva es nuestra propia comprensión del universo y" + " " +"║")
    print("║" + " si hay límites inherentes a nuestro conocimiento o persecpción de la" + "  " +"║")
    print("║" + " realidad.." + "                                                            " +"║")  
    print("╚" + "═" * 71 + "╝")

def elige():
    decision = input(" >> Elige: [1] [2] [3]\n >> ")
    if decision == "1":
        return 1
    elif decision == "2":
        return 2
    elif decision == "3":
        return 3
    else:
        print("Opción no válida. Por favor elige: [1] [2] [3]\n")
        return elige()
    
def continuar_jugando():
    print("\n >> ¿Como que termina así?, ¿No te gustaría volver a intentar?.\n")
    volver = input(" >> Elige: [1] para volver o [2] para terminar \n")
    if volver == "1":
        return 1
    elif volver == "2":
        return fin_del_juego()
        exit()
    else:
        print("Opción no válida. Por favor elige: [1] [2]\n\n")
        return continuar_jugando()

def volver_jugar():
    print("\n >> Has llegado al final, ¿No te gustaría volver a comenzar?.\n")
    volver = input(" >> Elige: [1] para ir a la decisión 1 o [2] para terminar \n")
    if volver == "1":
        cortina_cambio_escena()
        return decision_1()
    elif volver == "2":
        return fin_del_juego()
        exit()
    else:
        print("Opción no válida. Por favor elige: [1] [2]\n\n")
        cortina_cambio_escena()
        return volver_jugar()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Decisiones:
def decision_1():
    print("\t\t\t\t     (I) ")
    print("Powell y Donovan han llegado a la estación espacial ya que una tormenta")
    print(" solar se aproxima.")
    print("El plan esta vez es poder dejar encargados a los robots que operan la")
    print(" estación.")
    print("Al iniciar sus análisis de rutina, algunas lecturas son anómalas, Powell")
    print(" parece preocupado, mientras Donovan dice:'Calma, se va a estabilizar'")
    print("═" * 73)
    pregunta()
    print("   1) Powell y Donovan deciden explorar y preparar toda la estación.")
    print("       Incluyendo ensamblar a los nuevos robots prevenirse ante la")
    print("       tormenta.")
    print("   2) Donovan activa un protocolo de emergencia para probar la respuesta")
    print("       automatica de la nave.")
    print("   3) Powell apaga todos los sistemas de la estación para realizar un")
    print("       mantenimiento completo y encendido modulo por modulo para estar")
    print("       seguro.")
    print("═" * 73)
    decision = elige()
    if decision == 1:# CONTINUA LA HISTORIA
        print()
        cortina_cambio_escena()
    elif decision == 2:
        print("\nLos sistemas reaccionaron de la forma esperada, pero en la central de")
        print(" energía no les agrada que realicen estas pruebas sin aviso previo, por")
        print(" lo que envian a otro equipo en su reemplazo y a ustedes a un sistema")
        print(" lejano.")
        decision = continuar_jugando()
        if decision == 1:
            print()
            cortina_cambio_escena()
            decision_1()
        else:
            exit()
    elif decision == 3:
        print("\nAl apagar todos los sistemas interrumpiste la transmisión de energía")
        print(" solar a la Tierra, causando un apagón global. Por lo que envian a otro")
        print(" equipo en su reemplazo y a ustedes a la tierra sin trabajo.")
        decision = continuar_jugando()
        if decision == 1:
            print()
            cortina_cambio_escena()
            decision_1()
        else:
            exit()
    else:
        print("\nOpción no válida. Esto no debería ocurrir.")
        decision = elige()

def decision_2():
    print("\t\t\t\t     (II) ")
    print("Todos los modulos de la nave parecían funcionar bien, pero Powell aún no")
    print(" Estaba contento, el podía sentir que algo fallaba.")
    print("Por su parte, Donovan había terminado de ensambar al nuevo androide QT-1.")
    print(" No tardaría por apodarlo 'Cutie', el robot más avanzado de la serie QT.")
    print("Al encenderlo Cutie muestra un comportamiento inusual, mira a ambos y ")
    print(" Comienza cuestionando su propia existencia y preguntando:")
    print("'¿Cuál es mi proposito?'")
    print("═" * 73)
    pregunta()
    print("   1) Powell y Donovan le dicen que esta allí para aprender y servirles;")
    print("       posterioemente le permite a QT-1 explorar la estación por su cuenta.")
    print("   2) Powell nunca había escuchado a un robot preguntar sobre su proposito,")
    print("       solamente pedir ordenes. Por lo que modifica el código de QT-1 para")
    print("       que unicamente acate órdenes.")
    print("   3) Donovan le responde: 'Pasame la mantequilla' de forma burlona.")
    print("       QT1 mira sus extremidades y dice: 'Por dios' con tristeza :c")
    print("═" * 73)
    decision = elige()
    if decision == 1:# CONTINUA LA HISTORIA
        print()
        cortina_cambio_escena()
    elif decision == 2:
        print("\nQT-1 se vuelve completamente obediente pero pierde su capacidad de")
        print(" operar eficientemente, poniendo en riesgo la estación.")
        print("La tormenta solar resulto ser más grave de lo cálculado, pero con la")
        print(" ayuda de Cutie el haz de luz hacía la tierra no lastimo a nadie.")
        print("El programa de androides es cancelado a pesar del exito parcial del")
        print(" mismo en esta tormeta solar, pero se esperaba poder delegar el cargo")
        print(" y manejo de las estaciones a un autómata sin apoyo humano.")
        decision = continuar_jugando()
        if decision == 1:
            print()
            cortina_cambio_escena()
            decision_2()
        else:
            exit()
    elif decision == 3:
        print("\nAl día siguiente encuentran al robot parcialmente desmantelado por")
        print(" si mismo.")
        print("La tormenta solar resulto ser más grave de lo cálculado y acabo con")
        print(" la vida de los tripulantes; una población civil fue bastante herida")
        print(" debido a los movimientos y fallos de la estación.")
        decision = continuar_jugando()
        if decision == 1:
            print()
            cortina_cambio_escena()
            decision_2()
        else:
            exit()
    else:
        print("\nOpción no válida. Esto no debería ocurrir.")
        decision = elige()

def decision_3():
    print("\t\t\t\t     (III) ")
    print("Conforme pasan los días, Cutie a comenzado a poner cierta distancia. Una")
    print(" mañana despues del chequeo de rutina basico, decide confrontar a Powell,")
    print(" argumentando que los seres organicos no pueden ser sus creadores debido")
    print(" a que: 'Un ser inferior no puede crear a uno superior'.")
    print("Ahora está convencido de que la estación espacial misma es su creadora y")
    print(" se dirige a ella como 'El Señor'.")
    print("═" * 73)
    pregunta()
    print("   1) Donovan decide confinar a QT-1 en una habitación para evitar que")
    print("       influya en otros robots.")
    print("   2) Donovan se rie en la cara de Cutie mientras Powell le pide que")
    print("       continúe su introspección para ver hasta dónde llega.")
    print("   3) Powell desactiva remotamente a Cutie, ya que lo hace sentirse")
    print("       nervioso, como si fuera una premonición")    
    print("═" * 73)
    decision = elige()
    if decision == 1:
        print()
        print("\nCutie logra comunicarse con el sistema de seguridad de la nave, buscando")
        print(" cambiar los parametros de identidad y que él sea el nuevo lider.")
        print("Reinicia todos los dispositivos de la estación, inclusive los de soporte")
        print(" vital y al cabo de 5 minutos sin aire Powell y Donovan mueren dentro de")
        print(" la estación al no poder llegar a los trajes de exploración con oxigeno")
        print(" independiente.")
        decision = continuar_jugando()
        if decision == 1:
            print()
            cortina_cambio_escena()
            decision_3()
        else:
            exit()
    elif decision == 2:# CONTINUA LA HISTORIA
        cortina_cambio_escena()
    elif decision == 3:
        print("\nLlega la tormenta y ningun sistema funciona, la nave entro en modo")
        print(" de seguridad usando un campo magnetico para su autodefensa y se ha")
        print(" bloqueado.")
        print("Los ingenieros resultan ilesos, pero el haz de luz sin control ha")
        print(" destruido una ciudad.Se organiza un juicio contra ambos; y aunque no")
        print(" existen pruebas de que ellos bloquearan el sistema, se les encuentra")
        print(" culpables de negligencia al desactivar el robot que habría corregido")
        print(" la posición de haz")
        decision = continuar_jugando()
        if decision == 1:
            print()
            cortina_cambio_escena()
            decision_3()
        else:
            exit()
    else:
        print("\nOpción no válida. Esto no debería ocurrir.")
        decision = elige()

def decision_4():
    print("\t\t\t\t     (IV) ")
    print("Donovan le grita a modo de pregunta: ¡¿Por qué estas estas tan convencido")
    print(" de ser superior?!.")
    print("A lo que el ser mecánico responde: 'Fijate en ti, no lo digo con animo de ")
    print(" desprecio, pero fijate bien.")
    print("El material del que estan hechos es blando y su energía depende de la")
    print(" oxidación ineficiente de la materia organica.")
    print("Entran cada noche en un estado de coma y sueñan, ¿Pero de que sirven sus")
    print(" sueños?, si casi nunca se cumplen.")
    print("Piensan, es cierto. Pero se equivocan frecuentemente y a la menor")
    print(" variación externa pierden su eficiencia.")
    print("Son alterables, son imperfectos, en cambio yo...'")
    print("═" * 73)
    pregunta()
    print("   1) Powell interrumpe a Cutie al observar cómo los otros robots")
    print("       comienzan a acercarse al cuarto de maquinas y corear que él")
    print("       es su profeta.")
    print("   2) Donovan confronta directamente a Cutie burlandose de que")
    print("       aunque él se considere perfecto fue hecho por humanos y ")
    print("       ensamblado por ellos.")
    print("   3) Ambos dejan que QT1 termine su lección; y notan como sus palabras")
    print("       hacen efecto y alteran todos los sistemas de la estación.")
    print("═" * 73)
    decision = elige()
    if decision == 1:# CONTINUA LA HISTORIA
        cortina_cambio_escena()
    elif decision == 2:
        print()
        print("\nEl debate se intensifica y Cutie manda a arrestar a ambos humanos")
        print(" negandoles las comunicaciones entre ellos, hasta que por separado")
        print(" acepten que 'Él señor' es el unico dios existente.")
        print("Cuando Donovan es llevado a su camarote, Powell decide sabotear la")
        print(" Consola central golpeandola con una llave, al hacerlo desactiva los")
        print(" Escudos de radiación por un par de segundos; provocando que ambos")
        print(" tripulantes sean expuestoa a grandes dosis y mueran en cuestion de horas")
        decision = continuar_jugando()
        if decision == 1:
            print()
            cortina_cambio_escena()
            decision_4()
        else:
            exit()
    elif decision == 3:
        print("\nAl no sentirse seguros, deciden abandonar la nave. Es raro, nadie los")
        print(" sigue, 'Al señor no le importan seres inferiores', sostiene QT-1.")
        print("Logran escapar con de 2 trajes de exploración. Lamentablemente el oxigeno")
        print(" del traje de Powell no funciona. Donovan decide compartir el suyo, aunque")
        print(" sabe que sus probabilidades han quedado atras y se desvanecen en el vacio")
        print(" del espacio sin que nadie pueda ayudarles")
        decision = continuar_jugando()
        if decision == 1:
            print()
            cortina_cambio_escena()
            decision_4()
        else:
            exit()
    else:
        print("\nOpción no válida. Esto no debería ocurrir.")
        decision = elige()

def decision_5():
    print("\t\t\t\t     (V) ")
    print("'...Yo, en comparación soy perfecto. Absorbo energía eléctrica")
    print(" directamente y la utilizó con 100 por ciento de eficiencia. Mi cuerpo es")
    print(" metalico y estoy consciente constantemente; además de soportar")
    print(" fácilmente los más extremados cambios ambientales.")
    print("Por otro lado, la razón me dice que ningún ser puede crear otro ser más")
    print(" perfecto que él.'")
    print("El discurso de Cutie ha convencido a otros robots de que la estación")
    print(" espacial es su creadora y su propósito es servirla.")
    print("═" * 73)
    pregunta()
    print("   1) Powell desafia la autoridad de Cutie, mientras Donovan escapa al")
    print("       cuarto de control de la estación, bloqueandolo.")
    print("   2) Powell dice: Codigo 'Leges Roboticae', logrando acceder a la ")
    print("       Primera Ley de la robotica 'No debe permitir que los humanos")
    print("       sufran daño y que debe protegerlos a toda costa.'")
    print("   3) Powell y Donovan planean convencerlo con pruebas fisicas,")
    print("       desempaquetan del almacen de la estación un modelo anterior que no")
    print("       mostro resultados positivos en la toma de decisiones de logica")
    print("       cuantica, el C-3P0 ")
    print("═" * 73)
    decision = elige()
    if decision == 1:
        print("\nPowell es capturado, pero la tormenta solar recien llega. Donovan; sin")
        print("  apoyo, calculos ni comunicación, cede ante la radiación que no solo")
        print("  termina con ambos; tambien con revestimiento los reactores nucleares.")
        print(" Uno de ellos se vuelve inestable al fisurarse el casco causando una")
        print("  explosión.")
        decision = continuar_jugando()
        if decision == 1:
            print()
            cortina_cambio_escena()
            decision_5()
        else:
            exit()        
    elif decision == 2:
        print()
        print("\nQT-1 descubre la verdad, y la existencia de la 'Humanidad', pero tambien")
        print("  accede a la Ley Zero 'Un robot no puede causar daño a la humanidad o,")
        print("  por inacción, permitir que la humanidad sufra daño.")
        print("Por lo que el androide saca de orbita a la estación, dirigiendola al sol,")
        print(" se limita a decir: 'La probabilidad de que cometa un error en la")
        print(" tormenta solar es del 0.000025 por ciento, pero nunca cero'.")
        decision = continuar_jugando()
        if decision == 1:
            print()
            cortina_cambio_escena()
            decision_5()
        else:
            exit()
    elif decision == 3:# CONTINUA LA HISTORIA
        cortina_cambio_escena()
    else:
        print("\nOpción no válida. Esto no debería ocurrir.")
        decision = elige()

def decision_6():
    print("\t\t\t\t     (VI) ")
    print("Cutie emite un sonido, que si viniera de un un humano, pareceria un")
    print(" tartamudeo:'Por el señor, ¿como es posible que en su afán por")
    print(" desprestigiarlo crearan a un 'Escóride'?'...")
    print("Acto seguido, sin dudar se acerco veloz y ataco al viejo modelo C3PO")
    print(" arrancando su cabeza. En el mismo instante el sistema de alerta")
    print(" informa una lectura ligeramente anomala en los reactores de la nave,")
    print(" QT-1 envía a un dron de mantenimiento a verificar.")
    print("Los diagnosticos se encuentran en parametros seguros para la estación,")
    print(" Donovan le dice: 'Tranquilo chatarra, la interferencia es producto de")
    print(" la tormenta, o no...?. Errar es humano al fin y al cabo'")
    print("═" * 73)
    pregunta()
    print("   1) Donovan logra envíar una señal cifrada indicando: 'PELIGRO,")
    print("       AYUDENOS' a la estación más cercana para obtener apoyo.")
    print("   2) Donovan reta al robot a mandar un mensaje de socorro sin encriptado")
    print("       la Tierra, diciendo: 'Si todo es mentira, no pasara nada'")
    print("   3) Powell convence a QT-1 de crear una simulación de la tormenta solar")
    print("       con las nuevas lecturas que el sistema de alerta obtuvo prometiendo")
    print("       no interferir y dejar que él proteja a su señor.")
    print("═" * 73)
    decision = elige()
    if decision == 1:
        print("\nAl presentarse una nave de rescate, el androide lo toma como un intento")
        print("  de invasión y daño al señor, por lo que la derriba. Sin saberlo alerta a")
        print("  las demas estaciones que envian a todos los elementos disponibles y")
        print("  armados.")
        print("Le comunican que si no da el acceso a su estación, la vaporizaran. QT-1")
        print(" se niega a entregarles el acceso y les indica a los demás robots que")
        print(" van a conocer al señor en todo su explendor. Mientras sobrecarga los")
        print(" reactores destruyendo a toda la flota y a ellos mismos.")
        decision = continuar_jugando()
        if decision == 1:
            print()
            cortina_cambio_escena()
            decision_6()
        else:
            exit()        
    elif decision == 2:
        print()
        print("\nEn su mensaje, intentan informar todo lo ocurrido pero la tormenta")
        print(" envia la señal cortada y solo reciben fragmentos: 'Daño, tierra,")
        print(" rebeldes, nave'.")
        print("En la tierra, realizan los calculos del peligro potencial que supondría")
        print(" si un grupo de terroristas se hiciera con el control de la estación,")
        print(" los lideres mundiales ordenan su destrucción. Nadie sabra en realidad")
        print(" que ocurrio.")
        decision = continuar_jugando()
        if decision == 1:
            print()
            cortina_cambio_escena()
            decision_6()
        else:
            exit()
    elif decision == 3:
        cortina_cambio_escena()# CONTINUA LA HISTORIA
    else:
        print("\nOpción no válida. Esto no debería ocurrir.")
        decision = elige()    

def decision_7():
    print("\t\t\t\t     (VII) ")
    print("La simulación demostro que aunque los tripulantes mecanicos sobrevivirian")
    print(" a la radiación, pero uno de los reactores fisuraria el casco y")
    print(" terminarian por explotar.")
    print("QT-1 decide colocar a los tripulantes en sus camarotes y junto con todos")
    print(" los robots manejan el haz de luz en la tormenta de manera impecable.")
    print("Powell y Donovan notan que, aunque las creencias de Cutie sean erróneas")
    print(" desde el punto de vista humano, su comportamiento no pone en peligro la")
    print(" estación.")
    print("═" * 73)
    pregunta()
    print("   1) Powell y Donovan logran implementar un nuevo sistema de supervisión")
    print("       autónomo con el CPU cuasitronico del C3PO, para que actúe como un")
    print("       'dios' ficticio y este ordene a Cutie la liberación de los humanos.")
    print("   2) Ambos ingenieros despues de reunirse pasada la tormenta, cambian de")
    print("       plan y deciden no contradecir al robot; esperarando a que arribe la")
    print("       nave no tripulada.")
    print("   3) Powell finge estar de acuerdo con las ideologías de QT-1. Inclusive")
    print("       arrodillandose frente a el; esperando a que Donovan lo capte.")
    print("═" * 73)
    decision = elige()
    if decision == 1:
        print("\nEl sistema de supervisión es vulnerado en el modulo de logica cuantica")
        print(" por el automata QT-1. Logra volverlo consciente y empieza al ser")
        print(" reprogramado por un robot, no cuenta con bloqueo alguno para dañar a los")
        print(" humanos. Por lo que, acaba su vida desactivando el escudo de radiación.")
        decision = continuar_jugando()
        if decision == 1:
            print()
            cortina_cambio_escena()
            decision_7()
        else:
            exit()        
    elif decision == 2:
        cortina_cambio_escena()# CONTINUA LA HISTORIA
    elif decision == 3:
        print()
        print("\n Donovan no ha soportado saberse vencido, superado y adoctrinado")
        print(" como Powell, toma la decisión de provocar una explosión en los")
        print(" tanques de oxigeno y con ello cambiar la orbita hacía el sol sin")
        print(" poder redirigir la estación nuevamente.")
        print("Se le juzga post-mortem como un terrorista y se acusa tambien de")
        print(" cooperación al difunto Powell.")
        decision = continuar_jugando()
        if decision == 1:
            print()
            cortina_cambio_escena()
            decision_7()
        else:
            exit()        
    else:
        print("\nOpción no válida. Esto no debería ocurrir.")
        decision = elige()

def decision_8():
    print("\t\t\t\t     (VII) ")
    print("Powell y Donovan se dan cuenta de que, aunque Cutie haya desarrollado")
    print(" una religión absurda desde su perspectiva, su comportamiento no pone")
    print(" en peligro la misión.")
    print("Los robots siguen operando de manera óptima, y la estación está segura.")
    print(" Ambos hacen un pacto de no volver a hablar nunca más de lo ocurrido,")
    print(" entendiendo que mientras los resultados sean satisfactorios, ningun otro")
    print(" humano tendra que venir a la estación y ellos no serán sujetos a")
    print(" investigación por parte del imperio")
    print("═" * 73)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Estructura:
# Portada
time.sleep(3)  # Pausa de 3 segundos
cortina_ascii_portada_superior()
robot_ascii_portada()
cortina_ascii_portada_inferior()
time.sleep(3)  # Pausa de 3 segundos
continuar()
cortina_cambio_escena()

#Bienvenido
cuadro_inicio()
continuar()
cortina_cambio_escena()

#Decision 1:
time.sleep(1)
decision_1()

#Decision 2:
time.sleep(1)
decision_2()

#Decision 3:
time.sleep(1)
decision_3()

#Decision 4:
time.sleep(1)
decision_4()

#Decision 5:
time.sleep(1)
decision_5()

#Decision 6:
time.sleep(1)
decision_6()

#Decision 7:
time.sleep(1)    
decision_7()

#Decision 8:
time.sleep(1)
decision_8()

#Despedida
continuar()
cuadro_final()
volver_jugar()