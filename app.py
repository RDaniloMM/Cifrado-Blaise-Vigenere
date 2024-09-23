import customtkinter as ctk
# components
from components.SidebarFrame import SidebarFrame
from components.PageContainerFrame import PageContainerFrame
# pages
from pages.HomePage import Page as HomePage
from pages.VigenereCifrado import Page as VigenereCifrado
from pages.VigenereDecifrado import Page as VigenereDecifrado

# Configuración de customtkinter
ctk.set_appearance_mode("dark")  # Modo oscuro
ctk.set_default_color_theme("blue")  # Tema de color

# Clase principal de la aplicación
class CriptografiaApp(ctk.CTk):
    WIDTH = 680
    HEIGHT = 480
    
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("Aprendiende Criptografía")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.update()
        self.minsize(self.winfo_width(), self.winfo_height())

        # Configurar las filas y columnas de la ventana principal
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Inicializar los frames independientes
        self.sidebar_frame = SidebarFrame(self, app=self)  # Pasamos la referencia de la app para el control
        self.page_container = PageContainerFrame(self)

        # Diccionario para almacenar las clases de las páginas
        self.pages = {}

        # Cargar dinámicamente las páginas
        self.add_page("Inicio", HomePage)
        self.sidebar_frame.add_title("Blaise Vigenere")
        self.add_page("Cifrado", VigenereCifrado)
        self.add_page("Decifrado", VigenereDecifrado)

        # Inicialmente mostrar la primera página
        self.show_page("Inicio")

    def add_page(self, page_name, page_class):
        # Registra una nueva página en el sistema
        self.pages[page_name] = page_class(self.page_container)

        # Crear el botón correspondiente en el sidebar
        self.sidebar_frame.add_menu_button(page_name)

    def show_page(self, page_name):
        # Muestra la página seleccionada
        page = self.pages[page_name]
        page.tkraise()
