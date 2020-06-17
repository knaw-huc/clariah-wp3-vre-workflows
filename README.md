# VRE Workflows

## Webservice workflows in vogelvlucht
Zie `./doc/wp3-vre-workflow-inventarisatie.pdf` voor de details.
1. Automatische linguïstische verrijking van een Nederlandse tekst en doorzoeken in Autosearch
   - Docx => **Piereling** => FoLiA => **Frog** => getokeniseerde FoLiA => **Autosearch**
2. Automatische linguïstische verrijking van een Nederlandse tekst en visualiseren/bewerken/doorzoeken in FLAT
   - Odt => **Piereling** => FoLiA => **Frog** => getokeniseerde FoLiA => **FLAT**
3. Automatische linguïstische verrijking van een Nederlandse corpus en doorzoeken in Autosearch
   - Docx => **Piereling** => Zip met FoLiA's => **Frog** => Zip met getokeniseerde FoLiA's => **Autosearch**
4. Alpino: Automatische syntactische verrijking van een Nederlandse tekst visualisatie in PaQU
   - Html => **OpenConvert** => Txt => **Alpino** => Zip met Alpino xml => **PaQu**
5. PICCL: OCR, Tekstnormalisatie en Linguistische verrijking
   - a. Tiff => **PICCL** => FoLiA => **Autosearch**
   - b. Tiff => **PICCL** => FoLiA => **FLAT**
6. GreTeL: TEI corpus upload en zoeken in treebanks
   - Tei => **GreTeL**
7. Autosearch
   - Tei => **Autosearch**

## Werk in context CLARIAH WP3
Deze scripts zijn gemaakt in de context van CLARIAH WP3 om te zien in hoeverre enkele
voorbeeld workflows daadwerkelijk in de praktijk uit te voeren zijn en in welke mate
ze met eenvoudige (Python) scripting te automatiseren zijn.
Heb je zelf zo'n workflow, en heb je hulp nodig om deze scripts in jouw context werkend
te krijgen, schroom dan niet contact op te nemen met [HuC DI :: Team Text](mailto:text@di.huc.knaw.nl)
