import pyautogui
import time
import random

def move_mouse_to(x, y):
    """Move o mouse para uma posição específica na tela."""
    pyautogui.moveTo(x, y, duration=0.5)  # Move o mouse mais rapidamente
    print(f"Mouse movido para ({x}, {y})")

def capture_screen(region=None):
    """Captura uma parte da tela e salva a imagem em um arquivo."""
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save("screenshot.png")
    print("Captura de tela salva como 'screenshot.png'")

def locate_and_click(image_path):
    """Localiza uma imagem na tela e clica nela se encontrada."""
    try:
        location = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)
        if location:
            pyautogui.click(location)
            print(f"Clicado na imagem encontrada em {location}")
        else:
            print("Imagem não encontrada na tela.")
    except Exception as e:
        print(f"Erro ao localizar imagem: {e}")

def click_and_type_message(x, y, num_messages, typing_speed=0.02, wait_time=0.10):
    """Clica em uma posição específica e envia um número específico de mensagens com emojis."""
    pyautogui.click(x, y)  # Clique na posição especificada
    print(f"Clicado na posição ({x}, {y})")

    # Lista de mensagens e emojis fofos
    messages = [
        "Tenha um bom dia",
        "Afirmativo",
        "Tem razao",
        "Claro",
        "Sim",
        "Tudo bem",
        "Oi",  # "Você é meu raio de sol"
        "Impressionante",       # "Meu amor"
        "Entendi",   # "Sinto sua falta"
        "Estou resolvendo esse assunto",      # "Você é minha vida"
        "Bom dia",      # "Te adoro"
        "Lucas" # "Amo você muito"
    ]

    emojis = ["❤️", "💕", "💖", "😘", "🌹", "😍", "☀️", "💔"]

    for _ in range(num_messages):
        # Escolher uma mensagem aleatória
        message = random.choice(messages)
        pyautogui.write(message, interval=typing_speed)
        pyautogui.press('enter')  # Enviar a mensagem
        print(f"Mensagem enviada: {message}")

        # Enviar uma sequência de emojis aleatórios
        for _ in range(3):  # Enviar 3 emojis
            emoji = random.choice(emojis)
            pyautogui.write(emoji, interval=typing_speed)
            pyautogui.press('enter')  # Enviar o emoji
            time.sleep(0.1)  # Pequena pausa entre os envios de emojis

        time.sleep(wait_time)  # Esperar antes de enviar a próxima mensagem

def main():
    # Configuração inicial
    pyautogui.FAILSAFE = True  # Ativa o fail-safe para parar o script movendo o mouse para o canto da tela
    print("Iniciando script...")

    # Move o mouse para uma posição inicial
    move_mouse_to(45, 260)
    time.sleep(0.5)  # Pausa para garantir que o movimento foi concluído

    # Captura uma área da tela
    capture_screen(region=(45, 260, 467, 519))
    time.sleep(0.5)  # Pausa após a captura

    # Localiza e clica em um ícone
    locate_and_click('iconelucas.png')  # Substitua 'icon.png' pelo caminho da imagem do ícone

    # Clique em uma posição específica e envie mensagens
    num_messages = 8  # Defina quantas mensagens você quer enviar
    click_and_type_message(636, 685, num_messages, typing_speed=0.1, wait_time=0.25)

    print("Script concluído.")

if __name__ == "__main__":
    main()
