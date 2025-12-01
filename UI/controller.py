import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """
        # TODO

        try:
            soglia = float(self._view.guadagno_medio_minimo.value)
        except ValueError:
            self._view.show_alert("Inserisci un numero valido")
            return


        self._model.costruisci_grafo(soglia)
        numero_edges=self._model.get_num_edges()
        numero_nodes = self._model.get_num_nodes()
        tratte =self._model.get_all_edges()

        tratte_filtrate=[]
        for (u,v), peso in tratte.items():
            if peso >= soglia:
                tratte_filtrate.append (((u, v), peso))

        self._view.lista_visualizzazione.controls.clear()
        self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di hub: {numero_nodes}"))
        self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di tratte: {numero_edges}"))
        self._view.lista_visualizzazione.controls.append(ft.Text("Tratte che superano la soglia:"))

        for (u, v), peso in tratte_filtrate:
            self._view.lista_visualizzazione.controls.append(ft.Text(f"{u} -->  {v} : {peso}"))

        self._view.lista_visualizzazione.update()




