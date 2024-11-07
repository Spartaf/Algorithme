from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import random
import sv_ttk
from Algo_visu import Bubble_sort


# Fonction

data = []

def draw_data(data, color):
    Canvas.delete("all")
    canvas_height = 560
    canvas_width = 1175
    x_width = canvas_width / (len(data))
    offset = 0
    spacing_rect = 0 
    max_data = max(data)
    normalized_data = [i/max_data for i in data]
    for i, height in enumerate(normalized_data):
        x0 = i*x_width +offset + spacing_rect
        y0 = canvas_height - height*530

        x1 = (i+1) * x_width
        y1 = canvas_height

        Canvas.create_rectangle(x0,y0,x1,y1, fill = color[i])
        if len(data)<=50:
            Canvas.create_text(x0+(x_width/2), y0-4, text = str(data[i]), font=("Arial", "15", "bold"))

    window.update_idletasks()

def generate():
    #tirons data aléatoiremet
    try:
        nb_value = int(nb_val.get())
    except:
        nb_value = 100
    
    try:
        max_value = int(max_val.get())
    except:
        max_value = 1000
    
    if max_value < 0:
        max_value = 0
    if max_value > 10000:
        max_value = 10000

    if nb_value <= 0:
        nb_value = 2
    if nb_value > 1500:
        nb_value = 1500
    

    global data
    data = [random.randint(0, max_value) for i in range(nb_value)]

    draw_data(data, ['red' for i in range(len(data))])


def start_sorting():
    global data

    Bubble_sort(data, draw_data, speed_scale.get())


# Initialisation de la fenêtre
window = ThemedTk("dark")
window.title('Sorting Algorithm Visualizer')
window.geometry("1200x800")
# Changement automatique de theme vers sun-valley
sv_ttk.set_theme("dark")


# Variable de l'algoritme a visusaliser
selected_algorithm = StringVar()
# Liste des différents algoritmes
List_algo = ["Bubble sort", "Selection sort" ,"Insersion sort","Merge sort", "Quick sort"]


# Selection de l'algorithme

select_algo_label = Label(
    master = window,
    text ="Algorithm : ", 
    font=("Arial", "16", "bold"), 
    width=10,
    padx= 7, pady= 7)
select_algo_label.place(x = 0, y = 0)

select_algo_menu = ttk.Combobox(
    master = window, 
    font = ("Arial", "16"), 
    width = "15", 
    state = "readonly",
    textvariable = selected_algorithm,
    values=List_algo)

select_algo_menu.focus()

select_algo_menu.place(x = 145, y = 4)
select_algo_menu.current(0)


# Bouton de lancement 

sorting_button = Button(
    master= window,
    text = "Start Sorting",
    width= 20,
    font = ("Arial", "16", "bold"),
    bd=5,
    command= start_sorting,
)
sorting_button.place(x = 500, y = 4)

# Bouton pour generer les nombres(bar)

generate_button = Button(
    master = window,
    text = "Generate random",
    width= 20,
    bd=5,
    font = ("Arial", "16", "bold"),
    command=generate
)
generate_button.place(x = 800, y = 4)


# Curseur pour la vitesse de l'algo
speed_label = Label(
    master = window,
    text ="speed", 
    font=("Arial", "14","bold"), 
    fg="black",
    width=17,
    bg="white",
    )
speed_label.place(x = 89, y = 80)

speed_scale = Scale(
    master=window,
    from_=0.1,
    to=5.0,
    length= 200,
    font=("Arial", "14","bold"),
    fg="black",
    orient=HORIZONTAL,
    resolution=1,

    bd= 4,
    bg="white"
)
speed_scale.place(x = 89, y=110 )

# Maximum des valeur

max_label = Label(
    master = window,
    text ="Max (0, 10000)", 
    font=("Arial", "14","bold"), 
    fg="black",
    width=17,
    bg="white",
    bd = 3
    )
max_label.place(x = 360, y = 80)

max_val = StringVar() 
max_entry = Entry(
    master=window,
    textvariable= max_val,
    bg="white",
    width=19,
    fg="black",
    font=("Arial", "14","bold"),
    insertbackground="black"
)
max_entry.place(x = 360, y = 115)

# Nombre de valeurs

nb_val_label = Label(
    master = window,
    text ="nb val (0, 1000)", 
    font=("Arial", "14","bold"), 
    fg="black",
    width=17,
    bg="white",
    bd = 3
    )
nb_val_label.place(x = 580, y = 80)

nb_val = StringVar() 
nb_val_entry = Entry(
    master=window,
    textvariable= nb_val,
    bg="white",
    width=19,
    fg="black",
    font=("Arial", "14","bold"),
    insertbackground="black"
)
nb_val_entry.place(x = 580, y = 115)

# Canvas

Canvas = Canvas(
    master= window,
    width=1175,
    height=560,
    bg="white"

)
Canvas.place(x=10, y =220)

# lancement
window.mainloop()

