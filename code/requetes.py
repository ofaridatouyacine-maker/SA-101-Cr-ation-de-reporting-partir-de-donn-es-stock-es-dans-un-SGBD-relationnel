import sqlite3  # on a utiliser le sqlite 3
import pandas as pd

# Connexion à la base de données depuis UKsafetyRoads(1).sqlite
cnxn = sqlite3.connect("C:/Users/HP/Downloads/UKSafetyRoads (1).sqlite")

# REQUÊTE ACCIDENT
script_accident = """
SELECT 
    accident.accident_index,
    accident.speed_limit, 
    accident.date, 
    accident.time, 
    accident.day_of_week,
    c1.label AS district_name,
    c2.label AS accident_severity,
    c3.label AS road_type,
    c4.label AS weather_conditions, 
    c5.label AS urban_or_rural_area
FROM accident
LEFT JOIN codebook AS c1
    ON c1."table" = 'Accident'
    AND c1."field name" = 'local_authority_district'
    AND c1."code/format" = accident.local_authority_district
LEFT JOIN codebook AS c2
    ON c2."table" = 'Accident'
    AND c2."field name" = 'accident_severity'
    AND c2."code/format" = accident.accident_severity
LEFT JOIN codebook AS c3
    ON c3."table" = 'Accident'
    AND c3."field name" = 'road_type'
    AND c3."code/format" = accident.road_type
LEFT JOIN codebook AS c4
    ON c4."table" = 'Accident'
    AND c4."field name" = 'weather_conditions'
    AND c4."code/format" = accident.weather_conditions
LEFT JOIN codebook AS c5
    ON c5."table" = 'Accident'
    AND c5."field name" = 'urban_or_rural_area'
    AND c5."code/format" = accident.urban_or_rural_area;
"""

# REQUÊTE VEHICLE
script_vehicle = """
SELECT 
    vehicle.accident_index,
    c1.label AS vehicle_type
FROM vehicle
LEFT JOIN codebook AS c1
    ON c1."table" = 'Vehicle'
    AND c1."field name" = 'vehicle_type'
    AND c1."code/format" = vehicle.vehicle_type;
"""

# REQUÊTE CASUALTY
script_casualty = """
SELECT 
    casualty.accident_index,
    casualty.age_of_casualty,
    c1.label AS casualty_type,
    c2.label AS casualty_severity
FROM casualty
LEFT JOIN codebook AS c1
    ON c1."table" = 'Casualty'
    AND c1."field name" = 'casualty_class'
    AND c1."code/format" = casualty.casualty_class
LEFT JOIN codebook AS c2
    ON c2."table" = 'Casualty'
    AND c2."field name" = 'casualty_severity'
    AND c2."code/format" = casualty.casualty_severity;
"""


# LECTURE DES DONNÉES
df_accident = pd.read_sql_query(script_accident, cnxn)
df_vehicle = pd.read_sql_query(script_vehicle, cnxn)
df_casualty = pd.read_sql_query(script_casualty, cnxn)

# EXPORT EXCEL

with pd.ExcelWriter('sae1-01.xlsx', engine='openpyxl') as writer:
    df_accident.to_excel(writer, sheet_name='accident', index=False)
    df_vehicle.to_excel(writer, sheet_name='vehicle', index=False)
    df_casualty.to_excel(writer, sheet_name='casualty', index=False)

# Fermeture de la connexion
cnxn.close()      

#####################################




