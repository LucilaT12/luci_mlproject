from mlproject.distance import haversine

def test_type_of_haversine():
    assert type(haversine(2, 0, 0, 0)) == float
    
# esto es recomendable que lo agregue para que en la terminal me diga donde esta el error
# esta funcion se llama a si misma y ejecuta lo que esta despues del if
if __name__ == "__main__":
    test_type_of_haversine()