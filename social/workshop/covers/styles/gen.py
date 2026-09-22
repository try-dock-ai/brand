import os,base64
MASK="data:image/png;base64,"+base64.b64encode(open("mike-cutout.png","rb").read()).decode()
FONTS = "@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,700;0,9..144,900;1,9..144,300;1,9..144,700&family=Inter:wght@400;500;600;700;800;900&family=Anton&family=Space+Grotesk:wght@500;700&family=JetBrains+Mono:wght@400;700&family=Playfair+Display:ital,wght@0,700;0,900;1,700&display=swap');"
BASE = "*{box-sizing:border-box;margin:0;padding:0}body{margin:0;-webkit-font-smoothing:antialiased;font-family:Inter,system-ui,sans-serif}.t{width:1080px;height:1080px;position:relative;overflow:hidden}"
# duotone mike: wrapper masked to cutout, colored bg, grayscale img multiplied
def duotone(color, w, extra_style, dots=True, dot=5, cls="dm"):
    return f"""
<div class="{cls}" style="position:absolute;{extra_style};width:{w}px;aspect-ratio:700/810;background:{color};-webkit-mask-image:url({MASK});-webkit-mask-size:contain;-webkit-mask-repeat:no-repeat;-webkit-mask-position:center;">
  <img src="../mike-cutout.png" style="width:100%;height:100%;display:block;filter:grayscale(1) contrast(1.05) brightness(1.75);mix-blend-mode:multiply">
  {'<div style="position:absolute;inset:0;background-image:radial-gradient(circle, rgba(0,0,0,.55) 1px, transparent 1.6px);background-size:%dpx %dpx;mix-blend-mode:overlay;opacity:.85"></div>' % (dot,dot) if dots else ''}
</div>"""

posters = {}

# 1 ZINE DUOTONE (closest to reference)
posters['01-zine-duotone'] = f"""
<style>{FONTS}{BASE}
.t{{background:#F1EEE6}}
.strip{{position:absolute;top:-6px;left:-20px;width:1140px;display:flex;flex-wrap:wrap;gap:6px 10px;transform:rotate(-2deg)}}
.tag{{font-family:Fraunces,serif;font-style:italic;font-weight:700;font-size:26px;padding:4px 12px;border-radius:6px;color:#fff;background:#14171F;box-shadow:0 0 0 3px #fff}}
.tag.b{{background:#2384FD}}
.intro{{position:absolute;left:80px;top:180px;font-size:34px;color:#14171F}}
.intro b{{font-style:italic;font-weight:800}}
.h1{{position:absolute;left:76px;top:236px;z-index:3;font-family:Fraunces,serif;font-weight:900;font-size:128px;line-height:.98;color:#14171F;letter-spacing:-0.02em}}
.mark{{display:inline-block;background:#2384FD;color:#fff;padding:0 18px 6px;transform:rotate(-1.2deg);box-shadow:6px 6px 0 rgba(20,23,31,.12)}}
.small{{font-family:Inter;font-weight:800;font-size:38px;color:#2384FD;display:inline-block;vertical-align:middle;margin-right:14px}}
.sub{{position:absolute;left:80px;top:690px;font-size:40px;line-height:1.2;color:#14171F;width:520px}}
.sub b{{font-weight:800;text-decoration:underline;text-decoration-thickness:6px;text-underline-offset:8px}}
.stk{{position:absolute;left:300px;top:850px;z-index:5;background:#14171F;color:#fff;font-family:Inter;font-weight:800;font-size:26px;line-height:1.25;padding:20px 26px;border-radius:10px;transform:rotate(-6deg);width:400px;box-shadow:0 0 0 4px #fff}}
.stk span{{color:#2384FD}}
.lock{{position:absolute;left:80px;bottom:60px;width:180px}}
</style>
<div class="t">
  <div class="strip">{''.join('<span class="tag%s">@trydock</span>' % (' b' if i%3 else '') for i in range(18))}</div>
  <div class="intro">What a <b>$100M ARR founder</b> does next</div>
  <div class="h1"><span class="mark">MIKE BUILT</span><br>BRANCH TO<br>$100M ARR</div>
  <div class="sub"><b>The next one</b> runs on a team of AI agents.</div>
  {duotone('#2384FD', 520, 'right:-30px;bottom:-30px;z-index:2', dot=5)}
  <div class="stk">Free live workshop with <span>Mike Molinet</span>, co-founder of Branch. Sept 30, 10 AM PT.</div>
  <img class="lock" src="../lockup-dark-trim.png">
</div>"""

