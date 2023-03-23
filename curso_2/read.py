import csv

def read_csv(path):
   with open(path, "r") as csvfile: 
        """
        with es una estructura de control que lo que hace es decirle que abra
        archivo y despues de la ejecucion del codigo lo cierre
        """

        reader = csv.reader(csvfile, delimiter= ",")
        header = next(reader) 
        """
        Con next se le dice que creea un  lista que puede iterar segun 
        los renglones que uno desee
        """
        
        data = []
    #print(header)
        for row in reader:
            #print(row)
            iterable = zip(header, row)
            # print(list(iterable))
            """Aqui zip lo que hace es crear un lista de tuplas en este caso los 
            valores de la tuplas son el nombre de la columna  y su valor. y como
            aqui se esta iterando se hace por cada renglon
            """

            custumer_ditc = {key : value for key, value in iterable}
            #print(custumer_ditc)

            """
            Para este dictionay comprenhention primero se le da la estructura
            (key : value), leugo se le dice que cree el diccionario apartir
            de las de las lista de tuplas[(a,b), (c,d)] creadas con iterable 
            (for key, value in iterable) donde le dice que key es el primer 
            parametro de la tupla (a) y value es es segundo valor de la tupla
            (b), y asi sucesivamente para cada lista (renglon) de tuplas 
            """
            data.append(custumer_ditc)

        return data
    


if __name__ == "__main__ ":
    data = read_csv("/Users/santiagoquintero/Documents/python/reto_platzi/curso_2/Customers.csv")
    print(data)
"""
Esto se utiliza para decirle que este modulo lo corra como un script
"""