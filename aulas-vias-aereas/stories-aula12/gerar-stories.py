import os, subprocess
A = '/home/user/elo-vital/aulas-vias-aereas'
IMG = A + '/slides-aula12/img'
FOTO = '/tmp/claude-0/-home-user-elo-vital/6b6bd2fd-3602-5233-a93b-cc4bb011aadf/scratchpad/capa/carla-gamba.jpg'
OUT = A + '/stories-aula12'
os.makedirs(OUT, exist_ok=True)
D = os.path.dirname(os.path.abspath(__file__))

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');
:root{--dark:#17112c;--gold:#E0A93B;--ink:#2A2526;--lav:#A5A5D3;--paper:#FBFAFB;--wine:#690D0E;--mute:#6E6A8E;--red:#A50F12}
*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;height:1920px;font-family:Poppins,sans-serif;position:relative;overflow:hidden}
.light{background:linear-gradient(160deg,#F3F2F9 0%,#E4E3EE 60%,#D9D7EA 100%);color:var(--ink)}
.dark{background:radial-gradient(circle at 80% 85%,#5b4a6e 0%,rgba(91,74,110,0) 45%),linear-gradient(160deg,#2a1d33 0%,#1b1820 55%,#141218 100%);color:#fff}
.wine{background:radial-gradient(circle at 85% 90%,#8e1d22 0%,rgba(142,29,34,0) 50%),linear-gradient(160deg,#7a1013 0%,#5a0a0c 100%);color:#FBEDED}
.gray{background:radial-gradient(circle at 85% 88%,#4a4652 0%,rgba(74,70,82,0) 48%),linear-gradient(160deg,#34323a 0%,#232227 55%,#18171b 100%);color:#F2EFF4}
.gray,.wine{--acc:#F4C46A}
.gray h1,.wine h1{color:#fff}
.gray p,.wine p{color:#F2EFF4}
.gray .pill,.wine .pill{color:#fff;border-color:rgba(255,255,255,.45)}
.gray .line{background:var(--gold)} .wine .line{background:#E8B4B8}
.gray .ref{color:#C9C3DA} .wine .ref{color:#E8C9CB}
.gray .brand{color:#C9C3DA}
.brand{position:absolute;left:90px;top:150px;font-size:24px;letter-spacing:.24em;font-weight:600;color:var(--mute)}
.dark .brand,.wine .brand{color:#C9C3DA}
.kick{font-size:28px;letter-spacing:.2em;font-weight:700;color:var(--gold);text-transform:uppercase}
h1{font-weight:800;line-height:1.08;color:var(--wine)}
.dark h1,.wine h1{color:#fff}
p{font-size:38px;line-height:1.38}
.ref{font-size:26px;color:var(--mute);font-weight:500}
.dark .ref,.wine .ref{color:#C9C3DA}
.box{position:absolute;left:90px;right:90px}
.line{width:120px;height:8px;background:var(--lav);border-radius:4px;margin:30px 0}
.red{display:inline-block;background:var(--red);color:#fff;padding:4px 22px;transform:rotate(-2deg);box-shadow:0 12px 30px rgba(0,0,0,.35)}
.pill{display:inline-block;border:3px solid var(--lav);border-radius:60px;padding:14px 34px;font-size:30px;font-weight:600}
.foto{position:absolute;border-radius:50%;overflow:hidden;border:10px solid #2d2a33;box-shadow:0 30px 60px rgba(0,0,0,.45)}
.foto img{width:100%;height:100%;object-fit:cover;object-position:50% 20%}
.sig{font-size:30px;color:#E8E1EC;font-weight:500}
"""

def page(cls, body):
    return f"<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><style>{CSS}</style></head><body class='{cls}'>{body}</body></html>"

BR = "<div class='brand'>PROJETO CULTURA DE SEGURANÇA · AULA #12</div>"

S = {}
S['Story 1 - tela 1 - enquete'] = page('gray', BR + f"""
<img src='file://{IMG}/pretraq.png' style='position:absolute;right:-40px;top:200px;width:640px;opacity:.95'>
<div class='box' style='top:1060px'>
  <div class='kick'>Monitorização</div>
  <h1 style='font-size:76px;margin-top:20px'>Qual é o primeiro recurso de monitorização da sua clínica?</h1>
</div>
<div class='box' style='top:1560px'><div class='ref'>Responda na enquete ↓ · a resposta vem no próximo story</div></div>
""")
S['Story 1 - tela 2 - resposta'] = page('wine', BR + f"""
<div class='box' style='top:330px'>
  <div class='kick'>A resposta</div>
  <h1 style='font-size:120px;margin-top:16px'>Equipe<br>treinada.</h1>
  <div class='line'></div>
</div>
<div class='box' style='top:800px'>
  <p>Em ordem decrescente de importância rotineira, <b style='color:var(--acc)'>Fukayama e Yagiela</b> situam o <b style='color:var(--acc)'>pessoal responsável</b> em primeiro lugar entre os recursos de monitorização:</p>
  <div style='margin-top:36px;display:grid;gap:16px'>
    <div class='pill' style='background:#fff;color:var(--wine);border-color:#fff'>1 · Pessoal responsável</div>
    <div class='pill'>2 · Pressão arterial não invasiva</div>
    <div class='pill'>3 · Oxímetro de pulso</div>
    <div class='pill'>4 · ECG</div>
    <div class='pill'>5 · Estetoscópio pré-traqueal ou capnógrafo</div>
  </div>
  <h1 style='font-size:50px;margin-top:56px'>E o que essa equipe precisa reconhecer antes do procedimento?</h1>
  <div class='ref' style='margin-top:26px'>Fukayama H, Yagiela JA. Int Dent J, 2006</div>
</div>
""")
S['Story 2 - apneia 48 por cento'] = page('gray', BR + f"""
<svg width='500' height='482' viewBox='0 0 560 540' style='position:absolute;right:50px;top:190px'>
<defs>
<radialGradient id='mg' cx='35%' cy='35%' r='75%'><stop offset='0' stop-color='#FFF4C8'/><stop offset='.55' stop-color='#F2CD6E'/><stop offset='1' stop-color='#C9962E'/></radialGradient>
<radialGradient id='st' cx='50%' cy='50%' r='50%'><stop offset='0' stop-color='#FFFFFF'/><stop offset='1' stop-color='#F4C46A'/></radialGradient>
<radialGradient id='halo' cx='50%' cy='50%' r='50%'><stop offset='0' stop-color='#F4C46A' stop-opacity='.28'/><stop offset='1' stop-color='#F4C46A' stop-opacity='0'/></radialGradient>
<filter id='glow' x='-80%' y='-80%' width='260%' height='260%'><feGaussianBlur stdDeviation='3' result='b'/><feMerge><feMergeNode in='b'/><feMergeNode in='SourceGraphic'/></feMerge></filter>
<mask id='cres'><rect width='560' height='540' fill='black'/><circle cx='250' cy='260' r='120' fill='white'/><circle cx='305' cy='215' r='108' fill='black'/></mask>
</defs>
<circle cx='351' cy='505' r='2' fill='#F4EBD0' opacity='0.6'/><circle cx='69' cy='57' r='3' fill='#F4EBD0' opacity='0.4'/><circle cx='394' cy='318' r='2' fill='#F4EBD0' opacity='0.8'/><circle cx='239' cy='39' r='2' fill='#F4EBD0' opacity='0.6'/><circle cx='448' cy='55' r='2' fill='#F4EBD0' opacity='0.4'/><circle cx='454' cy='50' r='3' fill='#F4EBD0' opacity='0.4'/><circle cx='248' cy='342' r='3' fill='#F4EBD0' opacity='0.8'/><circle cx='83' cy='315' r='3' fill='#F4EBD0' opacity='0.6'/><circle cx='70' cy='519' r='2' fill='#F4EBD0' opacity='0.4'/><circle cx='156' cy='168' r='2.5' fill='#F4EBD0' opacity='0.4'/><circle cx='140' cy='312' r='2.5' fill='#F4EBD0' opacity='0.8'/><circle cx='205' cy='72' r='3' fill='#F4EBD0' opacity='0.8'/><circle cx='212' cy='210' r='2' fill='#F4EBD0' opacity='0.8'/><circle cx='84' cy='308' r='2' fill='#F4EBD0' opacity='0.8'/><circle cx='230' cy='274' r='3' fill='#F4EBD0' opacity='0.8'/><circle cx='457' cy='417' r='2.5' fill='#F4EBD0' opacity='0.6'/><circle cx='484' cy='205' r='2.5' fill='#F4EBD0' opacity='0.4'/><circle cx='204' cy='377' r='2' fill='#F4EBD0' opacity='0.4'/><circle cx='327' cy='288' r='2.5' fill='#F4EBD0' opacity='0.6'/><circle cx='479' cy='167' r='3' fill='#F4EBD0' opacity='0.4'/><circle cx='140' cy='282' r='2.5' fill='#F4EBD0' opacity='0.4'/><circle cx='370' cy='97' r='2.5' fill='#F4EBD0' opacity='0.6'/>
<circle cx='250' cy='260' r='190' fill='url(#halo)'/>
<g mask='url(#cres)'><circle cx='250' cy='260' r='120' fill='url(#mg)'/></g>
<polygon points='110.0,64.0 115.1,84.9 136.0,90.0 115.1,95.1 110.0,116.0 104.9,95.1 84.0,90.0 104.9,84.9' fill='url(#st)' opacity='1' filter='url(#glow)'/><polygon points='300.0,44.0 303.2,56.8 316.0,60.0 303.2,63.2 300.0,76.0 296.8,63.2 284.0,60.0 296.8,56.8' fill='url(#st)' opacity='0.9' filter='url(#glow)'/><polygon points='420.0,148.0 424.4,165.6 442.0,170.0 424.4,174.4 420.0,192.0 415.6,174.4 398.0,170.0 415.6,165.6' fill='url(#st)' opacity='1' filter='url(#glow)'/><polygon points='60.0,247.0 62.6,257.4 73.0,260.0 62.6,262.6 60.0,273.0 57.4,262.6 47.0,260.0 57.4,257.4' fill='url(#st)' opacity='0.8' filter='url(#glow)'/><polygon points='470.0,315.0 473.0,327.0 485.0,330.0 473.0,333.0 470.0,345.0 467.0,333.0 455.0,330.0 467.0,327.0' fill='url(#st)' opacity='0.85' filter='url(#glow)'/><polygon points='230.0,408.0 232.4,417.6 242.0,420.0 232.4,422.4 230.0,432.0 227.6,422.4 218.0,420.0 227.6,417.6' fill='url(#st)' opacity='0.7' filter='url(#glow)'/><polygon points='380.0,451.0 383.8,466.2 399.0,470.0 383.8,473.8 380.0,489.0 376.2,473.8 361.0,470.0 376.2,466.2' fill='url(#st)' opacity='0.95' filter='url(#glow)'/><polygon points='30.0,411.0 31.8,418.2 39.0,420.0 31.8,421.8 30.0,429.0 28.2,421.8 21.0,420.0 28.2,418.2' fill='url(#st)' opacity='0.6' filter='url(#glow)'/><polygon points='500.0,50.0 502.0,58.0 510.0,60.0 502.0,62.0 500.0,70.0 498.0,62.0 490.0,60.0 498.0,58.0' fill='url(#st)' opacity='0.7' filter='url(#glow)'/><polygon points='160.0,172.0 161.6,178.4 168.0,180.0 161.6,181.6 160.0,188.0 158.4,181.6 152.0,180.0 158.4,178.4' fill='url(#st)' opacity='0.6' filter='url(#glow)'/><polygon points='340.0,293.0 341.4,298.6 347.0,300.0 341.4,301.4 340.0,307.0 338.6,301.4 333.0,300.0 338.6,298.6' fill='url(#st)' opacity='0.6' filter='url(#glow)'/><polygon points='520.0,442.0 521.6,448.4 528.0,450.0 521.6,451.6 520.0,458.0 518.4,451.6 512.0,450.0 518.4,448.4' fill='url(#st)' opacity='0.6' filter='url(#glow)'/>
</svg>
<div class='box' style='top:700px'>
  <div class='kick'>Avaliação da via aérea</div>
  <div style='font-size:300px;font-weight:900;color:#fff;line-height:1;margin-top:20px;letter-spacing:-.02em'>48%</div>
  <p style='font-size:44px;margin-top:24px'>dos pacientes avaliados em clínicas odontológicas apresentaram <b style='color:var(--acc)'>risco para apneia obstrutiva do sono</b>.</p>
  <div class='ref' style='margin-top:20px'>Lonia et al., Medicina, 2020 · 1.000 pacientes</div>
  <div class='line'></div>
  <p>Um paciente aparentemente hígido pode apresentar fatores predisponentes à disfunção respiratória.</p>
  <h1 style='font-size:54px;margin-top:40px'>Como identificá-los na primeira consulta?</h1>
</div>
""")
S['Story 3 - protocolo de dois minutos'] = page('wine', BR + f"""
<img src='file://{IMG}/perfil.png' style='position:absolute;right:-60px;top:150px;width:470px;opacity:.85'>
<div class='box' style='top:330px'>
  <div style='width:300px;height:300px;border-radius:50%;background:#fff;border:14px solid var(--wine);display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 20px 50px rgba(105,13,14,.15)'>
    <div style='font-size:30px;color:var(--mute);font-weight:600'>cerca de</div>
    <div style='font-size:110px;font-weight:900;color:var(--wine);line-height:1'>2</div>
    <div style='font-size:34px;color:var(--wine);font-weight:700'>minutos</div>
  </div>
</div>
<div class='box' style='top:800px'>
  <div class='kick'>Primeira consulta</div>
  <h1 style='font-size:62px;margin-top:20px'>E se você pudesse incorporar à primeira consulta um protocolo de aproximadamente dois minutos para orientar a avaliação da via aérea?</h1>
  <div class='line'></div>
  <p>Reconhecer o risco é o primeiro passo para uma assistência mais segura.</p>
  <div class='ref' style='margin-top:30px'>Investigar · mensurar · examinar · decidir · registrar</div>
</div>
""")
S['Story 4 - hoje 11h11'] = page('dark', BR + f"""
<div class='foto' style='left:90px;top:280px;width:440px;height:440px'><img src='file://{FOTO}'></div>
<img src='file://{IMG}/perfil.png' style='position:absolute;right:-70px;top:190px;width:500px;opacity:.5'>
<div class='box' style='top:760px'><div class='sig'>Profa. Carla Gamba, MSc</div></div>
<div class='box' style='top:860px'>
  <div class='kick'>Hoje, às 11h11 · YouTube</div>
  <h1 style='font-size:84px;margin-top:20px;text-transform:uppercase;font-weight:900;line-height:1.02'>Respirar não é sinônimo <span class='red' style='margin-top:14px'>de oxigenar!</span></h1>
  <p style='font-size:36px;margin-top:44px;font-weight:700;letter-spacing:.04em'>VENTILAÇÃO • OXIGENAÇÃO • PERFUSÃO</p>
  <p style='font-size:34px;margin-top:20px;color:#E8E1EC'>Aula #12 · Avaliação da via aérea do adulto e da criança. Anatomia, fisiologia, ferramentas clínicas e reconhecimento do risco.</p>
</div>
<div class='box' style='top:1500px'><div class='ref'>↓ Assistir à aula</div></div>
""")
S['Story 5 - SAVO'] = page('dark', BR.replace('AULA #12', 'SAVO') + f"""
<img src='file://{IMG}/perfil.png' style='position:absolute;right:-60px;top:150px;width:400px;opacity:.45'>
<div class='foto' style='left:90px;top:300px;width:300px;height:300px;border-width:8px'><img src='file://{FOTO}'></div>
<div class='box' style='top:700px'>
  <h1 style='font-size:68px'>Reconhecer o risco é o primeiro passo.<br><span style='color:var(--lav)'>Aprofundar sua preparação é o próximo.</span></h1>
  <div class='line'></div>
  <div class='kick' style='font-size:26px'>SAVO · Suporte Avançado de Vida para a Odontologia</div>
  <p style='margin-top:24px;color:#E8E1EC'>Avaliação clínica, monitorização, farmacologia e resposta às emergências na Odontologia.</p>
  <div style='display:flex;gap:18px;flex-wrap:wrap;margin-top:36px'>
    <div class='pill' style='color:#fff'>32 horas</div>
    <div class='pill' style='color:#fff'>Turma de até 20</div>
    <div class='pill' style='color:#fff'>Etapa presencial no Rio</div>
  </div>
</div>
<div class='box' style='top:1500px'><div class='ref'>↓ Conheça o SAVO · Nenhum curso habilita, inclusive o nosso.</div></div>
""")
S['Story 5b - Trilha 295 Online'] = page('wine', BR.replace('AULA #12', 'TRILHA 295') + f"""
<div class='foto' style='left:90px;top:300px;width:300px;height:300px;border-width:8px;border-color:#4a0709'><img src='file://{FOTO}'></div>
<img src='file://{IMG}/pretraq.png' style='position:absolute;right:-90px;top:170px;width:470px;opacity:.35'>
<div class='box' style='top:700px'>
  <div class='kick'>Para quem já tem a sedação na rotina</div>
  <h1 style='font-size:70px;margin-top:20px'>Trilha 295 Online</h1>
  <p style='margin-top:20px'>Complementação de carga horária e certificações para a Habilitação Básica em Sedação.</p>
  <div style='margin-top:44px;border-left:8px solid #E8B4B8;padding-left:30px'>
    <div style='font-size:30px;color:#E8B4B8;font-weight:600'>Formato</div>
    <div style='font-size:52px;font-weight:800;color:#fff'>104 horas telepresenciais</div>
  </div>
</div>
<div class='box' style='top:1500px'><div class='ref' style='color:#E8C9CB'>↓ Conheça a Trilha 295 · Nenhum curso habilita, inclusive o nosso.</div></div>
""")

JS = "const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});for(const [h,o] of JSON.parse(process.argv[1])){await p.goto('file://'+h);await p.waitForTimeout(1200);await p.screenshot({path:o});}await b.close()})()"
jobs = []
for name, html in S.items():
    h = os.path.join(D, name.replace(' ', '_') + '.html')
    open(h, 'w', encoding='utf8').write(html)
    jobs.append([h, os.path.join(OUT, name + '.png')])
import json
subprocess.run(['node', '-e', JS, json.dumps(jobs)], check=True)
print('ok', len(jobs))
