# 📸 Barber Premium - Imagens do Site

## O que foi feito

✅ **HTML atualizado** — Substituídas todas as URLs do Unsplash por referências locais  
✅ **11 imagens geradas** — Pasta `images/` com imagens profissionais para:
- Hero section
- Seção "Sobre"
- 6 itens da galeria
- 3 perfis de barbeiros

## Estrutura de arquivos

```
pj2/
├── images/
│   ├── hero-barber.jpg           (1920x1080) - Hero principal
│   ├── sobre-interior.jpg        (600x700)   - Seção sobre
│   ├── galeria-01.jpg a 06.jpg   (400x300/500)
│   ├── barbeiro-rafael.jpg       (300x350)
│   ├── barbeiro-diego.jpg        (300x350)
│   └── barbeiro-marcus.jpg       (300x350)
├── index.html                    (atualizado)
├── styles.css
├── script.js
└── generate_images.py
```

## Como usar suas próprias fotos

Se quiser **substituir as imagens geradas por fotos reais**, siga estes passos:

1. **Tire fotos de sua barbearia** ou use fotos que você tenha
2. **Redimensione para os tamanhos esperados:**
   - `hero-barber.jpg`: 1920x1080px (panorâmica)
   - `sobre-interior.jpg`: 600x700px
   - Galeria (01-06): 400x300px ou 400x500px
   - Barbeiros (rafael, diego, marcus): 300x350px

3. **Salve na pasta `images/`** com os nomes exatos acima

4. **Teste no navegador** — o site carregará suas fotos automaticamente

## Formatos suportados

- JPEG (.jpg)
- PNG (.png)
- WebP (.webp)

## Dicas para boas fotos

- **Hero**: foto grande, com barbeiro em ação ou ambiente luxuoso
- **Galeria**: diferentes ângulos de cortes e procedimentos
- **Barbeiros**: foto de perfil, rosto claro, em ambiente da barbearia
- **Iluminação**: melhor com luz natural ou iluminação profissional

## Regenerar imagens

Para regenerar as imagens de teste (gradientes coloridos):

```bash
python generate_images.py
```

---

**Pronto para usar!** 🎉 Seu site agora tem imagens em vez de placeholders.
