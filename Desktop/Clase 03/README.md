# 📚 Sistema de Registro de Calificaciones

> Programa en Python para registrar y calcular el promedio de calificaciones de la carrera de Tecnologías de la Información.

---

## 📋 Materias incluidas

| # | Materia |
|---|---------|
| 1 | Computación en la Nube |
| 2 | Sistemas Operativos |
| 3 | Bases de Datos |
| 4 | Estructuras de Datos |
| 5 | Metodologías Ágiles |
| 6 | Desarrollo Full Stack |
| 7 | Gestión de Redes |

---

## ⚙️ Requisitos

- Python 3.x instalado
- No requiere librerías externas

---

## ▶️ Cómo ejecutar

```bash
python calificaciones.py
```

O si tienes Python 2 y 3 en el mismo sistema:

```bash
python3 calificaciones.py
```

---

## 🧠 ¿Cómo se construyó el código?

### 1. Estructura de datos

Se usan dos estructuras principales:

```python
materias = ["Computación en la Nube", "Sistemas Operativos", ...]  # list
calificaciones = {}  # dict — clave: materia, valor: calificación
```

- **`materias`** → lista con los nombres de las 7 materias predefinidas.
- **`calificaciones`** → diccionario que se llena durante la ejecución.

---

### 2. Entrada de datos con validación

Se recorre `materias` con un `for`. Dentro, un `while True` repite la pregunta hasta recibir un dato válido:

```python
for materia in materias:
    while True:
        try:
            cal = float(input(f"Ingresa tu calificación para '{materia}' (0-100): "))
            if 0 <= cal <= 100:
                calificaciones[materia] = cal
                break
            else:
                print("⚠ Por favor ingresa un valor entre 0 y 100.")
        except ValueError:
            print("⚠ Valor inválido. Ingresa un número.")
```

- `try / except ValueError` — captura el error si se escribe texto en lugar de número.
- Rango `0–100` — rechaza valores fuera del rango permitido.

---

### 3. Cálculo del promedio

```python
promedio = sum(calificaciones.values()) / len(calificaciones)
```

- `sum()` suma todas las calificaciones del diccionario.
- `len()` divide entre el total de materias (7).

---

### 4. Formato del reporte

Se usa f-string con especificadores de alineación para que la tabla se vea ordenada:

```python
print(f"{materia:<30} {cal:>10.1f}  {estado}")
```

| Especificador | Significado |
|---|---|
| `:<30` | Alinea texto a la izquierda en 30 caracteres |
| `:>10.1f` | Alinea número a la derecha con 1 decimal en 10 caracteres |

---

### 5. Niveles de desempeño

```python
if promedio >= 90:    nivel = "Excelente 🏆"
elif promedio >= 80:  nivel = "Muy Bien 🎯"
elif promedio >= 70:  nivel = "Bien ✅"
elif promedio >= 60:  nivel = "Suficiente ⚠"
else:                 nivel = "Reprobado ✗"
```

| Rango | Nivel |
|-------|-------|
| 90 – 100 | Excelente |
| 80 – 89 | Muy Bien |
| 70 – 79 | Bien |
| 60 – 69 | Suficiente |
| 0 – 59 | Reprobado |

---

### 6. Resumen de materias reprobadas

```python
aprobadas = sum(1 for c in calificaciones.values() if c >= 60)
```

Usa comprensión de listas para contar cuántas materias tienen calificación mayor o igual a 60. Si hay reprobadas, las lista con su nombre y calificación.

---

## 🖥️ Ejemplo de salida

```
==================================================
   REGISTRO DE CALIFICACIONES - CARRERA TI
==================================================

Ingresa tu calificación para 'Computación en la Nube' (0-100): 85
Ingresa tu calificación para 'Sistemas Operativos' (0-100): 72
...

==================================================
         REPORTE DE CALIFICACIONES
==================================================
MATERIA                        CALIFICACIÓN
--------------------------------------------------
Computación en la Nube               85.0  ✓
Sistemas Operativos                  72.0  ✓
Bases de Datos                       90.0  ✓
Estructuras de Datos                 55.0  ✗
Metodologías Ágiles                  78.0  ✓
Desarrollo Full Stack                88.0  ✓
Gestión de Redes                     65.0  ✓
--------------------------------------------------
PROMEDIO GENERAL                     76.1
==================================================

Nivel de desempeño: Bien ✅
Materias aprobadas: 6/7

Materias a recuperar:
  - Estructuras de Datos: 55.0
==================================================
```

---

## 📁 Archivos del proyecto

```
📦 proyecto-calificaciones
 ┗ 📄 calificaciones.py   — script principal
 ┗ 📄 README.md           — este archivo
```

---

*Desarrollado con Python 3 · Carrera Tecnologías de la Información*
