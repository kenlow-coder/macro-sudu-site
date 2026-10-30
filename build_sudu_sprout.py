from pathlib import Path
import re

src = Path("index.html")
out = Path("sudu-sprout/index.html")
out.parent.mkdir(parents=True, exist_ok=True)
s = src.read_text(encoding="utf-8")
emblem_b64 = Path("assets/brand/sudu-sprout-emblem.b64").read_text(encoding="ascii").strip()
wordmark_b64 = Path("assets/brand/sudu-sprout-wordmark.b64").read_text(encoding="ascii").strip()
emblem_uri = "data:image/png;base64," + emblem_b64
wordmark_uri = "data:image/png;base64," + wordmark_b64

s = s.replace("Macro Sudu", "Sudu & Sprout")
s = s.replace("macroSuduDraft", "suduSproutDraft")
s = s.replace("macro-sudu-draft", "sudu-sprout-draft")
s = re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Sudu & Sprout - chef-cooked, macro-measured chilled meals for busy Malaysians.">',s,count=1)
s = re.sub(r'<title>.*?</title>','<title>Sudu & Sprout | Good food made simple</title>',s,count=1)

for old,new in {"#0d4a3a":"#244b35","#173f32":"#173c2d","#ef6c00":"#d8491b","#f2b319":"#9b9a59","#173127":"#203329","#0a3429":"#173c2d"}.items():
    s=s.replace(old,new)

s = re.sub(r'<div class="announcement">.*?</div>','<div class="announcement">CHEF-COOKED · MACRO-MEASURED · HALAL INGREDIENTS · FRESHLY CHILLED</div>',s,count=1,flags=re.S)

brand_css = r'''
.ss-lockup{display:flex;align-items:center;gap:9px;min-width:0}
.ss-emblem-img{display:block;object-fit:contain;flex:0 0 auto;width:42px;height:42px}
.ss-wordmark-img{display:block;object-fit:contain;object-position:left center;width:178px;height:auto}
.ss-lockup.compact .ss-emblem-img{width:36px;height:36px}
.ss-lockup.compact .ss-wordmark-img{width:155px}
.ss-lockup.large .ss-emblem-img{width:62px;height:62px}
.ss-lockup.large .ss-wordmark-img{width:220px}
.hero-mark .ss-emblem-img{width:48px;height:48px}
.cta-logo.ss-emblem-img{width:76px;height:76px}
.success-icon.ss-emblem-img{width:78px;height:78px;margin:0 auto 16px}
.ss-round{position:relative;display:inline-grid;place-items:center;flex:0 0 auto;width:42px;height:42px;border:2px solid var(--orange);border-radius:50%;background:#fff8ed;color:var(--orange);font:800 17px/1 Georgia,"Times New Roman",serif;letter-spacing:-.08em}
.ss-round:before,.ss-round:after{content:"";position:absolute;background:var(--green);border-radius:100% 0 100% 0}
.ss-round:before{width:7px;height:15px;left:8px;bottom:6px;transform:rotate(-34deg)}
.ss-round:after{width:6px;height:12px;left:15px;bottom:5px;transform:rotate(28deg);background:#7d874d}
.ss-wordmark{display:inline-flex;align-items:baseline;white-space:nowrap;color:var(--orange);font:700 1.58rem/1 Georgia,"Times New Roman",serif;letter-spacing:-.055em}
.ss-wordmark .amp{color:var(--green);font-size:.88em;margin:0 .08em}
.ss-wordmark .leaf{display:inline-block;width:8px;height:13px;margin-left:5px;background:var(--green);border-radius:100% 0 100% 0;transform:rotate(35deg) translateY(-2px)}
.ss-lockup.compact .ss-round{width:36px;height:36px;font-size:14px}
.ss-lockup.compact .ss-wordmark{font-size:1.28rem}
.ss-lockup.large .ss-round{width:58px;height:58px;font-size:22px}
.ss-lockup.large .ss-wordmark{font-size:1.75rem}
h1,.section-head h2,.health-copy h2,.plan-main>h2,.location-card h2,.cta-panel h2,.faq-intro h2,.portal-card h3{font-family:Georgia,"Times New Roman",serif;font-weight:700}
.hero{background:radial-gradient(circle at 82% 18%,rgba(155,154,89,.12),transparent 31%)}
.benefits{background:linear-gradient(135deg,#244b35 0%,#173c2d 100%)}
.health-copy{background:linear-gradient(145deg,#244b35 0%,#173c2d 100%)}
'''
s=s.replace("</style>",brand_css+"\n</style>",1)

lockup=f'<span class="ss-lockup"><img class="ss-emblem-img" src="{emblem_uri}" alt=""><img class="ss-wordmark-img" src="{wordmark_uri}" alt="Sudu &amp; Sprout"></span>'
compact=f'<span class="ss-lockup compact"><img class="ss-emblem-img" src="{emblem_uri}" alt=""><img class="ss-wordmark-img" src="{wordmark_uri}" alt="Sudu &amp; Sprout"></span>'
large=f'<span class="ss-lockup large"><img class="ss-emblem-img" src="{emblem_uri}" alt=""><img class="ss-wordmark-img" src="{wordmark_uri}" alt="Sudu &amp; Sprout"></span>'

