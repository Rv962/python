travel_log = [
{
"country" : "France",
"visited" :[ "paris" , "bijon", "mont"],
"times" :  5 } , 
{
"country" : "india",
"visited" :[ "Delhi" , "Goa", "Mumbai"],
"times" :  4}
 ]

def add_new(place_visited, cities_visited, times_visited):
    new_country = { }
    new_country["country"]  = place_visited
    new_country["visited"] = cities_visited
    new_country["times"] = times_visited
    travel_log.append(new_country)
    
    
country = input("enter country: ")
visited = input ("entry cities with comma : ").split()
times = input ("no. of times visited: ")

#add_new("russia", ["Berlin", "moscow", "beirut"], 3 )
add_new(country, visited, times)
print(travel_log)