# 2 NEWSPAPER
body = "Mike Molinet co-founded Branch and scaled it past $100M in annual recurring revenue. His second company is being built by a team of AI agents doing the marketing, engineering and operations work. On Sept 30 he shows exactly how, live, in 90 minutes. No setup, no AI experience required. Bring a laptop and a real task from your own business. "
posters['02-newspaper'] = f"""
<style>{FONTS}{BASE}
.t{{background:#F5F2EB;padding:56px 64px;color:#111}}
.mast{{font-family:'Playfair Display',serif;font-weight:900;font-size:92px;text-align:center;letter-spacing:-0.02em;line-height:1}}
.date{{display:flex;justify-content:space-between;font-size:20px;font-weight:600;border-top:3px solid #111;border-bottom:1px solid #111;padding:10px 0;margin-top:14px;text-transform:uppercase;letter-spacing:.08em}}
.hl{{font-family:'Playfair Display',serif;font-weight:900;font-size:66px;line-height:1.04;margin-top:34px;letter-spacing:-0.01em}}
.deck{{font-family:'Playfair Display',serif;font-style:italic;font-size:28px;margin-top:18px;color:#333}}
.cols{{display:flex;gap:28px;margin-top:26px;height:430px}}
.col{{flex:1;font-family:Fraunces,serif;font-size:19px;line-height:1.45;text-align:justify;column-count:1}}
.col p+p{{margin-top:12px}}
.photo{{width:470px;position:relative;border:1px solid #111;background:#ddd;overflow:hidden}}
.cap{{font-size:16px;font-style:italic;margin-top:8px;font-family:Fraunces,serif}}
.foot{{position:absolute;left:64px;right:64px;bottom:48px;border-top:3px solid #111;padding-top:12px;display:flex;justify-content:space-between;font-weight:800;font-size:22px}}
.lock{{width:120px}}
</style>
<div class="t">
  <div class="mast">The Dock Dispatch</div>
  <div class="date"><span>Wednesday, September 30, 2026</span><span>Free live edition</span><span>10 AM PT</span></div>
  <div class="hl">Founder who built Branch to $100M ARR now runs his next company on AI agents</div>
  <div class="deck">Mike Molinet to demonstrate the whole operation live, in a 90 minute workshop open to the public.</div>
  <div class="cols">
    <div class="col"><p>{body}</p><p>Attendees will watch an agent get set up for a real business task, end to end, then connect it to the tools their own company already uses. Registration is free at luma.com/cor2m92d.</p></div>
    <div>
      <div class="photo" style="height:380px">{duotone('#6B6B6B', 470, 'left:0;bottom:-40px', dot=4)}</div>
      <div class="cap">Molinet, photographed at Dock headquarters. He co-founded Branch in 2014.</div>
    </div>
  </div>
  <div class="foot"><span>Register free: luma.com/cor2m92d</span><img class="lock" src="../lockup-dark-trim.png"></div>
</div>"""

