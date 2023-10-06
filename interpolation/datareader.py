import pandas as pd

# Ruta al archivo de texto
fileTxt = "data\SCD30_CO2.txt"

# Definir los nombres de las columnas
columns = ["Timestamp1", "Timestamps", "Sensor", "Data Type", "Data 1", "Data 2", "Data 3"]

# Crear una lista para almacenar los datos válidos
datosValidos = []

# Abrir el archivo de texto y procesar cada línea
with open(fileTxt, 'r') as file:
    for line in file:
        parts = line.strip().split(' ')
        # Verificar que la línea tenga la cantidad esperada de campos
        if len(parts) == 7:
            # Convertir los campos numéricos a float si es necesario
            try:
                parts[4] = float(parts[4])
                parts[5] = float(parts[5])
                parts[6] = float(parts[6])
            except ValueError:
                print(f"Error en la línea: {line.strip()}")
                continue  # Saltar esta línea si hay un error en los campos numéricos
            datosValidos.append(parts)

# Crear un DataFrame a partir de los datos válidos
df = pd.DataFrame(datosValidos, columns=columns)

sensorName = df.iloc[0, 2] #Almacenamos el nombre del sensor 
dataType= df.iloc[0, 3]  # Almacenamos el tipo de dato

# Eliminar las columnas "Timestamps1", "Sensor" y "TipoDato" del DataFrame
df = df.drop(["Timestamp1", "Sensor", "Data Type"], axis=1)

# Configura opciones de visualización
pd.set_option('display.max_rows', None)  # Mostrar todas las filas
pd.set_option('display.max_columns', None)  # Mostrar todas las columnas
pd.set_option('display.width', None)  # Ancho de la pantalla sin restricciones

# Verificar el DataFrame después de eliminar las columnas
print(df)
