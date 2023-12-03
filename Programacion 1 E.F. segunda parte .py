
#SEGUNDA PARTE
# EJERCICIO>>>>7

import tkinter as tk

def actualizar_etiqueta():
    texto_ingresado = campo_entrada.get()
    etiqueta_resultado.config(text=texto_ingresado)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejercicio 7 - Tkinter")

# Crear y colocar los widgets en la ventana
etiqueta_instruccion = tk.Label(ventana, text="Ingrese un texto:")
etiqueta_instruccion.pack(pady=10)

campo_entrada = tk.Entry(ventana)
campo_entrada.pack(pady=10)

boton_actualizar = tk.Button(ventana, text="Actualizar Etiqueta", command=actualizar_etiqueta)
boton_actualizar.pack(pady=10)

etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack(pady=10)

# Iniciar el bucle de eventos
ventana.mainloop()


# EJERCICIO>>>>8

import tkinter as tk

def calcular():
    try:
        num1 = float(entrada_num1.get())
        num2 = float(entrada_num2.get())
        operacion = seleccion_operacion.get()

        if operacion == "Suma":
            resultado = num1 + num2
        elif operacion == "Resta":
            resultado = num1 - num2
        elif operacion == "Multiplicación":
            resultado = num1 * num2
        elif operacion == "División":
            resultado = num1 / num2
        else:
            resultado = "Operación no válida"

        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        etiqueta_resultado.config(text="Error: Ingrese números válidos")

# Crear la ventana principal
ventana_calculadora = tk.Tk()
ventana_calculadora.title("Calculadora Básica")

# Crear y colocar los widgets en la ventana
etiqueta_num1 = tk.Label(ventana_calculadora, text="Número 1:")
etiqueta_num1.grid(row=0, column=0, padx=10, pady=10)

entrada_num1 = tk.Entry(ventana_calculadora)
entrada_num1.grid(row=0, column=1, padx=10, pady=10)

etiqueta_num2 = tk.Label(ventana_calculadora, text="Número 2:")
etiqueta_num2.grid(row=1, column=0, padx=10, pady=10)

entrada_num2 = tk.Entry(ventana_calculadora)
entrada_num2.grid(row=1, column=1, padx=10, pady=10)

seleccion_operacion = tk.StringVar()
seleccion_operacion.set("Suma")

etiqueta_operacion = tk.Label(ventana_calculadora, text="Seleccione la operación:")
etiqueta_operacion.grid(row=2, column=0, padx=10, pady=10)

opciones_operacion = ["Suma", "Resta", "Multiplicación", "División"]
menu_operacion = tk.OptionMenu(ventana_calculadora, seleccion_operacion, *opciones_operacion)
menu_operacion.grid(row=2, column=1, padx=10, pady=10)

boton_calcular = tk.Button(ventana_calculadora, text="Calcular", command=calcular)
boton_calcular.grid(row=3, column=0, columnspan=2, pady=10)

etiqueta_resultado = tk.Label(ventana_calculadora, text="Resultado:")
etiqueta_resultado.grid(row=4, column=0, columnspan=2, pady=10)

# Iniciar el bucle de eventos
ventana_calculadora.mainloop()


# EJERCICIO>>>>9

import tkinter as tk

def cambiar_color(color):
    ventana.config(bg=color)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cambiar Color de Fondo")

# Crear y colocar los widgets en la ventana
boton_rojo = tk.Button(ventana, text="Rojo", command=lambda: cambiar_color("red"))
boton_rojo.pack(side=tk.LEFT, padx=10, pady=10)

boton_verde = tk.Button(ventana, text="Verde", command=lambda: cambiar_color("green"))
boton_verde.pack(side=tk.LEFT, padx=10, pady=10)

boton_azul = tk.Button(ventana, text="Azul", command=lambda: cambiar_color("blue"))
boton_azul.pack(side=tk.LEFT, padx=10, pady=10)

# Iniciar el bucle de eventos
ventana.mainloop()


# EJERCICIO>>>>10

import tkinter as tk

def mostrar_mensaje():
    opcion_seleccionada = seleccion_opciones.get()
    mensaje = f"Seleccionaste la opción: {opcion_seleccionada}"
    etiqueta_mensaje.config(text=mensaje)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz con Lista Desplegable")

# Crear y colocar los widgets en la ventana
etiqueta_instruccion = tk.Label(ventana, text="Selecciona una opción:")
etiqueta_instruccion.pack(pady=10)

opciones = ["Opción 1", "Opción 2", "Opción 3", "Opción 4"]

seleccion_opciones = tk.StringVar()
menu_desplegable = tk.OptionMenu(ventana, seleccion_opciones, *opciones)
menu_desplegable.pack(pady=10)

boton_mostrar_mensaje = tk.Button(ventana, text="MI PRIMER TINKER WILDER", command=mostrar_mensaje)
boton_mostrar_mensaje.pack(pady=10)

etiqueta_mensaje = tk.Label(ventana, text="")
etiqueta_mensaje.pack(pady=10)

# Iniciar el bucle de eventos
ventana.mainloop()