# 3 SWISS GRID
posters['03-swiss'] = f"""
<style>{FONTS}{BASE}
.t{{background:#fff;color:#111}}
.grid{{position:absolute;inset:0;background-image:linear-gradient(#e6e6e6 1px, transparent 1px),linear-gradient(90deg,#e6e6e6 1px, transparent 1px);background-size:120px 120px;background-position:60px 60px}}
.big{{position:absolute;left:52px;top:70px;font-weight:900;font-size:250px;letter-spacing:-0.07em;line-height:.9}}
.red{{position:absolute;left:60px;top:400px;width:60px;height:60px;background:#E63B2E}}
.arr{{position:absolute;left:60px;top:400px;font-weight:900;font-size:60px;letter-spacing:-0.03em;padding-left:80px;line-height:60px}}
.txt{{position:absolute;left:60px;top:540px;width:520px;font-size:30px;line-height:1.3;font-weight:500}}
.txt b{{font-weight:800}}
.meta{{position:absolute;left:60px;bottom:60px;font-size:18px;line-height:1.5;font-weight:600;text-transform:uppercase;letter-spacing:.06em}}
.ph{{position:absolute;right:60px;bottom:60px;width:420px;height:480px;background:#111;overflow:hidden}}
.ph img{{position:absolute;width:520px;left:-40px;bottom:-20px;filter:grayscale(1) contrast(1.2)}}
.lock{{position:absolute;right:60px;top:60px;width:150px}}
</style>
<div class="t">
  <div class="grid"></div>
  <div class="big">$100M</div>
  <div class="red"></div><div class="arr">ARR. Then again, with AI agents.</div>
  <div class="txt"><b>Mike Molinet</b> co-founded Branch and grew it to $100M ARR. His next company runs on a team of AI agents. He shows how, live.</div>
  <div class="meta">Free live workshop<br>Wed Sept 30, 10:00 PT<br>luma.com/cor2m92d</div>
  <div class="ph"><img src="../mike-cutout.png"></div>
  <img class="lock" src="../lockup-dark-trim.png">
</div>"""

# 4 BLACK ELECTRIC
posters['04-black-electric'] = f"""
<style>{FONTS}{BASE}
.t{{background:#0B0C10;color:#fff}}
.mike{{position:absolute;right:-90px;bottom:-20px;width:720px;filter:grayscale(1) contrast(1.4) brightness(.95)}}
.fade{{position:absolute;inset:0;background:linear-gradient(90deg,#0B0C10 30%,rgba(11,12,16,0) 70%)}}
.h1{{position:absolute;left:72px;top:230px;font-weight:900;font-size:78px;line-height:1;letter-spacing:-0.04em;width:680px;z-index:3}}
.h1 span{{color:#2384FD}}
.rule{{position:absolute;left:72px;top:600px;width:120px;height:8px;background:#2384FD}}
.sub{{position:absolute;left:72px;top:636px;font-size:30px;line-height:1.35;width:520px;color:#C9CCD6;z-index:3}}
.mono{{position:absolute;left:72px;bottom:72px;font-family:'JetBrains Mono',monospace;font-size:22px;color:#8A8F9C;letter-spacing:.04em;z-index:3}}
.mono b{{color:#fff}}
.lock{{position:absolute;left:72px;top:72px;width:170px;z-index:3}}
</style>
<div class="t">
  <img class="mike" src="../mike-cutout.png"><div class="fade"></div>
  <img class="lock" src="../lockup-white-trim.png">
  <div class="h1">Mike built Branch to <span>$100M ARR.</span><br>The next one runs on AI agents.</div>
  <div class="rule"></div>
  <div class="sub">A free 90 minute live workshop with Mike Molinet, co-founder of Branch.</div>
  <div class="mono">LIVE WORKSHOP &nbsp;/&nbsp; <b>SEPT 30</b> &nbsp;/&nbsp; <b>10:00 PT</b> &nbsp;/&nbsp; trydock.ai</div>
</div>"""

# 5 RISO
posters['05-riso'] = f"""
<style>{FONTS}{BASE}
.t{{background:#F6F1E3}}
.grain{{position:absolute;inset:0;opacity:.35;mix-blend-mode:multiply;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2'/><feColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 .5 0'/></filter><rect width='300' height='300' filter='url(%23n)'/></svg>");z-index:9;pointer-events:none}}
.h1{{position:absolute;left:64px;top:70px;font-family:Anton,Impact,sans-serif;font-size:150px;line-height:.92;color:#2140E8;text-transform:uppercase;letter-spacing:.01em;mix-blend-mode:multiply}}
.h2{{position:absolute;left:64px;top:540px;font-family:Anton,Impact,sans-serif;font-size:82px;line-height:.95;color:#FF3E7F;text-transform:uppercase;width:600px;mix-blend-mode:multiply}}
.foot{{position:absolute;left:64px;bottom:64px;font-family:'Space Grotesk';font-weight:700;font-size:28px;color:#14171F;line-height:1.35}}
.lock{{position:absolute;right:64px;top:64px;width:160px;z-index:5}}
</style>
<div class="t">
  <div class="h1">Built<br>Branch to<br>$100M ARR</div>
  <div class="h2">The next one runs on AI agents</div>
  {duotone('#FF3E7F', 620, 'right:-70px;bottom:-30px;transform:translate(10px,8px);opacity:.9;mix-blend-mode:multiply', dot=6)}
  {duotone('#2140E8', 620, 'right:-70px;bottom:-30px;mix-blend-mode:multiply', dot=6)}
  <div class="foot">Mike Molinet, co-founder of Branch<br>Free live workshop, Sept 30, 10 AM PT<br>trydock.ai</div>
  <img class="lock" src="../lockup-dark-trim.png">
  <div class="grain"></div>
</div>"""

