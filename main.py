import requests
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import credentials, firestore

# Inicializa o Firebase
cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "banco-8c10d",
    "private_key_id": "4e0d69821ec909ac984a968ae6e9d3492117b057",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDpZgsjwidbUOjI\nCyBeL6XoR0C+WfrxEdXe+mRmWwtW/ciV1ZobgG7WNdKABNNiwGQtOwRHIFCL34Ex\ngx58QshC7BKGiVx7S3IFd6BfIavqYj+ybx5sOU2yHzMkfxyY1v62rmySUUugO+TU\npNPnr073IiUYMnNMA6qk1Qr2SfJp8SwV7YodanrU9sjhH8z46kRerpQZW4hAiJ5S\nFIqHizlewq9JzbGtGum1h8SHs27KIK0YXK2/NZ9MyYtplgyilIJPXYPZnDQwv2+F\npClk++ruVk7LlmX8LdPpxmzT5s8k9TU7ueRXUcqmCtCK3mCHgoFf49LIOr4aTxDU\nT2zcVovXAgMBAAECggEARblANqx3iWYARFJelwRw8ZTnmHXU61NCqtvuRk2Ic7JY\ny7oF0ZVqhv+JJMlMRMHoq0JoIr9akI5yT9I1tzVUEfnoBtzeDc8Z/twfwouSifBT\nywA6/GWZ+k4rvwliB56idPxiXst+Zh2+XG/pBdtvIZDHuBTKMLkfryIdpjms+0yI\nnF0+RxWXgwZ67KkBumXsAXr6msouX7nfc9phF8ovG8fZ6iV6aci4SiU06GzOh1Zb\nOLqJ85xKmxorocB6Y935B+o8luWPUemlUOEv2gO20dsxwaEuUZgmkejhFco1zDq0\nb/KVl5G+xGRI9QtySY2SdTVXAFqCx+r/scxUg/lmwQKBgQD77bsujW6TQVZ1Qa7r\njaW6ZRzre06KYf+8t92fq+JRckGiZkoLobuw70zlGhTbU3nf3/Aq4eM0WQimUeYv\nYToYfA9Ty4QQC+NYqAB0XaqBt0V3iwS9FVVaAHsQnw80jlVZQjxfMSFcwV4ZvBZi\noLozbyTrm3uZnINJNpydpCigJwKBgQDtK6aRYOmXLY5PCAXcvuEu1/oo/+aIhwBa\neshBu2yP3wX749y23qM3KvJ4hpJt2vVUBM2n/4Z7sn6d2yTkSR2SkkaExabf+R8M\nSygaqjkoSSmjRx7ut4fmfihbJs7SfsR2jKIWG0rj94Qv85+zWxTTEaxpNJ/tuVIF\noz4JnMlU0QKBgHgAEEYnZkFMQROPWvOmwAdePH1KeenerkNFTZLN+/qRswPZN3H8\n8vtfsT/7wW2LgKUL9Uln2aLIuh8HKd7tsA+ToHVonppKH1vOgpDrQNmS48sCdBpg\n/Avn6LbNHSAKoErpCvrI2zxkex9FAWCvcKIpUevMXv6Xl82a7tUEKbnHAoGBAKrf\nZR2etg0ObFYyUI7vEyv9vSUm4YABy9ZkWb1J/HhXVWdajt1N4EfR8Gm3gu4U7+W9\npDHinpCmVCUFCzpSFzVPn/DuukDpql3gFB/J/m4w8AfMKNQSdJ4yzH6HokDzxjYn\nMmw886L05E7r9mZxO7qqJA6UNJlAiIC5UOv6Au/RAoGBAMZm8cH9Odvaggf2fhsx\nrjFZFvg7/Pgpgy2/Zx4Ps4PuAyFYTpmT2ewsCKwk+Yj1kN+XKqLcHRQ6em5+U0hU\nACZvCRQQpPymCIaKCzRRhTpohmXA+5ZAytUp0z+eIE/s8536JVvz9D/LljwuWuel\nn2DZ+Yp8CkwgBlbbHL0c5PoO\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-oidss@banco-8c10d.iam.gserviceaccount.com",
    "client_id": "115585617073045575999",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-oidss%40banco-8c10d.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
})

db = firestore.client()

# Função para verificar a estratégia
def verificar_estrategia(lista):
    for numero in lista[:4]:
        if numero >= 2:
            return False
    return True

# Função principal para buscar dados e salvar no Firebase
def main():
    url = 'https://estrelabet.com/ptb/games/detail/casino/normal/7787'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    resultados = [float(n) for n in soup.find(class_='result-history').text.replace('x', '').split('\n')][:10]
    
    if verificar_estrategia(resultados):
        print(f'Estratégia ok -> {resultados[:4]}')
        
        # Salvar no Firebase
        db.collection('resultados').add({
            'resultados': resultados
        })

    print(resultados)

if __name__ == "__main__":
    main()
