import speech_recognition as sr
import re
from twilio.rest import Client
from codigos import account_sid, auth_token, meu_numero, numero_twilio

# esse "Client" é quem faz a ligação, e ele usa as configurações de
# "account_sid", "auth_token", "meu_numero", "numero_twilio" para fazer isso


account_sid = account_sid
auth_token = auth_token
meu_numero = meu_numero
numero_twilio = numero_twilio

# usando esses dados ele vai fazer uma ligação
client = Client(account_sid, auth_token)

# essa é a mensage que vai ser passada na ligação de alerta
mensagem = """
<Response>
<Say language="pt-BR">
Cuidado, detectamos sinal de fraude ou golpe na sua ultima chamada telefonica!
Em seguida enviaremos um relatório de prevenção de fraude para evitar possíveis golpes
</Say>
</Response>
"""

# reconhecedor de fala
rec = sr.Recognizer()


with sr.Microphone(0) as mic:
    rec.adjust_for_ambient_noise(mic)
    print("Pode falar que eu vou gravar")
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")

    string = texto

    pattern = re.compile("senha")

    x = re.findall(pattern, string)

    if len(x) > 0:
        ligacao = client.calls.create(
            to=meu_numero,
            from_=numero_twilio,
            twiml=mensagem
        )
        print("Sucesso, alerta gerado!")
