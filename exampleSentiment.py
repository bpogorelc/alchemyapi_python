#!/usr/bin/env python

#	Copyright 2013 AlchemyAPI
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


from __future__ import print_function
from alchemyapi import AlchemyAPI
import json


#demo_text = 'Yesterday dumb Bob destroyed my fancy iPhone in beautiful Denver, Colorado. I guess I will have to head over to the Apple Store and buy a new one.'
demo_text = 'the reception staff when we arrived was extremely rude. We found blood and dry wine on our bed sheets and it took them 1 hour to bring new sheets (that we had a to change ourselves) and did not offer any compensation outside of drinks. Durng the weekend you can hearthe sounds of the nightclub that is next door.'
#demo_text = 'He viajado con LAN antes y mi experiencia ha sido muy positiva. Estoy complacido y satisfecho. Hasta el momento todo ha marchado como debe ser.'
#demo_text = 'Me siento feliz de regalar este ticket y de haber encontrado el dia esperado y recibir a unos tios que el algun momento de mi juventud me dieron la oportunidad de ser muy feliz.'
#demo_text = 'No estoy de acuerdo que con solo el hecho de entregar los datos de mi tarjeta de credito se haga la compra instantaneamente sin ingresar a mi banco con las respectivas claves de seguridad. No es primera vez que me sucede  prefiero seguir paso a paso el pago de la transaccion ya que no he autorizado ningun convenio  para que se realice de esa forma. No me da seguridad el uso de mi tarjeta sin clave alguna.'
#demo_text = 'Nunca he podido hacer compra por la pgina. Hoy trate por ipad, iphone, mi laptop que es una macbook pro, desde mi pc de escitorio windows y todas dicen que el pago es rechazado solo al ingresr el medio de pago ya sea mi tarjeta de credito visa o mi cuenta de ahorros.'
#demo_text = 'Tuve que hacer dos reservas porque en ningun lado dice que no se puede pagar con tarjeta de un pais en el portal de otro. Por lo que la compra la pude realizar luego de ingresar diferentes tarjetas en tres oportunidades . Demaciados pasos y mucha inseguridad respecto a tantas veces ingresados los datos de tarjeta'
#demo_text = '1)Check in was 15:00 hrs but the room was not ready until after 16:00 hrs. 2) On sunday morning just after 08:00 we hade a breakfast but the food was very cold:('
#demo_text = 'La pagina es buena le falta almacenar los datos del pasajero para no tener que estan ingresando lodas las veces que uno compra los datos.' 

demo_url = 'http://www.npr.org/2013/11/26/247336038/dont-stuff-the-turkey-and-other-tips-from-americas-test-kitchen'
demo_html = '<html><head><title>Python Demo | AlchemyAPI</title></head><body><h1>Did you know that AlchemyAPI works on HTML?</h1><p>Well, you do now.</p></body></html>'
image_url = 'http://demo1.alchemyapi.com/images/vision/football.jpg'

print('')
print('')
print(
    '            ,                                                                                                                              ')
print(
    '      .I7777~                                                                                                                              ')
print(
    '     .I7777777                                                                                                                             ')
print(
    '   +.  77777777                                                                                                                            ')
print(
    ' =???,  I7777777=                                                                                                                          ')
print(
    '=??????   7777777?   ,:::===?                                                                                                              ')
print(
    '=???????.  777777777777777777~         .77:    ??           :7                                              =$,     :$$$$$$+  =$?          ')
print(
    ' ????????: .777777777777777777         II77    ??           :7                                              $$7     :$?   7$7 =$?          ')
print(
    '  .???????=  +7777777777777777        .7 =7:   ??   :7777+  :7:I777?    ?777I=  77~777? ,777I I7      77   +$?$:    :$?    $$ =$?          ')
print(
    '    ???????+  ~777???+===:::         :7+  ~7   ?? .77    +7 :7?.   II  7~   ,I7 77+   I77   ~7 ?7    =7:  .$, =$    :$?  ,$$? =$?          ')
print(
    '    ,???????~                        77    7:  ?? ?I.     7 :7     :7 ~7      7 77    =7:    7  7    7~   7$   $=   :$$$$$$~  =$?          ')
print(
    '    .???????  ,???I77777777777~     :77777777~ ?? 7:        :7     :7 777777777:77    =7     7  +7  ~7   $$$$$$$$I  :$?       =$?          ')
print(
    '   .???????  ,7777777777777777      7=      77 ?? I+      7 :7     :7 ??      7,77    =7     7   7~ 7,  =$7     $$, :$?       =$?          ')
print(
    '  .???????. I77777777777777777     +7       ,7???  77    I7 :7     :7  7~   .?7 77    =7     7   ,77I   $+       7$ :$?       =$?          ')
print(
    ' ,???????= :77777777777777777~     7=        ~7??  ~I77777  :7     :7  ,777777. 77    =7     7    77,  +$        .$::$?       =$?          ')
print(
    ',???????  :7777777                                                                                77                                       ')
print(
    ' =?????  ,7777777                                                                               77=                                        ')
print(
    '   +?+  7777777?                                                                                                                           ')
print(
    '    +  ~7777777                                                                                                                            ')
print(
    '       I777777                                                                                                                             ')
print(
    '          :~                                                                                                                               ')


# Create the AlchemyAPI Object
alchemyapi = AlchemyAPI()

print('')
print('')
print('############################################')
print('#   Entity Extraction Example              #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.entities('text', demo_text, {'sentiment': 1})

if response['status'] == 'OK':
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Entities ##')
    for entity in response['entities']:
        print('text: ', entity['text'].encode('utf-8'))
        print('type: ', entity['type'])
        print('relevance: ', entity['relevance'])
        print('sentiment: ', entity['sentiment']['type'])
        if 'score' in entity['sentiment']:
            print('sentiment score: ' + entity['sentiment']['score'])
        print('')
else:
    print('Error in entity extraction call: ', response['statusInfo'])


print('')
print('')
print('')
print('############################################')
print('#   Keyword Extraction Example             #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.keywords('text', demo_text, {'sentiment': 1})

if response['status'] == 'OK':
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Keywords ##')
    for keyword in response['keywords']:
        print('text: ', keyword['text'].encode('utf-8'))
        print('relevance: ', keyword['relevance'])
        print('sentiment: ', keyword['sentiment']['type'])
        if 'score' in keyword['sentiment']:
            print('sentiment score: ' + keyword['sentiment']['score'])
        print('')
else:
    print('Error in keyword extaction call: ', response['statusInfo'])


print('')
print('')
print('')
print('############################################')
print('#   Concept Tagging Example                #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.concepts('text', demo_text)

if response['status'] == 'OK':
    print('## Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Concepts ##')
    for concept in response['concepts']:
        print('text: ', concept['text'])
        print('relevance: ', concept['relevance'])
        print('')
else:
    print('Error in concept tagging call: ', response['statusInfo'])


print('')
print('')
print('')
print('############################################')
print('#   Sentiment Analysis Example             #')
print('############################################')
print('')
print('')

#print('Processing html: ', demo_html)
print('Processing text: ', demo_text)
print('')

#response = alchemyapi.sentiment('html', demo_html)
response = alchemyapi.sentiment('text', demo_text)

if response['status'] == 'OK':
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Document Sentiment ##')
    print('type: ', response['docSentiment']['type'])

    if 'score' in response['docSentiment']:
        print('score: ', response['docSentiment']['score'])
else:
    print('Error in sentiment analysis call: ', response['statusInfo'])