s=re.sub(r'<a class="brand" href="#top" aria-label="[^"]* home">.*?</a>','<a class="brand" href="#top" aria-label="Sudu &amp; Sprout home">'+lockup+'</a>',s,count=1,flags=re.S)
s=re.sub(r'<div class="hero-mark">.*?</div>',f'<div class="hero-mark"><img class="ss-emblem-img" src="{emblem_uri}" alt=""></div>',s,count=1,flags=re.S)
s=re.sub(r'<div class="summary-brand">.*?</div>','<div class="summary-brand">'+compact+'</div>',s,count=1,flags=re.S)
s=re.sub(r'<div class="brand-lockup-inner">.*?</div>','<div class="brand-lockup-inner">'+large+'</div>',s,count=1,flags=re.S)
s=re.sub(r'<div class="location-visual"><img[^>]*></div>','<div class="location-visual">'+large+'</div>',s,count=1,flags=re.S)
s=re.sub(r'<img class="cta-logo"[^>]*>',f'<img class="cta-logo ss-emblem-img" src="{emblem_uri}" alt="Sudu &amp; Sprout">',s)
s=re.sub(r'<a class="footer-lockup" href="#top">.*?</a>','<a class="footer-lockup" href="#top">'+large+'</a>',s,count=1,flags=re.S)
s=re.sub(r'<div class="portal-brand">.*?</div>','<div class="portal-brand">'+compact+'</div>',s,flags=re.S)
s=re.sub(r'<img class="success-icon"[^>]*>',f'<img class="success-icon ss-emblem-img" src="{emblem_uri}" alt="Sudu &amp; Sprout">',s)

favicon=f'<link rel="icon" type="image/png" href="{emblem_uri}">'
s=re.sub(r'<link rel="icon"[^>]*>',favicon,s,count=1) if re.search(r'<link rel="icon"[^>]*>',s) else s.replace("</title>","</title>"+favicon,1)

s=s.replace('<span class="eyebrow">Eat well, every day</span>','<span class="eyebrow">Good food fuels a brighter you</span>',1)

words=["Chef-cooked","Measured macros","Balanced eating","Halal ingredients","Fresh chilled meals","Ready in minutes","Protein-packed","Healthy convenience"]
ticker="".join("<span>"+w+"</span>" for w in words*2)
s=re.sub(r'<div class="ticker" aria-hidden="true"><div class="ticker-track">.*?</div></div>','<div class="ticker" aria-hidden="true"><div class="ticker-track">'+ticker+'</div></div>',s,count=1,flags=re.S)

s=s.replace("Mixed","Balanced")
s=s.replace("'mixed':'Balanced'","'balanced':'Balanced'")
s=s.replace('data-pref="mixed"','data-pref="balanced"')
s=s.replace("selectedPref='mixed'","selectedPref='balanced'")
s=s.replace("Choose Mixed, Meat Only or Vegetarian.","Choose Balanced, Meat Only or Vegetarian.")

s=s.replace("Try Macro Sudu","Try Sudu &amp; Sprout")
s=s.replace("LAUNCHING OFFER · 40% OFF","LAUNCH OFFER")
s=s.replace("40% launch offer","Launch pricing")
s=s.replace("after the 40% introductory discount","with the introductory launch offer")
s=s.replace("Launch discount","Launch saving")

if '<a href="#faq">FAQ</a>' not in s:
    s=s.replace('<a href="#delivery">Delivery</a><a class="cta"','<a href="#delivery">Delivery</a><a href="#faq">FAQ</a><a class="cta"',1)

s=s.replace("Professionally cooked, macro-measured meals designed to make healthier everyday eating easier in Kuala Lumpur.","Chef-cooked, macro-measured chilled meals designed to make balanced everyday eating easier.")
s=s.replace("© 2026 Sudu & Sprout · Operated by Sudu & Sprout Enterprise","© 2026 Sudu & Sprout · Sudu & Sprout Enterprise")
# Customer contact / social links
s=re.sub(
    r'<div class="footer-col"><strong>Customer</strong>.*?</div>',
    '<div class="footer-col"><strong>Customer</strong>'
    '<a href="#plans">Build your box</a>'
    '<a href="mailto:sudusprout@gmail.com">Email us</a>'
    '<a href="https://www.instagram.com/sudusprout/" target="_blank" rel="noopener">Instagram @sudusprout</a>'
    '<a href="https://wa.me/60109131129" target="_blank" rel="noopener">WhatsApp us</a>'
    '<a href="#faq">FAQ</a></div>',
    s,count=1,flags=re.S
)

