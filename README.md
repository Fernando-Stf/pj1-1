# Barber Premium — Landing Page

Uma landing page profissional de barbearia premium, desenvolvida com HTML, CSS e JavaScript puro. Design editorial sofisticado com foco em conversão.

## 🎨 Características

- **Design Editorial:** Hierarquia visual clara, tipografia elegante, espaçamentos generosos
- **Responsivo:** Mobile-first, otimizado para todos os dispositivos
- **Performance:** Lazy loading, CSS minificado, sem dependências pesadas
- **Acessível:** WCAG AA compliant, keyboard navigation, semântica HTML
- **Interativo:** Galeria com lightbox, smooth scrolling, animações sutis
- **SEO:** Meta tags, Open Graph, estrutura semântica

## 📋 Estrutura de Arquivos

```
pj2/
├── index.html          # Estrutura HTML semântica
├── styles.css          # Estilos CSS moderno
├── script.js           # Interatividade e animações
├── PRODUCT.md          # Documentação do produto
├── DESIGN.md           # Especificação de design
├── README.md           # Este arquivo
└── images/             # Pasta para imagens (criar)
    ├── hero.jpg
    ├── sobre.jpg
    └── [outros...]
```

## 🚀 Como Usar

### 1. Setup Inicial

```bash
# Clone ou copie os arquivos para seu servidor
cd pj2
```

### 2. Configuração de Imagens

Substitua as URLs do Unsplash por imagens reais:

**No `index.html`, procure por:**
- `https://images.unsplash.com/photo-...`

**Substitua por caminhos locais:**
```html
<img src="/images/hero.jpg" alt="...">
```

### 3. Atualizar Informações de Contato

**Procure pelos seguintes placeholders:**

```html
<!-- WhatsApp (substituir número) -->
href="https://wa.me/5511999999999?text=..."

<!-- Telefone -->
href="tel:+5511999999999"

<!-- Endereço -->
Rua Exemplo, 123
São Paulo, SP

<!-- Horários -->
Seg-Sex: 09:00 - 20:00
```

### 4. Servir Localmente (Desenvolvimento)

**Python 3:**
```bash
python -m http.server 8000
```

**Node.js (http-server):**
```bash
npx http-server
```

**Acesse:** `http://localhost:8000`

### 5. Deploy para Produção

#### Opção 1: Vercel (recomendado para performance)
```bash
npm install -g vercel
vercel
```

#### Opção 2: Netlify
```bash
npm install -g netlify-cli
netlify deploy
```

#### Opção 3: Servidor Tradicional
Copie os arquivos via FTP/SFTP para seu servidor.

## 🎯 Seções do Site

| Seção | Descrição | CTA |
|-------|-----------|-----|
| **Hero** | Impacto visual, headline, CTAs | AGENDAR / CONHEÇA |
| **Sobre** | História da barbearia, stats | — |
| **Experiência** | Diferenciais (4 items) | — |
| **Serviços** | Ofertas com preços (4 serviços) | — |
| **Galeria** | Grid assimétrico de trabalhos | Lightbox |
| **Barbeiros** | Apresentação da equipe (3) | — |
| **Depoimentos** | Prova social (3 depoimentos) | — |
| **CTA Final** | Conversão final | AGENDAR / LIGAR |
| **Footer** | Contato, horários, social | Contato multi-canal |

## 🎨 Customização

### Paleta de Cores

Edite as variáveis CSS em `styles.css`:

```css
:root {
    --black: #000000;
    --dark-gray: #1a1a1a;
    --white: #f5f5f5;
    --accent: #c9a961;  /* Mudar para outra cor */
    --text-secondary: #808080;
    --transition: 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
```

### Tipografia

Altere no `<head>` do `index.html`:

```html
<!-- Mudar fontes do Google Fonts -->
<link href="https://fonts.googleapis.com/css2?family=SEU-SERIF:wght@700;900&family=SEU-SANS:wght@500;700&display=swap" rel="stylesheet">
```

