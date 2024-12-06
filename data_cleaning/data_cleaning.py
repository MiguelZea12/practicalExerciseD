import pandas as pd
from .utils import correct_family_history, sleep_duration_to_hours

def handle_missing_values(df, numeric_columns, categorical_columns):
    """
    Imputar los valores nulos en las columnas numéricas y categóricas.
    """
    for col in numeric_columns:
        df[col] = df[col].fillna(df[col].median())
    
    for col in categorical_columns:
        df[col] = df[col].fillna(df[col].mode()[0])

    return df

def correct_column_types(df):
    """
    Asegurarse de que las columnas tengan los tipos de datos correctos.
    """
    if df['id'].isnull().any():
        print("Advertencia: Hay valores nulos en la columna 'id'. Se eliminarán las filas con 'id' nulo.")
        df = df.dropna(subset=['id'])

    df['id'] = df['id'].astype(int)
    df['Age'] = df['Age'].astype(int)
    df['CGPA'] = df['CGPA'].astype(float)
    df['Academic Pressure'] = df['Academic Pressure'].astype(float)
    df['Work Pressure'] = df['Work Pressure'].astype(float)
    df['Study Satisfaction'] = df['Study Satisfaction'].astype(float)
    df['Job Satisfaction'] = df['Job Satisfaction'].astype(float)
    
    return df

def normalize_text_columns(df):
    """
    Normalizar las columnas de texto (ej. eliminar espacios extra, capitalizar correctamente).
    """
    df['Gender'] = df['Gender'].str.strip().str.capitalize()
    df['City'] = df['City'].str.strip().str.capitalize()
    df['Dietary Habits'] = df['Dietary Habits'].str.strip().str.capitalize()
    df['Degree'] = df['Degree'].str.strip().str.upper()

    return df

def transform_sleep_duration(df):
    """
    Transformar la columna 'Sleep Duration' a horas.
    """
    df['Sleep Duration'] = df['Sleep Duration'].apply(sleep_duration_to_hours)

    # Imputar valores faltantes con la mediana
    median_sleep_duration = df['Sleep Duration'].median()
    df['Sleep Duration'] = df['Sleep Duration'].fillna(median_sleep_duration)

    return df

def clean_family_history(df):
    """
    Limpiar la columna 'Family History of Mental Illness' para que solo tenga 'Yes' y 'No'.
    """
    df['Family History of Mental Illness'] = df['Family History of Mental Illness'].apply(correct_family_history)
    return df

def remove_anomalies(df):
    """
    Eliminar valores anómalos, como edades negativas.
    """
    df = df[df['Age'] > 0]  # Eliminar filas con edad negativa
    return df

def clean_data(df, numeric_columns, categorical_columns):
    """
    Función principal de limpieza de datos.
    """
    # Imputar valores faltantes
    df = handle_missing_values(df, numeric_columns, categorical_columns)
    
    # Corregir tipos de columnas
    df = correct_column_types(df)
    
    # Normalizar columnas de texto
    df = normalize_text_columns(df)
    
    # Transformar la columna 'Sleep Duration'
    df = transform_sleep_duration(df)
    
    # Limpiar la columna 'Family History of Mental Illness'
    df = clean_family_history(df)
    
    # Eliminar valores anómalos
    df = remove_anomalies(df)

    return df
