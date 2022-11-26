import requests

rickandmortyapi = "https://rickandmortyapi.com/api/character?page="



def api_get_request_character(num_page):
    return requests.get(rickandmortyapi+num_page).json()

def get_character_from_response(response_character):
    
    for i in response_character['results']:
        #print(i)
        print ("Personajes: ", i['name'])
    #print ("Personajes: ", response_character['results']['name'])
    
def get_info_from_character(num_page):
    response_character = api_get_request_character(num_page)
    #print ("Pagina : ",num_page)
    get_character_from_response(response_character) 
    


for i in range (1,22):
    #print(i)
    get_info_from_character(str(i))

#num_page=str(input("Numero de pagina: "))

#get_info_from_character(num_page)