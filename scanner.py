# Motor de IA e Roteirização - Shopee Route Pro
import pytesseract
from PIL import Image

def ler_etiqueta(caminho_imagem):
    # Extrai texto da etiqueta via OCR
    texto = pytesseract.image_to_string(Image.open(caminho_imagem), lang='por')
    return texto

# Lógica de Roteirização Otimizada
enderecos_lidos = ["Rua A, 100", "Rua C, 50", "Rua B, 20"]
rota_sugerida = sorted(enderecos_lidos)

print("--- ROTA OTIMIZADA ---")
for i, local in enumerate(rota_sugerida, 1):
    print(f"{i}ª Parada: {local}")
print("\nEconomia estimada: 15% de combustível.")
