import copy

# BUBBLE SORT   --- O(n^2) ---
#               --- 0(n) ---
#               --- O~(n^2) ---
#               --- Stable ---
#               --- Moyennement rapide ---

""" On compare tous les éléments conjoints deux à deux,
on s'arrete lorsque plus aucune permutation n'est possible le tableau est donc trié"""

def Bubble_sort(tab):
    permute = True
    while permute == True:
        # On a encore rien permurté
        permute = False
        for i in range(len(tab)-1):
            # On compare l'élément courant avec son conjoint
            if tab[i] > tab[i+1]:

                # On permute les deux éléments
                tmp = tab[i]
                tab[i] = tab[i+1]
                tab[i+1] = tmp

                # On a permuté 
                permute = True


#######################################################################################################
#######################################################################################################
#######################################################################################################


# SELECTION SORT   --- O(n^2) ---
#                  --- 0(n^2) ---
#                  --- 0~(n^2) ---
#                  --- Instable ---
#                  --- Lent ---

""" Pour chaque indice on cherche le minimum entre i et la fin et on permute min et i """

def get_min(tab, istart, iend):
    """ recherche le minimum entre les indices istart et iend"""
    imin = istart
    i = istart + 1
    while (i <= iend):
        if tab[i] < tab[imin]:
            imin = i
        i += 1
    return imin

def Selection_sort(tab):
    for i in range(len(tab) - 1):

        # On recherche l'indice du min entre i et la fin
        imin = get_min(tab, i, len(tab)-1)

        # On verifie que mini n'est pas à la position courante sinon il serait deja bien placé
        if imin != i:
            # On permute le min avec la position courant, tout ce qu'il y a avant est deja trié
            tmp = tab[i]
            tab[i] = tab[imin]
            tab[imin] = tmp


def Selection_sort_compact(tab):
    for i in range(len(tab) - 1):
        imin = i
        for j in range(i+1, len(tab)):
            if tab[j] < tab[imin]:
                imin = j
    
        # On permute indice minimun et indice courant
        tmp = tab[i]
        tab[i] = tab[imin]
        tab[imin] = tmp



#######################################################################################################
#######################################################################################################
#######################################################################################################




# INSERTION SORT   --- O(n^2) ---
#                  --- 0(n) ---
#                  --- O~(n^2) ---
#                  --- Stable ---
#                  --- Moyennement rapide ---


"""Pour chaque élément on tri le tableau à sa gauche en le placant dedans"""


def Insertion_sort(tab):
    for i in range(len(tab)):
        tmp = tab[i]
        # décaler tous les éléments T[0]...T[i-1] qui sont plus grands que tmp, en partant de T[i-1]
        j = i
        while j > 0 and tab[j-1] > tmp:
            tab[j] = tab[j-1]
            j -= 1
        # Placer tmp dans le trou laissé par le décalage 
        tab[j] = tmp



#######################################################################################################
#######################################################################################################
#######################################################################################################



# MERGE SORT   --- O(nlogn) ---
#              --- 0(nlogn) ---
#              --- O~(nlogn) ---
#              --- Stable ---
#              --- rapide ---

""" Diviser le tableau en deux a peut pret égal et appeler le tri sur chacune des deux sous liste (diviser pour reigner)
on fusionne ensuite les sous listes obtenues"""

