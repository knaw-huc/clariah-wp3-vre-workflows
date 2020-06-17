## 4. TIFF => AutoSearch Query

1. TIFF doc (scan) => PICCL met pos-tagging etc => FoLiA 
2. FoLiA => AutoSearch upload => Queries in Autosearch

## 1 TIFF => PICCL

Run: `python3 ./01-tiff-to-folia.py`

### 2 FoLiA => Autosearch

Run:
```
./02a-create-autosearch-collection.sh
./02b-add-autosearch-file.sh
```

## De PICCL-TICCL-discussie

In eerste instantie wilde ik PICCL lokaal draaien, maar hierbij stuitte ik op een aantal problemen. Een e-mail-wisseling met Maarten van Gompel volgde. Een korte samenvatting:

**Maarten:**
Ik moet ook wel even waarschuwen dat de huidige staat van PICCL veel te
wensen over laat. De achterliggende TICCL tools zijn al lange tijd niet
gereleased en niet in de pipeline geintegreerd ondanks, terwijl er wel
veel aan gebeurd is (zie
https://github.com/LanguageMachines/PICCL/issues/54), Mij is het niet
duidelijk welke richting PICCL nu opgaat en bij de bruikbaarheid van de
huidige release heb ik grote vraagtekens, de regie hiervoor ligt in
eerste instantie bij Martin Reynaert.

Github issue 54:
'[..] The latest release of ticcl-tools is more than a year old already, [..] The situation now is that nobody can use the very latest ticcltools
properly.'

**Bas:**
Wat betreft github.com/LanguageMachines/PICCL/issues/54:
Dit levert wel wat vragen op, voor zowel jou, Maarten, als Martin denk ik?
1. Is het nuttig om energie te steken in een piccl- en ticcl-workflow voor
de verouderde release?
2. Is er een release van de laatste ticcl-tools in de maak en wanneer komt
die uit?

**Maarten:**
Dat zijn inderdaad hele goede en zinnige vragen die eigenlijk alleen
Martin kan beantwoorden...

Martin Reynaert stond in de cc maar heeft nog niet gereageerd.

**HDJ**: (juni 2020) Voor de afronding van CLARIAH WP3 zijn Maarten en
Martin gevraagd om (desgewenst) een update te geven. Details hieronder.

**Maarten:**
Inmiddels is de situatie gelukkig wel wat opgeschoten. Misschien had je
het al gevolgd via de github issues, maar eind februari dit jaar was er
na lange tijd eindelijk wat schot in de zaak gekomen en hebben we met
Martin eens goed om de tafel gezeten om nieuwe releases van PICCL en
TICCL-tools te doen. Dat is inmiddels gebeurd dus de punten van
indertijd zijn gelukkig opgelost. Voor de toekomst blijft het ongewis,
want Ko, de programmeur die voor Martin aan ticcl-tools werktte, is
onlangs met pensioen gegaan, en aangezien er geen nieuwe maintainer voor
is vrees ik dat er voor onbepaalde tijd geen nieuwere releases van
ticcl-tools komen (en van piccl zelf dus ook niet veel).

**Martin:**
pending...
