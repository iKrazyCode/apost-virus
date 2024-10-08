import requests
from bs4 import BeautifulSoup
import re


class TipMiner:
    """
    import requests
    from bs4 import BeautifulSoup
    import re
    """

    @staticmethod
    def get_velas(qtd: int=1500) -> list:
        """
        Retorna uma lista de velas. Onde o primeiro indice, se trata da vela mais recente
        """
        url = f"https://www.tipminer.com/historico/blaze/crash?limit={qtd}"
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        soup = str(soup)
        rg = re.findall(r'\\\"result\\\":\\\"(\d*,*\d*x)\\\"', soup)
        return rg



# Aí zé a forma de usar -> 
velas = TipMiner.get_velas(1500)
print(velas)






