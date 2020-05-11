import hangmanModificado
import tictactoeModificado
import pickle
import PySimpleGUI as sg

def guardar (archivo, juegos):
     d={}
     d["Nombre"]= input("Ingrese nombre del jugador para tener un registro de a que juego/s acaba de jugar: ") 
     d["Juegos jugados"]= juegos
     with open(archivo, 'wb') as archdatos:
          pickle.dump(d,archdatos)
     print("Datos guardados!!!")

def leer (archivo):      #esta funcion no la pedia el enunciado, pero la uso para comprobar que los datos se guardaron.
     with open(archivo, 'rb') as archdatos:
          contenido= pickle.load(archdatos)
     print("El jugador {} jugó en total {} juegos.".format(contenido["Nombre"], len(contenido["Juegos jugados"])))
     for juego in contenido["Juegos jugados"]:
          print("Jugó al juego: "+ juego)


sg.change_look_and_feel("DarkGrey5")
layout = [[sg.Text("Elegí con qué juego querés jugar:", size=(34, 2))],
              [sg.Button('Ahorcado',size=(10,2)),sg.Button('Ta-TE-TI',size=(10,2)), sg.Button('Salir',size=(10,2))]]

def main(args):
     window = sg.Window("Menu de juegos",layout, text_justification='center')
     window.Finalize()
     jugados=[]
     sigo_jugando = True
     while sigo_jugando:
          event = window.read()[0]
          if ((event is None) or (event is "Salir")):
               sigo_jugando = False
          elif event == "Ahorcado":
               sg.Popup('El juego: {} se ejecutara en la consola de python'.format(event), title="Nuevo juego elegido.")
               hangmanModificado.main()
               sg.Popup("Juego terminado!",
                               "volviendo al menu de juegos.")
          elif event == "Ta-TE-TI":
               sg.Popup('El juego: {} se ejecutara en la consola de python'.format(event), title="Nuevo juego elegido.")
               tictactoeModificado.main()
               sg.Popup("Juego terminado!",
                               "volviendo al menu de juegos.")
          if  (((event != "Salir") and (event != None)) and (not(event in jugados))):
               jugados.append(event)
     window.close()
     guardar("DatosDeJuegoPickle.pickle", jugados)
     print()
     leer("DatosDeJuegoPickle.pickle")
     
if __name__ == '__main__':
     import sys
     sys.exit(main(sys.argv))


