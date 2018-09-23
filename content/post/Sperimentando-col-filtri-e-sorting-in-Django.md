+++
categories = ["dev"]
date = "2018-09-24T09:03:37+02:00"
description = "Diario di una personale avventura nel mondo dei filtri e sorting in django"
draft = true
feature_image = "/images/DV2so_fWAAMMD_v.png"
slug = "sperimentando_con_filtri_paginator_e_sorting_in_django"
tags = ["django,", "sorting,", "filters", "module", "paginator"]
title = "Sperimentando col filtri, paginator e sorting in Django"

+++
Ultimamente sto lavorando a tempo pieno a un progetto Django per la mia ditta. Lo abbiamo chiamato Celebro e per ora ha un grossissimo problema: filtri, sorting e paginator.

Fondamentalmente il problema si riassume con la rubrica del personale: deve essere ordinabile, filtrabile e visibile 20 elementi alla volta. Le tre cose assieme risultano essere difficili soprattutto se usi le Class View di Django.

Gli strumenti esaminati per risolvere il problema sono stati:

* **il paginator di Django**: funzionale e comodo, nulla da dire
* **django-filter**: praticamente la libreria standard per i filtri
* **django-table-2**: libreria per il sorting

Il primo risulta funzionante come un orologio sia sotto forma di funzione che di classe. 

Anche secondo risulta perfettamente funzionante sia come classe che come view e io sono molto contento.

Il terzo risulta perfettamente funzionante con gli altri ma leggermente limitato (produce solo table) ma sostanzialmente esattamente quello che ci serve.

Il problema risulta combinarli. I tre moduli sono "poco compatibili" tra di loro e ancora di più se si usa la Class View fornita da ogni uno.

Questo mi ha portato a scrivere un wrapper, che non mi piace.

Quindi qui annuncio lo sviluppo di un piccolo modulo per django che permetterà di avere queste tre funzioni in un unico compatto modo, con preferenza per la Class View... 