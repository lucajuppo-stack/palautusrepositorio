# Viikko 3 / tehtävä 8: agentti ja hyväksymistestit

Käytetty työkalu: **Hermes Agent** (Copilotin ja OpenCoden sijaan; tehtävänanto
sallii muunkin AI-avusteisen työkalun).

## Minkälaisen ohjetiedoston agentti generoi, ja mitä jouduit korjaamaan?

Ohjetiedosto on `login/AGENTS.md`. Sen sisältö:

- projekti on uv-projekti, komennot muodossa `uv run ...`
- sovellus käynnistetään `uv run python3 src/index.py`, portti 5001
- Robot-testit ajetaan `uv run robot src/tests`, ja Flask-sovelluksen on oltava
  käynnissä testien ajan; headless-ajo `uv run robot --variable HEADLESS:true src/tests`
- käyttäjätunnuksen ja salasanan validointi tapahtuu
  `src/services/user_service.py`:n `UserService.validate`-metodissa, virheet
  nostetaan `UserInputError`-poikkeuksena ja näytetään flash-viestinä
- avainsanojen sijoittelu: `resource.robot` vs. testitiedosto
- muutokset pieninä, ei uusia riippuvuuksia

Korjattavaa: tiedosto kirjoitettiin projektia lukemalla (`/init`-tyylinen
generointi ei ole Hermes Agentissa käytössä), ja siitä piti poistaa
ylimääräiset yleiset ohjeet, jotta tiedosto pysyy tiiviinä. Sisältöön lisättiin
käsin tieto siitä, että **testit ajetaan vasta kun sovellus on käynnissä**,
koska muuten agentti olisi ajanut testit tyhjään porttiin ja tulkinnut
yhteysvirheen testien epäonnistumiseksi.

## Noudattiko agentti pyyntöä kirjoittaa testit ennen toteutusta?

Kyllä. Järjestys oli:

1. Storyjen hyväksymiskriteerit kirjoitettiin Robot-testeiksi tiedostoon
   `src/tests/register.robot` ilman mitään muutosta sovelluskoodiin.
2. Testit ajettiin → 3 uutta testiä epäonnistui (`kallekalle`, `KalleKalle`,
   salasanan vahvistus eroaa). Epäonnistumisen syy oli oikea:
   `Title 'Welcome to Ohtu Application!' (str) should be 'Register' (str)`
   eli rekisteröityminen onnistui, vaikka sen olisi pitänyt epäonnistua.
   Tämä osoittaa, että testit oikeasti testaavat uutta toiminnallisuutta.
3. Vasta tämän jälkeen `UserService.validate`-metodiin lisättiin tarkistukset
   `password.isalpha()` ja `password != password_confirmation`.
4. Kaikki testit uudelleen: 15/15 läpi.

Tehtävän 7 kohdalla sama kaava toistettiin: `register.robot`-testit ensin
(2 epäonnistui), sitten pituustarkistukset `validate`-metodiin, sitten vihreää.

## Kuinka paljon jouduit ohjaamaan agenttia matkan varrella?

Vähän, mutta ei nollasti:

- Agentti ehdotti aluksi virheilmoituksia suomeksi; ne yhtenäistettiin
  englanniksi, koska sovelluksen olemassa olevat viestit ovat englanniksi.
- Agentti olisi sijoittanut `Set Username`/`Set Password`-avainsanat myös
  `register.robot`-tiedostoon. Ne siirrettiin `resource.robot`-tiedostoon ja
  poistettiin `login.robot`-tiedostosta, kuten materiaali neuvoo.
- Testien ajaminen vaati sen, että Flask-sovellus oli käynnissä erikseen
  (`uv run python3 src/index.py`) ja Chromium asennettuna tälle projektille
  (`uv run rfbrowser install chromium`). Tämä oli ohjeistettava agentille
  eksplisiittisesti.

## Hajosivatko testit, kun rikoit toteutuksen tarkoituksella?

Kyllä, molemmilla kerroilla.

| rikottu kohta | tulos |
| --- | --- |
| `password.isalpha()`-tarkistus poistettu (pelkistä kirjaimista koostuva salasana hyväksytään) | `Register With Password Consisting Only Of Letters` ja `... In Mixed Case` FAIL, 8/10 läpi |
| salasanan vahvistuksen tarkistus poistettu | `Register With Differing Password And Password Confirmation` FAIL, 9/10 läpi |

Toteutus palautettiin rikkomisen jälkeen ennalleen ja koko testisarja ajettiin
uudelleen: 15/15 läpi.

## Mitä uutta opit?

(Täytä tähän oma pohdintasi: mitä hyväksymistestien kirjoittaminen
testilähtöisesti opetti, mitä huomasit agentin vahvuuksista ja heikkouksista,
ja miten varmistut siitä, että agentin kirjoittamat testit eivät ole
"itsestäänselvästi läpimeneviä".)
