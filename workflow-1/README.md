## Worfklow #1: Word document => AutoSearch Query

Stappen:
1. Word document => OpenConvert => FoLiA
2. FoLiA => Frog => FoLiA
3. FoLiA => AutoSearch upload => Queries in AutoSearch

### 1.1 Word document => Piereling => FoLiA
We gebruiken de [Piereling webservice] uit Nijmegen.
Het Python script [01-doc-to-folia.py] maakt een project aan,
voegt het Word document aan het project doe, start de conversie op,
ontvangt het resultaat en verwijdert het project weer.

### (Obsolete) 1.1 Word document => OpenConvert => FoLiA

#### Online OpenConvert service
We gebruiken de [remote service bij INT] met de volgende parameters:
- Input format: word2010 ('docx')
- Output format: FoLiA ('folia')
- Linguistic annotation: geen ('-')
- Show output as Raw XML ('raw')
 
```
curl -s http://openconvert.clarin.inl.nl/openconvert/file \
	-F 'input=@CLARIN workshop-hist-nlp.docx' \
	-F 'format=docx' \
	-F 'to=folia' \
	-F 'tagger=-' \
	-F 'output=raw'
```
Field 'tagger' can also be 'tokenizer', or 'chn-tagger'

- 2019-10-09: Maarten v. Gompel gemaild met vraag welke tagger bedoeld wordt in deze workflow.

  Maarten en Antal: geen tagger gebruiken.

[remote service bij INT]: http://openconvert.clarin.inl.nl/openconvert/tagger/ui#file

### 1.2 FoLiA => Frog => FoLiA uit Nijmegen.
We gebruiken de [Frog webservice] uit Nijmegen.
Het Python script [02-folia-through-frog.py] maakt een project aan,
voegt het FoLiA bestand uit 1.1 aan het project toe, start de
behandeling door Frog op, ontvangt het resultaat en verwijdert
het project weer.

[Frog webservice]: https://webservices-lst.science.ru.nl/frog/

[01-doc-to-folia.py]: workflow-1/01-doc-to-folia.py
[02-folia-through-frog.py]: workflow-1/02-folia-through-frog.py

### (Obsolete) 1.2 FoLiA => Frog => FoLiA

We lopen tegen hetvolgende aan.
In de output van OpenConvert uit stap 1.1 blijkt, na conversie naar FoLiA, een
xml:id soms meerdere keren te zijn uitgedeeld.
Dit is geen 'legale' XML meer.
Dit leidt er bij de meeste XML parsers dan ook toe dat de input wordt geweigerd.

Zo ook Frog:
```
test.folia:1348: XML-error: ID pc.000001 already defined

frog-:retrieving FoLiA from 'test.folia' failed with exception:
frog-:XML error: document is invalid
frog-:problem frogging: test.folia
frog-:read failed
frog-:Fri Oct  4 14:47:24 2019 Frog finished
```

Hiervoor is een [bugreport](https://github.com/INL/OpenConvert/issues/4) ingediend bij INT / Jesse de Does.

Maarten van Gompel en Jan Odijk geven aan dat mogelijk Maarten's recent
uitgerolde [Piereling (source)] gebruikt kan worden i.p.v. OpenConvert:
- [Piereling webservice]
- [Piereling REST api]

Maarten:
De webservice vereist een account dat je hier kan aanmaken:
https://webservices-lst.science.ru.nl, aangezien we nog niet
bij de federated infrastructuur zijn aangesloten.

Hayco & Maarten:
- username: *REDACTED*
- password: *REDACTED*

[Piereling (source)]: https://github.com/proycon/piereling
[Piereling webservice]: https://webservices-lst.science.ru.nl/piereling/
[Piereling REST api]: https://webservices-lst.science.ru.nl/piereling/info/

### 1.3 FoLiA => AutoSearch upload => Queries in AutoSearch
1. Log in
2. Haal session cookies uit headers
3. Post files naar server.
4. Query.

### 1.3.1 Log in
Als we 'Frog' even overslaan en de FoLiA uit OpenConvert willen aanbieden in
AutoSearch, dan zien we dat de [CLARIN versie van AutoSearch]
netjes is beschermd door Federated Authenticatie. Een script kan dus niet
zonder meer calls doen naar de API, er is authenticatie / authorisatie nodig.
In dit geval via een Cookie in de browser.

[CLARIN versie van AutoSearch]: http://portal.clarin.inl.nl/autocorp/

## De Federated Authentication uitdaging
Voor pipelines in scripts roept dit meteen op tot keuzes:
- willen we AutoSearch zelf gaan hosten (zonder de authenticatie laag), of
  willen we de versie die bij portal.clarin draait, gebruiken?
- als we reeds bestaande dienst gebruiken: hoe om te gaan met inloggen?
  browser opstarten en gebruiker naar pagina dirigeren is geen punt, maar dan
  moet er flink 'gehackt' worden om authenticatie Cookie uit de browser te
  ontfutselen.
- willen we remote calls gaan doen, of gaan we een browser vanuit een script
  besturen om zo de files te laten uploaden in AutoSearch?

Ik heb even verder gezocht en als we de credentials na inloggen via de
browser "lenen", dan is ontsluiting van AutoSearch via REST calls prima te
doen. Nieuw corpus aanmaken, FoLiA bestanden (al dan niet door Frog getrokken)
uploaden, en corpus verwijderen zijn operaties die prima ondersteund
worden via remote calls.

================================================================================

### 1.3 FoLiA => AutoSearch upload => Queries in AutoSearch

Have to hijack cookie from webbrowser after succesful federated login, then use
cookie as per the following curl requests:

UPLOAD file 'test.folia':
```
curl -s 'https://portal.clarin.inl.nl/autoserver/*REDACTED*'
  -H 'Accept: application/json'
  -H 'COOKIE: *REDACTED*'
  -F 'data[]=@test.folia'
  | jq .
```

CREATE corpus:
```
curl -s -XPOST https://portal.clarin.inl.nl/autoserver/
  -H 'Accept: application/json'
  -H 'COOKIE: *REDACTED*'
  -d 'name=*REDACTED*'
  -d 'display=zandbak-1'
  -d 'format=folia'
  | jq .
```

DELETE corpus:
```
$ curl -s -XDELETE https://portal.clarin.inl.nl/autoserver/*REDACTED*
  -H 'Accept: application/json'
  -H 'COOKIE: *REDACTED*'
   | jq .
```
