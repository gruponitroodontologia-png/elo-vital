# Memória de trabalho — Grupo Nitro / SAVO

> Este arquivo é a **memória viva** da nossa colaboração. O Claude Code o lê
> automaticamente no início de cada sessão — então toda conversa nova já
> começa sabendo de tudo o que combinamos. **Mantê-lo atualizado é rotina:**
> ao fim de um bloco de trabalho relevante, atualizo e faço commit. A Carla
> pode pedir "salva o aprendizado" a qualquer momento.
>
> Nunca gravar segredos aqui (senhas, service_role, tokens). Isto é um
> arquivo versionado e público do repositório.

## Quem é quem
- **Carla Gamba** — CD, Mestre; cofundadora e coordenadora de cursos do Grupo
  Nitro. É a interlocutora principal e a **autoridade clínica**: conteúdo de
  saúde só vai ao ar com validação dela. Fala-se com ela em **português**.
- **Grupo Nitro** — formação em segurança e sedação em odontologia.

## Como trabalhamos (regras combinadas)
- **Idioma:** sempre português (pt-BR).
- **Branch de trabalho:** `claude/focused-planck-5yplma`. A página em produção
  sai da `main` (merge → Vercel). **Nunca publicar/colocar no ar sem
  autorização explícita da Carla.**
- A cada alteração: **commit + push** e, quando for a página de vendas,
  **republicar o Artifact** (mesmo link, ver abaixo) e **regenerar
  `savo-elementor.html`** a partir do `index.html`.
- Preferir **decisões de ofício** a ficar pedindo escolha a cada frase — a
  linguagem já está acordada (ver abaixo). A Carla valoriza ação e ousadia.
- Entregáveis (PDFs, imagens) são gerados com Chromium/Playwright
  (`/opt/pw-browsers/chromium-*/chrome-linux/chrome`, `--no-sandbox`).

## Produto principal: página de vendas do SAVO
- **SAVO** = Suporte Avançado de Vida para a Odontologia. Curso híbrido de
  **32h** (16h telepresenciais ao vivo + 16h presenciais), **Turma 1 no Rio
  de Janeiro**.
- Arquivo: **`index.html`** (servido na raiz pela Vercel). Versão Elementor:
  `savo-elementor.html` (fatia fonts+style+body, regenerada a cada mudança).
- **Domínio em produção:** https://savo.gruponitro.com.br (Vercel, deploy
  automático a partir da `main`).
- **Artifact (prévia compartilhável):**
  https://claude.ai/artifact/HjrWsq7giVDM7NxdQqUfBb
- **Datas Turma 1:** telepresencial ao vivo **28/11, 30/11, 01/12, 02/12**;
  presencial **5 e 6/12** (9h–19h), Rio de Janeiro.
- **Programa (ordem atual):** 01 Monitorização (Profª Sandra Chicharo) ·
  02 Fundamentação Jurídica (Carla Gamba e Danielle Coelho) · 03 Avaliação
  Clínica e Populações Especiais (Carla e Danielle) · 04 Farmacologia e
  Resposta à Emergência (Carla Gamba) · Etapa Presencial.
- **Preço:** 1º lote R$ 2.970 à vista · **12× R$ 307** · lotes R$ 2.970 /
  3.170 / 3.370, mudam a cada 20 dias.
- **Checkout (Kiwify):** https://pay.kiwify.com.br/sttjYOY
- **WhatsApp:** (21) 93500-3307 (botão flutuante "Fale conosco" + FAQ).
- **Prazo da CFO** usado no lançamento: **janeiro de 2027** (habilitação em
  sedação).
- Decisão clínica: **cricotireoidotomia / via aérea cirúrgica REMOVIDA** de
  toda a página (fora do escopo do CD). Via aérea termina em **dispositivos
  supraglóticos** (resgate ventilatório).
- **Open Graph:** `assets/og-savo.jpg` (1200×630), URL absoluta no domínio.

