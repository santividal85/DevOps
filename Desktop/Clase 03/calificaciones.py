materias = [
    "Computación en la Nube",
    "Sistemas Operativos",
    "Bases de Datos",
    "Estructuras de Datos",
    "Metodologías Ágiles",
    "Desarrollo Full Stack",
    "Gestión de Redes"
]

calificaciones = {}

print("=" * 50)
print("   REGISTRO DE CALIFICACIONES - CARRERA TI")
print("=" * 50)

for materia in materias:
    while True:
        try:
            cal = float(input(f"\nIngresa tu calificación para '{materia}' (0-100): "))
            if 0 <= cal <= 100:
                calificaciones[materia] = cal
                break
            else:
                print("  ⚠ Por favor ingresa un valor entre 0 y 100.")
        except ValueError:
            print("  ⚠ Valor inválido. Ingresa un número.")

promedio = sum(calificaciones.values()) / len(calificaciones)

print("\n")
print("=" * 50)
print("         REPORTE DE CALIFICACIONES")
print("=" * 50)
print(f"{'MATERIA':<30} {'CALIFICACIÓN':>12}")
print("-" * 50)

for materia, cal in calificaciones.items():
    estado = "✓" if cal >= 60 else "✗"
    print(f"{materia:<30} {cal:>10.1f}  {estado}")

print("-" * 50)
print(f"{'PROMEDIO GENERAL':<30} {promedio:>10.1f}")
print("=" * 50)

if promedio >= 90:
    nivel = "Excelente 🏆"
elif promedio >= 80:
    nivel = "Muy Bien 🎯"
elif promedio >= 70:
    nivel = "Bien ✅"
elif promedio >= 60:
    nivel = "Suficiente ⚠"
else:
    nivel = "Reprobado ✗"

print(f"\nNivel de desempeño: {nivel}")

aprobadas = sum(1 for c in calificaciones.values() if c >= 60)
reprobadas = len(calificaciones) - aprobadas
print(f"Materias aprobadas: {aprobadas}/{len(calificaciones)}")
if reprobadas > 0:
    print(f"Materias reprobadas: {reprobadas}")
    print("\nMaterias a recuperar:")
    for mat, cal in calificaciones.items():
        if cal < 60:
            print(f"  - {mat}: {cal:.1f}")

print("\n" + "=" * 50)
