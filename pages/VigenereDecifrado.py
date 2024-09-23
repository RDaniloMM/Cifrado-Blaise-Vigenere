import customtkinter as ctk
from tkinter import filedialog, messagebox
# componets
from components.BasePage import BasePage

from lib.file_management import leer_archivo, escribir_archivo
from lib.algoritmo_blaise_vigenere import descifrar, ALFABETOS

# Página 2
class Page(BasePage):
    title = "Descifrado por el Algoritmo de Blaise Vigenère"
    description = "Descifra un texto utilizando el algoritmo de Blaise Vigenère."
    
    def __init__(self, parent):
        super().__init__(parent, self.title, self.description)
        self.built_ui()
    
    def built_ui(self):
        # Variables
        self.file_path = ""
        self.clave = ctk.StringVar()
        self.alfabeto_seleccionado = ctk.StringVar(value="Alfabeto Español")  # Usamos StringVar
        
        self.frame = ctk.CTkFrame(self)
        self.frame.grid(row=2, column=0, padx=40, pady=40, sticky="n")
        
        # Labels y campos de entrada para los parámetros
        # Selector de alfabeto
        self.label_alfabeto = ctk.CTkLabel(self.frame, text="Seleccionar alfabeto:")
        self.label_alfabeto.grid(row=0, column=0, padx=10, pady=5)
        
        self.combo_alfabeto = ctk.CTkOptionMenu(self.frame, 
            variable=self.alfabeto_seleccionado, 
            values=list(ALFABETOS.keys()), 
            command=self.cambiar_alfabeto)
        self.combo_alfabeto.grid(row=0, column=1, padx=10, pady=5)
        
        # Botón para seleccionar archivo
        self.button_select_file = ctk.CTkButton(self.frame, text="Seleccionar archivo", command=self.select_file)
        self.button_select_file.grid(row=1, column=0, padx=10, pady=5)
        
        # Botón para limpiar el input
        self.button_clear = ctk.CTkButton(self.frame, text="Limpiar", command=self.clear_input)
        self.button_clear.grid(row=1, column=1, padx=10, pady=10)
        
        # Entrada de texto
        self.text_input = ctk.CTkTextbox(self.frame, width=500, height=100)
        self.text_input.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        
        self.label_clave = ctk.CTkLabel(self.frame, text="Clave:")
        self.label_clave.grid(row=3, column=0, padx=10, pady=5)
        
        self.entry_clave = ctk.CTkEntry(self.frame,textvariable=self.clave, placeholder_text="Ingrese la clave")
        self.entry_clave.grid(row=3, column=1, padx=10, pady=5)
        
        # Botón para ejecutar
        self.button_execute = ctk.CTkButton(self.frame, text="Ejecutar", command=self.ejecutar)
        self.button_execute.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        
        # Botón para guardar el texto procesado
        self.button_save = ctk.CTkButton(self.frame, text="Guardar", command=self.guardar_texto)
        self.button_save.grid(row=5, column=0, padx=10, pady=10)
        
        # Botón para limpiar los campos
        self.button_output = ctk.CTkButton(self.frame, text="Limpiar", command=self.clear_output)
        self.button_output.grid(row=5, column=1, padx=10, pady=10)
        
        # Cuadro de texto para mostrar el resultado
        self.text_output = ctk.CTkTextbox(self.frame, width=500, height=100)
        self.text_output.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
    
    def cambiar_alfabeto(self, selected):
        self.alfabeto_seleccionado.set(selected)

    def select_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if self.file_path:
            # Leer el archivo y mostrar en el cuadro de texto
            texto = leer_archivo(self.file_path)
            self.text_input.delete(1.0, ctk.END)
            self.text_input.insert(ctk.END, texto)
            messagebox.showinfo("Archivo seleccionado", f"Archivo seleccionado: {self.file_path}")
        else:
            messagebox.showwarning("Error", "No se seleccionó ningún archivo")

    def ejecutar(self):
        texto = self.text_input.get(1.0, ctk.END).strip()

        if not texto:
            messagebox.showwarning("Error", "Debe ingresar o seleccionar un archivo con texto.")
            return

        if not self.clave.get():
            messagebox.showwarning("Error", "Debe ingresar una clave.")
            return

        alfabeto_seleccionado = ALFABETOS[self.alfabeto_seleccionado.get()]  # Obtener el alfabeto seleccionado

        self.resultado = descifrar(texto, self.clave.get(), alfabeto_seleccionado)
        self.text_output.delete(1.0, ctk.END)
        self.text_output.insert(ctk.END, self.resultado)

    def guardar_texto(self):
        if not self.resultado:
            messagebox.showwarning("Error", "No hay texto procesado para guardar.")
            return

        ruta_salida = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if ruta_salida:
            escribir_archivo(ruta_salida, self.resultado)
            messagebox.showinfo("Éxito", "El texto procesado ha sido guardado.")
    
    def clear_input(self):
        # Limpia todos los campos de entrada y el tablero de salida
        self.text_input.delete(1.0, ctk.END)
        
    def clear_output(self):
        self.text_output.delete(1.0, ctk.END)