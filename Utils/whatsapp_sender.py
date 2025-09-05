import pyautogui
import pyperclip
import time

# Reemplaza estos valores con las coordenadas reales del input de WhatsApp Web
INPUT_X = 552  # ejemplo
INPUT_Y = 220  # ejemplo


def enviar_mensaje_whatsapp(mensaje):
    """
    Hace clic en el input del chat de WhatsApp Web, pega el mensaje y lo envía.
    """
    pyautogui.click(INPUT_X, INPUT_Y)
    time.sleep(0.5)  # Espera a que el input esté activo
    pyperclip.copy(mensaje)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)
    pyautogui.press("enter")
