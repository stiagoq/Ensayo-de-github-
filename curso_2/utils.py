import read
import graf


def age_custumers(data, gender):
    new_data = data.copy()

    if str(gender).capitalize() == "Female":
        gende_list = list(filter(lambda item: item["Gender"] == str(gender).capitalize(), new_data))
        
    
    elif str(gender).capitalize() == "Male":
        gende_list = list(filter(lambda item: item["Gender"] == str(gender).capitalize(), new_data))

        """
        Aqui se crea una lista y se filtar por genero en este. en la lambda function se le dice 
        que  la columna a utilizar es Gender(item["Gender"]) de Custumers.csv y que esta columna
        se va a filtrar por el genero ("Female or Male)
        """
    
    custumers_id = list(map(lambda x : x["CustomerID"], gende_list))
    """
    Aqui se crea una lista con con map que contenga la columna customerID  con la lambda funtion 
    (x["CustomerID"]).
    """
    custumers_age = list(map(lambda x : int(x["Age"]), gende_list))
    """
     Aqui se crea una lista con con map que contenga la columna Age  con la lambda funtion 
    (x["Age]) adicinalment se le dige que la lista sea numero y no strings
    """
    custumers_dict = dict(zip(custumers_id, custumers_age))
    """
    Aqui se crea un diccionario apartir de las lista de tuplas creadas con zip
    """

    return custumers_dict



def clasi_age(dictionary):
    cust_age = list(dictionary.values())
    """
    Aqui se crea una lista con los valores del dicionario (custumers_dict)
    """
    men_age = list(filter(lambda x :  True if x >0 and x <18 else False, cust_age )) 
    adol_age = list(filter(lambda x :  True if x >=18 and x < 35 else False, cust_age )) 
    adul_age = list(filter(lambda x :  True if x >=35 and x <= 60 else False, cust_age )) 
    may_age = list(filter(lambda x :  True if x >60 else False, cust_age )) 
    """
    Aqui se crean filtros para para clasificar la edad de los hombres o mujeres que 
    compram en la tienda 
    """

    labels = ["menores", "adolecentes", "adultos", "adulto_mayor"]
    values = [len(men_age), len(adol_age), len(adul_age), len(may_age)]
    print(values)
    """
    Aqui se crea un diccionario con las etiquetas de las clasificaciones (key) y los valores del
    diccionario van a ser la cantidad de datos en cada una de las clasificaciones.
    """

    return labels , values

if __name__ == '__main__':
    data = read.read_csv("//Users/santiagoquintero/Documents/python/reto_platzi/curso_2/Customers.csv")
    gender = input('Genero a consultar => ')
    dictionary = age_custumers(data,gender)
    labels, values = clasi_age(dictionary)
    graf.pie_tor(labels,values)
