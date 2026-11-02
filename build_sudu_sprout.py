from pathlib import Path
import re

src = Path("index.html")
out = Path("sudu-sprout/index.html")
out.parent.mkdir(parents=True, exist_ok=True)
s = src.read_text(encoding="utf-8")
emblem_b64 = Path("assets/brand/sudu-sprout-emblem.b64").read_text(encoding="ascii").strip()
wordmark_b64 = Path("assets/brand/sudu-sprout-wordmark.b64").read_text(encoding="ascii").strip()
favicon_b64 = Path("assets/brand/sudu-sprout-favicon.b64").read_text(encoding="ascii").strip()
favicon_ico_b64 = Path("assets/brand/sudu-sprout-favicon-ico.b64").read_text(encoding="ascii").strip()
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

favicon_uri=f"data:image/png;base64,{favicon_b64}"
favicon_ico_uri=f"data:image/x-icon;base64,{favicon_ico_b64}"
favicon=(
    f'<link rel="icon" type="image/png" sizes="64x64" href="{favicon_uri}">'
    f'<link rel="shortcut icon" type="image/x-icon" href="{favicon_ico_uri}">'
    f'<link rel="apple-touch-icon" href="{favicon_uri}">'
)
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
    '<a href="https://www.facebook.com/profile.php?id=61595074215241" target="_blank" rel="noopener">Facebook</a>'
    '<a href="https://xhslink.cn/m/532Djq1OS01" target="_blank" rel="noopener">Xiaohongshu / RedNote</a>'
    '<a href="https://wa.me/60109131129" target="_blank" rel="noopener">WhatsApp us</a>'
    '<a href="https://chat.whatsapp.com/BCWRL470r4TGOHF0WpDmi9" target="_blank" rel="noopener">Join WhatsApp Community</a>'
    '<a href="#faq">FAQ</a></div>',
    s,count=1,flags=re.S
)

