# Harrastusseurasovellus

Sovelluksen käyttäjä voi perustaa ryhmän tietylle harrastukselle tai toiminnalle, johon toiset käyttäjät voivat liittyä. Sovellusta voi käyttää osallistujien määrän seuraamiseen ja käytännön asioista (paikka ja aika) ilmoittamiseen.

Sovelluksen ominaisuuksia ovat:

1. Käyttäjä voi luoda uuden tunnuksen ja kirjautua sillä sisään ja ulos. 
2. Käyttäjä näkee aiemmin luodut harrastusryhmät listana ja voi hakea niitä paikkakunnittain ja teemoittain.
3. Käyttäjä voi lisätä uuden harrastusryhmän järjestelmään ja poistaa aiemmin luomansa ryhmän.
4. Ryhmän perustaja voi lisätä ja poistaa uuden kokoontumismerkinnän, joka sisältää tapaamisen kuvauksen, paikan ja ajan. 
5. Ryhmän osallistuja voi merkitä osallistuvansa tai jäävänsä pois luodusta tapaamisesta.
6. Ylläpitäjä voi edellä mainittujen toimintojen lisäksi poistaa ryhmiä tai kokoontumismerkintöjä.  
7. Ylläpitäjä voi luoda ja poistaa uusia teemoja, joihin harrastusryhmät voidaan luokitella.

Päivitys 4.8.
Kirjautumisen jälkeen käyttäjä voi lisätä uuden harrastusryhmän järjestelmään ja näkee rekisteröidyt ryhmät listana etusivulla (eivät sisällä vielä paikkakuntaa ja teemaa). Sovellusta voi testata luomalla tiedostossa schema.sql osoitetut tietokantataulut ja lisäämällä oma .env tiedosto, joka sisältää seuraavat rivit DATABASE_URL=postgresql:///(oma tunnus) ja SECRET_KEY=(oma salainen avain).
Lisäksi virtuaaliympäristöön asennetaan riippuvuudet tarvittaessa komennolla

(venv) $ pip install -r requirements.txt
