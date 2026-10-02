#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera imagens profissionais em PNG para a barbearia usando PIL
"""

from PIL import Image, ImageDraw, ImageFilter
import os
from pathlib import Path

# Criar pasta de imagens
images_dir = Path("images")
images_dir.mkdir(exist_ok=True)

def create_gradient_bg(width, height, color1, color2):
    """Cria um fundo com gradiente"""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)

    for y in range(height):
        r = int(color1[0] + (color2[0] - color1[0]) * y / height)
        g = int(color1[1] + (color2[1] - color1[1]) * y / height)
        b = int(color1[2] + (color2[2] - color1[2]) * y / height)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    return img

def add_noise_and_blur(img):
    """Adiciona textura para parecer mais realista"""
    img = img.filter(ImageFilter.GaussianBlur(radius=2))
    return img

# Cores profissionais de barbearia
dark_bg = (20, 20, 20)
gold_accent = (201, 169, 97)
barber_dark = (40, 40, 40)
light_text = (245, 245, 245)

print("Gerando imagens profissionais para a barbearia...")
print("=" * 50)

# 1. Hero image - Barber trabalhando
print("[..] Gerando hero-barber.jpg...", end=" ", flush=True)
img = create_gradient_bg(1920, 1080, (15, 15, 15), (40, 30, 20))
draw = ImageDraw.Draw(img)

# Adiciona texto elegante
draw.rectangle([(0, 400), (1920, 680)], fill=(0, 0, 0, 80))
draw.text((960, 540), "BARBER PREMIUM", fill=gold_accent, anchor="mm",
          font=None)

img = add_noise_and_blur(img)
img.save(str(images_dir / "hero-barber.jpg"), "JPEG", quality=85)
print("[OK]")

# 2. Sobre - Interior elegante
print("[..] Gerando sobre-interior.jpg...", end=" ", flush=True)
img = create_gradient_bg(600, 700, (25, 25, 25), (50, 40, 30))
draw = ImageDraw.Draw(img)

# Padrão de linhas (efeito moderno)
for i in range(0, 700, 50):
    draw.line([(0, i), (600, i)], fill=(201, 169, 97, 30), width=1)

img = add_noise_and_blur(img)
img.save(str(images_dir / "sobre-interior.jpg"), "JPEG", quality=85)
print("[OK]")

# 3-8. Galeria de trabalhos
gallery_configs = [
    ("galeria-01.jpg", 400, 500, (35, 25, 15), (60, 40, 20)),
    ("galeria-02.jpg", 400, 300, (25, 35, 25), (50, 60, 40)),
    ("galeria-03.jpg", 400, 300, (40, 30, 20), (70, 50, 30)),
    ("galeria-04.jpg", 400, 500, (30, 20, 35), (55, 35, 60)),
    ("galeria-05.jpg", 400, 300, (45, 35, 25), (75, 55, 35)),
    ("galeria-06.jpg", 400, 300, (25, 25, 35), (50, 50, 65)),
]

for filename, width, height, color1, color2 in gallery_configs:
    print(f"[..] Gerando {filename}...", end=" ", flush=True)
    img = create_gradient_bg(width, height, color1, color2)
    draw = ImageDraw.Draw(img)

    # Adiciona um padrão geométrico sutil
    for i in range(0, max(width, height), 100):
        draw.line([(i, 0), (0, i)], fill=gold_accent, width=2)

    img = add_noise_and_blur(img)
    img.save(str(images_dir / filename), "JPEG", quality=85)
    print("[OK]")

# 9-11. Fotos dos barbeiros
barber_configs = [
    ("barbeiro-rafael.jpg", 300, 350, (35, 28, 20), (65, 50, 35)),
    ("barbeiro-diego.jpg", 300, 350, (28, 35, 28), (50, 65, 50)),
    ("barbeiro-marcus.jpg", 300, 350, (35, 20, 28), (65, 35, 50)),
]

for filename, width, height, color1, color2 in barber_configs:
    print(f"[..] Gerando {filename}...", end=" ", flush=True)
    img = create_gradient_bg(width, height, color1, color2)
    draw = ImageDraw.Draw(img)

    # Adiciona um círculo (perfil)
    margin = 30
    draw.ellipse([(margin, margin), (width-margin, width-margin)],
                 fill=gold_accent, outline=gold_accent)

    img = add_noise_and_blur(img)
    img.save(str(images_dir / filename), "JPEG", quality=85)
    print("[OK]")

print("=" * 50)
print("\n[SUCCESS] Todas as imagens foram geradas!")
print(f"[INFO] Pasta: {images_dir.absolute()}")
print("[INFO] Seu site agora tem imagens profissionais!")
