import customtkinter as ctk
import tkinter as tk
# componets
from components.BasePage import BasePage
# algorithms

class Page(BasePage):
    title = "Presentacion de Proyecto"
    description = "Algortimos de criptografia clasica"
    
    def __init__(self, parent):
        super().__init__(parent, self.title, self.description)
        self.built_ui()
    
    def built_ui(self):
        # Contenido específico para esta página
        self.label_curso = ctk.CTkLabel(self, text="Seguridad Informatica", font=("Arial", 20))
        self.label_curso.grid(row=2, column=0, padx=20, pady=20)
        self.label_profesor = ctk.CTkLabel(self, text="Profesor: Ing. Llamozas Escalante, Freeman Hugo")
        self.label_profesor.grid(row=3, column=0, padx=20, pady=20)
        self.label_fecha = ctk.CTkLabel(self, text="Fecha: 22 de Septiembre de 2024")
        self.label_fecha.grid(row=4, column=0, padx=20, pady=20)
        self.label_grupo = ctk.CTkLabel(self, text="Equipo: 2")
        self.label_grupo.grid(row=5, column=0, padx=20, pady=20)
        # integrantes
        self.label_integrantes = ctk.CTkLabel(self, text="Integrantes:")
        self.label_integrantes.grid(row=6, column=0, padx=20, pady=20)
        self.label_integrantes1 = ctk.CTkLabel(self, text="1. Chambilla Chambilla Hernan Ander  2021-119104")
        self.label_integrantes1.grid(row=7, column=0, padx=20, pady=20)
        self.label_integrantes2 = ctk.CTkLabel(self, text="2. Juan Carlos Lopez")
        self.label_integrantes2.grid(row=8, column=0, padx=20, pady=20)
        self.label_integrantes3 = ctk.CTkLabel(self, text="3. Jose Luis Gonzalez")
        self.label_integrantes3.grid(row=9, column=0, padx=20, pady=20)
        self.label_integrantes4 = ctk.CTkLabel(self, text="4. Juan Carlos Lopez")
        self.label_integrantes4.grid(row=10, column=0, padx=20, pady=20)
        
        
        