import random

favorite_places_and_foods= ["Erzurum","Hatay","Kayseri","Mersin","Antep","Cağ Kebabı","Künefe","Mantı","Tantuni","Katmer"]
Place = favorite_places_and_foods[0:5]
Food = favorite_places_and_foods[5:10]

seçim=random.randint(0,4)

print(Place[seçim],"->",Food[seçim])




