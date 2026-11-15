# Hotel Lucea · Napoli — sito web
*"Dove Napoli si accende"*

Sito statico (HTML + CSS + JavaScript puro, senza framework, senza backend). Leggero, veloce, bilingue IT/EN, installabile come app (PWA).

---

## 1. Come aprirlo
**Il modo più semplice:** doppio clic su `index.html`. Si apre nel browser e funziona.

**Consigliato per le prove** (abilita anche la modalità offline/PWA): da terminale, dentro la cartella del sito:
```bash
python3 -m http.server 8000
```
poi apri <http://localhost:8000>.

## 2. Inserire i contatti (un solo file)
Apri **`js/config.js`** con un qualsiasi editor di testo e compila i campi tra virgolette:

| Campo | Cosa scrivere | Esempio di formato |
|---|---|---|
| `email` | email dell'hotel | `info@tuodominio.it` |
| `tel` | telefono fisso, come vuoi che appaia | `+39 081 …` |
| `web` | indirizzo completo del sito | `https://www.tuodominio.it` |
| `cell` | cellulare | `+39 3…` |
| `whatsapp` | numero WhatsApp **solo cifre**, con prefisso internazionale, senza `+` e spazi | `39…` |
| `indirizzo.via` / `cap` | via, numero civico e CAP | |
| `mappaEmbedUrl` | Google Maps → Condividi → *Incorpora una mappa* → copia solo l'URL dentro `src="…"` | |
| `bookingEngineUrl` | (facoltativo) link al booking engine, se lo attiverai | |
| `instagram`, `facebook` | (facoltativi) link ai profili | |
| `melodiaUrl` | sito di Hotel Melodia | |
| `cin`, `piva` | CIN (Codice Identificativo Nazionale, obbligatorio per le strutture ricettive) e Partita IVA | |
| `privacyUrl` | link alla privacy policy | |

Finché un campo è vuoto, il sito mostra **[da compilare]** e disattiva i pulsanti collegati (WhatsApp, email, mappa). Appena lo compili, tutto si attiva da solo: pulsante WhatsApp flottante, modulo di prenotazione, link, mappa e dati strutturati per Google (schema.org).

## 3. Cos'altro va personalizzato
- **Foto reali**: le immagini in `img/` (`camera-*.svg`, `galleria-*.svg`) sono illustrazioni segnaposto. Sostituiscile con foto vere (JPG/WebP, idealmente 1600×1067 px, < 300 KB) e aggiorna il nome del file in `index.html` (cerca `img/camera-` e `img/galleria-`). Togli poi le etichette "Foto reale in arrivo" (`photo-badge`).
- **Camere**: nomi, descrizioni, ospiti, metri quadri, vista e prezzi (ora `€ —`) in `index.html` (sezione `id="camere"`) e, per l'inglese, in `js/i18n.js` (chiavi `room1…room4`).
- **Storia dell'hotel**: sezione `id="storia"` (testo segnaposto).
- **Servizi**: l'elenco è indicativo, conferma quelli reali (sezione `id="servizi"`).
- **Recensioni**: per ora c'è solo lo spazio riservato. Si può inserire un widget ufficiale (Google, Booking.com, TripAdvisor) al posto del riquadro nella sezione `id="recensioni"`.
- **Testi in inglese**: tutti in `js/i18n.js`. I testi italiani sono direttamente in `index.html`.

## 4. Pubblicarlo online
**Netlify (il più semplice, gratuito):** vai su <https://app.netlify.com/drop> e trascina l'intera cartella del sito. In pochi secondi è online; poi puoi collegare il tuo dominio da *Domain settings*.

**GitHub Pages:** crea un repository, carica i file della cartella (con `index.html` nella radice), poi *Settings → Pages → Deploy from branch → main / root*.

**Hosting tradizionale (Aruba, Register, SiteGround…):** carica via FTP il contenuto della cartella nella directory pubblica (`public_html` o `www`).

Dopo la pubblicazione: compila `web` in `js/config.js`, verifica l'anteprima social con <https://www.opengraph.xyz> e i dati strutturati con <https://search.google.com/test/rich-results>.
Se aggiorni i file e usi la PWA, cambia `lucea-v1` in `lucea-v2` dentro `sw.js` per forzare l'aggiornamento della cache.

## 5. Funzionalità
- **Hero cinematografico**: il sole sorge dietro i profili di Monte Somma e Vesuvio (vettore originale dell'insegna); scorrendo la scena resta ferma e passa dall'alba alla notte: il sole tramonta, compaiono le stelle e si accendono le luci della città e della costa ("Dove Napoli si accende").
- Filo d'ottone luminoso che segna l'avanzamento nella pagina, titoli che "si accendono" con un riflesso d'ottone, card con luce che segue il mouse.
- Animazioni all'ingresso delle sezioni (IntersectionObserver) e parallasse della galleria con le *CSS scroll-driven animations* dove supportate, con fallback automatico.
- Rispetta **"riduci movimento"** del sistema operativo.
- **Mobile-first**, responsive fino al 4K.
- **IT/EN** con selettore (si ricorda la scelta; link diretti `?lang=en`).
- **Tema chiaro/scuro** automatico secondo il dispositivo, più un pulsante manuale.
- **Accessibile**: HTML semantico, link "Vai al contenuto", navigazione da tastiera, focus visibile, testi alternativi, contrasti AA.
- **Veloce**: nessun framework, font self-hosted in WOFF2 (sottoinsieme latino), immagini vettoriali e caricate in modo lazy.
- **SEO**: meta tag, Open Graph/Twitter card (`img/og-image.png`), hreflang, dati strutturati schema.org `Hotel` (si aggiornano da `config.js`).
- **PWA**: manifest, icone e service worker per l'uso offline (su http/https).
- **Prenotazione** senza backend: date con calcolo notti, ospiti e camera, poi messaggio precompilato su **WhatsApp** o **email**. Nessun dato viene salvato.
- Sezione **"Il nostro gemello: Hotel Melodia"**, pulsante **WhatsApp flottante**, mappa (segnaposto finché non inserisci il link).
- Nessun cookie di profilazione.

## 6. Struttura
```
index.html            pagina (testi italiani)
css/style.css         stile e animazioni
js/config.js          ← CONTATTI DA COMPILARE
js/i18n.js            testi inglesi + messaggi dinamici
js/main.js            interazioni
fonts/                Cormorant Garamond, Montserrat (OFL)
img/                  simbolo, icone, illustrazioni segnaposto, og-image
manifest.webmanifest, sw.js, robots.txt
screenshots/          anteprime desktop e mobile
strumenti/            script usati per generare il sito (facoltativi)
CREDITS.md            crediti e licenze
```
> Nota su `strumenti/`: `costruisci.py` rigenera `index.html` da `index.template.html`. Se modifichi direttamente `index.html` non rilanciarlo, o le modifiche verranno sovrascritte.
