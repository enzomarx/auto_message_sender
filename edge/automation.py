import pyautogui
import time

time.sleep(5)
def move_mouse_to(x, y):
    """Move o mouse para uma posição específica na tela."""
    pyautogui.moveTo(x, y, duration=1)  # move o mouse com uma animação suave
    print(f"Mouse movido para ({x}, {y})")

def capture_screen(region=None):
    """Captura uma parte da tela e salva a imagem em um arquivo."""
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save("screenshot.png")
    print("Captura de tela salva como 'screenshot.png'")

def locate_and_click(image_path):
    """Localiza uma imagem na tela e clica nela se encontrada."""
    try:
        # localiza a imagem na tela
        location = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)
        if location:
            pyautogui.click(location)
            print(f"Clicado na imagem encontrada em {location}")
        else:
            print("Imagem não encontrada na tela.")
    except Exception as e:
        print(f"Erro ao localizar imagem: {e}")

def main():
    # Configuração inicial
    pyautogui.FAILSAFE = True  # Ativa o fail-safe para parar o script movendo o mouse para o canto da tela
    print("Iniciando script...")

    # Move o mouse para uma posição inicial
    move_mouse_to(364, 238)
    time.sleep(1)  # Pausa para garantir que o movimento foi concluído

    # Captura uma área da tela
    capture_screen(region=(364, 238, 544, 358))  # Captura uma área de 300x300 pixels na posição (100, 100)
    time.sleep(1)  # Pausa após a captura

    # Localiza e clica em um ícone
    locate_and_click('shoppe.png')  # Substitua 'icon.png' pelo caminho da imagem do ícone

    print("Script concluído.")

if __name__ == "__main__":
    main()
