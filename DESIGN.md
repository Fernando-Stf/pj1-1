# DESIGN.md — Barber Premium Landing Page

## Visão Geral

Landing page de barbearia premium com design editorial sofisticado. O site comunica exclusividade através de hierarquia visual clara, tipografia elegante e espaçamentos generosos. Foco em conversão (agendamento) sem sacrificar a qualidade visual.

## Arquitetura Visual

### Paleta de Cores

| Nome | Hex | Uso |
|------|-----|-----|
| Preto Absoluto | #000000 | Background principal, textos |
| Cinza Carvão | #1a1a1a | Backgrounds secundários |
| Branco/Off-white | #f5f5f5 | Textos claros |
| Bege Envelhecido | #c9a961 | Accents, botões, detalhes |
| Cinza Neutro | #808080 | Textos secundários |

**Filosofia:** Alto contraste, elegância discreta. O ouro não brilha; é sofisticado e envelhecido.

### Tipografia

| Uso | Fonte | Peso | Tamanho |
|-----|-------|------|--------|
| Títulos Grandes | Playfair Display | 900 | 64px-80px |
| Títulos Seção | Playfair Display | 700 | 36px-64px |
| Subtítulos | Montserrat | 700 | 18px-32px |
| Labels/CTAs | Montserrat | 600-700 | 12px-14px |
| Corpo | Inter | 400-500 | 14px-16px |
| Small Text | Inter | 400 | 12px-14px |

**Hierarquia:** Serifada (Playfair) para impacto; sans-serif limpa (Inter) para legibilidade.

### Espaçamentos

- **Padding de seção:** 6rem (desktop), 3rem (mobile)
- **Gap entre items:** 2-4rem (desktop)
- **Padding interno de cards:** 2-2.5rem
- **Margem de container:** 2rem (desktop), 1rem (mobile)

**Princípio:** Respiro visual. Poucos elementos, bem distribuídos.

## Componentes & Patterns

### Navbar
- **Estado padrão:** Transparente com logo/texto em branco
- **Estado scrolled:** Background semi-transparente com backdrop blur
- **Mobile:** Menu hamburger elegante com animação de transformação
- **Links:** Underline animado em hover (accent color)

### Hero
- **Layout:** Tela cheia com imagem de fundo
- **Overlay:** Escuro sutil (50% opacidade) para legibilidade
- **Conteúdo:** Centralizado, com animações fade-in sequenciadas
- **CTAs:** Primária (accent) e secundária (outline)
- **Scroll indicator:** Animação bounce ao fundo

### Sobre
- **Layout:** Grid 2 colunas (desktop), 1 coluna (mobile)
- **Imagem:** Lado esquerdo, sem border radius
- **Conteúdo:** Lado direito com stats em pequeno grid
- **Stats:** Número grande em accent, label pequeno

### Experiência
- **Layout:** Grid 4 colunas (desktop), responsivo em mobile
- **Número:** Grande e em accent (01, 02, 03, 04)
- **Título:** Maiúscula, peso 700
- **Descrição:** Curta, max 2 linhas

### Serviços
- **Layout:** Grid 4 colunas (desktop)
- **Card:** Background escuro com border sutil, hover eleva e muda border
- **Accent line:** Topo do card com gradiente em hover
- **Preço:** Grande, em accent, no final do card

### Galeria
- **Layout:** Grid assimétrico com masonry (itens altos variam)
- **Hover:** Imagem amplificada + overlay com botão expand
- **Lightbox:** Modal com imagem grande, navegação anterior/próximo, keyboard support

### Barbeiros
- **Layout:** Grid 3 colunas (desktop)
- **Card:** Sem border, image hover amplifica
- **Título:** Maiúscula, especialidade em accent
- **Descrição:** Curta, texto secundário

### Depoimentos
- **Layout:** Grid 3 colunas (desktop)
- **Card:** Background escuro com left border accent
- **Stars:** Accent color, sem half-stars
- **Texto:** Curto, marca de aspas implícita na formatação

### CTA Final
- **Layout:** Centralizado
- **Título:** Grande e ousado
- **Botões:** 2 colunas (desktop), empilhados (mobile)

### Footer
- **Layout:** Grid 4 colunas (desktop), responsivo
- **Sections:** Brand, Contato, Horários, Social
- **Social icons:** Circular, hover inverte cores

## Animações

| Elemento | Animação | Trigger |
|----------|----------|---------|
| Hero content | Fade-in up sequenciado | Page load |
| Seções | Fade-in | Scroll into view |
| Imagens | Amplificação suave | Hover |
| Navlinks | Underline animado | Hover |
| Botões | Elevação + cor | Hover |
| Scroll indicator | Bounce infinito | Hero |

**Princípio:** Sutis, não disruptivas. Transição padrão: 0.3s cubic-bezier.

## Responsividade

### Breakpoints
- **Desktop:** 1200px+
- **Tablet:** 768px-1199px
- **Mobile:** <768px
- **Small mobile:** <480px

### Ajustes por Breakpoint

| Elemento | Desktop | Tablet | Mobile |
|----------|---------|--------|--------|
| Hero title | 80px | 56px | 32px |
| Section title | 64px | 48px | 28px |
| Grids | Multi-col | 2-3 col | 1 col |
| Padding | 6rem | 4rem | 2rem |
| Navbar menu | Horizontal | Hamburger | Hamburger |

## Acessibilidade

- Contraste WCAG AA em todas as cores
- Labels semânticas em formulários
- Botões com aria-labels
- Keyboard navigation (Tab, Enter, Escape, Arrows)
- Focus indicators visíveis
- Imagens com alt text descritivo

## Performance

- Lazy loading de imagens
- CSS minificado
- JavaScript otimizado
- Nenhuma dependência externa pesada
- Lighthouse target: 90+
- First Contentful Paint: <2s

## Conveções de Código

- **HTML:** Semântico, nomes descritivos
- **CSS:** BEM-ish, variáveis CSS, grid/flexbox
- **JS:** Vanilla, modular, sem jQuery
- **Imagens:** WebP quando possível, fallback JPG/PNG

## Sessões Principais

1. **Navbar** — Navegação fixa, scroll-aware
2. **Hero** — Impacto visual máximo, CTAs diretos
3. **Sobre** — Storytelling + números
4. **Experiência** — Diferenciais em padrão editorial
5. **Serviços** — Ofertas com preços, sem excesso
6. **Galeria** — Trabalhos visuais, exploráveis
7. **Barbeiros** — Humanização da equipe
8. **Depoimentos** — Prova social legítima
9. **CTA Final** — Conversão final
10. **Footer** — Informações, social links

## Fluxo de Conversão

1. Hero: AGENDAR HORÁRIO (WhatsApp)
2. Navbar: Botão AGENDAR (fixo)
3. CTA Final: AGENDAR VIA WHATSAPP + LIGAR
4. Footer: Contato multi-canal (tel, WhatsApp, endereço)

**Integração necessária:**
- Atualizar WhatsApp link com número real
- Atualizar telefone
- Atualizar endereço e horários
- Imagens reais de barbearia/barbeiros

---

**Versão:** 1.0
**Data:** 2026-10-01
**Status:** Pronto para desenvolvimento
