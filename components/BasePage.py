import customtkinter as ctk

# Clase base para las páginas
class BasePage(ctk.CTkFrame):
    def __init__(self, parent, title, description):
        super().__init__(parent)
        self.grid(row=0, column=0, sticky="nsew")
        
        # Asegurar que el contenido esté anclado en la parte superior
        self.grid_rowconfigure(0, weight=0)  # No permitir que se expanda
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)  # Esto permite que los elementos de abajo se expandan
        self.grid_columnconfigure(0, weight=1)

        # Título y descripción anclados en la parte superior
        self.label = ctk.CTkLabel(self, text=title, font=ctk.CTkFont(size=24))
        self.label.grid(row=0, column=0, padx=20, pady=(20, 5), sticky="n")

        self.description = ctk.CTkLabel(self, text=description, font=ctk.CTkFont(size=16))
        self.description.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="n")