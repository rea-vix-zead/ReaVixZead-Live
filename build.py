"""Build the generated static pages; no external dependencies required."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).parent
BASE = 'https://rea-vix-zead.github.io/ReaVixZead-Live/'
LINKS = {
    'twitch': 'https://www.twitch.tv/rea_vix_zead',
    'youtube': 'https://www.youtube.com/@雷貝斯傑德_Rea_Vix_Zead',
    'discord': 'https://discord.gg/UBVjfp7vX5',
    'shared': 'https://discord.gg/FZmGSzxWY2',
    'linkgoods': 'https://linkgoods.com/reavixzead',
    'instagram': 'https://www.instagram.com/rea_vix_zead/?hl=zh-tw',
    'threads': 'https://www.threads.com/@rea_vix_zead',
    'facebook': 'https://www.facebook.com/ReaVixZead/',
    'x': 'https://x.com/Rea_Vix_Ze_ad',
    'hivebee': 'https://hivebee.com.tw/ReaVixZead/donate',
    'opay': 'https://payment.opay.tw/Broadcaster/Donate/5CC0559ED98B603A4CF3B829C1A68800',
}
EMAIL = 'rea_vix_zead_0624@carpkingdom.com'

def icon(name='arrow'):
    paths = {
        'arrow': '<path d="M5 12h14m-6-6 6 6-6 6"/>',
        'external': '<path d="M8 5H5v14h14v-3M12 5h7v7M10 14l9-9"/>',
        'play': '<path d="m9 5 11 7-11 7z"/>',
        'chat': '<path d="M4 4h16v12H9l-5 4z"/><path d="M8 9h8M8 12h5"/>',
        'heart': '<path d="M12 20 4.5 12.5a5 5 0 0 1 7.5-6.6 5 5 0 0 1 7.5 6.6Z"/>',
        'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 6 9 7 9-7"/>',
        'star': '<path d="m12 3 2.8 5.7 6.2.9-4.5 4.4 1.1 6.2-5.6-3-5.6 3 1.1-6.2L3 9.6l6.2-.9Z"/>',
    }
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths[name]}</svg>'

def ext(key, label, classes='', symbol='external'):
    return f'<a class="{classes}" href="{escape(LINKS[key],quote=True)}" target="_blank" rel="noopener noreferrer">{label}{icon(symbol)}</a>'

def btn(href, label, secondary=False):
    return f'<a class="button {"button-secondary" if secondary else ""}" href="{href}">{label}{icon()}</a>'

NAV = [('index.html','首頁'),('about.html','認識杰德'),('community.html','社群與投稿'),('social.html','社群即時動態'),('schedule.html','直播行程'),('watch.html','直播播放器'),('support.html','支持與合作')]
def header(page):
    nav=''.join(f'<a href="{url}"'+(' aria-current="page"' if page==url else '')+f'>{name}</a>' for url,name in NAV)
    return f'''<a class="skip-link" href="#main">跳至主要內容</a>
    <header class="site-header"><div class="header-inner container">
    <a href="index.html" class="brand" aria-label="Rea_Vix_Zead 首頁"><span class="brand-mark">RVZ<span>✦</span></span><span class="brand-name">Rea_Vix_Zead<small>雷貝斯杰德</small></span></a>
    <button class="menu-toggle" aria-label="開啟導覽選單" aria-controls="site-nav" aria-expanded="false"><span></span><span></span></button>
    <nav class="nav" id="site-nav" aria-label="主要導覽">{nav}</nav>
    {ext('twitch','前往 Twitch','header-watch','play')}</div></header>'''

def footer():
    return f'''<footer class="site-footer"><div class="container footer-top"><a class="brand" href="index.html"><span class="brand-mark">RVZ<span>✦</span></span><span class="brand-name">Rea_Vix_Zead<small>遊戲、聊天，還有一起玩的你。</small></span></a>
    <div class="footer-links">{ext('twitch','Twitch')}{ext('youtube','YouTube')}{ext('linkgoods','LINKGOODS')}</div></div>
    <div class="container footer-bottom"><p>© 2026 Rea_Vix_Zead. 角色圖像權利歸原權利人所有。</p><a href="support.html#contact">合作與聯絡</a><a href="about.html#guidelines">互動小約定</a></div></footer>
    <div class="toast" role="status" aria-live="polite" hidden></div><script src="assets/site.js?v=1" defer></script>'''

def page_head(kicker, title, desc):
    return f'<section class="page-heading container"><p class="eyebrow">{kicker}</p><h1>{title}</h1><p class="intro">{desc}</p></section>'

def contact_strip():
    return f'<section class="section container"><div class="closing-strip"><div><p class="eyebrow">SEE YOU IN CHAT</p><h2>下一場，在聊天室見。</h2><p>開台時間不固定，追蹤 Twitch，接收開台通知。</p></div>{ext("twitch","去 Twitch 找我","button","play")}</div></section>'

def highlight_section(kind):
    title, description = {
        'video': ('杰德精華', '第一支直播精華上架後，會放在這裡。'),
        'playlist': ('杰德精華播放清單', '精華播放清單準備好後，就能在這裡接著看。'),
    }[kind]
    return f'''
<section class="section container" id="highlights" aria-labelledby="highlights-title">
  <div class="schedule-shell" data-youtube-highlight="{kind}">
    <div class="embed-heading">
      <div>
        <p class="eyebrow">REA_VIX_ZEAD / YOUTUBE</p>
        <h2 id="highlights-title">{title}</h2>
        <p data-highlight-placeholder>{description}</p>
      </div>
      {ext('youtube', '前往 YouTube 頻道', 'text-link')}
    </div>
    <div class="twitch-frame" data-highlight-player hidden></div>
  </div>
</section>
<script src="assets/highlights.js" defer></script>'''

home=f'''
<section class="hero container"><div class="hero-copy"><p class="eyebrow"><span class="tiny-star">✦</span> REA_VIX_ZEAD · GAMING VTUBER</p>
<h1>一起玩，<br><span>就很好。</span></h1><p class="hero-name">雷貝斯杰德 <span>/ Rea_Vix_Zead</span></p>
<p class="hero-description">不定時上線打遊戲，也喜歡和你一起玩。<br>找個舒服的位置，來聊天室坐坐吧。</p>
<div class="hero-actions">{ext('twitch','前往直播間','button','play')}{btn('about.html','先認識我',True)}</div>
<p class="schedule-note"><span></span> 開台時間不固定 · 最新動態以 Twitch 為準</p></div>
<div class="portrait-stage"><div class="stage-orbit orbit-a"></div><div class="stage-orbit orbit-b"></div><div class="stage-grid"></div><span class="stage-coordinate">RVZ / PLAYER 01</span>
<img class="hero-portrait" src="assets/avatar.jpg" width="1484" height="1484" alt="Rea_Vix_Zead，黑髮紅眼的角色形象" fetchpriority="high">
<span class="stage-star star-a" aria-hidden="true">✦</span><span class="stage-star star-b" aria-hidden="true">+</span><div class="stage-caption"><span>GAME. CHAT. CONNECT.</span><small>歡迎進入我的直播小宇宙</small></div></div></section>
<section class="platform-rail container" aria-label="常用平台"><span class="rail-label">FIND ME HERE <span>↘</span></span>{ext('twitch','TWITCH','rail-link','play')}{ext('youtube','YOUTUBE','rail-link','play')}{ext('discord','DISCORD','rail-link','chat')}</section>
{highlight_section('video')}
<section class="section container"><div class="section-heading"><div><p class="eyebrow">GOOD GAMES, BETTER COMPANY</p><h2>不只看遊戲，<br>也一起創造好玩的時刻。</h2></div><a class="text-link" href="about.html">關於這個頻道 {icon()}</a></div>
<div class="experience-grid"><article class="experience"><span class="section-number">01 / PLAY</span><h3>遊戲時間</h3><p>跟著我一起進入遊戲，看看這次會遇上什麼有趣的事情。</p></article><article class="experience"><span class="section-number">02 / TOGETHER</span><h3>一起玩才有趣</h3><p>喜歡和觀眾一起玩。能否一起加入，就依當次直播與遊戲安排。</p></article><article class="experience"><span class="section-number">03 / HANG OUT</span><h3>來坐坐、聊聊天</h3><p>不用想好話題，也不必每次都出聲。自在地看台，就是一種陪伴。</p></article></div></section>
<section class="section container"><div class="community-feature"><div><p class="eyebrow">THE PARTY DOESN’T END HERE</p><h2>下播之後，<br><span>我們還能在這裡碰面。</span></h2><p>我的主要 Discord、與其他直播朋友共用的社群，還有留給故事與提問的入口。選一個你喜歡的方式，繼續這段連結。</p>{btn('community.html','找到你的社群入口')}</div><div class="chat-art" aria-hidden="true"><span class="chat-art-star">✦</span><div class="bubble bubble-a">有人要一起玩嗎？<small>GAME LOBBY / READY</small></div><div class="bubble bubble-b">來了，等我一下！<span>✧</span></div><div class="chat-art-label">GOOD COMPANY. GOOD TIMES.</div></div></div></section>
{contact_strip()}'''

about=f'''{page_head('BEHIND THE SCREEN','嗨，我是<br><span>雷貝斯杰德。</span>','Rea_Vix_Zead，一個喜歡遊戲，也喜歡和觀眾一起玩的 VTuber。')}
<section class="section container"><div class="about-intro"><div class="about-picture"><img src="assets/avatar.jpg" width="1484" height="1484" alt="雷貝斯杰德的角色形象"><span>REA_VIX_ZEAD / THE PLAYER</span></div><div class="prose"><p class="eyebrow">A LITTLE ABOUT ME</p><h2>螢幕這端是我，<br>另一端是你。</h2><p>平常興趣很多，也喜歡分享遊戲、生活與遇到的新鮮事。直播主要是打遊戲給大家看，也很喜歡有機會和觀眾一起玩。</p><p>沒有刻意把角色與本人分成兩套設定；我用虛擬形象和大家見面，也希望保留現實身分的隱私。一起享受遊戲與相處的時光，就很足夠。</p><div class="identity-tags"><span>遊戲直播</span><span>觀眾互動</span><span>不固定開台</span></div>{ext('twitch','來我的頻道坐坐','text-link')}</div></div></section>
<section class="section container" id="guidelines"><div class="section-heading"><div><p class="eyebrow">KEEP IT COMFY</p><h2>一起玩的幾個小約定</h2></div><p>讓每個人都能舒服地待在這裡。</p></div><div class="rules-grid"><article><span>01</span><h3>尊重彼此</h3><p>友善聊天，避免人身攻擊、歧視與讓人不舒服的言語。</p></article><article><span>02</span><h3>暴雷前先問問</h3><p>劇情、解法或遊戲提示，先確認當下是否需要，再分享給大家。</p></article><article><span>03</span><h3>保護隱私</h3><p>不公開或追問我與其他觀眾的現實身分、地址或私人資料。</p></article><article><span>04</span><h3>留一點空間</h3><p>避免洗版與未經同意的廣告。當次直播的安排，以頻道說明為準。</p></article></div></section>{contact_strip()}'''

socials=''.join(ext(k,label,'social-link') for k,label in [('twitch','Twitch'),('youtube','YouTube'),('instagram','Instagram'),('threads','Threads'),('facebook','Facebook'),('x','X'),('linkgoods','LINKGOODS')])
community=f'''{page_head('FIND YOUR PARTY','一起上線，<br><span>也一起聊天。</span>','直播之外，這裡還有讓你認識大家、分享故事，以及留下問題的入口。')}
<section class="section container"><div class="section-heading"><div><p class="eyebrow">DISCORD COMMUNITIES</p><h2>兩個社群，不同的相處方式。</h2></div></div><div class="community-grid"><article class="community-card"><div class="card-icon">{icon('chat')}</div><span class="pill">我的主要 Discord</span><h3>平常互動，<br>就來這裡找我。</h3><p>這是我的主要 Discord。想和我聊天、交流或一起玩，可以先從這裡開始；進入後請先閱讀社群介紹與規則。</p>{ext('discord','前往主要 Discord','button')}</article><article class="community-card members-card"><div class="card-icon">{icon('star')}</div><span class="pill">直播朋友共用社群</span><h3>和我、直播朋友們，<br>一起交流與玩遊戲。</h3><p>這是和其他直播朋友共用的 Discord，除了找我，也可以和大家聊天、交流，或揪團一起玩。加入後先看看社群規則，再一起參與互動。</p>{ext('shared','前往直播朋友共用 Discord','button button-secondary')}</article></div></section>
<section class="section container"><div class="story-panel"><div><p class="eyebrow">YOUR STORY, YOUR WAY</p><h2>有故事想說？<br><span>我在這裡聽。</span></h2><p>故事、問題、建議，或只是想分享一件小事，都可以從 LINKGOODS 的表單入口開始。</p>{ext('linkgoods','前往投稿與回饋入口','button')}</div><div class="story-notes"><div><span>01</span><h3>想收到個人回覆</h3><p>填寫 E-mail，可透過不公開的個人回覆方式聯絡。</p></div><div><span>02</span><h3>想用純匿名方式分享</h3><p>不填 E-mail，依表單說明以匿名公開方式處理；請避開你或他人的敏感資訊。</p></div></div></div></section>
<section class="section container"><div class="section-heading"><div><p class="eyebrow">AROUND THE INTERNET</p><h2>在其他地方找到我</h2></div></div><div class="social-grid">{socials}</div></section>'''

support=f'''{page_head('THANKS FOR BEING HERE','有你在，<br><span>就是很棒的支持。</span>','來看台、一起玩、在聊天室打聲招呼，都是支持。付費支持請依自己的狀況與意願選擇。')}
<section class="section container"><div class="support-grid"><article class="support-card"><div class="card-icon">{icon('play')}</div><h2>Twitch 頻道</h2><p>追蹤頻道、參與直播，或查看 Twitch 當下提供的訂閱方式與說明。</p>{ext('twitch','前往 Twitch','text-link')}</article><article class="support-card"><div class="card-icon">{icon('heart')}</div><h2>HiveBee 贊助</h2><p>透過第三方平台支持直播；金額、付款與留言方式，依該平台頁面說明。</p>{ext('hivebee','前往 HiveBee','text-link')}</article><article class="support-card"><div class="card-icon">{icon('heart')}</div><h2>歐付寶贊助</h2><p>使用歐付寶的第三方贊助入口。若需辨識身分，可依頁面說明填寫 DC／Twitch 名稱。</p>{ext('opay','前往歐付寶','text-link')}</article></div></section>
<section class="section container" id="contact"><div class="contact-box"><div><p class="eyebrow">LET’S MAKE SOMETHING FUN</p><h2>合作、聯動，<br>或一個有趣的點子。</h2><p>歡迎透過下方信箱聯絡。來信可簡單說明主題、合作內容、預計時間與方便回覆的方式。</p><a class="email-link" href="mailto:{EMAIL}">{EMAIL}</a><div class="hero-actions"><a class="button" href="mailto:{EMAIL}">寄信給我 {icon('mail')}</a><button class="button button-secondary" data-copy-email="{EMAIL}">複製信箱 {icon()}</button></div></div><div class="contact-decoration" aria-hidden="true">✦<span>LET’S<br>CONNECT.</span></div></div></section>
<section class="section container"><div class="small-note"><h2>更多連結與推薦資訊</h2><p>其他平台、推薦與支持入口，集中整理在 LINKGOODS。</p>{ext('linkgoods','開啟完整個人名片','text-link')}</div></section>'''

SOCIAL_PREVIEWS = [
    ('x', 'X', '@Rea_Vix_Ze_ad', '公開置頂貼文',
     '<blockquote class="twitter-tweet" data-theme="dark" data-dnt="true"><a href="https://twitter.com/Rea_Vix_Ze_ad/status/2000704320854221127">在 X 查看置頂貼文</a></blockquote>',
     'https://platform.twitter.com/widgets.js'),
    ('facebook', 'Facebook', 'Reavixzead雷貝斯杰德', '公開粉絲專頁預覽',
     '<iframe title="雷貝斯杰德的 Facebook 粉絲專頁" src="https://www.facebook.com/plugins/page.php?href=https%3A%2F%2Fwww.facebook.com%2FReaVixZead%2F&amp;tabs=timeline&amp;width=360&amp;height=500&amp;small_header=true&amp;adapt_container_width=true" height="500"></iframe>',
     ''),
    ('instagram', 'Instagram', '@rea_vix_zead', '精選公開貼文',
     '<iframe title="雷貝斯杰德的 Instagram 公開貼文" src="https://www.instagram.com/p/DZ-EKZwCUuu/embed/" height="530"></iframe>',
     ''),
    ('threads', 'Threads', '@rea_vix_zead', '精選公開貼文',
     '<blockquote class="text-post-media" data-text-post-permalink="https://www.threads.com/@rea_vix_zead/post/Dclb_kRFG5H" data-text-post-version="0"><a href="https://www.threads.com/@rea_vix_zead/post/Dclb_kRFG5H">在 Threads 查看這則貼文</a></blockquote>',
     'https://www.threads.com/embed.js'),
]

def social_preview(key, name, handle, kind, embed, script):
    script_attr = f' data-script="{script}"' if script else ''
    return f'''
    <article class="social-preview"{script_attr}>
      <header class="social-panel-head">
        <div>
          <h2 class="social-platform-name">{name}</h2>
          <p class="social-handle">{handle}</p>
        </div>
        {ext(key, f'前往 {name}', 'text-link')}
      </header>
      <p class="social-kind">{kind}</p>
      <div class="social-embed">{embed}</div>
      <p class="social-hint">若預覽未顯示，可前往 {name} 查看。</p>
    </article>'''

social = page_head(
    'SOCIAL UPDATES', '社群<span>即時動態</span>',
    '在這裡查看雷貝斯杰德的公開社群動態與精選貼文。'
) + f'''
<section class="section container" aria-label="社群動態預覽">
  <div class="social-previews">
    {''.join(social_preview(*platform) for platform in SOCIAL_PREVIEWS)}
  </div>
</section>
<script src="assets/social-grid.js" defer></script>
'''

pages = {
    'index.html': ('直播個人網站','遊戲、聊天，還有一起玩的你。雷貝斯杰德 Rea_Vix_Zead 的 Twitch、社群與投稿入口。',home),
    'about.html': ('認識杰德','認識 VTuber 雷貝斯杰德，以及直播互動的小約定。',about),
    'community.html': ('社群與投稿','找到我的主要 Discord、與其他直播朋友共用的社群，以及故事投稿與其他平台入口。',community),
    'social.html': ('社群即時動態','在站內查看雷貝斯杰德的 X、Facebook、Instagram 與 Threads 公開內容。',social),
    'support.html': ('支持與合作','Twitch、第三方贊助、合作聯動與電子郵件聯絡方式。',support),
}
def render_page(filename, title, description, body):
    extra_style = '<link rel="stylesheet" href="assets/social-grid.css">' if filename == 'social.html' else ''
    return f'''<!doctype html>
<html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#1b0c18"><meta name="description" content="{escape(description,quote=True)}"><title>{title}｜Rea_Vix_Zead 雷貝斯杰德</title><link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="canonical" href="{BASE+filename}"><meta property="og:type" content="website"><meta property="og:title" content="{title}｜Rea_Vix_Zead"><meta property="og:description" content="{escape(description,quote=True)}"><meta property="og:url" content="{BASE+filename}"><meta property="og:image" content="{BASE}assets/avatar.jpg"><link rel="stylesheet" href="assets/site.css?v=raven-2">{extra_style}</head>
<body>{header(filename)}<main id="main">{body}</main>{footer()}</body></html>'''

def sitemap():
    urls = ''.join(f'<url><loc>{BASE}{name}</loc></url>' for name, _ in NAV)
    return '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + urls + '</urlset>'

if __name__ == '__main__':
    for filename, (title, description, body) in pages.items():
        (ROOT / filename).write_text(render_page(filename, title, description, body), encoding='utf-8')
    (ROOT / 'sitemap.xml').write_text(sitemap(), encoding='utf-8')
    (ROOT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n', encoding='utf-8')
    (ROOT / '.nojekyll').touch()
    print(f'Built {len(pages)} pages.')
