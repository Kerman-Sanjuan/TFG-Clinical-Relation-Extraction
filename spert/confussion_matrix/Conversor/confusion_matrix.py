import json
from mlxtend.plotting import plot_confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
import sys


class compute_matrix:

    def __init__(self, origen, destination):
        self.origen = origen
        self.destination = destination
        self.ner_matrix = [[]]
        self.re_matrix = [[]]
        self.lista_de_relaciones = []
        self.lista_de_palabras = []
        self.lista_de_palabras_indices = {}
        self.lista_de_relaciones_indices = {}
        self.lista_de_cordenadas = []
        with open(self.origen) as f:
            self.real_dict = json.load(f)
        with open(self.destination) as f2:
            self.predicted_dict = json.load(f2)

    def inicializar_matrices(self):
        # NER
        for phrase in self.real_dict:

            for entity in phrase["entities"]:
                if entity["type"] not in self.lista_de_palabras:
                    self.lista_de_palabras.append(entity["type"])
                 # Con esto sabemos que diferentes entidades corresponden al conjunto de datos.
            for relation in phrase["relations"]:
                if relation["type"] not in self.lista_de_relaciones:
                    self.lista_de_relaciones.append(relation["type"])

        aux = list(self.lista_de_relaciones)
        aux.append("None")
        self.lista_de_relaciones = aux

        aux = list(self.lista_de_palabras)
        aux.append("None")
        self.lista_de_palabras = aux
        # Ahora creamos los indices
        i = 0
        for palabras in self.lista_de_palabras:
            self.lista_de_palabras_indices[palabras] = i
            i += 1
        j = 0
        for relaciones in self.lista_de_relaciones:
            self.lista_de_relaciones_indices[relaciones] = j
            j += 1

        self.ner_matrix = [[0 for i in range(
            len(self.lista_de_palabras))] for j in range(len(self.lista_de_palabras))]
        self.re_matrix = [[0 for i in range(len(self.lista_de_relaciones))] for j in range(
            len(self.lista_de_relaciones))]

        # RE

    def calculate_ner(self):
        for idx, p in enumerate(self.predicted_dict):
            for entity in p["entities"]:
                ent_cord = (entity["start"], entity["end"])
                print(self.lista_de_palabras_indices)
                self.anadir_a_matriz(ent_cord, entity["type"], idx)
                # Ahora en el caso que se encuentre
                self.anadir_a_matriz_izquierda(idx)

    def anadir_a_matriz(self, ent_cord, ent_type, index):
        # Saber si las cordenadas existen y en ese caso decidir donde colocarlo.

        frase = self.real_dict[index]
        anadido = False
        for entity in frase["entities"]:
            # Significa que es la misma palabra
            if ent_cord == (entity["start"], entity["end"]):
                self.ner_matrix[self.lista_de_palabras_indices[entity["type"]]
                                ][self.lista_de_palabras_indices[ent_type]] += 1
                anadido = True

        if not anadido:
            print("Este se va a none")
            self.ner_matrix[self.lista_de_palabras_indices["None"]
                            ][self.lista_de_palabras_indices[ent_type]] += 1

    def anadir_a_matriz_izquierda(self, idx):
        esta = False
        for entity in self.real_dict[idx]["entities"]:
            ent_cord = (entity["start"], entity["end"])
            for entidad in self.predicted_dict[idx]["entities"]:
                if ent_cord == (entidad["start"], entidad["end"]):
                    esta = True
            if not esta:
                self.ner_matrix[self.lista_de_palabras_indices[entity["type"]]
                                ][self.lista_de_palabras_indices["None"]] += 1

    def calculate_re(self):
        """ Calcula RE, se da por valido si la relacion es correctamente clasificada y los elementos que la componen son los mismos"""
        for idx, p in enumerate(self.predicted_dict):
            for relation in p["relations"]:
                rel_cord = (relation["head"], relation["tail"])
                self.anadir_a_matriz_re(rel_cord, relation["type"], idx)
                # Ahora en el caso que se encuentre
                self.anadir_a_matriz_izquierda_re(idx)

    def anadir_a_matriz_re(self, re_cord, ent_type, index):
        frase = self.real_dict[index]
        anadido = False
        for relation in frase["relations"]:
            # Significa que es la misma palabra
            if re_cord == (relation["head"], relation["tail"]):
                self.re_matrix[self.lista_de_relaciones_indices[relation["type"]]
                               ][self.lista_de_relaciones_indices[ent_type]] += 1
                anadido = True

        if not anadido:
            
            print(re_cord)
            print(frase)
            self.re_matrix[self.lista_de_relaciones_indices["None"]
                           ][self.lista_de_relaciones_indices[ent_type]] += 1

    def anadir_a_matriz_izquierda_re(self, idx):
        esta = False
        for relation in self.real_dict[idx]["relations"]:
            ent_cord = (relation["head"], relation["tail"])
            for entidad in self.predicted_dict[idx]["relations"]:
                if ent_cord == (relation["head"], relation["tail"]):
                    esta = True
            if not esta:
                print("Este se va a none izquierda ")
                self.re_matrix[self.lista_de_relaciones_indices[relation["type"]]
                               ][self.lista_de_relaciones_indices["None"]] += 1

    def mostrar_matriz(self):

        # Your Confusion Matrix
        cm = np.array(self.ner_matrix)

        # Classes
        classes = self.lista_de_palabras

        figure, ax = plot_confusion_matrix(conf_mat=cm,
                                           class_names=classes,
                                           colorbar=True,
                                           )

        plt.show()

        cm_ner = np.array(self.re_matrix)
        classes = self.lista_de_relaciones
        figure2, ax2 = plot_confusion_matrix(conf_mat=cm_ner,
                                             class_names=classes,
                                             colorbar=True,
                                             )
        plt.show()
    # Tenemos que saber si estas cordenadas existen.

    def compute(self):
        # Primero inicializamos ambas matrices.
        self.inicializar_matrices()

        self.calculate_ner()
        print(self.ner_matrix)

        self.calculate_re()
        print(self.re_matrix)

        self.mostrar_matriz()