## Produto: Fundamentos da Estratégia Multimodal na Sedação (online)
- Curso 100% online gravado, 46h, 12 meses de acesso. Artifact (prévia):
  https://claude.ai/artifact/46ToVGfgvDErju9tTR8dYt · cópia da fonte em
  `multimodal/index.html` (atualizar a cópia a cada republicação).
- Black Friday até 07/12: **12× R$ 197 ou R$ 1.970** à vista (regular R$ 2.970)
  + bônus Emergências Médicas 8h (teórico) + mentoria 1h para os 5 primeiros.
- Posicionamento: *"Não é mais um curso de sedação. É o raciocínio
  farmacológico que decide a sedação."* Seção "Critério, não receita".
- **Hero da página multimodal (12/11/2026):** o botão de compra e o preço
  (12x de R$ 197 · R$ 1.970 à vista) ficam **na primeira tela**, no celular e no
  desktop (medido com Playwright: antes o botão caía a ~340 px abaixo da dobra no
  celular). Barra fixa no rodapé do celular ("Quero me inscrever") aparece quando
  o botão do topo sai da tela e some na área de compra. O botão do hero leva a
  `#inscricao`; **o link de checkout do curso multimodal ainda não existe**
  (`data-todo="link de checkout"`).
- **Página multimodal enxuta (12/11/2026):** de 16 para **9 blocos** (Para quem ·
  Critério, não receita + conceito · Depoimentos · Programa em acordeão ·
  Quem conduz · Como funciona + é/não é · Investimento único com garantia · FAQ ·
  Fechamento); texto −20%; **um só texto de botão** ("Quero me inscrever");
  **foto da Profa. Carla** (assets/carla-gamba.jpg, embutida) no hero e em Quem
  conduz. Cópia de segurança do estado anterior fora do repositório.
- **Espaçamento da página multimodal (12/11/2026, skill artifact-design):**
  ritmo único (seções `clamp(56px,8vw,88px)`, grades e cartões com `clamp`),
  medida de leitura 68ch, `text-wrap: balance/pretty`, bloco "Critério" em 2×2
  com o mesmo estilo de cartão das demais seções (sem barra lateral), acordeão
  com título e "+" alinhados. A Carla lembra de uma skill de tipografia/interface
  que "começa com ok": **não existe na conta** (21 skills ativas conferidas);
  usadas `artifact-design` (sessão) e, se preciso, `theme-factory`.
- **Números com movimento (12/11/2026):** faixa logo abaixo do topo da página
  multimodal com 4 números **verdadeiros** que contam de 0 até o valor ao entrar
  na tela (26 anos · 46 h · 5 workshops · 12 meses). Números finais já no HTML
  (sem JS e com "movimento reduzido" nada anima). Referência da Carla: página
  lp.ciclosaude.com.br/curso-sme (GreatPages; números "+800 Alunos, 35h, 23Gb";
  o script de animação é externo e não foi lido). **Nunca inventar números de
  prova social**; pedir à Carla dados reais (alunos formados, turmas, horas).
- **Removido** da seção "Para quem" o trecho com a estimativa de Silveira et al.
  (J Dent 2021) e a referência no fim (decisão da Carla); a frase inicial "O medo
  odontológico acomete parcela expressiva da população adulta" ficou **sem fonte**.
- **Depoimentos colocados (12/11/2026):** pasta "Depoimentos Estratégia Multimodal"
  (Drive): **Dra. Juliana** (odontopediatra; texto de postagem dela, lido por OCR do
  print "Depoimento Juliana.jpeg") já na página; **Ana Paula** (vídeo mp4 15,5 MB,
  dono estudiofnoleto@gmail.com) **não cabe**: o conector baixa só até 10 MB e a página
  não toca vídeo de Drive/YouTube → precisa de **link** (YouTube "não listado" ou Drive
  "qualquer pessoa com o link") para um botão "Assistir". Faltam sobrenome/profissão/
  cidade e **autorização de imagem/texto** de cada pessoa. **Não colocar vídeos de
  alunos no repositório (é público).**
