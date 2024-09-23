import customtkinter as ctk

# Frame para la barra lateral (Sidebar)
class SidebarFrame(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, width=200, corner_radius=0)
        self.grid(row=0, column=0, sticky="nsew")
        
        # Título del Sidebar
        self.sidebar_title = ctk.CTkLabel(self, text="Menú", font=ctk.CTkFont(size=20, weight="bold"))
        self.sidebar_title.grid(row=0, column=0, padx=20, pady=10)
        
        # Variable para acceder a la aplicación principal
        self.app = app
    
    def add_menu_button(self, page_name):
        # Agrega un botón al Sidebar para cambiar entre páginas
        button = ctk.CTkButton(self, text=page_name, command=lambda: self.app.show_page(page_name))
        button.grid(padx=20, pady=10)
        
    def add_title(self, title):
        # Agrega un título al Sidebar
        label = ctk.CTkLabel(self, text=title, font=ctk.CTkFont(size=16, weight="bold"))
        label.grid(padx=20, pady=10)
        
    def add_label(self, text):
        # Agrega un label al Sidebar
        label = ctk.CTkLabel(self, text=text)
        label.grid(padx=20, pady=10)