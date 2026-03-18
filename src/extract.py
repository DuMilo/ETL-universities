import requests

class Extract():
    
    def __init__(self):
        pass

    def extract_country(self, pais: str):

        pais_url = pais.title().replace(' ', '+')
        
        url = f"http://universities.hipolabs.com/search?country={pais_url}"

        response = requests.get(url)
        response.raise_for_status()
        universities = response.json()

        return universities