# Add recurring delivery preferences and customer research fields.
delivery_fields = '''
      <label class="full">Delivery area
        <select name="deliveryArea" id="deliveryArea" required>
          <option value="">Select one</option>
          <option value="Kepong">Kepong — Free delivery</option>
          <option value="Sungai Buloh">Sungai Buloh — RM5 / meal</option>
          <option value="Bangsar">Bangsar — RM5 / meal</option>
          <option value="Other KL">Other KL — delivery fee confirmed before payment</option>
        </select>
      </label>
      <label class="full">Preferred weekly delivery day
        <select name="deliveryDay" id="deliveryDay" required>
          <option value="">Select one</option>
          <option>Monday</option><option>Tuesday</option><option>Wednesday</option>
          <option>Thursday</option><option>Friday</option><option>Saturday</option><option>Sunday</option>
        </select>
      </label>
      <label>Delivery fee<input name="deliveryFee" id="deliveryFee" readonly value="Select delivery area"></label>
      <label>Estimated weekly total<input name="estimatedTotal" id="estimatedTotal" readonly value="—"></label>
'''
s=re.sub(
    r'(<label>Postcode<input name="postcode" id="detailsPostcode" autocomplete="postal-code" required></label>)',
    r'\1'+delivery_fields,
    s,count=1
)

goal_field = '''
      <label class="full">What is your main goal for subscribing?
        <select name="mainGoal" required>
          <option value="">Select one</option>
          <option>Save time / avoid meal prep</option>
          <option>Eat more balanced meals</option>
          <option>Hit my daily protein target</option>
          <option>Build or maintain muscle</option>
          <option>Lose body fat / manage weight</option>
          <option>Track calories and macros more easily</option>
          <option>Convenient meals for work</option>
          <option>Support an active lifestyle</option>
          <option>Other</option>
        </select>
      </label>
'''
s=re.sub(
    r'(<label class="full">Where did you hear about us\?.*?</label>)',
    r'\1'+goal_field,
    s,count=1,flags=re.S
)

# Clarify subscription / delivery rules while payment backend is being connected.
s=s.replace(
    '<button class="cta portal-submit full" type="submit">SAVE CUSTOMER DETAILS</button>',
    '<div class="full" style="padding:12px 14px;border:1px solid rgba(36,75,53,.14);border-radius:14px;background:#fff8ed;color:#50635a;font-size:.8rem;line-height:1.5"><strong style="color:#244b35">Weekly subscription:</strong> auto-renews each week. You can skip, pause or cancel future weeks before the cutoff. Meal changes close at 6:00 PM two days before your delivery day.</div><button class="cta portal-submit full" type="submit">SAVE ORDER DETAILS</button>'
)

delivery_js = r'''
<script>
(() => {
  const area = document.getElementById('deliveryArea');
  const feeField = document.getElementById('deliveryFee');
  const totalField = document.getElementById('estimatedTotal');
  const mealTotal = document.getElementById('sumTotal');
  const countEl = document.getElementById('sumCount');
  if (!area || !feeField || !totalField) return;

  const parseRM = value => {
    const n = Number(String(value || '').replace(/[^0-9.]/g,''));
    return Number.isFinite(n) ? n : 0;
  };
  const money = n => 'RM' + Number(n).toFixed(2);

  function updateDeliveryEstimate(){
    const count = Number((countEl && countEl.textContent) || 0);
    const subtotal = parseRM(mealTotal && mealTotal.textContent);
    let fee = 0;
    let quoted = false;

    if (area.value === 'Sungai Buloh' || area.value === 'Bangsar') fee = count * 5;
    else if (area.value === 'Other KL') quoted = true;

    if (!area.value){
      feeField.value = 'Select delivery area';
      totalField.value = '—';
    } else if (quoted){
      feeField.value = 'To be confirmed';
      totalField.value = money(subtotal) + ' + delivery';
    } else {
      feeField.value = money(fee);
      totalField.value = money(subtotal + fee);
    }
  }

  area.addEventListener('change', updateDeliveryEstimate);
  document.addEventListener('click', e => {
    if (e.target.closest('#chooseMealsBtn,#continueBtn,.count-btn,.plan-tier')) {
      setTimeout(updateDeliveryEstimate, 0);
    }
  });
  if (mealTotal) new MutationObserver(updateDeliveryEstimate).observe(mealTotal,{childList:true,characterData:true,subtree:true});
  updateDeliveryEstimate();
})();
</script>
'''
s=s.replace('</body>',delivery_js+'\n</body>',1)

if "Macro Sudu" in s: raise RuntimeError("Brand rename incomplete")
if re.search(r'\bvegan\b',s,re.I): raise RuntimeError("Vegan wording still present")
for req in ["Balanced","Meat Only","Vegetarian","Halal ingredients","Sudu & Sprout"]:
    if req not in s and req.replace("&","&amp;") not in s: raise RuntimeError("Missing "+req)

out.write_text(s,encoding="utf-8")
print("Built",out,out.stat().st_size)
