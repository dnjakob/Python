print('hallo')

import openai
schnittstelle = ''

def befehl(details):
    anfrage = openai.Completion.create(model="text-davinci-003", prompt=details, max_tokens=1024, api_key=schnittstelle)
    nachricht = anfrage.choices[0].text
    return nachricht

ergebnis = befehl('')
print(ergebnis)