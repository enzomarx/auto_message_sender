import customtkinter as ctk
import pyautogui
import time
import random
from datetime import datetime
import os
from tkinter import filedialog, messagebox


# Configurações de cor e tema
ctk.set_appearance_mode("Light")  # Usando o modo claro para melhorar o contraste com as cores vermelhas e rosas
ctk.set_default_color_theme("dark-blue")


class AutoMessageApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da Janela Principal
        self.title("Auto Message Sender")
        self.geometry("700x500")

        # Alterações nas cores
        self.configure(bg="#FFC1CC")  # Fundo rosa claro

        # Variáveis Padrão
        self.icon_path = ctk.StringVar(value="icon.png")
        self.screenshot_region = ctk.StringVar(value="45,260,467,519")  # Posição e tamanho padrão (x, y, width, height)
        self.messages = [
            "Eu te amo ❤️", "Amo você 💕", "Você é meu amor 💖", "Te adoro 😘",
            "Você é minha vida 🌹", "Te amo muito 😍", "Ты мое солнышко ☀️",
            "Моя любовь 💕", "Скучаю по тебе 💔", "Ты моя жизнь 🌹",
            "Обожаю тебя 😘", "Люблю тебя сильно ❤️"
        ]

        self.schedule_date = None
        self.schedule_time = None

        # Frame de Configurações
        self.settings_frame = ctk.CTkFrame(self)
        self.settings_frame.pack(pady=20, padx=10, fill="x")
        self.settings_frame.configure(fg_color="#FF69B4")  # Definir cor de fundo correta para o CTkFrame

        # Selecionar ícone
        self.icon_label = ctk.CTkLabel(self.settings_frame, text="Caminho do Ícone:", text_color="white")
        self.icon_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.icon_entry = ctk.CTkEntry(self.settings_frame, textvariable=self.icon_path, width=200)
        self.icon_entry.grid(row=0, column=1, padx=5, pady=5)
        self.icon_button = ctk.CTkButton(self.settings_frame, text="Selecionar", command=self.select_icon, fg_color="#DC143C", hover_color="#FF6347")
        self.icon_button.grid(row=0, column=2, padx=5, pady=5)

        # Selecionar região de captura de tela
        self.screenshot_label = ctk.CTkLabel(self.settings_frame, text="Região de Captura de Tela (x,y,w,h):", text_color="white")
        self.screenshot_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.screenshot_entry = ctk.CTkEntry(self.settings_frame, textvariable=self.screenshot_region, width=200)
        self.screenshot_entry.grid(row=1, column=1, padx=5, pady=5)
        self.default_button = ctk.CTkButton(self.settings_frame, text="Usar Padrões", command=self.use_default_settings, fg_color="#DC143C", hover_color="#FF6347")
        self.default_button.grid(row=1, column=2, padx=5, pady=5)

        # Área de Mensagens
        self.message_frame = ctk.CTkFrame(self)
        self.message_frame.pack(pady=20, padx=10, fill="both", expand=True)
        self.message_frame.configure(fg_color="#FFC1CC")  # Definir cor de fundo correta para o CTkFrame

        self.message_textbox = ctk.CTkTextbox(self.message_frame, height=150, width=300)
        self.message_textbox.pack(side="left", padx=10, pady=10, fill="both", expand=True)
        self.update_message_list()

        self.add_message_button = ctk.CTkButton(self.message_frame, text="Adicionar Mensagem", command=self.add_message, fg_color="#DC143C", hover_color="#FF6347")
        self.add_message_button.pack(side="top", padx=10, pady=5)
        self.remove_message_button = ctk.CTkButton(self.message_frame, text="Remover Mensagem", command=self.remove_message, fg_color="#DC143C", hover_color="#FF6347")
        self.remove_message_button.pack(side="top", padx=10, pady=5)

        # Geração de Mensagem Procedural ou Personalizada
        self.generation_frame = ctk.CTkFrame(self)
        self.generation_frame.pack(pady=20, padx=10, fill="x")
        self.generation_frame.configure(fg_color="#FF69B4")

        self.generation_option = ctk.StringVar(value="procedural")
        self.procedural_radio = ctk.CTkRadioButton(self.generation_frame, text="Geração Procedural", variable=self.generation_option, value="procedural", text_color="white")
        self.procedural_radio.pack(side="left", padx=5)
        self.custom_radio = ctk.CTkRadioButton(self.generation_frame, text="Geração Personalizada", variable=self.generation_option, value="custom", text_color="white")
        self.custom_radio.pack(side="left", padx=5)

        self.custom_message_entry = ctk.CTkEntry(self.generation_frame, placeholder_text="Digite sua mensagem personalizada aqui", width=250)
        self.custom_message_entry.pack(side="left", padx=5)

        # Botão para iniciar a automação
        self.start_button = ctk.CTkButton(self, text="Iniciar Automação", command=self.start_automation, fg_color="#DC143C", hover_color="#FF6347")
        self.start_button.pack(pady=20)

        # Agendar Envio de Mensagem
        self.schedule_frame = ctk.CTkFrame(self)
        self.schedule_frame.pack(pady=20, padx=10, fill="x")
        self.schedule_frame.configure(fg_color="#FFC1CC")

        self.schedule_button = ctk.CTkButton(self.schedule_frame, text="Agendar Envio", command=self.schedule_message, fg_color="#DC143C", hover_color="#FF6347")
        self.schedule_button.pack(pady=5)

        self.schedule_entry = ctk.CTkEntry(self.schedule_frame, placeholder_text="Data e hora (dd/mm/yyyy hh:mm)", width=250)
        self.schedule_entry.pack(pady=5)

    def select_icon(self):
        file_path = filedialog.askopenfilename(filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpg;*.jpeg")])
        if file_path:
            self.icon_path.set(file_path)
            messagebox.showinfo("Ícone Selecionado", f"Ícone selecionado: {file_path}")

    def use_default_settings(self):
        self.icon_path.set("icon.png")
        self.screenshot_region.set("45,260,467,519")
        messagebox.showinfo("Configurações Padrão", "Configurações padrão aplicadas.")

    def update_message_list(self):
        self.message_textbox.delete("1.0", ctk.END)
        for msg in self.messages:
            self.message_textbox.insert(ctk.END, msg + "\n")

    def add_message(self):
        new_message = self.custom_message_entry.get()
        if new_message:
            self.messages.append(new_message)
            self.update_message_list()
            self.custom_message_entry.delete(0, ctk.END)

    def remove_message(self):
        try:
            selected_message = self.message_textbox.get("sel.first", "sel.last").strip()
            if selected_message in self.messages:
                self.messages.remove(selected_message)
                self.update_message_list()
        except:
            messagebox.showwarning("Aviso", "Por favor, selecione uma mensagem para remover.")

    def start_automation(self):
        if self.generation_option.get() == "procedural":
            self.run_procedural()
        else:
            self.run_custom()

    def run_procedural(self):
        print("Iniciando geração procedural de mensagens...")
        self.automate_typing(self.messages)

    def run_custom(self):
        custom_message = self.custom_message_entry.get()
        if custom_message:
            print(f"Enviando mensagem personalizada: {custom_message}")
            self.automate_typing([custom_message])

    def automate_typing(self, messages):
        time.sleep(2)  # Espera 2 segundos antes de começar
        for message in messages:
            pyautogui.typewrite(message)
            pyautogui.press("enter")
            time.sleep(1)  # Pausa de 1 segundo entre as mensagens

    def schedule_message(self):
        schedule_time = self.schedule_entry.get()
        try:
            self.schedule_date = datetime.strptime(schedule_time, "%d/%m/%Y %H:%M")
            delay = (self.schedule_date - datetime.now()).total_seconds()
            if delay > 0:
                self.after(int(delay * 1000), self.start_automation)
                messagebox.showinfo("Agendamento", f"Mensagem agendada para {self.schedule_date}")
            else:
                messagebox.showwarning("Erro de Agendamento", "A data e hora devem ser futuras.")
        except ValueError:
            messagebox.showerror("Erro de Formato", "Formato de data e hora inválido. Por favor, use o formato dd/mm/yyyy hh:mm.")

if __name__ == "__main__":
    app = AutoMessageApp()
    app.mainloop()
