---
title: Pipenv e come tutto è in uno
slug: pipenv-e-come-tutto-e-in-uno
date: 2017-07-01 00:00:00 +0000
categories:
- dev
tags:
- python
- pipenv
aliases:
- "/dev/pipenv-e-come-tutto-e-in-uno/"
description: Assistiamo al matrimonio di Pipfile, Pip e PipEnv

feature_image: "/post/pipenv-e-come-tutto-e-in-uno/pipenv-tutto.jpg"
feature_link: "https://unsplash.com/photos/vYFcHzLYpmU"
feature_text: "Photo by Max Letek on Unsplash"
---
Io sono un appassionato di podcast. Mi piace ascoltarli quando vado in giro e quando vado in palestra. E uno di questi è quello di [Kenneth Reitz](https://www.kennethreitz.org/), autore di svariati moduli python tra cui _Requests_ che tutti i pythonisti conoscono e usano.
L'ultimo progetto suo di mio interesse è PipEnv, _sacro matrimonio di pipfile, pip e virtualenv_.

Partiamo dalla base: per fare un progetto python solitamente si passano 3 fasi obligatorie

* Si crea un _virtualenv_ su cui lavorare, in cui i pacchetti installati non vanno in conflitto con quelli nel sistema ottenendo così un ambiente pulito su cui lavorare
* Si fa una selezione dei moduli necessari per il progetto e li si installa nel _virtualenv_ attraverso _pip_
* Si produce dal _virtualenv_ un file di _requirements.txt_ che indica cosa è installato

Questo porta a dover tenere sempre aggiornato e pulito il _virtualenv_, sempre aggiornato il file _requirements.txt_ e fissare le versioni minime richieste (o addirittura la versione stessa) del modulo nel _requirements.txt_.

PipEnv di conseguenza fa tutto questo per te con pochi e semplici comandi.

## Ad esempio?
Mettiamo caso che io debba creare uno script in python che mi recuperi dei feed rss e me li salvi in locale.

* Creo una cartella per il progetto, in modo da metterci tutto quello di cui ho bisogno

        mkdir progetto_python

* Scelgo che versione di python usare, se quella corrente o quella _legacy_

        pipenv --three #versione corrente di python 3.x
        # alternativamente
        pipenv --two #legacy 2.7.x

* Inizio a scrivere codice e a installare pacchetti necessari per il progetto

        pipenv install request
        pipenv install flask

Questi comandi assieme a quello iniziale, mi permette di creare un _pipfile_ che descrive i moduli da me installati. La cosa più bella di questo _pipfile_ è che permette di avere più "ambienti" indicati nello stesso file. Questo significa che posso avere "testing", "travis", "dev" e "prod" tutti descritti in un unico file e gestiti in modo automatico.

Quindi mi accordo che  _flask_ non mi serve più perchè ho riscritto tutto in modo da non usarlo e rendere in codice più leggibile... Quindi cosa faccio?

        pipenv uninstall flask

Questo comando elimina dal _pipfile_ flask rendendolo così "pulito" e sempre aggiornato.

Una volta definito il _pipfile_ bisogna creare il _pipfile.lock_, ovvero una versione automatica, generata dall' "installazione corrente" in modo da riprodurre perfettamente l'ambiente.

        pipenv lock

Questo fissa i moduli installati con versione, hash e altri dati sia per i pacchetti indicati sia che con le loro dipendenze, in modo da ottenere tutte le indicazioni per riprodurre quel esatto ambiente.

# Tutto qui?
No, il sistema crea all'inizio un _virtualenv_ per il progetto e lo popola secondo le indicazioni passate dal terminale.
Questo ambiente virtuale è accessibile attraverso il comando

        pipenv shell

che apre una shell nel _virtualenv_ del progetto e permette di eseguire comandi nella stessa _virtualenv_.

In oltre _PipEnv_ permette di convertire, se non presenti, i _requirements.txt_ in _pipfile_ e di aggiornare tutti i pacchetti attraverso

        pipenv update

## Conclusione
Personalmente spero che questo sistema, o per lo meno _pipfile_, diventi lo standard per lo sviluppo di applicazioni python e soppianti i file _requirements.txt_ che trovo particolarmente poco pratici e troppo sintetici anche se fanno esattamente quello per cui sono stati pensati
