# 📋 Registro de Datos Personales

Script de Python que solicita al usuario ingresar sus datos personales por consola y los muestra organizados al final.

---

## ¿Qué hace?

El programa pide los siguientes datos:

- **Nombre completo** — texto libre
- **Edad** — número entero
- **Sexo** — elige entre `masculino`, `femenino` u `otro`
- **Estatura** — número decimal en centímetros

Una vez ingresados todos los datos, los muestra en un resumen formateado.

---

## Validaciones

- Ningún campo puede quedar vacío
- La edad debe ser un número entero válido
- La estatura debe ser un número decimal válido
- El sexo solo acepta las opciones permitidas

Si el usuario ingresa un valor incorrecto, el programa lo notifica y vuelve a pedirlo.

---

## Cómo ejecutarlo

```bash
python datospersonales.py
```

> Requiere Python 3.x

---

## Ejemplo de uso

```
----------------------------------------
   REGISTRO DE DATOS PERSONALES
----------------------------------------
  Llena los campos a continuacion:

  Nombre completo: Santiago Sánchez
  Edad: 20
  Sexo (masculino/femenino/otro): masculino
  Estatura en cm (ej. 175): 175.5

----------------------------------------
   DATOS REGISTRADOS
----------------------------------------
  Nombre:   Santiago Sánchez
  Edad:     20 años
  Sexo:     Masculino
  Estatura: 175.5 cm
----------------------------------------
```

---

## Estructura del código

| Función | Descripción |
|---|---|
| `separador()` | Imprime una línea divisoria de guiones |
| `obtener_dato()` | Solicita y valida un campo del usuario |
| `main()` | Controla el flujo principal del programa |