# Add recurring delivery preferences and customer research fields.
delivery_fields = '''
      <label class="full">Delivery area
        <input name="deliveryArea" id="deliveryArea" readonly value="Enter postcode to check coverage">
        <small id="deliveryCoverage" class="address-help">We currently deliver only to selected postcodes in Kepong, Sungai Buloh and Bangsar.</small>
      </label>
      <label class="full">Preferred weekly delivery day · morning delivery
        <select name="deliveryDay" id="deliveryDay" required>
          <option value="">Select one</option>
          <option>Monday</option><option>Tuesday</option><option>Wednesday</option>
          <option>Thursday</option><option>Friday</option><option>Saturday</option><option>Sunday</option>
        </select>
        <small id="deliveryTiming" class="address-help">We deliver every morning, Monday–Sunday. Orders close at 6:00 PM, two calendar days before delivery.</small>
      </label>
      <label>Delivery fee<input name="deliveryFee" id="deliveryFee" readonly value="Enter postcode"></label>
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

# Add Malaysia address autocomplete to the delivery details form.
address_css = r'''
.address-autocomplete-wrap{position:relative}
.address-suggestions{position:absolute;left:0;right:0;top:calc(100% - 18px);z-index:40;display:none;max-height:230px;overflow:auto;background:#fff;border:1px solid rgba(36,75,53,.18);border-radius:12px;box-shadow:0 16px 40px rgba(25,48,34,.16)}
.address-suggestions.open{display:block}
.address-suggestion{display:block;width:100%;border:0;border-bottom:1px solid rgba(36,75,53,.08);background:#fff;text-align:left;padding:11px 12px;color:#203329;cursor:pointer;font:inherit;line-height:1.35}
.address-suggestion:last-child{border-bottom:0}
.address-suggestion:hover,.address-suggestion:focus{background:#fff8ed;outline:none}
.address-suggestion strong{display:block;font-size:.86rem;color:#244b35}
.address-suggestion span{display:block;margin-top:2px;font-size:.74rem;color:#6f7d75}
.address-help{display:block;margin-top:6px;font-size:.72rem;color:#718078;line-height:1.35}
'''
s=s.replace("</style>",address_css+"\n</style>",1)

old_address = '<label class="full">Delivery address<textarea name="address" rows="3" autocomplete="street-address" required></textarea></label>'
new_address = '''<label class="full address-autocomplete-wrap">Delivery address
        <textarea name="address" id="detailsAddress" rows="3" autocomplete="off" aria-autocomplete="list" aria-controls="addressSuggestions" placeholder="Start with house number, street or postcode" required></textarea>
        <div class="address-suggestions" id="addressSuggestions" role="listbox" aria-label="Address suggestions"></div>
        <small class="address-help">Start typing a house number, road name or postcode. Select a suggestion to fill the address and postcode.</small>
      </label>'''
if old_address not in s:
    raise RuntimeError("Could not find delivery address field")
s=s.replace(old_address,new_address,1)

# Clarify subscription / delivery rules while payment backend is being connected.
s=s.replace(
    '<button class="cta portal-submit full" type="submit">SAVE CUSTOMER DETAILS</button>',
    '<div class="full" style="padding:12px 14px;border:1px solid rgba(36,75,53,.14);border-radius:14px;background:#fff8ed;color:#50635a;font-size:.8rem;line-height:1.5"><strong style="color:#244b35">Weekly subscription:</strong> auto-renews each week. You can skip, pause or cancel future weeks before the cutoff. Meal changes close at 6:00 PM two days before your delivery day.</div><button class="cta portal-submit full" type="submit">PLACE ORDER &amp; VIEW PAYMENT DETAILS</button>'
)


# Connect the final customer-details form to the production Supabase backend.
old_submit = r'''  $('#detailsForm').addEventListener('submit',e=>{
    e.preventDefault();
    const data=Object.fromEntries(new FormData(e.currentTarget).entries());
    data.preference=PREFS[selectedPref];
    data.plan=currentPlan().name;
    data.mealCount=targetMeals;
    data.pricePerMeal=effectiveLaunch();
    data.total=targetMeals*effectiveLaunch();
    data.meals=Object.entries(counts).filter(([,qty])=>qty>0).map(([name,qty])=>({name,qty}));
    data.savedAt=new Date().toISOString();
    try{localStorage.setItem('macroSuduOrderDraft',JSON.stringify(data));}catch(err){}
    closePortal('detailsPortal');
    $('#successText').textContent='Thanks, '+data.name+'. Your '+data.plan+' box with '+data.mealCount+' meals has been saved in this browser as a prototype order draft.';
    openPortal('successPortal');
  });'''

new_submit = r'''  $('#detailsForm').addEventListener('submit',async e=>{
    e.preventDefault();
    const form=e.currentTarget;
    if(form.dataset.submitting==='1') return;

    const data=Object.fromEntries(new FormData(form).entries());
    const meals=Object.entries(counts).filter(([,qty])=>qty>0).map(([name,qty])=>({meal_name:name,quantity:qty}));
    const mealSubtotal=targetMeals*effectiveLaunch();
    const payload={
      full_name:data.name,
      email:data.email,
      phone:data.phone,
      age:Number(data.age),
      weight_kg:Number(data.weight),
      address:data.address,
      postcode:data.postcode,
      delivery_area:data.deliveryArea,
      delivery_day:data.deliveryDay,
      plan:currentPlan().name,
      meal_preference:PREFS[selectedPref],
      meals_per_week:targetMeals,
      meal_subtotal:mealSubtotal,
      items:meals,
      allergies:data.allergies,
      source:data.source,
      main_goal:data.mainGoal,
      marketing_consent:false,
      query_string:window.location.search
    };

    const button=form.querySelector('.portal-submit');
    let errorBox=document.getElementById('orderSaveError');
    if(!errorBox){
      errorBox=document.createElement('div');
      errorBox.id='orderSaveError';
      errorBox.className='full';
      errorBox.style.cssText='display:none;padding:11px 13px;border:1px solid rgba(180,45,35,.25);border-radius:12px;background:#fff2ef;color:#8a2d22;font-size:.82rem;line-height:1.45';
      form.insertBefore(errorBox,button);
    }

    const originalText=button.textContent;
    form.dataset.submitting='1';
    button.disabled=true;
    button.textContent='SAVING ORDER...';
    errorBox.style.display='none';

    try{
      const response=await fetch('https://cahoocydfiujuelkrqqf.supabase.co/functions/v1/create-subscription-order',{
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body:JSON.stringify(payload)
      });
      const result=await response.json().catch(()=>({}));
      if(!response.ok || !result.ok) throw new Error(result.error||'Could not save your order. Please try again.');

      const saved={
        ...data,
        preference:PREFS[selectedPref],
        plan:currentPlan().name,
        mealCount:targetMeals,
        pricePerMeal:effectiveLaunch(),
        mealSubtotal:result.meal_subtotal,
        deliveryFee:result.delivery_fee,
        total:result.total_amount,
        deliveryQuoteRequired:Boolean(result.delivery_quote_required),
        meals:meals.map(x=>({name:x.meal_name,qty:x.quantity})),
        orderNumber:result.order_number,
        deliveryDate:result.delivery_date,
        cutoffAt:result.cutoff_at,
        savedAt:new Date().toISOString()
      };
      try{localStorage.setItem('suduSproutOrderDraft',JSON.stringify(saved));}catch(err){}

      closePortal('detailsPortal');
      const quoteNote=result.delivery_quote_required?' Your delivery fee will be confirmed with you before payment.':'';
      const deliveryDateText=result.delivery_date
        ? new Intl.DateTimeFormat('en-MY',{weekday:'long',day:'numeric',month:'short',year:'numeric',timeZone:'Asia/Kuala_Lumpur'}).format(new Date(result.delivery_date+'T08:00:00+08:00'))
        : data.deliveryDay;
      $('#successText').textContent='Thanks, '+data.name+'. Your '+currentPlan().name+' subscription order '+result.order_number+' has been received. Your first morning delivery is '+deliveryDateText+'.'+quoteNote;

      const successPortal=$('#successPortal');
      if(successPortal){
        let payBox=document.getElementById('bankTransferBox');
        if(!payBox){
          payBox=document.createElement('div');
          payBox.id='bankTransferBox';
          payBox.style.cssText='margin:18px 0 8px;padding:18px;border:1px solid rgba(36,75,53,.18);border-radius:16px;background:#fffaf2;text-align:left;line-height:1.55';
          const successText=$('#successText');
          if(successText) successText.insertAdjacentElement('afterend',payBox);
        }
        const amount='RM'+Number(result.total_amount||0).toFixed(2);
        const orderRef=String(result.order_number||'');
        const waMessage='Hi Sudu & Sprout, I have made payment for order '+orderRef+' ('+amount+'). I will attach my payment receipt here.';
        payBox.innerHTML=
          '<strong style="display:block;font-size:1rem;margin-bottom:8px;color:#173c2d">Bank Transfer Payment</strong>'+
          '<div style="font-size:.88rem;color:#425247;margin-bottom:12px">Please transfer <strong>'+amount+'</strong> using your order ID <strong>'+orderRef+'</strong> as the payment reference where possible.</div>'+
          '<div style="display:grid;grid-template-columns:110px 1fr;gap:5px 12px;font-size:.9rem;margin-bottom:14px">'+
            '<span style="color:#6a746c">Bank</span><strong>Boost Bank</strong>'+
            '<span style="color:#6a746c">Account name</span><strong>CHONG KIN HOE</strong>'+
            '<span style="color:#6a746c">Account no.</span><strong>1003 0045 8300</strong>'+
            '<span style="color:#6a746c">Amount</span><strong>'+amount+'</strong>'+
            '<span style="color:#6a746c">Reference</span><strong>'+orderRef+'</strong>'+
          '</div>'+
          '<a href="https://wa.me/60109131129?text='+encodeURIComponent(waMessage)+'" target="_blank" rel="noopener" style="display:block;text-align:center;padding:12px 14px;border-radius:12px;background:#244b35;color:white;text-decoration:none;font-weight:800">I\'VE PAID — WHATSAPP RECEIPT</a>'+
          '<div style="font-size:.76rem;color:#6a746c;margin-top:10px;text-align:center">Prefer cash? WhatsApp us first to arrange payment before delivery.</div>';
      }
      openPortal('successPortal');
    }catch(err){
      errorBox.textContent=err instanceof Error?err.message:'Could not save your order. Please try again.';
      errorBox.style.display='block';
    }finally{
      form.dataset.submitting='';
      button.disabled=false;
      button.textContent=originalText;
    }
  });'''

if old_submit not in s:
    raise RuntimeError("Could not find the customer-details submit handler")
s=s.replace(old_submit,new_submit,1)

s=s.replace(
    'Prototype note: this demo stores the completed order in this browser only. Connect this form to Google Forms/Sheets or your live checkout before launch.',
    'Your order details are securely saved when you submit this form. Payment is confirmed separately until online recurring payment is enabled.'
)
s=s.replace(
    'By continuing, you agree to our future Terms &amp; Privacy Policy. No payment is taken in this prototype.',
    'By continuing, you agree to our future Terms &amp; Privacy Policy. Payment is made by bank transfer after your order is submitted.'
)


# Validate postcode coverage at the first checkout gate.
old_start_submit = r'''  $('#startForm').addEventListener('submit',e=>{
    e.preventDefault();
    gateComplete=true;
    $('#detailsEmail').value=$('#startEmail').value.trim();
    $('#detailsPostcode').value=$('#startPostcode').value.trim();
    closePortal('startPortal');
    $('#menu').scrollIntoView({behavior:'smooth',block:'start'});
    setTimeout(()=>$('#menu').classList.add('menu-ready'),250);
  });'''

new_start_submit = r'''  $('#startForm').addEventListener('submit',e=>{
    e.preventDefault();
    const form=e.currentTarget;
    const postcode=$('#startPostcode').value.trim().replace(/\D/g,'');
    const coverage={
      '52000':'Kepong','52100':'Kepong','52200':'Kepong',
      '47000':'Sungai Buloh',
      '59000':'Bangsar','59100':'Bangsar','59200':'Bangsar'
    };
    let coverageError=document.getElementById('startCoverageError');
    if(!coverageError){
      coverageError=document.createElement('div');
      coverageError.id='startCoverageError';
      coverageError.style.cssText='display:none;margin-top:10px;padding:10px 12px;border:1px solid rgba(180,45,35,.25);border-radius:12px;background:#fff2ef;color:#8a2d22;font-size:.8rem;line-height:1.45';
      form.appendChild(coverageError);
    }
    if(!coverage[postcode]){
      coverageError.textContent=postcode.length===5
        ? 'Sorry, we do not deliver to postcode '+postcode+' yet. We currently cover selected postcodes in Kepong, Sungai Buloh and Bangsar.'
        : 'Please enter a valid 5-digit postcode.';
      coverageError.style.display='block';
      gateComplete=false;
      return;
    }
    coverageError.style.display='none';
    gateComplete=true;
    $('#detailsEmail').value=$('#startEmail').value.trim();
    $('#detailsPostcode').value=postcode;
    $('#detailsPostcode').dispatchEvent(new Event('input',{bubbles:true}));
    closePortal('startPortal');
    $('#menu').scrollIntoView({behavior:'smooth',block:'start'});
    setTimeout(()=>$('#menu').classList.add('menu-ready'),250);
  });'''

if old_start_submit not in s:
    raise RuntimeError("Could not find start-form submit handler")
s=s.replace(old_start_submit,new_start_submit,1)

delivery_js = r'''
<script>
(() => {
  const area = document.getElementById('deliveryArea');
  const coverage = document.getElementById('deliveryCoverage');
  const postcode = document.getElementById('detailsPostcode');
  const feeField = document.getElementById('deliveryFee');
  const totalField = document.getElementById('estimatedTotal');
  const mealTotal = document.getElementById('sumTotal');
  const countEl = document.getElementById('sumCount');
  const form = document.getElementById('detailsForm');
  const deliveryDay = document.getElementById('deliveryDay');
  const deliveryTiming = document.getElementById('deliveryTiming');
  if (!area || !postcode || !feeField || !totalField) return;

  const DAY_INDEX = {Sunday:0,Monday:1,Tuesday:2,Wednesday:3,Thursday:4,Friday:5,Saturday:6};

  function malaysiaTodayParts(){
    const parts = new Intl.DateTimeFormat('en-CA',{
      timeZone:'Asia/Kuala_Lumpur',year:'numeric',month:'2-digit',day:'2-digit'
    }).formatToParts(new Date());
    const o={};
    parts.forEach(p=>{ if(p.type!=='literal') o[p.type]=p.value; });
    return {year:Number(o.year),month:Number(o.month),day:Number(o.day)};
  }

  function dateStringUTC(d){
    return d.getUTCFullYear()+'-'+String(d.getUTCMonth()+1).padStart(2,'0')+'-'+String(d.getUTCDate()).padStart(2,'0');
  }

  function nextEligibleDelivery(dayName){
    const target=DAY_INDEX[dayName];
    if(target===undefined) return null;
    const p=malaysiaTodayParts();
    const base=Date.UTC(p.year,p.month-1,p.day);
    for(let offset=0;offset<=14;offset++){
      const candidate=new Date(base+offset*86400000);
      if(candidate.getUTCDay()!==target) continue;
      const ds=dateStringUTC(candidate);
      const cutoff=new Date(ds+'T18:00:00+08:00');
      cutoff.setTime(cutoff.getTime()-2*86400000);
      if(Date.now()<=cutoff.getTime()) return {date:ds,cutoff};
    }
    return null;
  }

  function updateDeliveryTiming(){
    if(!deliveryTiming || !deliveryDay) return;
    if(!deliveryDay.value){
      deliveryTiming.textContent='We deliver every morning, Monday–Sunday. Orders close at 6:00 PM, two calendar days before delivery.';
      return;
    }
    const slot=nextEligibleDelivery(deliveryDay.value);
    if(!slot){
      deliveryTiming.textContent='Please choose another delivery day.';
      return;
    }
    const dateText=new Intl.DateTimeFormat('en-MY',{
      weekday:'long',day:'numeric',month:'short',year:'numeric',timeZone:'Asia/Kuala_Lumpur'
    }).format(new Date(slot.date+'T08:00:00+08:00'));
    const cutoffText=new Intl.DateTimeFormat('en-MY',{
      weekday:'short',day:'numeric',month:'short',hour:'numeric',minute:'2-digit',hour12:true,timeZone:'Asia/Kuala_Lumpur'
    }).format(slot.cutoff);
    deliveryTiming.textContent='Next available morning delivery: '+dateText+' · order cutoff: '+cutoffText+'.';
  }

  const COVERAGE = {
    '52000': {area:'Kepong', fee:0},
    '52100': {area:'Kepong', fee:0},
    '52200': {area:'Kepong', fee:0},
    '47000': {area:'Sungai Buloh', fee:5},
    '59000': {area:'Bangsar', fee:5},
    '59100': {area:'Bangsar', fee:5},
    '59200': {area:'Bangsar', fee:5}
  };

  const parseRM = value => {
    const n = Number(String(value || '').replace(/[^0-9.]/g,''));
    return Number.isFinite(n) ? n : 0;
  };
  const money = n => 'RM' + Number(n).toFixed(2);

  function updateDeliveryEstimate(){
    const pc = String(postcode.value || '').replace(/\D/g,'').slice(0,5);
    if (postcode.value !== pc) postcode.value = pc;
    const zone = COVERAGE[pc];
    const count = Number((countEl && countEl.textContent) || 0);
    const subtotal = parseRM(mealTotal && mealTotal.textContent);
    const submit = form && form.querySelector('.portal-submit');

    if (!pc){
      area.value = 'Enter postcode to check coverage';
      feeField.value = 'Enter postcode';
      totalField.value = '—';
      if(coverage){
        coverage.textContent='We currently deliver only to selected postcodes in Kepong, Sungai Buloh and Bangsar.';
        coverage.style.color='#718078';
      }
      if(submit) submit.disabled=false;
      return;
    }

    if (pc.length < 5){
      area.value = 'Checking postcode…';
      feeField.value = '—';
      totalField.value = '—';
      if(coverage){
        coverage.textContent='Enter the full 5-digit postcode.';
        coverage.style.color='#718078';
      }
      if(submit) submit.disabled=true;
      return;
    }

    if (!zone){
      area.value = 'Not covered yet';
      feeField.value = 'Not available';
      totalField.value = '—';
      if(coverage){
        coverage.textContent='Sorry, we do not deliver to postcode '+pc+' yet.';
        coverage.style.color='#8a2d22';
      }
      if(submit) submit.disabled=true;
      return;
    }

    area.value = zone.area;
    const fee = zone.fee * count;
    feeField.value = money(fee);
    totalField.value = money(subtotal + fee);
    if(coverage){
      coverage.textContent='✓ '+zone.area+' is covered for delivery.';
      coverage.style.color='#244b35';
    }
    if(submit) submit.disabled=false;
  }

  postcode.addEventListener('input', updateDeliveryEstimate);
  postcode.addEventListener('change', updateDeliveryEstimate);
  if(deliveryDay) deliveryDay.addEventListener('change', updateDeliveryTiming);
  document.addEventListener('click', e => {
    if (e.target.closest('#chooseMealsBtn,#continueBtn,.count-btn,.plan-tier')) {
      setTimeout(updateDeliveryEstimate, 0);
    }
  });
  if (mealTotal) new MutationObserver(updateDeliveryEstimate).observe(mealTotal,{childList:true,characterData:true,subtree:true});
  updateDeliveryEstimate();
  updateDeliveryTiming();
})();
</script>
'''
address_js = r'''
<script>
(() => {
  const address = document.getElementById('detailsAddress');
  const postcode = document.getElementById('detailsPostcode');
  const box = document.getElementById('addressSuggestions');
  if (!address || !postcode || !box) return;

  let timer = null;
  let controller = null;

  const clean = value => String(value || '').trim();
  const parts = p => [
    p.housenumber,
    p.street || p.name,
    p.district,
    p.city || p.county,
    p.state,
    p.postcode
  ].filter(Boolean).map(clean);

  const uniqueParts = list => {
    const seen = new Set();
    return list.filter(value => {
      const key = value.toLowerCase();
      if (!value || seen.has(key)) return false;
      seen.add(key);
      return true;
    });
  };

  const hide = () => {
    box.classList.remove('open');
    box.replaceChildren();
  };

  const selectFeature = feature => {
    const p = feature.properties || {};
    const values = uniqueParts(parts(p));
    const pc = clean(p.postcode);
    address.value = values.join(', ');
    if (pc) postcode.value = pc;
    hide();
    address.dispatchEvent(new Event('change', {bubbles:true}));
    postcode.dispatchEvent(new Event('change', {bubbles:true}));
  };

  const render = features => {
    hide();
    const malaysia = features.filter(f => {
      const cc = clean(f?.properties?.countrycode).toLowerCase();
      const country = clean(f?.properties?.country).toLowerCase();
      return !cc || cc === 'my' || country === 'malaysia';
    }).slice(0,6);

    if (!malaysia.length) return;

    malaysia.forEach(feature => {
      const p = feature.properties || {};
      const line = uniqueParts(parts(p)).join(', ');
      if (!line) return;
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'address-suggestion';
      button.setAttribute('role','option');

      const main = document.createElement('strong');
      main.textContent = [p.housenumber, p.street || p.name].filter(Boolean).join(' ') || line;
      const sub = document.createElement('span');
      sub.textContent = line + (p.country ? ', ' + p.country : '');

      button.append(main, sub);
      button.addEventListener('click', () => selectFeature(feature));
      box.appendChild(button);
    });

    if (box.childElementCount) box.classList.add('open');
  };

  async function searchAddress(){
    const a = clean(address.value);
    const pc = clean(postcode.value);
    const query = [a, pc, 'Malaysia'].filter(Boolean).join(', ');
    if ((a + pc).replace(/\s/g,'').length < 3) {
      hide();
      return;
    }

    if (controller) controller.abort();
    controller = new AbortController();

    try {
      const url = 'https://photon.komoot.io/api/?q=' + encodeURIComponent(query) +
        '&limit=8&lang=en&bbox=99.5,0.5,119.5,7.5';
      const response = await fetch(url, {signal:controller.signal, headers:{'Accept':'application/json'}});
      if (!response.ok) throw new Error('Address lookup unavailable');
      const data = await response.json();
      render(Array.isArray(data.features) ? data.features : []);
    } catch (err) {
      if (err && err.name === 'AbortError') return;
      hide();
    }
  }

  const queue = () => {
    clearTimeout(timer);
    timer = setTimeout(searchAddress, 320);
  };

  address.addEventListener('input', queue);
  postcode.addEventListener('input', queue);
  address.addEventListener('focus', () => {
    if (box.childElementCount) box.classList.add('open');
    else queue();
  });
  postcode.addEventListener('focus', queue);
  document.addEventListener('click', e => {
    if (!e.target.closest('.address-autocomplete-wrap')) hide();
  });
  address.addEventListener('keydown', e => {
    if (e.key === 'Escape') hide();
  });
})();
</script>
'''
s=s.replace('</body>',delivery_js+'\n'+address_js+'\n</body>',1)

# Add a second checkout CTA at the bottom of the meal menu.
menu_checkout_js = r'''
<style>
.menu-bottom-checkout{margin:28px auto 0;display:flex;flex-direction:column;align-items:center;gap:9px;text-align:center}
.menu-bottom-checkout .cta{min-width:220px;min-height:50px;font-size:.92rem}
.menu-bottom-checkout .cta:disabled{opacity:.48;cursor:not-allowed;transform:none;box-shadow:none}
.menu-bottom-checkout small{color:#69766f;font-size:.78rem}
@media(max-width:640px){.menu-bottom-checkout .cta{width:100%;min-height:52px}}
</style>
<script>
(() => {
  const menu=document.getElementById('menu');
  const grid=menu && menu.querySelector('.menu-grid');
  const primary=document.getElementById('continueBtn');
  if(!menu || !grid || !primary || document.getElementById('menuCheckoutBottom')) return;

  const wrap=document.createElement('div');
  wrap.className='menu-bottom-checkout';

  const button=document.createElement('button');
  button.type='button';
  button.className='cta';
  button.id='menuCheckoutBottom';
  button.textContent='CHECKOUT';

  const note=document.createElement('small');
  note.id='menuCheckoutBottomNote';

  wrap.append(button,note);
  grid.insertAdjacentElement('afterend',wrap);

  const sync=()=>{
    button.disabled=primary.disabled;
    const progress=document.getElementById('boxProgress');
    note.textContent=primary.disabled
      ? 'Complete your box ('+(progress ? progress.textContent : '')+') to continue.'
      : 'Your box is ready — continue to customer details and payment.';
  };

  button.addEventListener('click',()=>{
    if(primary.disabled){
      primary.scrollIntoView({behavior:'smooth',block:'center'});
      return;
    }
    primary.click();
  });

  new MutationObserver(sync).observe(primary,{attributes:true,attributeFilter:['disabled']});
  const progress=document.getElementById('boxProgress');
  if(progress) new MutationObserver(sync).observe(progress,{childList:true,characterData:true,subtree:true});
  sync();
})();
</script>
'''
s=s.replace('</body>',menu_checkout_js+'\n</body>',1)

# Launch-readiness cleanup: remove placeholders, make manual payment clear,
# align delivery messaging, and prevent unavailable options from being ordered.
s=re.sub(r'<section class="reviews" id="reviews">.*?</section>\s*','',s,count=1,flags=re.S)

s=s.replace(
    'Choose a plan, fill your box, then send us your customer details. The ordering flow can later be connected to payment when the full website goes live.',
    'Choose your meals, submit your details, then pay by bank transfer. Once paid, send your receipt to us on WhatsApp for verification.'
)
s=s.replace('BOX SAVED','ORDER RECEIVED')
s=s.replace('Your Sudu & Sprout order draft is ready.','Your Sudu & Sprout order has been received.')

s=s.replace(
    '<strong style="color:#244b35">Weekly subscription:</strong> auto-renews each week. You can skip, pause or cancel future weeks before the cutoff. Meal changes close at 6:00 PM two days before your delivery day.',
    '<strong style="color:#244b35">Weekly meal plan:</strong> we deliver every morning, Monday to Sunday. Orders close at 6:00 PM, two calendar days before delivery. If this week\'s cutoff has passed, your first delivery automatically moves to the same weekday next week. No automatic payment is taken; each order is confirmed after we verify your bank-transfer receipt.'
)
s=s.replace(
    'Your order details are securely saved when you submit this form. Payment is confirmed separately until online recurring payment is enabled.',
    'Your order is saved when you submit this form. Complete the bank transfer afterwards and send your receipt by WhatsApp; your payment remains pending until we verify it.'
)

s=s.replace(
    'Currently focused on Kepong, with wider KL and Central Selangor expansion planned.',
    'Currently delivering to selected postcodes in Kepong, Sungai Buloh and Bangsar.'
)
s=s.replace(
    '<p>We are currently focused on Kepong. Kuala Lumpur and Central Selangor are planned next as we expand our delivery coverage.</p><span class="pill">Kepong · current</span><span class="pill">Kuala Lumpur · soon</span><span class="pill">Central Selangor · soon</span>',
    '<p>We deliver fresh chilled meals every morning, Monday to Sunday, to selected postcodes in Kepong, Sungai Buloh and Bangsar. Kepong delivery is free; Sungai Buloh and Bangsar are RM5 per meal. Enter your postcode at checkout to confirm coverage.</p><span class="pill">Kepong · 52000 / 52100 / 52200</span><span class="pill">Sungai Buloh · 47000</span><span class="pill">Bangsar · 59000 / 59100 / 59200</span>'
)
s=s.replace(
    'We are starting with selected delivery areas around <strong>Kepong and the wider KL / Central Selangor area</strong>, with plans to expand. Delivery availability will depend on your postcode.',
    'We currently deliver to selected postcodes in <strong>Kepong, Sungai Buloh and Bangsar</strong>. Enter your postcode at checkout to confirm coverage and the applicable delivery fee.'
)

s=s.replace(
    '<p>Choose Balanced, Meat Only or Vegetarian. You can still view the full Sudu & Sprout menu.</p>',
    '<p>Choose Balanced or Meat Only for the current launch menu. Vegetarian is coming later.</p>'
)
s=s.replace(
    '<button type="button" class="option-btn pref" data-pref="vegetarian">Vegetarian</button>',
    '<button type="button" class="option-btn pref" data-pref="vegetarian" disabled aria-disabled="true" title="Coming later">Vegetarian · Coming later</button>'
)


# Subtle disabled-state styling for options that are not yet orderable.
s=s.replace(
    '</style>',
    '.option-btn:disabled,.plan-tier:disabled{opacity:.52;cursor:not-allowed;filter:saturate(.55);box-shadow:none}.option-btn:disabled:hover,.plan-tier:disabled:hover{transform:none}\\n</style>',
    1
)

if "Macro Sudu" in s: raise RuntimeError("Brand rename incomplete")
if re.search(r'\bvegan\b',s,re.I): raise RuntimeError("Vegan wording still present")
for req in ["Balanced","Meat Only","Halal ingredients","Sudu & Sprout"]:
    if req not in s and req.replace("&","&amp;") not in s: raise RuntimeError("Missing "+req)
for banned in ["Sample review 01","prototype order draft","auto-renews each week","Meal selections close at 6:00 PM","ordering flow can later be connected to payment"]:
    if banned in s: raise RuntimeError("Launch cleanup incomplete: "+banned)

out.write_text(s,encoding="utf-8")
print("Built",out,out.stat().st_size)
