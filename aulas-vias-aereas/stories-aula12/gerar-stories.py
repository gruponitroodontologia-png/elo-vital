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
<img src='file://{IMG}/pretraq.png' style='position:absolute;right:-60px;top:250px;width:760px;opacity:.95'>
<div class='box' style='top:900px'>
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
<img src='file://{IMG}/lua.png' style='position:absolute;right:-110px;top:170px;width:440px;opacity:.95'>
<div class='box' style='top:560px'>
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
<img src='file://{IMG}/perfil.png' style='position:absolute;right:-140px;top:180px;width:700px;opacity:.9'>
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
<img src='file://{IMG}/perfil.png' style='position:absolute;right:-150px;top:220px;width:620px;opacity:.55'>
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
<img src='file://{IMG}/perfil.png' style='position:absolute;right:-130px;top:170px;width:480px;opacity:.5'>
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
<img src='file://{IMG}/pretraq.png' style='position:absolute;right:-180px;top:200px;width:600px;opacity:.35'>
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
