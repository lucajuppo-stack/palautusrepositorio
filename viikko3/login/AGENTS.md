# Ohjeet koodausagentille (AGENTS.md)

Tämä hakemisto on WebLogin-sovellus, jota käytetään TKT20006-kurssin
viikon 3 tehtävissä 5–8. Lue nämä ohjeet ennen kuin muutat koodia.

## Projekti ja komennot

- Kyseessä on **uv-projekti** (`pyproject.toml`, `uv.lock`, Python 3.14).
  Kaikki komennot suoritetaan muodossa `uv run ...`, älä käytä `pip`-komentoa
  äläkä luo uutta virtuaaliympäristöä.
- Riippuvuudet asennetaan komennolla `uv sync`.
- Sovellus käynnistetään hakemistossa `login` komennolla
  `uv run python3 src/index.py`. Sovellus kuuntelee portissa **5001**
  (http://localhost:5001).
- Selaintesti tarvitsee asennetun Chromium-selaimen:
  `uv run rfbrowser install chromium`.

## Testit

- Robot Framework -testit suoritetaan komennolla `uv run robot src/tests`.
- **Flask-sovelluksen on oltava käynnissä** testien ajan, muuten testit
  epäonnistuvat heti.
- Yksittäinen testitapaus: `uv run robot -t "Testin nimi" src/tests/register.robot`.
- Headless-ajo (esim. CI): `uv run robot --variable HEADLESS:true src/tests`.
- Testitiedostot: `home.robot`, `login.robot`, `register.robot`.
  Useassa testitiedostossa käytettävät avainsanat ja muuttujat kuuluvat
  tiedostoon `resource.robot`, yhden tiedoston avainsanat sen omaan
  tiedostoon. Älä kopioi avainsanaa tiedostosta toiseen.
- Jokainen testi alkaa tunnetusta tilasta: `Test Setup` tyhjentää käyttäjät
  (`POST /tests/reset`) ja luo tarvittavat käyttäjät `AppLibrary.py`:n avulla.

## Arkkitehtuuri ja validoinnin sijainti

- Kerrosarkkitehtuuri: `src/app.py` (Flask-reitit ja lomakkeiden käsittely),
  `src/services/user_service.py` (sovelluslogiikka), `src/repositories/user_repository.py`
  (käyttäjien tallennus muistiin), `src/entities/user.py` (käyttäjä-olio),
  `src/templates/` (Jinja-pohjat).
- **Käyttäjätunnuksen ja salasanan validointi tapahtuu
  `src/services/user_service.py`-tiedoston `UserService`-luokan metodissa
  `validate`.** Virhetilanteissa nostetaan `UserInputError`, jonka viesti
  näytetään käyttäjälle lomakkeella flash-viestinä. Älä lisää validointia
  reitteihin tai lomakepohjiin.
- Uuden käyttäjän luonti tapahtuu `UserService.create_user`-metodissa, joka
  kutsuu ensin `validate`-metodia ja sitten `UserRepository.create`-metodia.
  `UserRepository` hylkää jo olemassa olevan käyttäjätunnuksen.
- Muutokset tehdään pieninä: älä muokkaa tiedostoja, joita tehtävä ei vaadi,
  äläkä lisää uusia riippuvuuksia ilman pyyntöä.
