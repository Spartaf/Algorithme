import time
def Bubble_sort(tab, drawdata, timetick):
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
                drawdata(tab, ["yellow" if k == i or k == i+1 else "red" for k in range(len(tab))])
                time.sleep(5-timetick)


                # On a permuté 
                permute = True
    drawdata(tab, ["yellow" for i in range(len(tab))])