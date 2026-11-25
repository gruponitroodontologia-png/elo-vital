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
- **Datas Turma 1 (ADIADA — jan/2027):** não houve quórum para 5-6/12.
  Presencial **22 e 23 de janeiro de 2027** (9h–19h), Rio de Janeiro.
  Telepresencial (4 encontros ao vivo): **datas a definir** ("data em breve").
  Na página, cabeçalhos dos módulos: "Ao vivo · 4h · data em breve".
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
- **REGRA REGULATÓRIA (crítica):** NÃO citar prazo nem prorrogação da CFO 295
  em peça pública antes de publicação oficial — a Carla integra a comissão do
  CFO. Reassegurar por ângulo factual (dar entrada na documentação + taxa
  inicia o processo na regional; o preparo é preservado), nunca por promessa
  de prazo.
- "**Nenhum curso habilita; quem decide é o Conselho**" é regra da **Trilha
  295 / Habilitação em Sedação** — NÃO cabe ao SAVO/SBV (que são certificados
  próprios). Nunca prometer habilitação.
- Existe a skill **headlines-nitro** (regras de marca/regulatórias da Carla):
  usar para headlines/títulos/chamadas. Sem emoji; local só "Rio de Janeiro";
  registro técnico, sonoro, sem gíria.

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

## PSP — Envelope de Segurança e base legal dos fármacos (nov/2026)
- Oficina 1 (Resort da Odontopediatria) está no **Google Drive**: "Roteiro Oficina
  de Envelope de Segurança - Resort ODP.docx", "Caderno de Atividades — PSP —
  Envelope de Segurança", "O Envelope de Segurança" (fundamentos), "CASO 1".
- Continuação (Claude Docs): **Envelope de Segurança Farmacológico** — fármacos
  com ação direta/indireta no SNC, 8 dimensões, 3 casos, caderno, base normativa
  (Portaria 344/1998 etc.): https://claude.ai/artifact/PJGNpSqyBLBhAqnqPKw8YU
- **Fundamentação legal do uso de fármacos pelo CD na prevenção e no manejo de
  emergências médicas** (Lei 5.081/1966 art. 6º II e VIII → CFO 295/2026; 4
  pilares; literatura; norma → POP do PSP): https://claude.ai/artifact/Nyzcs2CjnZ4c7DioNo1jt3
- **Drive (25/11/2026):** pastas "PSP - Arquivos" e "Resort das Odontopediatras -
  Disney - Glorinha", arquivos com prefixo `241126DINÂMICA PSP - ...`: Envelope
  Farmacológico (PDF), Fundamentação legal (PDF), Resumo prático de abertura e
  Roteiro completo do workshop (Google Docs; gabaritos dos casos a validar).
  Convenção da Carla: data DDMMAA no início do nome do arquivo, não na pasta.
- Pontos legais **conferidos em 25/11/2026** (PDF da CFO 295 e RDC 1.002
  comentada no Drive da Carla + busca): Lei 5.081 art. 6º II e VIII (antecedente:
  Lei 1.314/1951); CFO 295 arts. 11 §1º, 14, 15 §2º (SAVO ou equivalente + SBV
  da equipe, todos os níveis), 25 VII, 66 (revoga CFO 51/2004); CFO 22/2001;
  RDC 1.002 arts. 36, 114, 116; Código de Ética arts. 11 VII e X, 17; Notificação
  B nacional desde a RDC 873/2024. A rede do ambiente bloqueia gov.br/planalto/
  CFO/câmara — a Carla não quis liberar; usar Drive dela e busca web.

## Pendências / próximos passos
- **Definir e divulgar as datas telepresenciais** da turma de jan/2027.
- Comunicado de adiamento (5-6/12 → 22-23/01) já redigido; sem promessa de
  prazo do CFO.
- Confirmar a **data-limite exata + artigo** do prazo da CFO (hoje usamos
  "janeiro de 2027" como informado pela Carla).
- Alinhar **títulos do corpo docente** da página com o Guia (ex.: Profª Dra.
  Carla Gamba + Board/Loyola; Luiz Alberto — Mestre em Saúde Coletiva; etc.).
- Checar discrepância do checkout: página anuncia 12× R$ 307; Kiwify calculava
  R$ 307,17 (17 centavos).
- (Opcional) Liberar Supabase na rede do ambiente + guardar `SUPABASE_SERVICE_KEY`
  como secret para consultas via CLI.