- **Decisão da Carla (12/11/2026):** na página multimodal entra **só o depoimento
  escrito** (Dra. Juliana); sem vídeos. Seção "Depoimento" com um único cartão em
  destaque. Pendentes: sobrenome/cidade da Juliana e autorização de uso.
- **Depoimentos na página (12/11/2026, 3 cartões de texto):** Dra. Juliana Giraldi
  (Estratégia Multimodal); **Leandro** (aluno do Guia Clínico do N₂O, online; print de
  conversa de WhatsApp — **cortada a frase "sem risco"**, afirmação absoluta que a
  Carla precisa validar antes de qualquer uso); **Odontovolp Cursos** (story do
  Instagram: "Quem não assistiu perdeu o espetáculo!", sobre a aula dos Profs. Luiz
  Alberto e Carla Gamba). **Não usados:** mensagem com foto do SAVO (presencial) e a
  repetição do story. Pendentes: **autorização** de Leandro (conversa privada) e da
  Odontovolp; sobrenomes.
- **Depoimentos na página multimodal, versão final (12/11/2026, 5 cartões de texto):**
  Dra. Juliana Giraldi · Leandro (Guia Clínico do N₂O) · Odontovolp Cursos ·
  **Dra. Rosane Sartori** (Caxias do Sul/RS; trecho "não somente sobre o que fazer,
  mas também sobre o que não fazer", com "[…]" no início porque a frase original
  começava com "Desde a minha ida ao Resort") · **Alessandra Rech** (professora de
  sedação inalatória e odontopediatria; trecho "não só de aprendizado científico,
  mas aprendizado humano"). A Carla informou que **Rosane e Alessandra também
  fizeram o curso online**. **Não usado:** o texto da Alessandra sobre a Imersão
  (prática clínica = presencial) — reservar para a página da Trilha 295.
  Pendentes: **autorização** de cada pessoa (conversas privadas de WhatsApp) e da
  Odontovolp; sobrenome do Leandro.
- **Página multimodal (12/11/2026, rodada final):** "Quem conduz" agora usa os
  **mini-currículos da página do SAVO** (Carla e Luiz Alberto, com foto de cada um);
  **omitido** o trecho "participou da construção da Resolução CFO 51/2004" que o SAVO
  traz para a Carla, por contrariar a regra do time (sem citar participação em
  comissões) — **a Carla decide** se restitui. **"Carga horária por nível" removida**
  (decisão da Carla). **CFO 295/2026 confirmada** pela Carla; sem citar artigo
  específico. Pendentes de página: checkout, garantia (texto), 4 itens de FAQ e a
  validação dos workshops/mentoria.
- **Garantia (12/11/2026):** 7 dias a partir da compra, sem justificar, reembolso
  integral (mínimo legal do art. 49 do CDC; a Carla achou longo, mas **não pode ser
  menor**). Proteção legítima: liberação progressiva das etapas e liberar o acesso
  logo após a compra (a contagem começa na liberação).
- **Depoimentos para a página multimodal:** a Carla decidiu que **valem
  depoimentos de cursos online; presenciais não**. Existe a pasta "Depoimentos
  Estratégia Multimodal" (só 1 vídeo, Ana Paula, 2022), Lab Nitro, e
  "Depoimentos turma 1" (09 vídeos, ago/2026, formação não identificada). Lista
  para escolha no Drive (ADMINISTRATIVO): "Depoimentos para escolher: página
  Fundamentos da Estratégia Multimodal". Embutir só os que ela marcar, com
  autorização de imagem, em endereço que abra sem login.
- **Concorrência (11/11/2026):** Dra. Adriana Correia (IBRAS, @odontologiasemmedo)
  — "Black Sedação 2026": combo dos cursos online *Sedando Sem Medo* +
  *Emergências no Consultório*; página de captura, preço revelado em live
  **13/11 às 19h30**. Oferta quase espelho da nossa (sedação + emergências) →
  emergências não diferencia; diferencial é método multimodal, URM/cálculo de
  doses, evidência e transparência (não habilita). Também existe
  "Sedação Multimodal Personalizada" (Dr. Luciano Augusto de Jesus, Hotmart).
- **Autoridade do Grupo Nitro (dito pela Carla, 11/11/2026):** *"habilitamos a
  primeira turma no Brasil"* e **26 anos ensinando sedação inclusiva**. Usado
  no hero, nos números e no corpo docente da página multimodal; é o contra-
  argumento aos ~20 anos da concorrente.
- **Fatos confirmados pela Carla (12/11/2026):** habilitou a **primeira turma
  do Brasil em 2000**; em **2004** o Grupo participou da construção da
  **Resolução CFO 51/2004** (sedação por via inalatória/N2O; publicada em
  30/04/2004 — conferida em fonte; um site de legislação indica revogação
  pela CFO 295/2026, **não confirmado**, não afirmar vigência).
- **Tese de marca (anti-marketing sem anti-ciência):** *"Quem não faz ciência
  vende certeza; nós vendemos dúvida calibrada"* — palestra do 6º EBSO
  ("Sedação é Inclusão"): filosofia provoca, ciência sustenta com o limite à
  vista; *"A dúvida não paralisa: ela define a dimensão do caminhar."*
  Slides e roteiro estão no Drive (Roteiro da Palestra; PDF dos slides).
- **Alfabetização × letramento em sedação** (Magda Soares, 1932–2023;
  alfabetização = domínio do sistema; letramento = uso nas práticas sociais;
  processos indissociáveis): enquadramento para a Aula #11 (3 aulas de via
  aérea) e para a conversa com os 40 da Lista VIP. Definições conferidas em
  fontes secundárias, não nos livros originais.
