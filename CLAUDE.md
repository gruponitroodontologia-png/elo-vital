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
  Nitro; **membro fundadora da SOBRASO** (sociedade afiliada à IFDAS — International
  Federation of Dental Anesthesiology Societies). É a interlocutora principal e a **autoridade clínica**: conteúdo de
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
- **Proibido "é da …"** como posse ("não é da sedação", "é da Odontologia"): usar "competência de", "domínio exclusivo de". "Pertencer" é aceitável.
- **Proibido o verbo "virar"** ("virar reflexo" etc.). Usar **transformar,
  consolidar, elevar, automatizar** (automaticidade).
- **A norma entra como confirmação, nunca como ameaça.** Não usar "cobrar".
  Preferir "a CFO 295/2026 estabelece…".
- **Títulos, assuntos de e-mail, títulos de reels e chamadas também em registro
  científico** (pedido da Carla, 09/11/2026): nada de ganchos coloquiais ou de
  efeito ("qual peça caiu?", "até amanhã", "o silêncio não é alívio"). Padrão:
  enunciado técnico, substantivo, com o conceito clínico explícito (ex.: "Via
  aérea, monitorização e suporte de vida: competências de toda a Odontologia").
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

## Projeto Cultura de Segurança (aulas semanais no YouTube)
- Aulas **semanais, quinta às 11h11**, numeradas "Aula #N". Pasta no Drive:
  "Youtube - Cultura de Segurança" (uma subpasta por aula). Cerca de 19 min.
- Formato: abertura **olho no olho (~1–2 min, sem slide)** → roteiro com
  ~10–12 slides no visual da página, **sem preço**.
- Toda semana: **roteiro + newsletter (terça 18h + lembrete quinta 7h, disparo
  Fabrício) + 1 reel + 2 stories** (formato confirmado pela Carla em 09/11/2026);
  há **depoimentos** de alunos para usar nos stories e na newsletter. Referências na descrição do YouTube.
- Regras da #10: nenhum curso habilita, inclusive o nosso; urgência só real
  (vagas, prazos de condição), nunca o prazo do Conselho.
- **RDC 1002/2025 = ANVISA**, publicada em 15/12/2025 (PSP do consultório; prazo de adequação a confirmar com a Carla).
- Novembro: aulas sustentam a venda da **Trilha 295**.

## Trilha 295 (Programa de Complementação para a Habilitação Básica)
- Lançada em live em 05/11/2026 (replay no Substack:
  https://gruponitro.substack.com/p/replay-live-lancamento-programa-de).
- Público: CD habilitado em N2O que já usa, ou não, benzodiazepínicos e
  anti-histamínicos com finalidade sedativa. Reúne complementação de carga
  horária + certificações exigidas para a Habilitação Básica em Sedação.
- Percursos versáteis (raciocínio farmacológico, prática clínica supervisionada,
  suporte de vida, ou completo até o pedido de registro). **Trilha 295 Online:
  104 h telepresenciais.** Página: https://gruponitrosedacao.com.br/trilha295
- Black Friday: 47% de redução no custo total até 16/11.
- `gruponitro.substack.com` está liberado na rede do ambiente (Instagram não).

## Aulas gratuitas de vias aéreas (11, 12 e 13)
- Material em `aulas-vias-aereas/` (dossiês 01–02 com DOIs, tradução do reel
  da Sedation Academy, roteiro das 3 aulas, texto "Olho no olho" da Aula 11).
- Tese: "a via aérea não é domínio exclusivo da sedação: é competência de toda a Odontologia". (Regra de linguagem: **nunca "é da …"** — ex.: "não é da sedação", "é da Odontologia"; "pertencer" é aceitável, mas preferir "competência de", "domínio exclusivo de".)
- **Aula #11: quinta, 12/11/2026, 11h11** · #12 em 19/11 · #13 em 26/11.
- Pacote completo da #11 (roteiro, newsletter, reels, stories) em
  `aulas-vias-aereas/05-aula11-pacote-da-semana.md`.
- SARI = Simplified Airway Risk Index (El-Ganzouri 1996).
- **Docs editáveis da #11 (Claude Docs):** teleprompter https://claude.ai/artifact/FRwXLA99vDpjVVGW2LZbjV ·
  campanha da semana (newsletter, e-mails, 5 reels, stories; vende **SAVO** para toda a Odontologia e
  **Trilha 295** para quem já tem a sedação na rotina) https://claude.ai/artifact/ChHhFHyL4GZ1EqRagrNmvU
- **Fio das peças de divulgação da série (#11–#13), pedido da Carla em 09/11:** partir do
  **estetoscópio pré-traqueal** (Boriosi 2019; Somri 2017), apresentar o que cada uma das 3
  aulas pretende, conectar à **alfabetização em cultura de segurança** (Magda Soares:
  alfabetização → letramento em camadas; a sedação é uma das camadas) e deixar claro que
  **há prazo e há razão** para a qualificação (Tokede 2024, Lo 2025). **Sobre prazos, basta citar
  que as resoluções (RDC 1002/2025 e CFO 295/2026) devem ser cumpridas — sem datas.** As regras
  não mudaram: norma como confirmação, nunca como ameaça.
- **Reel em tela dividida com o vídeo da Sedation Academy** (pedido de autorização em inglês + roteiro, sem dizer que o vídeo está "errado": o Projeto **amplia o olhar**): https://claude.ai/artifact/PXKnSGaXKguqNSmURqkF9V
- Apresentação final da #11: 15 slides (slide 2 = Apresentadora, padrão das aulas), sem marca d'água,
  PDF e PPTX sem notas (as notas aparecem no Zoom).

## Pendências / próximos passos
- **SBV NÃO é pré-requisito do SAVO** (Carla, 09/11/2026): é um produto que pode ser
  oferecido. A página de vendas (`index.html`) ainda diz que é pré-requisito (seção de
  pré-requisitos, ficha da turma e 2 perguntas do FAQ) — corrigir quando a Carla autorizar.
- Confirmar a **data-limite exata + artigo** do prazo da CFO (hoje usamos
  "janeiro de 2027" como informado pela Carla).
- Alinhar **títulos do corpo docente** da página com o Guia (Carla: **"Profa. Carla Gamba" (MSc), nunca "Dra."**, confirmado em 08/11/2026; Luiz Alberto — Mestre em Saúde Coletiva; etc.).
- Checar discrepância do checkout: página anuncia 12× R$ 307; Kiwify calculava
  R$ 307,17 (17 centavos).
- (Opcional) Liberar Supabase na rede do ambiente + guardar `SUPABASE_SERVICE_KEY`
  como secret para consultas via CLI.
