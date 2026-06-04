import requests
 
URL = "https://api-colombia.com/api/v1/Department"
 
def get_api(url):
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:    
        print("Error:", response.status_code)
        return None
    
if __name__ == "__main__":
    while True:
        department_input = input("Escribe un departamento de colombia que quieras consultar:\n")
        data = get_api(URL)
        if data:
            for data in data:
                if data['name'].lower() == department_input.lower():
                    print(data['name']+": "+data['description'])

        info = input("¿Quieres consultar otro departamento? (s/n):\n")
        if info.lower() != 's':
            break
        