- **"Receita de bolo" (Carla, 12/11/2026):** *"Não vendemos receita de bolo
  para sedação."* — substitui "certeza de vitrine". Crítica é à **categoria**
  (dose sem paciente); **não acusar concorrente nominalmente** sem prova.
  Evidência conferida no PubMed: **Coté et al., Pediatrics 2000**
  (DOI 10.1542/peds.106.4.633): 95 incidentes; eventos adversos mesmo com doses
  dentro dos limites; 3+ sedativos 18/20 vs 7/70; relatos de casos, sem
  denominador. **Bailey et al., Anesthesiology 1990** (DOI
  10.1097/00000542-199011000-00005): midazolam+fentanil, hipoxemia 11/12.
  Cuidado: no mesmo estudo, N2O + outra classe teve 9/10 desfechos adversos —
  o curso multimodal precisa ensinar *quando parar de associar*.
- **Projeto Cultura de Segurança** (aulas gratuitas semanais no YouTube): série
  de 3 aulas sobre via aérea (#11, #12, #13); #11 estreia quinta 12/11 às 11h11,
  com abertura do Dr. Jason Brady (Sedation Academy). Enquadramento do Grupo:
  **alfabetização em cultura de segurança** para toda a Odontologia (Magda
  Soares); o **letramento** vem em camadas: SAVO (toda a Odontologia) e Trilha
  295 (quem já tem sedação na rotina). Fonte: "Aula #11 · Campanha da semana",
  no Drive. A Lista VIP da Trilha 295 (live de 05/11) provavelmente é a origem
  dos "40" — a Black Friday da Trilha vai até 16/11; a do curso multimodal, até
  07/12 (não mandar duas ofertas concorrentes à mesma pessoa).
- Mensagem fixa do grupo de WhatsApp (320): trocar "decisão clínica por semana"
  por "conteúdos selecionados" + aulas gratuitas do Projeto Cultura de Segurança.
- Mensagem fixa do grupo de WhatsApp (320) e vídeos de 20 s para os 40: ver
  rascunhos desta sessão; **conteúdo clínico só vai ao ar com validação da Carla**.

## Regras de ouro do time (Roteiro de Atendimento WhatsApp v3, Drive)
- **Nunca citar CFO, CRO ou SOBRASO como chancela dos cursos, nem a participação
  da Profa. Carla em comissões.** **Nenhum curso habilita** (quem decide é o
  Conselho). Sempre **"Emergências Clínicas"**, nunca "médicas" (a página
  multimodal ainda diz "Emergências Médicas": conferir com a Carla).
- Mensagens saem **em nome da equipe**, individuais, **uma por vez**, máx. **25
  novas conversas/dia**, horários 11:30–12:30 e 18–19h (não sexta), resposta em
  até 1 h; checar CRM coluna Q (**NÃO OFERTAR** / **PAUSA**) antes de escrever.
- **Res. CFO 51/2004 está revogada** (a própria Carla diz na live de 05/11); só
  valem cursos com portaria SERESP até a publicação da 295. Na página multimodal
  foi **removida** a frase "participamos da construção da 51/2004" (violava a
  regra) e "habilitamos" virou "formamos a primeira turma de habilitação em
  sedação do Brasil, em 2000" (**a confirmar com a Carla**).
- **Lista VIP da Trilha 295 (os "40")**: live 05/11 20h; condição VIP até
  **16/11**; bônus até 27/11; matrícula até 30/11; vagas: 12 mentoria / 8
  imersão / 20 SAVO. Enquadramento do valor: **"Os três caminhos"** + **Plano
  Odisseia** (Recursos, Atratividade, Confiança, Coerência). **Não misturar**
  com a oferta do curso multimodal (até 07/12).
- **Toque 1 para os 40 (decidido com a Carla, 12/11/2026):** vídeo de 30 s que
  abre com *"Dr(a). [Nome], aqui é a professora Carla Gamba. Você está na Lista
  VIP da Trilha 295"* + **enquete de um toque no próprio WhatsApp** (os três
  caminhos), sem abrir documento. Depois, 2ª enquete: o que pesa mais
  (Recursos, Atratividade, Confiança, Coerência). Enquete: "Permitir várias
  respostas" desligado (como na Enquete 1 do roteiro do time).
