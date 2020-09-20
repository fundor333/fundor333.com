---
tags:
- bot
- python
- coding
date: 2017-02-11 00:00:00 +0000
title: Bot, Telegram e programmazione funzionale
slug: bot-telegram-e-programmazione-funzionale
categories:
- dev
description: Come un mio tentativo di imparare a usare i decoratori in python è sfociata
  in un bot in Python
aliases:
- "/dev/bot-telegram-e-programmazione-funzionale/"

feature_image: "bot-telegram.jpg"
feature_link: "https://unsplash.com/photos/3WLcQWnHB_Q"
feature_text: "Photo by Mae Mu on Unsplash"
---
Ho voluto provare a imparare a usare i decoratori e mi sono ritrovato a fare un intero bot telegram basato su codice funzionale e decoratori.

## L'inizio di tutto

Ho trovato una libreria Python per lo sviluppo di bot per Telegram (cosa che mi ha sempre affascinato) e ho deciso di provare a scrivere un bot semplice. Quindi inizio a utilizzare questa libreria [python-telegram-bot](https://python-telegram-bot.org/) e inizio a scrivere i primi metodi per gestire i comandi per il bot e noto una cosa: ogni volta che scrivo una funzione devo legarla a "ascoltatore" che la esegue quando riceve il comando.

Ad esempio se io ho definito prima qi questo frammento di codice una funzione _start_ che mi gestisce il comando omonimo, poi io devo registrarla all'updater attraverso il dispatcher come qui sotto.

{{< highlight python "hl_lines=8 15-17">}}
updater.dispatcher.add_handler(CommandHandler('start', start))
{{< / highlight  >}}


Visto che devo riscrivere questa riga per ogni volta che voglio scrivere un comando per il bot ho pensato che sarebbe bene avere un "alias" per questa riga di codice che prenda in input la stringa a cui voglio risponda e la funzione.

<!--more-->

## Alla ricerca di una alternativa
Da bravo programmatore ho subito pensato che:

 1. Io una cosa così la ho già vista
 2. Qualcosa dentro di me dice di guardare il mio codice di prova di _Flask_

Apro quindi il mio file _prova-stupida-flask.py_

{{< highlight python "hl_lines=8 15-17" >}}
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

if __name__ == "__main__":
	app.run()
{{< / highlight >}}

E capisco che _@app.route("")_ è un decoratore che collega la funzione _hello_ a un listener che risponde all'indirizzo _localhost/_. Esattamente quello che mi serve.

Da una sbirciata al sorgente di Flask produco una classe che gestisce il token e contiene il metodo

{{< highlight python "hl_lines=8 15-17" >}}
def command_handler(self, name):
	def decorator(f):
		self.updater.dispatcher.add_handler(CommandHandler(name, f))
		return f
	return decorator
{{< / highlight >}}

che mi permette di scrivere una funzione di gestione di un comando con un piccolo decoratore sopra che fa tutto il lavoro

{{< highlight python "hl_lines=8 15-17" >}}
@mybot.command_handler('start')
def start(bot,update):
	/* codice che genera il resto*/
{{<  / highlight >}}

E qui felice, continuo a scrivere codice fino ad accorgermi che continuavo a riscrivere la stessa funzione a meno di alcuni "parametri".

Ho quindi scritto un nuovo generatore di funzioni in modo tale

{{< highlight python "hl_lines=8 15-17" >}}
def location_generator(bot, name, text, lonlat):
  @bot.command_handler(name)
  def decoreted(bot, update):
	  logging.info("Give the " + name + " info")
	  BOTAN.track(update.message, name)
	  bot.sendMessage(chat_id=update.message.chat_id, text=text,parse_mode=ParseMode.MARKDOWN)
	  lon, lat = lonlat
	  bot.sendLocation(chat_id=update.message.chat_id, latitude=lat, longitude=lon)
	return decoreted
{{< / highlight >}}


In questo modo, una volta passati i parametri corretti, questo genererà una funzione per rispondere con un testo seguito da una location al comando assegnato.

## Conclusioni

Personalmente sono molto soddisfatto su come mi è venuto il plugin ma non sono soddisfatto di come è fatto il modulo... Forse ci metterò mano o ne faccio uno io stesso... Vedremo

Fundor333
