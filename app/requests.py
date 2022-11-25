import requests
from .models.rick_y_morty import Personajes
        

class Request:
    def __make_request(self, url: str):
        response = requests.get(url)
        payload = {}
        if response.status_code == 200:
            payload = response.json()
        return payload

    def characters(self):
        url = 'https://rickandmortyapi.com/api/character'
        payload = self.__make_request(url)
        results = payload.get('results', [])
        characters = []
        for character in results:
            characters.append(
                Personajes(character.get('id'),
                           character.get('name'),
                           character.get('status'),
                           character.get('gender'),
                           character.get('image')
                ).to_json()
                )
        return characters
     