import tkinter as tk
from tkinter import ttk, messagebox


# --- CONFIGURACIÓN DE LA APLICACIÓN ---
class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal - Tarea de Programación")
        self.root.geometry("650x450")

        # 1. ORGANIZACIÓN CON CONTENEDORES (Frames)
        # Frame para la entrada de datos (arriba)
        self.frame_entrada = tk.LabelFrame(self.root, text=" Registrar Nuevo Evento ", padx=10, pady=10)
        self.frame_entrada.pack(fill="x", padx=20, pady=10)

        # Frame para la visualización de la lista (centro)
        self.frame_lista = tk.Frame(self.root, padx=20)
        self.frame_lista.pack(fill="both", expand=True)

        # Frame para las acciones/botones (abajo)
        self.frame_acciones = tk.Frame(self.root, pady=15)
        self.frame_acciones.pack(fill="x", padx=20)

        self.crear_interfaz()

    def crear_interfaz(self):
        # 2. COMPONENTES DE ENTRADA (Labels y Entry)
        # Fecha
        tk.Label(self.frame_entrada, text="Fecha (DD/MM/AAAA):").grid(row=0, column=0, sticky="w", pady=5)
        self.ent_fecha = tk.Entry(self.frame_entrada)
        self.ent_fecha.grid(row=0, column=1, padx=5, pady=5)

        # Hora
        tk.Label(self.frame_entrada, text="Hora (HH:MM):").grid(row=0, column=2, sticky="w", pady=5)
        self.ent_hora = tk.Entry(self.frame_entrada)
        self.ent_hora.grid(row=0, column=3, padx=5, pady=5)

        # Descripción
        tk.Label(self.frame_entrada, text="Descripción:").grid(row=1, column=0, sticky="w", pady=5)
        self.ent_desc = tk.Entry(self.frame_entrada, width=50)
        self.ent_desc.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        # 3. COMPONENTES AVANZADOS (TreeView)
        self.tree = ttk.Treeview(self.frame_lista, columns=("Fecha", "Hora", "Descripción"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")

        # Ajuste de columnas
        self.tree.column("Fecha", width=100, anchor="center")
        self.tree.column("Hora", width=80, anchor="center")
        self.tree.column("Descripción", width=300)

        # Scrollbar para la lista
        scrollbar = ttk.Scrollbar(self.frame_lista, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # 4. BOTONES DE ACCIÓN
        self.btn_agregar = tk.Button(self.frame_acciones, text="Agregar Evento",
                                     command=self.agregar_evento, bg="#28a745", fg="white", width=15)
        self.btn_agregar.pack(side="left", padx=5)

        self.btn_eliminar = tk.Button(self.frame_acciones, text="Eliminar Seleccionado",
                                      command=self.eliminar_evento, bg="#dc3545", fg="white", width=20)
        self.btn_eliminar.pack(side="left", padx=5)

        self.btn_salir = tk.Button(self.frame_acciones, text="Salir",
                                   command=self.root.quit, bg="#6c757d", fg="white", width=10)
        self.btn_salir.pack(side="right", padx=5)

    # 5. MANEJO DE EVENTOS
    def agregar_evento(self):
        fecha = self.ent_fecha.get()
        hora = self.ent_hora.get()
        desc = self.ent_desc.get()

        if fecha and hora and desc:
            self.tree.insert("", "end", values=(fecha, hora, desc))
            # Limpiar campos tras agregar
            self.ent_fecha.delete(0, tk.END)
            self.ent_hora.delete(0, tk.END)
            self.ent_desc.delete(0, tk.END)
            messagebox.showinfo("Éxito", "Evento guardado correctamente.")
        else:
            messagebox.showwarning("Atención", "Todos los campos son obligatorios.")

    def eliminar_evento(self):
        item_seleccionado = self.tree.selection()
        if item_seleccionado:
            # Diálogo de confirmación
            confirmar = messagebox.askyesno("Confirmar", "¿Seguro que deseas eliminar el evento?")
            if confirmar:
                self.tree.delete(item_seleccionado)
        else:
            messagebox.showwarning("Error", "Selecciona un evento de la lista para eliminar.")


if __name__ == "__main__":
    ventana = tk.Tk()
    app = AgendaApp(ventana)
    ventana.mainloop()
