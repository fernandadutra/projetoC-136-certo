######## PARTE DO GOOGLE COLAB ########


#import pandas as pd
#import csv 
#from flask import Flask, jsonify, request
#from data import data

#Importe o aquivo final do projeto 131
#arq_proj131= pd.read_csv("C:/Users/55319/Documents/Code/ProjetoC-136/star_with_gravity.csv")

#rows = []

#with open("C:/Users/55319/Documents/Code/ProjetoC-136/star_with_gravity.csv", "r") as f:
  #csvreader = csv.reader(f)
  #for row in csvreader:
    #rows.append(row)

#headers = rows[0]
#stars_data_rows = rows[1:]
#print(headers)
#print(stars_data_rows[0])

#Crie as listas a partir das colunas do DataFrame
#name=arq_proj131["Star_name"].to_list()
#mass=arq_proj131["Mass"].to_list()
#radius=arq_proj131["Radius"].to_list()
#distance=arq_proj131["Distance"].to_list()
#gravity=arq_proj131["Gravity"].to_list()

#Faça uma lista dos dicionários a partir desses dados
#final_stars_list=[]

#for stars_data in stars_data_rows:
  #temp_dict={
    #"name": stars_data[1],
    #"star_mass": stars_data[3],
    #"star_radius": stars_data[4],
    #"star_distance": stars_data[2],
    #"star_gravity": stars_data[5]}
  #final_stars_list.append(temp_dict)
  
#print(final_stars_list)

#Copie a lista final 