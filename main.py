import pandas as pd
from data_cleaning.data_cleaning import clean_data

def main():
    # Ruta del archivo CSV de entrada
    file_path = 'mnt/data/Student_Depression_Dataset_With_Mixed_Errors.csv'
    df = pd.read_csv(file_path)

    # Columnas numéricas y categóricas
    numeric_columns = ['Age', 'Academic Pressure', 'Work Pressure', 'CGPA', 'Study Satisfaction', 'Job Satisfaction']
    categorical_columns = ['Gender', 'City', 'Profession', 'Dietary Habits', 'Degree', 
                           'Work/Study Hours', 'Financial Stress', 'Family History of Mental Illness', 
                           'Have you ever had suicidal thoughts ?', 'Depression']

    # Limpiar los datos
    df_cleaned = clean_data(df, numeric_columns, categorical_columns)

    # Guardar el dataset limpio
    cleaned_file_path = 'mnt/data/Cleaned_Student_Depression_Dataset_for_Analysis.csv'
    df_cleaned.to_csv(cleaned_file_path, index=False)

    print(f"El dataset limpio se ha guardado en: {cleaned_file_path}")

if __name__ == '__main__':
    main()