# 6 MAGAZINE COVER
posters['06-magazine'] = f"""
<style>{FONTS}{BASE}
.t{{background:#EDE9E0}}
.mast{{position:absolute;left:0;right:0;top:80px;text-align:center;font-family:'Playfair Display',serif;font-weight:900;font-size:230px;letter-spacing:-0.03em;color:#14171F;line-height:1}}
.mike{{position:absolute;left:50%;transform:translateX(-40%);bottom:-40px;width:680px;filter:drop-shadow(0 30px 40px rgba(0,0,0,.25));z-index:2}}
.issue{{position:absolute;left:64px;top:64px;font-size:20px;font-weight:700;letter-spacing:.12em;text-transform:uppercase}}
.lock{{position:absolute;right:64px;top:56px;width:150px}}
.cl{{position:absolute;font-family:'Playfair Display',serif;z-index:3}}
.cl.a{{left:64px;top:420px;width:330px;font-size:44px;font-weight:700;line-height:1.08}}
.cl.a span{{display:block;font-family:Inter;font-weight:600;font-size:20px;margin-top:12px;color:#444;letter-spacing:.02em}}
.cl.b{{right:64px;top:520px;width:250px;text-align:right;font-size:30px;font-style:italic;line-height:1.15}}
.cl.b b{{display:block;font-family:Inter;font-style:normal;font-weight:800;font-size:46px;color:#2384FD;letter-spacing:-0.02em}}
.bar{{position:absolute;left:64px;bottom:64px;height:70px;width:190px;background:repeating-linear-gradient(90deg,#14171F 0 3px,transparent 3px 6px,#14171F 6px 8px,transparent 8px 13px);z-index:3}}
.price{{position:absolute;right:64px;bottom:64px;font-weight:800;font-size:24px;z-index:3;background:#14171F;color:#fff;padding:12px 20px;border-radius:6px}}
</style>
<div class="t">
  <div class="issue">No. 09 · September 2026 · The founder issue</div>
  <img class="lock" src="../lockup-dark-trim.png">
  <div class="mast">FOUNDER</div>
  <img class="mike" src="../mike-cutout.png">
  <div class="cl a">The $100M ARR playbook, rebuilt with AI agents<span>Mike Molinet, co-founder of Branch, on company number two</span></div>
  <div class="cl b">Live and free<b>Sept 30</b>10 AM PT, 90 minutes</div>
  <div class="bar"></div>
  <div class="price">trydock.ai</div>
</div>"""