- **Descrição oficial do grupo da Comunidade (12/11/2026)** salva no Drive,
  pasta ADMINISTRATIVO: "Comunidade Oficial do Grupo Nitro: descrição do grupo
  (versão oficial)". Sem "habilitação" como produto; "26 anos"; itálico no
  WhatsApp com _sublinhados_.
- Divergência a resolver: previsão do curso de 200 h ("abril/maio 2027" na live
  vs "ainda não há como antecipar datas" no roteiro de vendas).

## Formulário de captura de leads → Supabase
- Seção após o FAQ: "Ficou interessado? Deixe seu contato." Campos: **Nome e
  WhatsApp obrigatórios, e-mail opcional**. Fallback para WhatsApp se a rede
  falhar.
- **Projeto Supabase:** ref `uwtdwzlewzbktlkluqmw`
  (https://uwtdwzlewzbktlkluqmw.supabase.co). Tabela **`leads`**
  (nome, telefone, email, origem='site-savo', criado_em). RLS **insert-only**
  para a chave pública (o site só grava; ninguém lê a base por ela — proposital).
- A **chave publishable** fica no `index.html` (é pública por design).
- Para **ler os leads**: usar o **conector MCP do Supabase** (quando
  disponível na sessão) ou o painel. Nunca commitar a `service_role`.
- Limitação conhecida: a **rede do ambiente bloqueia o domínio do Supabase**
  por `curl`/CLI, a menos que seja liberado em Network access do ambiente.

## Linguagem da marca (acordada — aplicar sempre)
- **Registro técnico-científico**, elevado, com **ritmo e sedução** (nada de
  frases chãs/amadoras). Público: cirurgiões-dentistas diferenciados.
- **Sempre ancorar afirmações clínicas em literatura real** (PubMed,
  conferida na fonte; nada de "(a verificar)"). Citar autor/ano; em vídeo
  falado a Carla gosta de dizer "a literatura diz: … — e cita os autores".
- **Proibido o verbo "virar"** ("virar reflexo" etc.). Usar **transformar,
  consolidar, elevar, automatizar** (automaticidade).
- **A norma entra como confirmação, nunca como ameaça.** Não usar "cobrar".
  Preferir "a CFO 295/2026 estabelece…".
- Termo da casa: **"sedação em odontologia"** (nunca "sedação odontológica").
- Sem promessa de faturamento; escassez só real (turma até 20, prazo CFO);
  títulos exatos; sedação profunda **não** como prática autorizada (suspensão
  judicial).
- Frase-âncora da norma: *"O cirurgião-dentista deverá estar apto a prevenir,
  reconhecer, manejar e resgatar."* (CFO 295/2026, art. 11, §1º).

## Guia Interno Nitro de Vendas e Sedução (base estratégica)
Doc (Claude Docs): "Guia Interno Nitro de Vendas e Sedução"
(artifact id `dda8d46e-6529-4cf0-bd4e-f621e375d841`). Essência:
- **Jornada de sedução (5 etapas):** Reconhecer o risco → Incomodar (oceano
  vermelho) → Revelar o caminho → Destravar objeções → Decidir. A oferta só
  depois que o colega sente o problema.
- **Princípios-chave:** 1) risco antes do desejo; 3) o colega chega à
  conclusão por si (perguntar antes de afirmar); 4) fisiologia antes da norma;
  5) norma como confirmação; 6) todo risco vem com o caminho; 10) só prometer
  o que se entrega.
