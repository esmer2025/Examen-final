import customtkinter as ctk


# ---------------- FUNCIONES ----------------

def registrar_producto():
    producto = entrada_producto.get()
    precio = entrada_precio.get()

    if producto == "" or precio == "":
        etiqueta_resultado.configure(
            text="Por favor, complete todos los campos."
        )
    else:
        etiqueta_resultado.configure(
            text=f"Producto registrado: {producto} | Precio: Q{precio}"
        )


def limpiar():
    entrada_producto.delete(0, "end")
    entrada_precio.delete(0, "end")
    etiqueta_resultado.configure(text="")


# ---------------- CONFIGURACIÓN ----------------

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Registro de Producto")
app.geometry("450x400")
app.resizable(False, False)


# ---------------- INTERFAZ ----------------

titulo = ctk.CTkLabel(
    app,
    text="REGISTRO DE PRODUCTO-EXAMEN FINAL",
    font=("Arial", 24, "bold")
)
titulo.pack(pady=(30, 25))


label_producto = ctk.CTkLabel(
    app,
    text="Producto:",
    font=("Arial", 16)
)
label_producto.pack(pady=(5, 5))


entrada_producto = ctk.CTkEntry(
    app,
    placeholder_text="Ingrese el producto",
    width=300
)
entrada_producto.pack(pady=(0, 15))


label_precio = ctk.CTkLabel(
    app,
    text="Precio:",
    font=("Arial", 16)
)
label_precio.pack(pady=(5, 5))


entrada_precio = ctk.CTkEntry(
    app,
    placeholder_text="Ingrese el precio",
    width=300
)
entrada_precio.pack(pady=(0, 20))


# ---------------- BOTONES ----------------

frame_botones = ctk.CTkFrame(app, fg_color="transparent")
frame_botones.pack(pady=5)


boton_registrar = ctk.CTkButton(
    frame_botones,
    text="Registrar",
    width=130,
    command=registrar_producto
)
boton_registrar.grid(row=0, column=0, padx=10)


boton_limpiar = ctk.CTkButton(
    frame_botones,
    text="Limpiar",
    width=130,
    command=limpiar
)
boton_limpiar.grid(row=0, column=1, padx=10)


# ---------------- RESULTADO ----------------

etiqueta_resultado = ctk.CTkLabel(
    app,
    text="",
    font=("Arial", 14)
)
etiqueta_resultado.pack(pady=25)


# ---------------- EJECUTAR ----------------

app.mainloop()