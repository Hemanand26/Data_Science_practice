my_data = {"name":["hema","mohan","sibu"],"team":["CSK","RR","MI"],"AGE": [26, 27, 27]}
print(my_data)
my_data["name"][0] = "navo"
my_data["team"][0] = "RCB"
my_data["AGE"][0] = "25"
print(my_data)

india_team = {1:"Rohit",2:"Kohli",3:"HP",4:"JP"}
print(india_team)
india_team1 = {5:"Natu",6:"Badri"}
india_team.update(india_team1)
# print(india_team + india_team1)
print(india_team)
