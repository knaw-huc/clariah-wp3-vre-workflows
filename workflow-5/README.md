## Workflow #5/#7: CHA corpus/TEI corpus => upload in GrETEL 4 => Queries in GrETEL 4

Stappen:
1. Stop documenten in zip
2. Upload in GrETEL 4
3. Wacht op email
4. Queries in GrETEL 4

### Stop documenten in zip

`zip corpus.zip *.xml` of iets dergelijks.

### Upload in GrETEL 4

Ga naar http://gretel.hum.uu.nl/gretel-upload/index.php/upload, log in met het
guest-account, upload de zip. Echte accounts worden volgens het login-scherm
alleen verstrekt binnen de letterenfaculteit van de UU.

Installeren van een custom GrETEL is ingewikkeld. Er is geen Dockerfile en de
instructies, vooral voor de configuratie, zijn vrij summier. De mogelijkheid
om een corpus te uploaden woont in een aparte plugin. Die heeft een API, maar
alleen voor queries, niet voor upload.

### Wacht op email

GrETEL stuurt een mail naar het opgegeven mailadres, maar voor het gastaccount
werkt dat natuurlijk niet. Bij een geüpload corpus hoort wel een log dat
periodiek geraadpleegd kan worden.

### Queries in GrETEL 4

Het uploaden van een bestand geeft het volgende log:

    2019-10-24 12:55:02 	info    Processing started
    2019-10-24 12:55:07 	info 	Started corpus2folia preprocessing
    2019-10-24 12:55:07 	error 	Problem executing corpus2alpino. Is it installed? Check the Apache log or inspect ./uploads/corpus/5db18306238f8/tei/10.xml.
    2019-10-24 12:55:07 	error 	Aborted corpus2folia preprocessing
    2019-10-24 12:55:08 	info 	Processing completed

Het lijkt erop dat de GrETEL-installatie bij de UU kapot is.
