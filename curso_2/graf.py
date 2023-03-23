import matplotlib.pyplot as plt # libreria para graficas

def pie_tor(labels, values):
    fig, ax = plt.subplots()
    """
    Aqui se define la figura a realizar y los ejes de la grafica
    con subplots()
    """
    ax.pie(values,labels=labels)
    """
    Aqui se le dice que tipo de grafica se quiere realizar
    con ax.pie() en este caso es un grafico de torta
    """
    ax.axis('equal')
    """
    Aqui se le dije que el eje va a ser para una grafica de torta 
    """
    plt.show()


if __name__ == "__main__":
  labels = ["a", "b", "c"]
  values = [100,200,80]
  pie_tor(labels, values)