# 7 STICKER COLLAGE
posters['07-sticker-collage'] = f"""
<style>{FONTS}{BASE}
.t{{background:#EFEAE0;font-family:'Space Grotesk',Inter,sans-serif}}
.mike{{position:absolute;left:50%;transform:translateX(-50%);bottom:-30px;width:640px;z-index:2;filter:drop-shadow(8px 0 0 #fff) drop-shadow(-8px 0 0 #fff) drop-shadow(0 8px 0 #fff) drop-shadow(0 -8px 0 #fff) drop-shadow(0 20px 30px rgba(0,0,0,.2))}}
.h1{{position:absolute;left:64px;top:150px;font-weight:700;font-size:74px;line-height:1;letter-spacing:-0.03em;width:960px;color:#14171F;z-index:1}}
.s{{position:absolute;z-index:3;font-weight:700;padding:14px 24px;border-radius:12px;box-shadow:0 0 0 5px #fff,0 10px 20px rgba(0,0,0,.18);font-size:34px}}
.tape{{position:absolute;width:180px;height:44px;background:rgba(255,220,80,.75);z-index:4;transform:rotate(-8deg)}}
.lock{{position:absolute;left:64px;top:64px;width:170px}}
.foot{{position:absolute;right:64px;top:70px;font-weight:700;font-size:22px;color:#14171F}}
</style>
<div class="t">
  <img class="lock" src="../lockup-dark-trim.png"><div class="foot">trydock.ai</div>
  <div class="h1">Mike built Branch to $100M ARR. The next one runs on AI agents.</div>
  <img class="mike" src="../mike-cutout.png">
  <div class="s" style="left:70px;top:470px;background:#FFD23F;transform:rotate(-9deg);font-size:44px">$100M ARR</div>
  <div class="s" style="right:60px;top:520px;background:#2384FD;color:#fff;transform:rotate(7deg)">AI AGENTS</div>
  <div class="s" style="left:90px;top:760px;background:#FF3E7F;color:#fff;transform:rotate(5deg);border-radius:999px;width:200px;height:200px;display:flex;align-items:center;justify-content:center;text-align:center;line-height:1.05;font-size:38px">SEPT<br>30</div>
  <div class="s" style="right:70px;top:800px;background:#14171F;color:#fff;transform:rotate(-6deg);font-size:26px;width:280px;line-height:1.2">Free live workshop<br>10 AM PT · 90 min</div>
  <div class="s" style="right:250px;top:400px;background:#fff;color:#14171F;transform:rotate(3deg);font-size:24px;padding:10px 18px">Mike Molinet · co-founder, Branch</div>
  <div class="tape" style="right:120px;top:300px;transform:rotate(12deg)"></div>
</div>"""

# 8 MINIMAL LUXURY
posters['08-minimal-serif'] = f"""
<style>{FONTS}{BASE}
.t{{background:#FBFAF6;color:#14171F;padding:72px}}
.big{{position:absolute;left:56px;top:110px;font-family:Fraunces,serif;font-weight:300;font-size:400px;letter-spacing:-0.06em;line-height:1;color:#14171F}}
.it{{position:absolute;left:72px;top:560px;font-family:Fraunces,serif;font-style:italic;font-weight:300;font-size:52px;line-height:1.15;width:640px;letter-spacing:-0.01em}}
.rule{{position:absolute;left:72px;right:72px;top:790px;height:1px;background:#14171F}}
.meta{{position:absolute;left:72px;top:820px;font-size:20px;font-weight:500;letter-spacing:.14em;text-transform:uppercase;line-height:1.9;color:#333}}
.circ{{position:absolute;right:72px;top:540px;width:230px;height:230px;border-radius:50%;overflow:hidden;background:#DEDBD2}}
.circ img{{position:absolute;width:270px;left:-20px;top:10px;filter:grayscale(1) contrast(1.1)}}
.lock{{position:absolute;right:72px;bottom:72px;width:150px}}
.arr{{position:absolute;left:72px;top:72px;font-size:20px;letter-spacing:.14em;text-transform:uppercase;font-weight:600}}
</style>
<div class="t">
  <div class="arr">Branch, annual recurring revenue</div>
  <div class="circ"><img src="../mike-cutout.png"></div>
  <div class="big">$100M</div>
  <div class="it">and then Mike Molinet started over, this time with a team of AI agents.</div>
  <div class="rule"></div>
  <div class="meta">Free live workshop · Wednesday Sept 30 · 10 AM PT<br>90 minutes · Register at luma.com/cor2m92d</div>
  <img class="lock" src="../lockup-dark-trim.png">
</div>"""

