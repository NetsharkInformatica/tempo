import requests
from appi import chave




def obterCoordenada(apiKey,cidade,estado,pais, limit=1):
        
    
        url=f"http://api.openweathermap.org/geo/1.0/direct?q={cidade},{estado},{pais}&limit={limit}&appid={apiKey}"
        apiKey=chave
        cidade= "sao-caetano-do-sul"
        estado="SP"
        pais="BR" 
   

    #api de geolocalização

    

    #requisição
        requisicao = requests.get(url).json()

        return requisicao[0]["name"]
    

obterCoordenada(
    
    apiKey="chave",
    cidade="São Caetano Do Sul",
    estado="SP",
    pais="BR",
)


