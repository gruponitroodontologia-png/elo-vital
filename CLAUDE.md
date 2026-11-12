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
