import tkinter as tk
from tkinter import messagebox


# Clase principal para la interfaz de la Lista de Tareas
class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tarea: Gestión de Lista de Tareas")
        self.root.geometry("400x500")

        # --- Interfaz Gráfica ---

        # Campo de entrada (Entry) para escribir nuevas tareas
        self.task_entry = tk.Entry(root, font=("Arial", 12))
        self.task_entry.pack(pady=10, padx=20, fill=tk.X)

        # MANEJO DE EVENTOS: Al presionar 'Enter' se añade la tarea automáticamente
        self.task_entry.bind('<Return>', lambda event: self.add_task())

        # Botón para Añadir Tarea
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task, bg="#4caf50", fg="white")
        self.add_button.pack(pady=5)

        # Componente de lista (Listbox) para mostrar las tareas actuales
        self.tasks_listbox = tk.Listbox(root, font=("Arial", 12), selectmode=tk.SINGLE)
        self.tasks_listbox.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        # EVENTO OPCIONAL: Doble clic en una tarea para marcarla como completada
        self.tasks_listbox.bind('<Double-Button-1>', lambda event: self.mark_completed())

        # Botones inferiores para acciones de gestión
        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.mark_completed, bg="#2196f3",
                                         fg="white")
        self.complete_button.pack(side=tk.LEFT, padx=30, pady=10)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task, bg="#f44336", fg="white")
        self.delete_button.pack(side=tk.RIGHT, padx=30, pady=10)

    # --- Lógica de la Aplicación ---

    def add_task(self):
        """Añade la tarea del campo de entrada a la lista."""
        task = self.task_entry.get()
        if task.strip() != "":
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)  # Limpia el campo tras añadir
        else:
            messagebox.showwarning("Entrada vacía", "Por favor, escribe una tarea.")

    def mark_completed(self):
        """Modifica visualmente la tarea seleccionada para indicar que terminó."""
        try:
            index = self.tasks_listbox.curselection()[0]
            task = self.tasks_listbox.get(index)

            # Si no está marcada, le agregamos un prefijo y cambiamos el color
            if not task.startswith("✔ "):
                new_text = f"✔ {task}"
                self.tasks_listbox.delete(index)
                self.tasks_listbox.insert(index, new_text)
                self.tasks_listbox.itemconfig(index, fg="gray")
        except IndexError:
            messagebox.showwarning("Selección", "Selecciona una tarea de la lista primero.")

    def delete_task(self):
        """Remueve la tarea seleccionada del componente Listbox."""
        try:
            index = self.tasks_listbox.curselection()[0]
            self.tasks_listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Selección", "Selecciona la tarea que deseas eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()