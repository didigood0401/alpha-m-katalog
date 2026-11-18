import re,sys
sys.stdout.reconfigure(encoding='utf-8')
D=sys.argv[1]
t=open(D+'/live.html',encoding='utf-8').read()
U='https://alpha-m-oil.ru/wp-content/uploads/2024/04/'
G=[('Нефтепродукты',[
 ('gasoline.png','Бензин','АИ-95-К4 · АИ-95-К5 · АИ-92-К2'),
 ('condensat.png','Дизельное топливо','ДТ-Л-К5 летнее · ДТ-З-К5 зимнее · ДТ-А-К5 арктическое · ДТ-Е-К5 межсезонное · ДТ-З-К5'),
 ('condensat.png','Дистиллят газового конденсата ДГКС','высокосернистое дизельное топливо'),
 ('bitum.png','Мазут топочный марка 100','содержание серы менее 3,5%'),
 ('bitum.png','Масла индустриальные','И-20, И-40'),
 ('bitum.png','Битумы нефтяные','дорожные, кровельные')]),
 ('Химическая продукция',[
 ('Methanol-3d-formula.png','Метанол технический марка А','ГОСТ 2222-95'),
 ('Methanol-3d-formula.png','Метанол технический марка А1',''),
 ('Acetone-3D-balls.png','Ацетон технический','ГОСТ 2768-84'),
 ('Toluene-from-xtal-3D-balls.png','Толуол нефтяной','растворитель, ГОСТ 14710-78'),
 ('uvd.png','Эфир метил-трет-бутиловый (МТБЭ)','марка А')]),
 ('Углеводородное сырьё',[
 ('condensat.png','Конденсат газовый стабильный','ГОСТ Р 54389-2011: 1 группа - Сосногорский ГПЗ, Сургутский ЗСК; 2 группа - Астраханский ГПЗ'),
 ('gasoline.png','Бензин газовый стабильный БГС',''),
 ('uvd.png','Фракция изопентановая','марка А'),
 ('uvd.png','Пентан-гексановая фракция','Амурский ГПЗ, Оренбургский ГЗ'),
 ('condensat.png','Дистиллят газового конденсата',''),
 ('absorb.png','Абсорбент олигомеризат',''),
 ('uvd.png','Широкая фракция лёгких углеводородов ШФЛУ',''),
 ('gasoline.png','Высокооктановые компоненты для производства бензина','')])]
def card(img,title,desc):
    d=f'<p class="elementor-image-box-description">{desc}</p>' if desc else ''
    return f'''<div class="elementor-element elementor-element-65719ad elementor-position-left elementor-vertical-align-middle elementor-widget__width-initial elementor-widget-tablet__width-initial elementor-widget-mobile__width-inherit elementor-widget elementor-widget-image-box" data-widget_type="image-box.default"><div class="elementor-widget-container"><div class="elementor-image-box-wrapper"><figure class="elementor-image-box-img"><img decoding="async" loading="lazy" width="200" height="200" src="{U}{img}" class="elementor-animation-pulse attachment-full size-full" alt="{title}"></figure><div class="elementor-image-box-content"><h3 class="elementor-image-box-title">{title}</h3>{d}</div></div></div></div>\n'''
def head(n,txt):
    return f'<div class="elementor-element elementor-widget elementor-widget-heading am-cat-h"><div class="elementor-widget-container"><h3 class="elementor-heading-title">{txt} <span>{n} поз.</span></h3></div></div>\n'
npos={'Нефтепродукты':12,'Химическая продукция':5,'Углеводородное сырьё':11}
new=''.join(head(npos[g],g)+''.join(card(*c) for c in cs) for g,cs in G)
a=t.find('<div class="elementor-element elementor-element-65719ad')
b=t.find('<section class="elementor-section elementor-inner-section elementor-element elementor-element-71aa9d2')
assert a>0 and b>a
t=t[:a]+new+t[b:]
css='''<style id="am-catalog">
.am-cat-h{width:100%;margin:34px 15px 6px}
.am-cat-h .elementor-heading-title{font-family:"Russo One",Sans-serif;font-size:26px;font-weight:500;text-transform:uppercase;color:var(--e-global-color-75ee670);border-bottom:2px solid #c8102e;padding-bottom:8px}
.am-cat-h span{font-family:"Oswald",Sans-serif;font-size:15px;color:#c8102e;margin-left:10px;letter-spacing:.04em}
.elementor-element-65719ad .elementor-image-box-description{margin:4px 0 0;font-size:14px;line-height:1.4;color:#666}
@media(max-width:767px){.am-cat-h .elementor-heading-title{font-size:21px}.am-cat-h{margin:24px 0 4px}}
</style>'''
t=t.replace('</head>','<meta name="robots" content="noindex,nofollow">\n'+css+'\n</head>',1)
t=t.replace('href="/','href="https://alpha-m-oil.ru/').replace("href='/","href='https://alpha-m-oil.ru/")
open(D+'/preview/index.html','w',encoding='utf-8').write(t)
print('ok',sum(len(c) for _,c in G))