def Merge_Sort(tab):
    if len(tab)>1:
        mid = len(tab)//2
        left = tab[:mid]
        right = tab[mid:]

        Merge_Sort(left)
        Merge_Sort(right)

        i=j=k=0  

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                tab[k] = tab[i]
                i+=1
            else:
                tab[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            tab[k]=left[i]
            i+=1
            k+=1

        while j < len(right):
            tab[k]=right[j]
            j=j+1
            k=k+1




#######################################################################################################
#######################################################################################################
#######################################################################################################


# TAS SORT     --- O(nlogn) ---
#              --- 0(nlogn) ---
#              --- O~(nlogn) ---
#              --- Instable ---
#              --- rapide ---

""" Création d'un tas (arbre parfait croissant) à partir de la liste puis suppression successive du minimum (racine) """

def inserer(tab,elt):
    tab.append(elt)
    
    fils = len(tab)-1
    pere = (fils-1)//2
    
    while pere >= 0 and tab[pere] > tab[fils]:
        tab[pere], tab[fils] = tab[fils],tab[pere]
        fils = pere
        pere = (fils-1)//2

def tamiser(tab):
    fin = False
    pere = 0
    fils = 2*pere + 1
    while fils < len(tab) and not fin:
        
        if fils < len(tab)- 1 and tab[fils + 1] < tab[fils]:
            fils += 1
        if tab[pere] > tab[fils]:
            tab[pere], tab[fils] = tab[fils],tab[pere]
            pere = fils
            fils = 2*pere +1 
        else:
            fin = True


def Heap_sort(tab):
    heap = []
    res = []
    
    for i in tab:
        inserer(heap, i)
    
    while heap != []:
        res.append(heap[0])
    
        heap[0], heap[-1] = heap[-1], heap[0]
        heap.pop()
        tamiser(heap)
    return res



#######################################################################################################
#######################################################################################################
#######################################################################################################


# QUICK SORT   --- O(n^2) ---
#              --- 0(nlogn) ---
#              --- O~(nlogn) ---
#              --- Instable ---
#              --- rapide ---


# Pas en place
def partion(tab , l1, l2):
    pivot = tab[0]
    for y in tab[1:]:
        if y > pivot:
            l2.append(y)
        else:
            l1.append(y)

def Quicksort(tab):
    if len(tab) > 1:
        l1 = []
        l2 = []
        l3 = []
        l3.append(tab[0])
        partion(tab, l1, l2)
        return Quicksort(l1) + l3 + Quicksort(l2)
    return tab


# En place
def partitionner(tab, debut, fin):
    valeur_pivot = tab[fin]
    indice_pivot = debut

    for i in range(debut, fin):
        if tab[i] <= valeur_pivot:
            tab[i], tab[indice_pivot] = tab[indice_pivot], tab[i]
            indice_pivot+=1

    tab[indice_pivot], tab[fin] = tab[fin], tab[indice_pivot]
    return indice_pivot


def Quicksort_place(tab, debut = 0 , fin = None):
    if fin == None:
        fin = len(tab) -1
    
    if fin > debut:

        pivot = partitionner(tab, debut, fin)
        Quicksort_place(tab,debut, pivot-1)
        Quicksort_place(tab, pivot + 1, fin)


#######################################################################################################
#######################################################################################################
#######################################################################################################


# TIMSORT      --- O(nlogn) ---
#              --- 0(n) ---
#              --- O~(nlogn) ---
#              --- Stable ---
#              --- rapide ---

def merge(left, right):
    tab= []
    i=j=k=0  

    while i < len(left) and j < len(right):
        
        if left[i] < right[j]:
            tab.append(left[i])
            i+=1
        else:
            tab.append(right[j])
            j+=1
        k+=1


    while i < len(left):
        tab.append(left[i])
        i+=1
        k+=1

    while j < len(right):
        tab.append(right[j])
        j=j+1
        k=k+1
    return tab

    
def Insertion_Timsort(tab, left=0, right=None):
    if right is None:
        right = len(tab) - 1

    for i in range(left + 1, right + 1):
        tmp = tab[i]
        # décaler tous les éléments T[0]...T[i-1] qui sont plus grands que tmp, en partant de T[i-1]
        j = i
        while j > left and tab[j-1] > tmp:
            tab[j] = tab[j-1]
            j -= 1
        # Placer tmp dans le trou laissé par le décalage 
        tab[j] = tmp


def Timsort(array):
    min_run = 32
    n = len(array)

    for i in range(0, n, min_run):
        Insertion_Timsort(array, i, min((i + min_run - 1), n - 1))
    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))
            merged_array = merge(
                array[start:midpoint + 1],
                array[midpoint + 1:end + 1])
            array[start:start + len(merged_array)] = merged_array
        size *= 2

    return array



#######################################################################################################
#######################################################################################################
#######################################################################################################



# COUNT SORT   --- O(n) ---
#              --- 0(n) ---
#              --- O~(n) ---
#              --- rapide ---

def Count_Sort(tab):
    maxVal = max(tab)
    res = [0 for i in range(maxVal+1)]

    for i in tab:
        res[i]+=1
    
    k = 0
    for i in range(len(res)):
        for j in range(res[i]):
            tab[k] = i
            k += 1



















# Vérification des temps et complexités

import random
import time
import matplotlib.pyplot as plt 
import numpy as np

N = 100000000

#tab1 = random.sample(range(0, 1000000), N)
tab1 = np.random.randint(low=0, high=N, size= N).tolist()
tab2 = tab1.copy()
tab3 = tab1.copy()
tab4 = tab1.copy()

start = time.time()
Count_Sort(tab1)
end = time.time()
time_tim = end - start
print(time_tim)



