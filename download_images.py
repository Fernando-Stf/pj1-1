#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para baixar imagens profissionais de barbearia do Pexels
Salva as imagens na pasta images/ com os nomes esperados pelo HTML
"""

import os
import sys
import urllib.request
import urllib.error
from pathlib import Path

# Configurar encoding para Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Criar pasta de imagens se não existir
images_dir = Path("images")
images_dir.mkdir(exist_ok=True)

# URLs de imagens profissionais de barbearia do Pexels
images = {
    "hero-barber.jpg": "https://images.pexels.com/photos/3962287/pexels-photo-3962287.jpeg?auto=compress&cs=tinysrgb&w=1920&h=1080&fit=crop",
    "sobre-interior.jpg": "https://images.pexels.com/photos/3945683/pexels-photo-3945683.jpeg?auto=compress&cs=tinysrgb&w=600&h=700&fit=crop",
    "galeria-01.jpg": "https://images.pexels.com/photos/3962289/pexels-photo-3962289.jpeg?auto=compress&cs=tinysrgb&w=400&h=500&fit=crop",
    "galeria-02.jpg": "https://images.pexels.com/photos/3962286/pexels-photo-3962286.jpeg?auto=compress&cs=tinysrgb&w=400&h=300&fit=crop",
    "galeria-03.jpg": "https://images.pexels.com/photos/3962290/pexels-photo-3962290.jpeg?auto=compress&cs=tinysrgb&w=400&h=300&fit=crop",
    "galeria-04.jpg": "https://images.pexels.com/photos/3962288/pexels-photo-3962288.jpeg?auto=compress&cs=tinysrgb&w=400&h=500&fit=crop",
    "galeria-05.jpg": "https://images.pexels.com/photos/3945684/pexels-photo-3945684.jpeg?auto=compress&cs=tinysrgb&w=400&h=300&fit=crop",
    "galeria-06.jpg": "https://images.pexels.com/photos/3962285/pexels-photo-3962285.jpeg?auto=compress&cs=tinysrgb&w=400&h=300&fit=crop",
    "barbeiro-rafael.jpg": "https://images.pexels.com/photos/1181690/pexels-photo-1181690.jpeg?auto=compress&cs=tinysrgb&w=300&h=350&fit=crop",
    "barbeiro-diego.jpg": "https://images.pexels.com/photos/1239291/pexels-photo-1239291.jpeg?auto=compress&cs=tinysrgb&w=300&h=350&fit=crop",
    "barbeiro-marcus.jpg": "https://images.pexels.com/photos/1040881/pexels-photo-1040881.jpeg?auto=compress&cs=tinysrgb&w=300&h=350&fit=crop",
}

print("Baixando imagens para a barbearia...")
print("=" * 50)

success_count = 0
failed_images = []

for filename, url in images.items():
    filepath = images_dir / filename

    try:
        print(f"[..] Baixando {filename}...", end=" ", flush=True)

        # Adiciona headers para evitar bloqueios
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        )

        urllib.request.urlretrieve(url, filepath)

        file_size = os.path.getsize(filepath) / 1024  # KB
        print(f"[OK] ({file_size:.1f} KB)")
        success_count += 1

    except urllib.error.URLError as e:
        print(f"[ERR] Erro de conexao")
        failed_images.append((filename, str(e)))
    except Exception as e:
        print(f"[ERR] {str(e)}")
        failed_images.append((filename, str(e)))

print("=" * 50)
print(f"\nResumo: {success_count}/{len(images)} imagens baixadas com sucesso!")

if failed_images:
    print(f"\n[!] {len(failed_images)} imagem(ns) falharam:")
    for filename, error in failed_images:
        print(f"    - {filename}: {error}")
    print("\nDica: Verifique sua conexao com a internet e tente novamente.")
else:
    print("\n[SUCCESS] Todas as imagens foram baixadas!")
    print("Seu site de barbearia agora tem fotos de verdade!")
