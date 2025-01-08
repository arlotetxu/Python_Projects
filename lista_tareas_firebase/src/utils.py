

def get_field_values(collection, field):
    """
    - Descripción:
        - Obtiene los valores del campo pasado en el parámetro 'field' de la colección.
    - Parámetros:
        - Collection: Coleccion de datos de Firestore.
        - Field: campo de la colección del que se quieren obtener los valores
    - Retorno:
        - values: lista con los diferentes valores obtenidos.
    """
    values = []
    all_data = collection.stream()
    for data in all_data:
        field_value = data.to_dict().get(field)
        if field_value:
            values.append(field_value)
    return values
