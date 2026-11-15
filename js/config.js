/* =====================================================================
   HOTEL LUCEA — CONFIGURAZIONE CONTATTI (unico file da compilare)
   ---------------------------------------------------------------------
   Compila i campi tra virgolette. Lascia "" (vuoto) ciò che non hai:
   il sito mostrerà automaticamente "[da compilare]" e disattiverà
   i pulsanti collegati (WhatsApp, email, mappa...).
   NON servono altre modifiche al codice.
   ===================================================================== */
window.LUCEA_CONFIG = {
  /* EMAIL — es. "info@tuodominio.it" */
  email: "",

  /* TEL — telefono fisso, come vuoi che appaia, es. "+39 081 000 0000" */
  tel: "",

  /* WEB — indirizzo completo del sito, es. "https://www.tuodominio.it"
     (serve anche per SEO, Open Graph e dati strutturati) */
  web: "",

  /* CELL — cellulare, come vuoi che appaia */
  cell: "",

  /* WHATSAPP — numero in formato internazionale SOLO CIFRE,
     senza "+", spazi o trattini. Es. Italia: "39" + numero */
  whatsapp: "",

  /* INDIRIZZO — via e numero civico, CAP, città */
  indirizzo: {
    via: "",
    cap: "",
    citta: "Napoli",
    provincia: "NA",
    paese: "IT"
  },

  /* MAPPA — URL "src" dell'iframe di Google Maps
     (Google Maps > Condividi > Incorpora una mappa > copia SOLO l'URL dentro src="...") */
  mappaEmbedUrl: "",

  /* LINK PRENOTAZIONE — se in futuro userai un booking engine
     (es. pagina del channel manager), incolla qui l'URL: comparirà un pulsante dedicato */
  bookingEngineUrl: "",

  /* SOCIAL (facoltativi) */
  instagram: "",
  facebook: "",

  /* GEMELLO — sito di Hotel Melodia (stesso ingresso) */
  melodiaUrl: "",

  /* DATI LEGALI — CIN (Codice Identificativo Nazionale della struttura) e Partita IVA */
  cin: "",
  piva: "",

  /* PRIVACY — URL della privacy policy (es. generata con iubenda) */
  privacyUrl: "",

  /* ORARI reception / check-in / check-out (facoltativi, testo libero) */
  checkin: "",
  checkout: ""
};
