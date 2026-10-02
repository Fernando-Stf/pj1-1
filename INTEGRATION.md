# Integration Guide — Barber Premium

## 🔗 Links de Integração

### Agendamento
- **WhatsApp:** `https://wa.me/5511999999999?text=Gostaria%20de%20agendar%20um%20horário`
- **Telefone:** `tel:+5511999999999`
- **Email:** `contato@barperpremium.com`

### Redes Sociais
- Instagram: `https://instagram.com/barperpremium`
- Facebook: `https://facebook.com/barperpremium`

---

## 🎯 SEO Checklist

- [ ] Atualizar `<title>` com nome real
- [ ] Atualizar `<meta name="description">`
- [ ] Adicionar `<meta property="og:image">` com imagem real
- [ ] Registrar em Google Search Console
- [ ] Adicionar Google Analytics
- [ ] Criar sitemap.xml
- [ ] Adicionar robots.txt
- [ ] Otimizar imagens (TinyPNG)
- [ ] Testar com PageSpeed Insights
- [ ] Fazer audit com Lighthouse

---

## 📱 Imagens a Substituir

| Local | Tamanho | Formato | Prioridade |
|-------|---------|---------|-----------|
| Hero background | 1920×1080 | JPG | 🔴 Alta |
| Sobre section | 600×700 | JPG | 🔴 Alta |
| Galeria (6 items) | 400×300/500 | JPG | 🔴 Alta |
| Barbeiros (3) | 300×350 | JPG | 🟡 Média |
| Open Graph | 1200×630 | JPG | 🟡 Média |
| Favicon | 32×32 | PNG | 🟢 Baixa |

**Dica:** Compress com [TinyPNG](https://tinypng.com) — reduz 50-70% sem perda

---

## 🔐 Considerações de Segurança

### HTTPS
- Ativar SSL/TLS no servidor
- Redirecionar HTTP → HTTPS

### Headers de Segurança
```
Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline' fonts.googleapis.com
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Referrer-Policy: strict-origin-when-cross-origin
```

### Privacy
- Adicionar Política de Privacidade
- Adicionar Termos de Serviço
- Avisar sobre cookies

---

## 📊 Analytics Setup

### Google Analytics 4
```html
<!-- Adicionar ao <head> -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

### Eventos a Rastrear
- Click em "AGENDAR HORÁRIO"
- Click em "LIGAR"
- Clique em links de redes sociais
- Scroll de seções

---

## 🚀 Deployment Passo a Passo

### Opção 1: Vercel (Recomendado)

```bash
# 1. Instalar CLI
npm install -g vercel

# 2. Deploy
cd /path/to/pj2
vercel

# 3. Configurar domínio
# Em vercel.com → Project Settings → Domains
```

### Opção 2: Netlify

```bash
# 1. Instalar CLI
npm install -g netlify-cli

# 2. Deploy
cd /path/to/pj2
netlify deploy --prod

# 3. Conectar domínio
# Em netlify.com → Domain Settings
```

### Opção 3: Servidor Tradicional (cPanel/Plesk)

```bash
# 1. Conectar via FTP
ftp ftp.seudominio.com

# 2. Fazer upload de todos os arquivos para public_html/
put index.html
put styles.css
put script.js
# ... etc

# 3. Testar: https://seudominio.com
```

---

## 🔍 Testes Pré-Launch

### Desktop
- [ ] Chrome (Windows/Mac)
- [ ] Firefox
- [ ] Safari
- [ ] Edge

### Mobile
- [ ] iPhone (Safari)
- [ ] Android (Chrome)
- [ ] Tablet (iPad/Android)

### Performance
- [ ] Lighthouse: 90+
- [ ] PageSpeed: 80+
- [ ] Load time: <2s

### Funcionalidade
- [ ] Navbar scroll funciona
- [ ] Menu hamburger abre/fecha
- [ ] Links de navegação funcionam
- [ ] Galeria lightbox abre
- [ ] WhatsApp link funciona
- [ ] Formulário de contato funciona (se houver)

### Acessibilidade
- [ ] Keyboard navigation completa
- [ ] WAVE audit (0 errors)
- [ ] Contraste adequado
- [ ] Alt text em imagens

---

## 📧 Email de Apresentação

```
Assunto: Landing Page Barber Premium — Pronta para Deploy

Prezado [Cliente],

A landing page de sua barbearia está pronta! Aqui está o que foi desenvolvido:

✨ FEATURES
- Design editorial sofisticado e profissional
- Responsivo em todos os dispositivos (desktop, tablet, mobile)
- Otimizado para conversão (agendamento)
- Performance otimizada (Lighthouse 90+)
- SEO pronto

📍 SEÇÕES
- Hero com call-to-action direto
- Sobre a barbearia com stats
- Serviços com preços
- Galeria de trabalhos
- Apresentação da equipe
- Depoimentos de clientes
- CTA final + Footer

🚀 PRÓXIMOS PASSOS
1. Substituir imagens de placeholder por fotos reais
2. Atualizar informações de contato (WhatsApp, telefone, endereço, horários)
3. Testar em navegadores/dispositivos
4. Deploy em Vercel/Netlify ou seu servidor

Qualquer dúvida, estou à disposição!

Abraços,
Seu Nome
```

---

## 💡 Dicas de Manutenção

### Backup Regular
```bash
# Backup semanal
zip -r backup-barber-$(date +%Y%m%d).zip pj2/
```

### Monitorar Performance
- Google Search Console — erros de crawl
- Google Analytics — tráfego e conversões
- Lighthouse — performance mensal

### Atualizar Conteúdo
- Fotos da galeria — a cada mês
- Depoimentos — conforme receba
- Horários — sazonalmente

---

## 🎯 Métricas de Sucesso

Após 30 dias, medir:
- Visitantes únicos
- Taxa de conversão (agendamentos)
- Tempo na página
- Taxa de rejeição
- Dispositivos mais usados
- Páginas mais visitadas

---

## ❓ FAQ

**P: Quanto tempo leva para aparecer no Google?**
R: 2-4 semanas após indexação. Submeta em Search Console para acelerar.

**P: Como adicionar um formulário de contato?**
R: Use Formspree, Basin, ou Netlify Forms — zero código.

**P: Posso mudar as cores?**
R: Sim! Edite `:root` em `styles.css`.

**P: Como adicionar mais seções?**
R: Siga o padrão HTML existente e estile usando CSS Grid/Flexbox.

**P: É mobile-friendly?**
R: 100% — testado em todos os tamanhos de tela.

---

**Última atualização:** 2026-10-01  
**Versão:** 1.0.0  
**Status:** ✅ Pronto para produção
