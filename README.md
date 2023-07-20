#  👩‍💻 Hackathon 50+ 🚀

A proposta desse hackathon era melhorar, de alguma
forma, a vida de pessoas que tem mais de 50 anos.

Diante disso, uma das constatações que fizemos diante
do tema que foi apresentado é que as pessoas mais
velhas se tornam o principal alvo de golpes e fraudes.

Nesse contexto a equipe que participei sugeriu que 
elaborassemos uma aplicação para tentar evitar, ou pelo
menos diminuir, os golpes que são aplicados por telefone. 

Assim, desenvolvemos um MVP da seguinte forma:

Após capturar um som utilizando a biblioteca 
 'speech_recognition' transcrevemos esse som
para texto, colocamos esse texto dentro de uma
variável e colocamos palavras chaves (que indicam alerta) para serem
identificadas dentro desse texto.

Caso alguma dessas palavras sejam identificadas
dentro do texto transcrito é acionada uma ligação,
utilizando a ferramenta Twilio, para enviar um alerta
sobre o que foi identificado dentro do áudio analisado.

obs.: TWILIO é uma ferramenta para enviar sms e para
fazer ligação e é preciso configurar uma conta no TWILIO 
para registrar o celular desejado e ter seus próprios dados
que são necessários para rodar a aplicação. Esses dados são:
account_sid, auth_token, meu_numero e numero_twilio.
Eu deixei esses meus dados em um arquivo privado chamado 
`codigos.py` e importei esse arquivo dentro do `chamada.py`.