- **Trilha Nitro:** Mapa de Decisão (grátis) → PSP → SBV → **SAVO** → Sedação.
- **Equipe = "Mente Mastermind":** multiprofissional (dentistas, enfermeiros,
  advogados) com vivência em sedação, emergências e terapia intensiva —
  *"quem ensina é quem pratica o resgate"*.
- **CTA de topo** padrão é o Mapa de Decisão (grátis); SAVO é degrau de decisão.

## Referências científicas já conferidas (banco de evidências)
- **McCaw et al., Adv Simul, 2023** — sem treino, o tempo até a ventilação de
  resgate sobe de ~57 para ~90 s em 4 meses. DOI 10.1186/s41077-023-00244-5
- **Weinger et al., 2026 (preprint)** — desempenho em crise associado à
  exposição prévia ao cenário crítico. DOI 10.64898/2026.09.10.26362280
- **Chan et al., PLOS Glob Public Health, 2023** — decaimento de habilidade em
  6 meses. DOI 10.1371/journal.pgph.0000705
- Vias aéreas/supraglóticos e laringoespasmo: dossiê já entregue (Rosenberg/
  Becker Anesth Prog 2014; NAEMSP 2022; de Carvalho CC Anesth Analg 2025;
  Weba 2025; Rasheed 2024; etc.).

## Lançamento (playbook)
- **Hoje (avant-première):** vídeo talking-head da Carla (teleprompter) para a
  **comunidade**, com o link de compra. Exclusivo, "vocês primeiro".
- **Amanhã:** **aula gratuita de vias aéreas** (YouTube) e, depois dela,
  **lançamento público** com Reels (talking-head) + carrossel + enquete nos
  Stories (pergunta: "paciente dessaturando — avalia primeiro: ventilação,
  perfusão ou oxigenação?").
- Gancho do lançamento: **"60 segundos"** (cena de emergência) + prazo da CFO.
- Formatos gravados pela Carla são **talking-head** (sem encaixar outras
  imagens); citações entram como **legenda**, não precisam ser faladas.

## Pendências / próximos passos
- Confirmar a **data-limite exata + artigo** do prazo da CFO (hoje usamos
  "janeiro de 2027" como informado pela Carla).
- Alinhar **títulos do corpo docente** da página com o Guia (ex.: Profª Dra.
  Carla Gamba + Board/Loyola; Luiz Alberto — Mestre em Saúde Coletiva; etc.).
- Checar discrepância do checkout: página anuncia 12× R$ 307; Kiwify calculava
  R$ 307,17 (17 centavos).
- (Opcional) Liberar Supabase na rede do ambiente + guardar `SUPABASE_SERVICE_KEY`
  como secret para consultas via CLI.
