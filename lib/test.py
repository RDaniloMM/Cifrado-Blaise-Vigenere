import customtkinter as ctk
from tkinter import filedialog, messagebox

from file_management import leer_archivo, escribir_archivo
from algoritmo_blaise_vigenere import cifrar, descifrar, ALFABETOS

# Aplicación CustomTkinter
class VigenereApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Cifrador/Descifrador Vigenère")
        self.geometry("600x600")

        # Variables
        self.file_path = ""
        self.clave = ctk.StringVar()
        self.option = ctk.StringVar(value="Cifrar")
        self.alfabeto_seleccionado = ctk.StringVar(value="Alfabeto Español")  # Usamos StringVar

        # Título
        self.label_title = ctk.CTkLabel(self, text="Cifrador/Descifrador de Vigenère", font=("Arial", 20))
        self.label_title.pack(pady=10)

        # Selector de alfabeto
        self.label_alfabeto = ctk.CTkLabel(self, text="Seleccionar alfabeto:")
        self.label_alfabeto.pack(pady=5)

        self.combo_alfabeto = ctk.CTkOptionMenu(self, 
            variable=self.alfabeto_seleccionado, 
            values=list(ALFABETOS.keys()), 
            command=self.cambiar_alfabeto)
        self.combo_alfabeto.pack(pady=5)

        # Botón para seleccionar archivo
        self.button_select_file = ctk.CTkButton(self, text="Seleccionar archivo", command=self.select_file)
        self.button_select_file.pack(pady=10)

        # Entrada de texto
        self.text_input = ctk.CTkTextbox(self, width=500, height=100)
        self.text_input.pack(pady=10)

        # Entrada para la clave
        self.entry_clave = ctk.CTkEntry(self, textvariable=self.clave, placeholder_text="Ingrese la clave")
        self.entry_clave.pack(pady=10)

        # Radio buttons para elegir entre cifrar y descifrar
        self.radio_cifrar = ctk.CTkRadioButton(self, text="Cifrar", variable=self.option, value="Cifrar")
        self.radio_descifrar = ctk.CTkRadioButton(self, text="Descifrar", variable=self.option, value="Descifrar")
        self.radio_cifrar.pack(pady=5)
        self.radio_descifrar.pack(pady=5)

        # Botón para ejecutar
        self.button_execute = ctk.CTkButton(self, text="Ejecutar", command=self.ejecutar)
        self.button_execute.pack(pady=10)

        # Botón para guardar el texto procesado
        self.button_save = ctk.CTkButton(self, text="Guardar texto procesado", command=self.guardar_texto)
        self.button_save.pack(pady=10)

        # Cuadro de texto para mostrar el resultado
        self.text_output = ctk.CTkTextbox(self, width=500, height=100)
        self.text_output.pack(pady=10)

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

        if self.option.get() == "Cifrar":
            self.resultado = cifrar(texto, self.clave.get(), alfabeto_seleccionado)
            self.text_output.delete(1.0, ctk.END)
            self.text_output.insert(ctk.END, self.resultado)
        elif self.option.get() == "Descifrar":
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

if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = VigenereApp()
    app.mainloop()
