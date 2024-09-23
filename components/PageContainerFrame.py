import customtkinter as ctk

# Frame para el contenedor principal de las páginas
class PageContainerFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(row=0, column=1, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)