Depois atualize o CSS:

```css
h1, h2, h3 {
    font-family: 'SEU-SERIF', serif;
}

body {
    font-family: 'SEU-SANS', sans-serif;
}
```

## ⚡ Performance

### Otimizações Implementadas

- ✅ Lazy loading de imagens
- ✅ CSS minificado
- ✅ JavaScript otimizado
- ✅ Nenhuma dependência externa pesada
- ✅ Imagens com srcset responsivo (adicionar manualmente)
- ✅ Service Worker pronto (descomentar `sw.js`)

### Melhorias Futuras

```html
<!-- Adicionar srcset para imagens responsivas -->
<img 
    src="image.jpg"
    srcset="image-sm.jpg 480w, image-md.jpg 768w, image-lg.jpg 1200w"
    sizes="(max-width: 480px) 100vw, (max-width: 768px) 90vw, 1200px"
    alt="Descrição"
>
```

## 🔧 Integrações

### WhatsApp

Link automático com mensagem personalizada:

```html
<!-- Botão WhatsApp -->
<a href="https://wa.me/5511999999999?text=Gostaria%20de%20agendar%20um%20horário" target="_blank">
    AGENDAR
</a>
```

**Teste antes:** https://wa.me/551199999999

### Analytics (Google Analytics)

Adicione ao `<head>`:

```html
<!-- Google Analytics 4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

### Facebook Pixel

Adicione ao `<head>`:

```html
<!-- Facebook Pixel -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', 'SEU_PIXEL_ID');
fbq('track', 'PageView');
</script>
```

## 📱 Responsividade

O site é otimizado para:

- ✅ Desktop (1200px+)
- ✅ Tablet (768px-1199px)
- ✅ Mobile (480px-767px)
- ✅ Small Mobile (<480px)

Teste em: [Chrome DevTools](https://developer.chrome.com/docs/devtools/)

## ♿ Acessibilidade

- ✅ Contraste WCAG AA
- ✅ Semântica HTML5
- ✅ Aria-labels em elementos interativos
- ✅ Keyboard navigation completa
- ✅ Alt text em todas as imagens

Valide em: [WAVE](https://wave.webaim.org/)

## 🔐 SEO

### Meta Tags (já inclusos)

```html
<meta name="description" content="...">
<meta property="og:title" content="...">
<meta property="og:image" content="...">
<meta property="og:description" content="...">
<meta property="og:url" content="...">
```

### Checklist SEO

- [ ] Atualizar `<title>` com seu nome de barbearia
- [ ] Atualizar meta descriptions
- [ ] Adicionar Open Graph image real
- [ ] Adicionar favicon customizado
- [ ] Criar sitemap.xml
- [ ] Registrar em Google Search Console
- [ ] Adicionar Google Analytics
- [ ] Otimizar imagens (Compress com TinyPNG)

## 🐛 Troubleshooting

### Imagens não aparecem
- Verifique os caminhos das imagens
- Use URLs absolutas para Unsplash (https://...)
- Compresse imagens com TinyPNG

### Scroll lento em mobile
- Reduza o tamanho das imagens
- Use formatos modernos (WebP)
- Ative lazy loading

### Menu hamburger não funciona
- Verifique se script.js está carregando
- Abra console (F12) para erros JavaScript

### CTA não abre WhatsApp
- Verifique o número de telefone (com código de país)
- Teste em: https://wa.me/5511999999999

## 📞 Suporte

Para dúvidas sobre implementação:

1. Verifique a documentação em `DESIGN.md`
2. Consulte `PRODUCT.md` para contexto do projeto
3. Valide HTML/CSS em validadores online

## 📄 Licença

Desenvolvido por Claude Code | Barber Premium © 2026

---

**Versão:** 1.0  
**Última atualização:** 2026-10-01  
**Status:** Pronto para produção
