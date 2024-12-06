import numpy as np

def correct_family_history(value):
    """
    Limpia la columna 'Family History of Mental Illness' asegurando que solo contenga 'Yes' o 'No'.
    """
    if isinstance(value, str):
        value = value.strip().lower()  # Convertir a minúsculas y eliminar espacios innecesarios
        if 'yes' in value:
            return 'Yes'
        elif 'no' in value:
            return 'No'
        elif 'sey' in value:  # Caso específico de 'sey' que debería ser 'Yes'
            return 'Yes'
        elif 'on' in value:  # Caso específico de 'on' que debería ser 'No'
            return 'No'
    return np.nan  # Si no es una cadena válida, devolvemos NaN

def sleep_duration_to_hours(sleep_duration):
    """
    Convierte los valores de 'Sleep Duration' a horas numéricas.
    """
    if isinstance(sleep_duration, str):
        if '5-6' in sleep_duration:
            return 5.5  # Promedio de 5-6 horas
        elif 'Less than 5' in sleep_duration:
            return 4.5  # Promedio para "Menos de 5 horas"
        elif '7-8' in sleep_duration:
            return 7.5  # Promedio de 7-8 horas
        elif 'More than 8' in sleep_duration:
            return 9.5  # Promedio para "Más de 8 horas"
    elif isinstance(sleep_duration, (float, int)):
        return sleep_duration  # Si ya es un número, devolvemos el valor tal como está
    return np.nan  # Si no se puede procesar, devolvemos NaN
