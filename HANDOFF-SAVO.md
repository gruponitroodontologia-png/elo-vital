# HANDOFF — Página de Vendas do SAVO (Grupo Nitro)

> **Como retomar:** numa nova conversa, diga _"retomar o plano do SAVO"_ ou peça para eu ler
> este arquivo (`HANDOFF-SAVO.md`). Ele resume tudo o que já foi feito e o que falta.
>
> **Última atualização:** 23/09/2026 · **Status geral:** página pronta e no GitHub; falta publicar no ar.

---

## 1. O que é o projeto
Landing page (página de vendas) do curso **SAVO — Suporte Avançado de Vida para a Odontologia**,
da linha **Cultura de Segurança** do Grupo Nitro. Feita para os padrões visuais da marca
(vinho/lavanda, fonte Poppins), no mesmo estilo das outras páginas de vendas do grupo.

## 2. Estado atual (o que está PRONTO)
- Página completa, responsiva (mobile/desktop) e **em HTML/CSS puro (sem JavaScript)** — para
  funcionar em qualquer lugar, inclusive dentro do widget de HTML do Elementor.
- Conteúdo baseado na ficha técnica revisada (revisão técnica de 15/09).
- **Dados já preenchidos:** data e local da 1ª turma (**5 e 6 de dezembro de 2026, no Rio de
  Janeiro**), preço, carga horária etc.
- Melhorias já incluídas: Open Graph/Twitter (compartilhamento), dados estruturados Schema.org
  (SEO), FAQ acessível (`<details>`).
- **Prévia navegável:** https://claude.ai/artifact/FjkNKWFBY1bt52PVfRioyy

## 3. Arquivos no repositório (`gruponitroodontologia-png/elo-vital`)
Branch de trabalho: **`claude/focused-planck-5yplma`** (tudo já commitado e enviado).
- `index.html` — a página completa (standalone). É esta que o Vercel publica.
- `savo-elementor.html` — o mesmo conteúdo em bloco, pronto para colar num widget HTML do
  Elementor (caso o caminho WordPress seja usado).
- `vercel.json` — configuração para o Vercel servir `index.html` na raiz do subdomínio.
- `assets/logo-white.png` — logo usada na página.
- `index.html` — página antiga do repo ("Elo Vital — Kit de Documentos"); **não** é o SAVO.

## 4. Dados da formação (referência)
- 32 horas · híbrida (16h telepresenciais ao vivo + 16h presenciais).
- 4 módulos ao vivo + etapa presencial (2 dias de 8h, 4 professores).
- Turmas de 12 a 20 cirurgiões-dentistas.
- 1ª turma: **5 e 6 de dezembro de 2026 — Rio de Janeiro**.
- Investimento: **R$ 2.970,00** à vista ou **12x de R$ 247,50** (com juros da operadora).
- Pré-requisito: SBV vigente (< 2 anos). O SAVO **não** habilita sedação isoladamente e **não**
  substitui SBV/ACLS (isso está dito na página, para transparência).
- Coordenação acadêmica: Profª Dra. Carla Gamba (foto ainda a inserir — hoje há um placeholder).

## 5. Infraestrutura descoberta (onde o site mora)
- **Domínio:** `gruponitrosedacao.com.br`, registrado no **Registro.br**.
- **DNS:** gerenciado no **Cloudflare** (é lá que se cria/edita subdomínio — NÃO no Registro.br).
- **Site atual:** **WordPress** gerenciado, plataforma **"MeuSite Profissional / Meu Site Pro"**
  (avisos vêm de `notificacoes@meuemailpro.com.br`), com **Elementor Pro** instalado.
- **Pessoa técnica anterior:** Denis Gomes (`dominios@denisgomes.com.br`) — era o contato técnico
  do domínio; o controle já foi transferido para a Carla.
- 🔒 **Credenciais (WordPress, Registro.br, Cloudflare) NÃO estão neste arquivo, por segurança.**
  Estão guardadas com a Carla/Olivia (recomendado: gerenciador de senhas). A senha do WordPress
  foi trocada em set/2026 e o acesso está sob controle da equipe.

## 6. Decisão de publicação
**Escolhido: subdomínio no Vercel** → **`savo.gruponitrosedacao.com.br`**, publicado a partir do
GitHub. Motivos: a página é estática (encaixe perfeito no Vercel), publicação rápida e automática a
cada ajuste, e alinha com o plano futuro.

**Futuro (projeto à parte, maior):** migrar o site inteiro do WordPress para o Vercel. Atenção:
WordPress é dinâmico (PHP + banco), então "migrar tudo" significa **reconstruir** (estático ou
headless) — não é copiar e colar. A landing do SAVO é o primeiro passo dessa direção.

## 7. PRÓXIMOS PASSOS (quando retomar)
1. **Decisão de código (pendente de autorização):** o Vercel publica a versão `main` por padrão.
   O trabalho está no branch `claude/focused-planck-5yplma`. Duas opções:
   - **(A, recomendado)** autorizar juntar o branch na **`main`** (só adiciona, não apaga nada);
   - **(B)** na importação do Vercel, escolher o branch de trabalho como "produção".
   > Obs.: por regra, eu só mexo na `main` com autorização explícita. Em 23/09 a Olivia sinalizou
   > que fará este passo "num próximo momento". Confirmar A ou B ao retomar.
2. **Vercel** (a Carla/Olivia faz, eu guio): criar conta entrando com o GitHub → **Add New
   Project** → importar `elo-vital` → **Deploy** (sem build, é estático) → testar no `...vercel.app`.
3. **Domínio:** no projeto Vercel → **Settings → Domains** → adicionar
   `savo.gruponitrosedacao.com.br` (o Vercel mostra o alvo do CNAME).
4. **Cloudflare:** criar registro **CNAME `savo`** apontando para o alvo do Vercel.
5. **Checkout:** plugar o **link real de pagamento** nos botões (hoje estão com placeholder `#`,
   marcados no código com `<!-- SUBSTITUIR pelo link real de checkout -->`).
6. **Opcionais:** imagem de compartilhamento (Open Graph 1200x630) e **foto da Profª Carla Gamba**
   (substituir o placeholder "CG").

## 8. Pendências abertas (decisões de quem toca o negócio)
- [ ] Autorizar caminho A ou B do passo 1.
- [ ] Fornecer o **link de checkout** do pagamento.
- [ ] (Opcional) imagem OG e foto da Carla.
- [ ] Definir se o WordPress atual (`/`) permanece e só o `savo.` vai para o Vercel (é o plano
      atual) — o site principal segue no WordPress por enquanto.

## 9. Contexto extra
- Foram guardadas 4 "skills" de UX/tipografia/texto em `~/.claude/skills/` **nesta máquina de
  trabalho** (efêmera) — para virarem permanentes, precisam ser adicionadas pela função de Skills
  nas configurações do Claude. Pasta de origem: `skills-ux-e-texto.zip`.
- Referências de marca usadas: `design_1.md` (guia de design) e 2 páginas de vendas antigas
  (SBV/Emergências e PSP) enviadas como modelo.

---
_Handoff gerado para retomar o trabalho da página do SAVO. Peça "retomar o plano do SAVO" a
qualquer momento._