# 9 TERMINAL
posters['09-terminal'] = f"""
<style>{FONTS}{BASE}
.t{{background:#0A0F1E;color:#E6EDF3;font-family:'JetBrains Mono',monospace}}
.win{{position:absolute;left:64px;top:64px;right:64px;bottom:64px;border:1px solid #2A3550;border-radius:16px;background:#0D1428;overflow:hidden}}
.bar{{height:52px;border-bottom:1px solid #2A3550;display:flex;align-items:center;gap:10px;padding:0 20px;font-size:16px;color:#7C8AA5}}
.dot{{width:14px;height:14px;border-radius:50%}}
.code{{padding:44px 48px;font-size:31px;line-height:1.7;width:640px}}
.p{{color:#7C8AA5}} .c{{color:#2384FD}} .g{{color:#3DDC97}} .y{{color:#FFD23F}} .w{{color:#fff;font-weight:700}}
.cur{{display:inline-block;width:18px;height:34px;background:#3DDC97;vertical-align:middle;margin-left:6px}}
.mike{{position:absolute;right:-30px;bottom:0;width:440px;filter:grayscale(1) contrast(1.3);opacity:.95}}
.scan{{position:absolute;right:0;bottom:0;width:440px;height:700px;background:repeating-linear-gradient(0deg,rgba(10,15,30,.55) 0 2px,transparent 2px 5px);pointer-events:none}}
.tint{{position:absolute;right:-30px;bottom:0;width:440px;aspect-ratio:700/810;background:#2384FD;mix-blend-mode:color;-webkit-mask-image:url({MASK});-webkit-mask-size:contain;-webkit-mask-repeat:no-repeat;-webkit-mask-position:center}}
.lock{{position:absolute;left:112px;bottom:104px;width:150px}}
</style>
<div class="t">
  <div class="win">
    <div class="bar"><span class="dot" style="background:#FF5F57"></span><span class="dot" style="background:#FEBC2E"></span><span class="dot" style="background:#28C840"></span>&nbsp; mike@dock ~ workshop</div>
    <div class="code">
<span class="p">$</span> <span class="c">mike</span> --history<br>
<span class="g">✓</span> Branch: co-founded 2014<br>
<span class="g">✓</span> ARR: <span class="w">$100M+</span><br><br>
<span class="p">$</span> <span class="c">mike</span> --next<br>
<span class="y">→</span> company #2<br>
<span class="y">→</span> team: <span class="w">[ai agents]</span><br><br>
<span class="p">$</span> <span class="c">dock</span> workshop --live<br>
<span class="y">→</span> <span class="w">Sept 30, 10:00 PT</span>, free<br>
<span class="y">→</span> luma.com/cor2m92d<span class="cur"></span>
    </div>
    <img class="mike" src="../mike-cutout.png"><div class="tint"></div><div class="scan"></div>
  </div>
  <img class="lock" src="../lockup-white-trim.png">
</div>"""

# 10 BAUHAUS BLOCKS
posters['10-bauhaus-blocks'] = f"""
<style>{FONTS}{BASE}
.t{{background:#F0EFE9;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr}}
.q{{position:relative;overflow:hidden}}
.q1{{background:#2384FD;color:#fff;padding:56px}}
.q1 h1{{font-weight:900;font-size:58px;line-height:.98;letter-spacing:-0.04em}}
.q2{{background:#FFD23F}}
.q2 .c{{position:absolute;width:420px;height:420px;border-radius:50%;background:#14171F;right:-90px;top:-90px}}
.q2 .n{{position:absolute;left:56px;bottom:56px;font-weight:900;font-size:120px;line-height:.9;letter-spacing:-0.05em;color:#14171F}}
.q2 .n span{{display:block;font-size:28px;letter-spacing:.1em;font-weight:700;margin-bottom:10px}}
.q3{{background:#14171F;color:#fff;padding:56px}}
.q3 .d{{font-weight:900;font-size:120px;letter-spacing:-0.05em;line-height:.9}}
.q3 .s{{font-size:26px;margin-top:22px;line-height:1.35;color:#C9CCD6;font-weight:600}}
.q3 .s b{{color:#fff}}
.q4{{background:#F0EFE9}}
.q4 img{{position:absolute;width:600px;left:-30px;bottom:-20px}}
.q3 .lock{{position:absolute;right:56px;bottom:56px;width:140px}}
</style>
<div class="t">
  <div class="q q1"><h1>Mike built Branch to $100M ARR.<br>The next one runs on AI agents.</h1></div>
  <div class="q q2"><div class="c"></div><div class="n"><span>WITH</span>Mike<br>Molinet</div></div>
  <div class="q q3"><div class="d">Sept<br>30</div><div class="s"><b>Free live workshop</b>, 10 AM PT, 90 minutes.<br>trydock.ai</div><img class="lock" src="../lockup-white-trim.png"></div>
  <div class="q q4"><img src="../mike-cutout.png"></div>
</div>"""

for name, html in posters.items():
    open(f'styles/{name}.html','w').write('<!doctype html><html><head><meta charset="utf-8">'+html+'</html>')
print(len(posters), 'written')
