from pathlib import Path
import re

POSTCODE_UI = r"""
<script id="ss-malaysia-postcode-lookup">
(() => {
  const postcode = document.getElementById('detailsPostcode');
  const address = document.getElementById('detailsAddress');
  if (!postcode || postcode.dataset.ssPostcodeReady === '1') return;
  postcode.dataset.ssPostcodeReady = '1';

  const wrap = document.createElement('div');
  wrap.id = 'ssPostcodeSuggestions';
  wrap.className = 'address-suggestions';
  wrap.setAttribute('role', 'listbox');
  wrap.setAttribute('aria-label', 'Malaysian postcode suggestions');
  postcode.insertAdjacentElement('afterend', wrap);

  const note = document.createElement('small');
  note.id = 'ssPostcodeStatus';
  note.className = 'address-help';
  note.setAttribute('aria-live', 'polite');
  wrap.insertAdjacentElement('afterend', note);

  const cache = new Map();
  let timer = null;
  let controller = null;

  const clean = value => String(value || '').trim();
  const show = () => wrap.classList.add('open');
  const hide = () => { wrap.classList.remove('open'); wrap.replaceChildren(); };

  async function loadPrefix(prefix) {
    if (cache.has(prefix)) return cache.get(prefix);
    const url = 'https://cdn.jsdelivr.net/npm/@acfatah/malaysia-postcodes-data@2/dist/' + prefix + 'xxx-postcodes.json';
    const response = await fetch(url, { headers: { Accept: 'application/json' } });
    if (!response.ok) throw new Error('Postcode list unavailable');
    const rows = await response.json();
    const list = Array.isArray(rows) ? rows : (Array.isArray(rows?.data) ? rows.data : []);
    cache.set(prefix, list);
    return list;
  }

  function render(rows, value) {
    hide();
    const matches = rows.filter(row => clean(row.postcode).startsWith(value)).slice(0, 8);
    if (!matches.length) {
      note.textContent = 'No postcode matches found. You can still enter your address manually.';
      return;
    }
    matches.forEach(row => {
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'address-suggestion';
      button.setAttribute('role', 'option');
      const main = document.createElement('strong');
      main.textContent = clean(row.postcode) + ' · ' + clean(row.city);
      const sub = document.createElement('span');
      sub.textContent = clean(row.state);
      button.append(main, sub);
      button.addEventListener('click', () => {
        postcode.value = clean(row.postcode);
        postcode.dispatchEvent(new Event('change', { bubbles: true }));
        hide();
        note.textContent = '✓ Postcode recognised: ' + clean(row.city) + ', ' + clean(row.state) + '. Now enter your house/unit number and street below.';
        if (address) address.focus();
      });
      wrap.appendChild(button);
    });
    show();
    note.textContent = 'Select the correct postcode and town/state. Address and house numbers are entered in the delivery address field below.';
  }

  async function search() {
    const value = postcode.value.replace(/\D/g, '').slice(0, 5);
    if (postcode.value !== value) postcode.value = value;
    if (value.length < 2) {
      hide();
      note.textContent = 'Enter your postcode first to find the matching town and state.';
      return;
    }
    const prefix = value.slice(0, 2);
    if (controller) controller.abort();
    controller = new AbortController();
    note.textContent = 'Looking up Malaysian postcodes…';
    try {
      const rows = await loadPrefix(prefix);
      if (controller.signal.aborted) return;
      render(rows, value);
      if (value.length === 5) {
        const exact = rows.find(row => clean(row.postcode) === value);
        if (exact) {
          note.textContent = '✓ ' + clean(exact.city) + ', ' + clean(exact.state) + '. Select the matching suggestion, then enter your house/unit number and street.';
        } else {
          note.textContent = 'This postcode was not found in the reference list. Check the digits or enter your address manually.';
        }
      }
    } catch (error) {
      if (error?.name === 'AbortError') return;
      hide();
      note.textContent = 'Postcode lookup is temporarily unavailable. You can still enter your address manually.';
    }
  }

  postcode.addEventListener('input', () => {
    clearTimeout(timer);
    timer = setTimeout(search, 220);
  });
  postcode.addEventListener('focus', () => {
    if (postcode.value.length >= 2) search();
  });
  document.addEventListener('click', event => {
    if (!event.target.closest('#detailsPostcode') && !event.target.closest('#ssPostcodeSuggestions')) hide();
  });
  note.textContent = 'Enter your postcode first to find the matching town and state.';
})();
</script>
"""

STYLE = r"""
<style id="ss-postcode-lookup-style">
#ssPostcodeSuggestions{position:relative;z-index:45;display:none;margin-top:6px;max-height:220px;overflow:auto;background:#fff;border:1px solid rgba(36,75,53,.18);border-radius:12px;box-shadow:0 12px 28px rgba(25,48,34,.12)}
#ssPostcodeSuggestions.open{display:block}
#detailsPostcode{letter-spacing:.04em}
</style>
"""

for path in (Path("index.html"), Path("sudu-sprout/index.html")):
    if not path.exists():
        continue
    html = path.read_text(encoding="utf-8")
    if 'id="ss-malaysia-postcode-lookup"' in html:
        continue
    if 'id="detailsPostcode"' not in html:
        continue
    html = html.replace("</head>", STYLE + "\n</head>", 1)
    html = html.replace("</body>", POSTCODE_UI + "\n</body>", 1)
    path.write_text(html, encoding="utf-8")
    print(f"Patched {path}")
