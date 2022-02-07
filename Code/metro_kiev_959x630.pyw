import sys
import tkinter as tk
import pandas as pd
from datetime import datetime
from PIL import ImageTk, Image
import os

data_file_name = "Code/data/datos.csv"
image_file_name = "Code/data/metro_kiev_959x630.png"


try:
   wd = sys._MEIPASS
except AttributeError:
   wd = os.getcwd()
data_file = os.path.join(wd,data_file_name)
image_file = os.path.join(wd,image_file_name)

data = pd.read_csv(data_file, index_col=0)
data = data*100

imagen = Image.open(image_file)


class Graph:


    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def a_star_algorithm(self, start_node, stop_node, hora, dia):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([start_node])
        closed_list = set([])
        peso = 0
        linea1 = ['Akademmistechko', 'Zhytomyrska', 'Sviatoshyn', 'Nyvky', 'Beresteiska', 'Shuliavska',
                  'Politekhnichnyi_Instytut', 'Vokzalna', 'Universytet', 'Teatralna', 'Jreshchatyk', 'Arsenalna',
                  'Dnipro', 'Hidropark', 'Livoberezhna', 'Darnytsia', 'Chernihivska', 'Lisova']
        linea2 = ['Heroiv_Dnipra', 'Minska', 'Obolon', 'Pochaina', 'Tarasa_Sevchenka', 'Kontraktova_Polscha',
                  'Poschtova_Polscha', 'Maidan_Nezalezhnosti', 'Ploshcha_Lva_Tolstoho', 'Olimpiiska', 'Palats_Ukrania',
                  'Lybidska', 'Demiivska', 'Holosiivska', 'Vasylkiivska', 'Vystavkovyi_Tsentr', 'Ipodrom', 'Teremki']
        linea3 = ['Syrets', 'Dorogozhychi', 'Lukianivska', 'Zoloti_Vorota', 'Palats_Sportu', 'Klovska', 'Pecherska',
                  'Druzhby_Narodiv', 'Vydubychi', 'Slavutych', 'Osokorky', 'Pozniaky', 'Jarkivska',
                  'Vyrlytsia,Boryspilska', 'Chervony_Jutir']
        frecuencias1 = [tiempo_en_segundos(2, 0), tiempo_en_segundos(3, 30), tiempo_en_segundos(3, 30)]
        frecuencias2 = [tiempo_en_segundos(2, 0), tiempo_en_segundos(5, 0), tiempo_en_segundos(4, 15)]
        frecuencias3 = [tiempo_en_segundos(2, 15), tiempo_en_segundos(4, 10), tiempo_en_segundos(6, 0)]

        diario = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        weekend = ['Saturday', 'Sunday']

        if 6 > hora > 0 or hora > 24:
            raise ValueError
        if dia in diario:
            if 7 < hora < 10 or 17 < hora < 20:
                if start_node in linea1:
                    peso += frecuencias1[1]
                if start_node in linea2:
                    peso += frecuencias2[1]
                if start_node in linea3:
                    peso += frecuencias3[1]
            if 6 < hora < 7 or 10 < hora < 17 or 17 < hora < 24:
                if start_node in linea1:
                    peso += frecuencias1[0]
                if start_node in linea2:
                    peso += frecuencias2[0]
                if start_node in linea3:
                    peso += frecuencias3[0]
        elif dia in weekend:
            if start_node in linea1:
                peso += frecuencias1[2]
            if start_node in linea2:
                peso += frecuencias2[2]
            if start_node in linea3:
                peso += frecuencias3[2]
        else:
            raise ValueError
        salida1 = [tiempo_en_segundos(1, 0), tiempo_en_segundos(1, 0), tiempo_en_segundos(1, 0),
                   tiempo_en_segundos(1, 0), tiempo_en_segundos(1, 0), tiempo_en_segundos(3, 35),
                   tiempo_en_segundos(2, 5), tiempo_en_segundos(2, 5), tiempo_en_segundos(4, 0),
                   tiempo_en_segundos(2, 0), tiempo_en_segundos(2, 30), tiempo_en_segundos(4, 20),
                   tiempo_en_segundos(1, 0), tiempo_en_segundos(1, 0), tiempo_en_segundos(1, 0),
                   tiempo_en_segundos(1, 0), tiempo_en_segundos(1, 0), tiempo_en_segundos(1, 0)]
        salida2 = [tiempo_en_segundos(1, 0), tiempo_en_segundos(1, 0), tiempo_en_segundos(1, 0),
                   tiempo_en_segundos(1, 0), tiempo_en_segundos(1, 0), tiempo_en_segundos(1, 0),
                   tiempo_en_segundos(1, 0), tiempo_en_segundos(2, 30), tiempo_en_segundos(2, 5),
                   tiempo_en_segundos(1, 0), tiempo_en_segundos(1, 0), tiempo_en_segundos(1, 0),
                   tiempo_en_segundos(1, 0), tiempo_en_segundos(1, 0), tiempo_en_segundos(1, 0),
                   tiempo_en_segundos(1, 0), tiempo_en_segundos(1, 0), tiempo_en_segundos(1, 0)]
        salida3 = [tiempo_en_segundos(2, 30), tiempo_en_segundos(3, 40), tiempo_en_segundos(2, 0),
                   tiempo_en_segundos(4, 10), tiempo_en_segundos(1, 40), tiempo_en_segundos(2, 0),
                   tiempo_en_segundos(4, 0), tiempo_en_segundos(2, 20), tiempo_en_segundos(1, 0),
                   tiempo_en_segundos(1, 0), tiempo_en_segundos(1, 0), tiempo_en_segundos(1, 0),
                   tiempo_en_segundos(1, 0), tiempo_en_segundos(1, 0), tiempo_en_segundos(1, 0),
                   tiempo_en_segundos(1, 0)]
        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity

        g = {}
        if stop_node in linea1:
            indice = linea1.index(stop_node)
            peso += salida1[indice]
        elif stop_node in linea2:
            indice = linea2.index(stop_node)
            peso += salida2[indice]
        elif stop_node in linea3:
            indice = linea3.index(stop_node)
            peso += salida3[indice]

        g[start_node] = 0
        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node
        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n == None or g[v] + data[v][stop_node] < g[n] + data[n][stop_node]:
                    n = v

            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    # print(n)
                    # peso += n.value()
                    n = parents[n]

                reconst_path.append(start_node)
                # peso += start_node.value()
                reconst_path.reverse()

                # print('Path found: {}'.format(reconst_path))
                return reconst_path, g[reconst_path[-1]] + peso
            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None

