
import random
import heapq
import math


class Taquin:
    def __init__(self, etat_initial):
        self.etat_initial = etat_initial
        self.dimension = int(math.sqrt(len(etat_initial)))

    def est_etat_final(self, etat):
        return etat == tuple(range(self.dimension ** 2))

    def actions_possibles(self, etat):
        actions = []
        index_case_vide = etat.index(0)
        x, y = index_case_vide // self.dimension, index_case_vide % self.dimension

        if x > 0:
            actions.append(-self.dimension)  # Déplacement vers le haut
        if x < self.dimension - 1:
            actions.append(self.dimension)  # Déplacement vers le bas
        if y > 0:
            actions.append(-1)  # Déplacement vers la gauche
        if y < self.dimension - 1:
            actions.append(1)  # Déplacement vers la droite

        return actions

    def appliquer_action(self, etat, action):
        index_case_vide = etat.index(0)
        index_case_adjacente = index_case_vide + action
        etat = list(etat)
        etat[index_case_vide], etat[index_case_adjacente] = etat[index_case_adjacente], etat[index_case_vide]
        return tuple(etat)

    def est_etat_valide(self, etat):
        inversions = 0
        for i in range(len(etat)):
            if etat[i] != 0:
                for j in range(i):
                    if etat[j] > etat[i]:
                        inversions += 1
        return inversions % 2 == 0

    def trouver_solution(self):
        etats_explores = set()
        etats_a_explorer = [(0, self.etat_initial)]
        while etats_a_explorer:
            cout, etat_courant = heapq.heappop(etats_a_explorer)
            if self.est_etat_final(etat_courant):
                return cout
            etats_explores.add(etat_courant)
            for action in self.actions_possibles(etat_courant):
                nouvel_etat = self.appliquer_action(etat_courant, action)
                if nouvel_etat not in etats_explores and self.est_etat_valide(nouvel_etat):
                    nouveau_cout = cout + 1
                    heapq.heappush(etats_a_explorer, (nouveau_cout + self.heuristique(nouvel_etat), nouvel_etat))
        return -1

    def heuristique(self, etat):
        distance_manhattan = 0
        for i in range(self.dimension ** 2):
            if etat[i] != 0:
                x, y = i // self.dimension, i % self.dimension
                x_final, y_final = etat[i] // self.dimension, etat[i] % self.dimension
                distance_manhattan += abs(x - x_final) + abs(y - y_final)
        return distance_manhattan

    def afficher_taquin(self, etat):
        for i in range(self.dimension):
            for j in range(self.dimension):
                print(etat[i * self.dimension + j], end="\t")
            print()
        print()

    def resoudre_taquin(self):
        print("Taquin initial :")
        self.afficher_taquin(self.etat_initial)

        solution = self.trouver_solution()
        if solution == -1:
            print("Pas de solution possible.")
        else:
            etats_explores = set()
            etats_a_explorer = [(0, self.etat_initial)]
            while etats_a_explorer:
                cout, etat_courant = heapq.heappop(etats_a_explorer)
                if self.est_etat_final(etat_courant):
                    print("Solution trouvée :")
                    self.afficher_taquin(etat_courant)
                    break
                etats_explores.add(etat_courant)
                for action in self.actions_possibles(etat_courant):
                    nouvel_etat = self.appliquer_action(etat_courant, action)
                    if nouvel_etat not in etats_explores and self.est_etat_valide(nouvel_etat):
                        nouveau_cout = cout + 1
                        heapq.heappush(etats_a_explorer, (nouveau_cout + self.heuristique(nouvel_etat), nouvel_etat))
            print("Nombre de mouvements nécessaires pour résoudre le taquin :", solution)

dimension = 3
etat_initial = list(range(dimension**2))
random.shuffle(etat_initial)
taquin = Taquin(tuple(etat_initial))
taquin.resoudre_taquin()


