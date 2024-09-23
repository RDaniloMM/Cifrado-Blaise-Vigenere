import customtkinter as ctk
from components.BasePage import BasePage

class Page(BasePage):
    title = "Presentación de Proyecto"
    description = "Cifrado de Blaise de Vigenere"
    
    def __init__(self, parent):
        super().__init__(parent, self.title, self.description)
        self.built_ui()
    
    def built_ui(self):
        # Configuramos la distribución del espacio vertical en el grid
        self.grid_rowconfigure(0, weight=1)  # Fila superior
        self.grid_rowconfigure(13, weight=1)  # Fila inferior para mantener espacio al final
        
        # Estilo elegante para los labels
        label_font_title = ("Arial", 20, "bold")  # Tamaño ajustado
        label_font_normal = ("Arial", 14)
        label_font_integrantes = ("Arial", 12)
        label_color = "#E0E0E0"  # Color claro para fondo oscuro
        title_color = "#FFA726"  # Color vibrante para los títulos

        # Añadimos un padding mayor entre la descripción y el label
        self.label_curso = ctk.CTkLabel(self, text="Seguridad Informática", font=label_font_title, text_color=title_color)
        self.label_curso.grid(row=2, column=0, padx=10, pady=(20, 10), sticky="n")  # Espacio mayor entre el título y la descripción

        # Mantenemos el profesor, equipo y otros labels bien alineados
        self.label_profesor = ctk.CTkLabel(self, text="Profesor: Ing. Llamozas Escalante, Freeman Hugo", font=label_font_normal, text_color=label_color)
        self.label_profesor.grid(row=3, column=0, padx=10, pady=2, sticky="n")

        self.label_grupo = ctk.CTkLabel(self, text="Equipo: 2", font=label_font_normal, text_color=label_color)
        self.label_grupo.grid(row=4, column=0, padx=10, pady=2, sticky="n")
        
        # Label de integrantes
        self.label_integrantes = ctk.CTkLabel(self, text="Integrantes:", font=label_font_normal, text_color=title_color)
        self.label_integrantes.grid(row=5, column=0, padx=10, pady=(10, 5), sticky="n")  # Añadí un padding superior e inferior

        integrantes = [
            "1. Chambilla Chambilla Hernan Ander 2021-119104",
            "2. Castro Flores Francisco José 2021-119101",
            "3. Moron Maylle Rivaldo Danilo 2021-119057",
            "4. Hermoza Gutierrez Juan José 2021-119039",
            "5. Peraza Chambilla Edson Josue 2020-119050"
        ]
        
        for i, integrante in enumerate(integrantes):
            label = ctk.CTkLabel(self, text=integrante, font=label_font_integrantes, text_color=label_color)
            label.grid(row=6 + i, column=0, padx=10, pady=2, sticky="n")

        # Añadimos espacio en la fila final para que no quede pegado al borde inferior
        self.grid_rowconfigure(12, weight=1)