tiempo_en_segundos = lambda x, y: x * 60 + y
tiempo_en_minitos = lambda x : str(x//60) +" minutos "+str(x%60)+" segundos "

Lista_de_adyacencias  = {'Akademmistechko':[('Zhytomyrska',tiempo_en_segundos(2,5))],
                    'Zhytomyrska':[ ('Akademmistechko',tiempo_en_segundos(2,5)) ,('Sviatoshyn',tiempo_en_segundos(2,30))] ,
                    'Sviatoshyn':[ ('Zhytomyrska',tiempo_en_segundos(2,30)) ,('Nyvky',tiempo_en_segundos(1,25))] ,
                    'Nyvky':[ ('Sviatoshyn',tiempo_en_segundos(1,25)) ,('Beresteiska',tiempo_en_segundos(2,25))] ,
                    'Beresteiska':[ ('Nyvky',tiempo_en_segundos(2,25)) ,('Shuliavska',tiempo_en_segundos(2,50))],
                    'Shuliavska':[ ('Beresteiska',tiempo_en_segundos(2,50)) ,('Politekhnichnyi_Instytut',tiempo_en_segundos(1,35))],
                    'Politekhnichnyi_Instytut':[ ('Shuliavska',tiempo_en_segundos(1,35)) ,('Vokzalna',tiempo_en_segundos(2,45))],
                    'Vokzalna':[ ('Politekhnichnyi_Instytut',tiempo_en_segundos(2,45)) ,('Universytet',tiempo_en_segundos(1,35))],
                    'Universytet':[ ('Vokzalna',tiempo_en_segundos(1,35)) ,('Teatralna',tiempo_en_segundos(1,30))],
                    'Teatralna':[ ('Universytet',tiempo_en_segundos(1,30)) ,('Jreshchatyk',tiempo_en_segundos(1,30)), ('Zoloti_Vorota',tiempo_en_segundos(3,20))],
                    'Jreshchatyk':[ ('Teatralna',tiempo_en_segundos(1,30)) ,('Arsenalna',tiempo_en_segundos(2,10)),('Maidan_Nezalezhnosti',tiempo_en_segundos(3,50))],
                    'Arsenalna':[('Jreshchatyk',tiempo_en_segundos(2,10)) ,('Dnipro',tiempo_en_segundos(1,30))],
                    'Dnipro':[('Arsenalna',tiempo_en_segundos(1,30)) ,('Hidropark',tiempo_en_segundos(2,10))],
                    'Hidropark':[('Dnipro',tiempo_en_segundos(2,10)) ,('Livoberezhna',tiempo_en_segundos(2,15))],
                    'Livoberezhna':[('Hidropark',tiempo_en_segundos(2,15)) ,('Darnytsia',tiempo_en_segundos(1,40))],
                    'Darnytsia': [('Livoberezhna',tiempo_en_segundos(1,40)) ,('Chernihivska',tiempo_en_segundos(2,5))],
                    'Chernihivska':[('Darnytsia',tiempo_en_segundos(2,5)) ,('Lisova',tiempo_en_segundos(1,55))],
                    'Lisova':[('Chernihivska',tiempo_en_segundos(1,55))],
                    'Heroiv_Dnipra':[('Minska',tiempo_en_segundos(1,50))],
                    'Minska':[('Heroiv_Dnipra',tiempo_en_segundos(1,50)) ,('Obolon',tiempo_en_segundos(1,30))],
                    'Obolon':[('Minska',tiempo_en_segundos(1,30)) ,('Pochaina',tiempo_en_segundos(2,10))],
                    'Pochaina':[('Obolon',tiempo_en_segundos(2,10)) ,('Tarasa_Sevchenka',tiempo_en_segundos(2,25))],
                    'Tarasa_Sevchenka':[('Pochaina',tiempo_en_segundos(2,25)) ,('Kontraktova_Polscha',tiempo_en_segundos(1,50))],
                    'Kontraktova_Polscha':[('Tarasa_Sevchenka',tiempo_en_segundos(1,50)) ,('Poschtova_Polscha',tiempo_en_segundos(1,20))],
                    'Poschtova_Polscha':[('Kontraktova_Polscha',tiempo_en_segundos(1,20)) ,('Maidan_Nezalezhnosti',tiempo_en_segundos(1,35))],
                    'Maidan_Nezalezhnosti':[('Poschtova_Polscha',tiempo_en_segundos(1,35)) ,('Ploshcha_Lva_Tolstoho',tiempo_en_segundos(1,35)),('Jreshchatyk',tiempo_en_segundos(3,50))],
                    'Ploshcha_Lva_Tolstoho':[('Maidan_Nezalezhnosti',tiempo_en_segundos(1,35)) ,('Olimpiiska',tiempo_en_segundos(1,25)),('Palats_Sportu',tiempo_en_segundos(3,20))],
                    'Olimpiiska':[('Ploshcha_Lva_Tolstoho',tiempo_en_segundos(1,25)) ,('Palats_Ukrania',tiempo_en_segundos(1,30))],
                    'Palats_Ukrania':[('Olimpiiska',tiempo_en_segundos(1,30)) ,('Lybidska',tiempo_en_segundos(1,15))],
                    'Lybidska':[('Palats_Ukrania',tiempo_en_segundos(1,15)) ,('Demiivska',tiempo_en_segundos(1,30))],
                    'Demiivska':[('Lybidska',tiempo_en_segundos(1,30)) ,('Holosiivska',tiempo_en_segundos(1,25))],
                    'Holosiivska':[('Demiivska',tiempo_en_segundos(1,25)) ,('Vasylkiivska',tiempo_en_segundos(1,5))],
                    'Vasylkiivska':[('Holosiivska',tiempo_en_segundos(1,5)) ,('Vystavkovyi_Tsentr',tiempo_en_segundos(3,0))],
                    'Vystavkovyi_Tsentr':[('Vasylkiivska',tiempo_en_segundos(3,0)) , ('Ipodrom',tiempo_en_segundos(1,20))],
                    'Ipodrom':[('Vystavkovyi_Tsentr',tiempo_en_segundos(1,20)) ,('Teremki',tiempo_en_segundos(2,10))],
                    'Teremki':[('Ipodrom',tiempo_en_segundos(2,10))],
                    'Syrets':[('Dorogozhychi',tiempo_en_segundos(2,0))],
                    'Dorogozhychi':[('Syrets',tiempo_en_segundos(2,0)) ,('Lukianivska',tiempo_en_segundos(3,5))],
                    'Lukianivska':[('Dorogozhychi',tiempo_en_segundos(3,5)) ,('Zoloti_Vorota',tiempo_en_segundos(4,30))],
                    'Zoloti_Vorota':[('Lukianivska',tiempo_en_segundos(4,30)) ,('Palats_Sportu',tiempo_en_segundos(1,25)),('Teatralna',tiempo_en_segundos(3,20))],
                    'Palats_Sportu':[('Zoloti_Vorota',tiempo_en_segundos(1,25)) ,('Klovska',tiempo_en_segundos(1,45)),('Ploshcha_Lva_Tolstoho',tiempo_en_segundos(3,20))],
                    'Klovska':[('Palats_Sportu',tiempo_en_segundos(1,45)) ,('Pecherska',tiempo_en_segundos(1,55))],
                    'Pecherska':[('Klovska',tiempo_en_segundos(1,55)) ,('Druzhby_Narodiv',tiempo_en_segundos(1,45))],
                    'Druzhby_Narodiv':[('Pecherska',tiempo_en_segundos(1,45)) ,('Vydubychi',tiempo_en_segundos(2,25))],
                    'Vydubychi':[('Druzhby_Narodiv',tiempo_en_segundos(2,25)) ,('Slavutych',tiempo_en_segundos(4,10))],
                    'Slavutych':[('Vydubychi',tiempo_en_segundos(4,10)) ,('Osokorky',tiempo_en_segundos(1,30))],
                    'Osokorky':[('Slavutych',tiempo_en_segundos(1,30)) ,('Pozniaky',tiempo_en_segundos(2,40))],
                    'Pozniaky':[('Osokorky',tiempo_en_segundos(2,40)) ,('Jarkivska',tiempo_en_segundos(2,40))],
                    'Jarkivska':[('Pozniaky',tiempo_en_segundos(2,40)) ,('Vyrlytsia',tiempo_en_segundos(1,50))],
                    'Vyrlytsia':[('Jarkivska',tiempo_en_segundos(1,50)) ,('Boryspilska',tiempo_en_segundos(2,0))],
                    'Boryspilska':[('Vyrlytsia',tiempo_en_segundos(2,0)) ,('Chervony_Jutir',tiempo_en_segundos(2,10))],
                    'Chervony_Jutir':[('Boryspilska',tiempo_en_segundos(2,10))]}
graph1 = Graph(Lista_de_adyacencias)


botones_l1 = []
botones_l2 = []
botones_l3 = []
m = [[0]*18,[0]*18,[0]*16]

paradas_nombres = {'Akademmistechko': 110,
                    'Zhytomyrska':111 ,
                    'Sviatoshyn':112,
                    'Nyvky':113,
                    'Beresteiska':114,
                    'Shuliavska':115,
                    'Politekhnichnyi_Instytut':116,
                    'Vokzalna':117,
                    'Universytet':118,
                    'Teatralna':119,
                    'Jreshchatyk':120,
                    'Arsenalna':121,
                    'Dnipro':122,
                    'Hidropark':123,
                    'Livoberezhna':124,
                    'Darnytsia': 125,
                    'Chernihivska':126,
                    'Lisova':127,
                    'Heroiv_Dnipra':210,
                    'Minska':211,
                    'Obolon':212,
                    'Pochaina':213,
                    'Tarasa_Sevchenka':214,
                    'Kontraktova_Polscha':215,
                    'Poschtova_Polscha':216,
                    'Maidan_Nezalezhnosti':217,
                    'Ploshcha_Lva_Tolstoho':218,
                    'Olimpiiska':219,
                    'Palats_Ukrania':220,
                    'Lybidska':221,
                    'Demiivska':222,
                    'Holosiivska':223,
                    'Vasylkiivska':224,
                    'Vystavkovyi_Tsentr':225,
                    'Ipodrom':226,
                    'Teremki':227,
                    'Syrets':310,
                    'Dorogozhychi':311,
                    'Lukianivska':312,
                    'Zoloti_Vorota':314,
                    'Palats_Sportu':315,
                    'Klovska':316,
                    'Pecherska':317,
                    'Druzhby_Narodiv':318,
                    'Vydubychi':319,
                    'Slavutych':321,
                    'Osokorky':322,
                    'Pozniaky':323,
                    'Jarkivska':324,
                    'Vyrlytsia':325,
                    'Boryspilska':326,
                    'Chervony_Jutir':327}


paradas_l3 = list(range(310,328))
del paradas_l3[3]
del paradas_l3[9]
paradas = [list(range(110,128)), list(range(210,228)), paradas_l3]

def nombres_a_numeros(nombres):
    numeros=[]
    for n in nombres:
        numeros.append(paradas_nombres[n])
    return numeros

def numero_a_nombre(n):
    nombres = list(paradas_nombres.keys())
    numeros = list(paradas_nombres.values())
    pos = numeros.index(n)
    return nombres[pos]

def calcular_ruta(origen, destino, hora):
    origen_nombre = numero_a_nombre(origen)
    destino_nombre = numero_a_nombre(destino)

    ahora = datetime.now()
    hora = ahora.hour

    ## ALGORITMO
    (ruta_nombres, t) = graph1.a_star_algorithm(origen_nombre, destino_nombre, 10, ahora.strftime("%A"))
    tiempo_label.config(text = tiempo_en_minitos(t))
    fecha_label.config(text= ahora.strftime("%c"))

    ruta = nombres_a_numeros(ruta_nombres)
    return ruta

def crear_boton(label, n): #Crea un boton con texto n que al ser pulsado cambia la etiqueta label por n
    return tk.Button(ventana, text = n, image = pixel, height = 10, width = 14, compound = 'c',command = lambda: cambiar_label(label, n))
def cambiar_label(label, n):
    label.config(text=n)
    eliminar_botones() #Despues de ser pulsado cualquier boton, se quitan todos de la ventana

def eliminar_botones(): #Quita todos los botones de la ventana y los elimina de las listas
    for i in range(len(botones_l1)):
        botones_l1[i].place_forget()
    for i in range(len(botones_l2)):
        botones_l2[i].place_forget()
    for i in range(len(botones_l3)):
        botones_l3[i].place_forget()
    del botones_l1[:]
    del botones_l2[:]
    del botones_l3[:]

def crear_botones(label):
    for i in range(18):  # Crea los botones de la l1
        botones_l1.append(crear_boton(label, i+110))
    for i in range(18): # Crea los botones de la l2
        botones_l2.append(crear_boton(label, i+210))
    for i in paradas_l3: # Crea los botones de la l3
        botones_l3.append(crear_boton(label, i))

def colocar_widgets(l1,l2,l3,decision): # Coloca los botones en la ventana exactamente en las posiciones (X, Y) de los pixeles que coinciden con su parada en la imagen de fondo
    #l1:
    for i in range(3):
        if (decision[0][i]==1):
            l1[i].place(x=105, y=260 + i * 29)
    for i in range(6):
        if (decision[0][i+3]==1):
            l1[i + 3].place(x=105 + i * 37, y=355)
    if (decision[0][9] == 1):
        l1[9].place(x=323, y=326)
    for i in range(3):
        if (decision[0][i+10]==1):
            l1[i + 10].place(x=375 + i * 47, y=312)
    for i in range(4):
        if (decision[0][i+13]==1):
            l1[i + 13].place(x=517 + i * 32, y=298 - i * 25)
    if (decision[0][17] == 1):
        l1[17].place(x=635, y=203)

    #l2:
    for i in range(8):
        if (decision[1][i]==1):
            l2[i].place(x=377, y=75 + i * 31)
    for i in range(5):
        if (decision[1][i+8]==1):
            l2[i + 8].place(x=375, y=368 + i * 43)
    for i in range(2):
        if (decision[1][i+13]==1):
            l2[i + 13].place(x=345 - i * 60, y=572)
    for i in range(3):
        if (decision[1][i+15]==1):
            l2[i + 15].place(x=233 - i * 43, y=572)
    #l3:
    for i in range(4):
        if (decision[2][i]==1):
            l3[i].place(x=221 + i * 30, y=169 + i * 45)
    if (decision[2][4] == 1):
        l3[4].place(x=398, y=368)
    for i in range(7):
        if (decision[2][i+5]==1):
            l3[i + 5].place(x=420 + i * 19, y=380 + i * 26)
    if (decision[2][12] == 1):
        l3[12].place(x=547, y=555)
    for i in range(3):
        if (decision[2][i+13]==1):
            l3[i+13].place(x=573 + i * 27, y=572)

def colocar_botones():
    colocar_widgets(botones_l1,botones_l2, botones_l3, [[1]*18,[1]*18,[1]*16])

def colocar_circulos(ruta): #Ruta es una lista de paradas
    for i in range(len(paradas)):
        for j in range(len(paradas[i])):
            if(paradas[i][j] in ruta):
                m[i][j] = 1
    colocar_widgets(circulos_l1, circulos_l2, circulos_l3, m)

def borrar_circulos():
    for i in range(len(circulos)):
        for j in range(len(circulos[i])):
            if(m[i][j]==1):
                circulos[i][j].place_forget()

def boton_fijar_origen(): # Pone en la etiqueta origen_label el texto que hay en origen_entry
    if(int(origen_entry.get()) in list(paradas_nombres.values())):
        origen_label.config(text = origen_entry.get())
def boton_fijar_destino(): # Igual con destino
    if (int(destino_entry.get()) in list(paradas_nombres.values())):
        destino_label.config(text = destino_entry.get())
def boton_fijar_hora():
    hora_label.config(text = hora_entry.get())

def boton_seleccionar_origen(): # Al pulsar "Seleccionar en el mapa", crea y coloca los botones que modifican la etiqueta origen_label
    crear_botones(origen_label)
    colocar_botones()
def boton_seleccionar_destino(): # Igual pero cambiando la etiqueta destino_label
    crear_botones(destino_label)
    colocar_botones()

def boton_calcular_ruta():
    colocar_circulos(calcular_ruta(origen_label.cget("text"),destino_label.cget("text"),hora_label.cget("text")))
    borrar_widgets()
    reiniciar.place(x=550, y=80)
    tiempo_text.place(x=600, y=350)
    tiempo_label.place(x=740, y=350)
    fecha_text.place(x=600, y=400)
    fecha_label.place(x=710, y=400)

def boton_reiniciar():
    reiniciar.place_forget()
    tiempo_text.place_forget()
    tiempo_label.place_forget()
    fecha_text.place_forget()
    fecha_label.place_forget()

    borrar_circulos()
    global m
    m = [[0] * 18, [0] * 18, [0] * 16]

    colocar_widgets_entrada()

def colocar_widgets_entrada():
    origen_text.place(x=750, y=60)
    origen_entry.place(x=800, y=60)
    fijar_origen.place(x=830, y=60)
    seleccionar_origen.place(x=750, y=82)
    destino_text.place(x=750, y=150)
    destino_entry.place(x=800, y=150)
    fijar_destino.place(x=830, y=150)
    seleccionar_destino.place(x=750, y=172)
    #hora_text.place(x=900, y=60)
    #hora_entry.place(x=990, y=60)
    #fijar_hora.place(x=1030, y=57)
    #hora_text2.place(x=900, y=425)
    #hora_label.place(x=985, y=425)
    origen_text2.place(x=700, y=430)
    origen_label.place(x=750, y=430)
    destino_text2.place(x=700, y=455)
    destino_label.place(x=750, y=455)
    boton_algoritmo.place(x=700, y=480)

def borrar_widgets():
    origen_text.place_forget()
    origen_entry.place_forget()
    fijar_origen.place_forget()
    seleccionar_origen.place_forget()
    destino_text.place_forget()
    destino_entry.place_forget()
    fijar_destino.place_forget()
    seleccionar_destino.place_forget()
    hora_text.place_forget()
    hora_entry.place_forget()
    fijar_hora.place_forget()
    hora_text2.place_forget()
    hora_label.place_forget()
    origen_text2.place_forget()
    origen_label.place_forget()
    destino_text2.place_forget()
    destino_label.place_forget()
    boton_algoritmo.place_forget()


ventana = tk.Tk()
ventana.geometry("959x630") # Mismo tamaño que el png
ventana.title("Metro Kiev")

imagen_metro = ImageTk.PhotoImage(imagen) # Poner ruta del png del plano del metro

fondo = tk.Canvas(ventana)
fondo.pack(fill="both", expand=True)
fondo.create_image(0, 0, image=imagen_metro, anchor="nw") # Creo y coloco la imagen del metro de fondo

pixel = tk.PhotoImage(width=1, height=1)

# Creo y coloco los botones labels y entrys para la seleccion de paradas (arriba):
origen_text = tk.Label(ventana, text ="Origen:")
origen_entry = tk.Entry(ventana, width = 4)
fijar_origen = tk.Button(ventana, text = "Fijar", command = boton_fijar_origen)
seleccionar_origen = tk.Button(ventana, text = "Seleccionar en el mapa", command = boton_seleccionar_origen)

destino_text = tk.Label(ventana, text ="Destino:")
destino_entry = tk.Entry(ventana, width = 4)
fijar_destino = tk.Button(ventana, text = "Fijar", command = boton_fijar_destino)
seleccionar_destino = tk.Button(ventana, text = "Seleccionar en el mapa", command = boton_seleccionar_destino)

hora_text = tk.Label(ventana, text ="Hora de salida:")
hora_entry = tk.Entry(ventana, width = 6)
fijar_hora = tk.Button(ventana, text = "Fijar", command = boton_fijar_hora)

# Creo y coloco las etiquetas con la informacion que va a usar el algoritmo (abajo):
hora_text2 = tk.Label(ventana, text ="Hora de salida:")
hora_label = tk.Label(ventana)

origen_text2 = tk.Label(ventana, text ="Origen:")
origen_label = tk.Label(ventana)

destino_text2 = tk.Label(ventana, text ="Destino:")
destino_label = tk.Label(ventana)

#Boton que inicia el algoritmo:
boton_algoritmo = tk.Button(ventana, text = "Calcular la ruta más corta", command = boton_calcular_ruta)

#Creo circulos amarillos por cada parada que representaran la ruta obtenida por el algoritmo:
circulos_l1 = []
for i in range(18):
    circulo = tk.Canvas(ventana, width=21, height=17, bg="red")
    circulo.create_oval(2, 2, 21, 17, fill="yellow")
    circulo.create_text(11, 11, font = ("Purisa",7), text=i+110)
    circulos_l1.append(circulo)
circulos_l2 = []
for i in range(18):
    circulo = tk.Canvas(ventana, width=21, height=17, bg="blue")
    circulo.create_oval(2, 2, 21, 17, fill="yellow")
    circulo.create_text(11, 11, font = ("Purisa",7), text=i+210)
    circulos_l2.append(circulo)
circulos_l3 = []
for i in paradas_l3:
    circulo = tk.Canvas(ventana, width=21, height=17, bg="green")
    circulo.create_oval(2, 2, 21, 17, fill="yellow")
    circulo.create_text(11, 11, font = ("Purisa",7), text=i)
    circulos_l3.append(circulo)
circulos = [circulos_l1,circulos_l2,circulos_l3]

reiniciar = tk.Button(ventana, text = "Calcular otra ruta", command = boton_reiniciar)
tiempo_text = tk.Label(ventana, text = "Tiempo estimado de ruta:")
tiempo_label = tk.Label(ventana)
fecha_text = tk.Label(ventana, text = "Ruta calculada para:")
fecha_label = tk.Label(ventana)

colocar_widgets_entrada()

ventana.mainloop()