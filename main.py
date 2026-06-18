import logger_config
import logging
from servicios_especificos import *

logging.info("Iniciando aplicación de reservas")

# ======================================================
# PRUEBA RESERVA DE SALA
# ======================================================

try:
    logging.info("Creando ReservaSala: Sala Ejecutiva")
    sala1 = ReservaSala(
        "Sala Ejecutiva",
        100000,
        20,
        disponible=True,
        aire_acondicionado=True,
        internet=True,
        videobeam=True
    )

    print(sala1.descripcion())
    logging.info("ReservaSala validada exitosamente")

    sala1.validar_disponibilidad()

    # Desglose del costo
    costo_base = sala1.costo_por_hora * sala1.horas
    recargo_aire = costo_base * 0.10 if sala1.aire_acondicionado else 0
    recargo_internet = costo_base * 0.05 if sala1.internet else 0
    recargo_videobeam = costo_base * 0.15 if sala1.videobeam else 0
    costo_total = sala1.calcular_costo(0)
    
    print("✓ DESGLOSE DE COSTO:")
    print(f"  - Costo base: ${costo_base:,.0f} ({sala1.costo_por_hora} x {sala1.horas} horas)")
    print(f"  - Recargo aire acondicionado: ${recargo_aire:,.0f}")
    print(f"  - Recargo internet: ${recargo_internet:,.0f}")
    print(f"  - Recargo videobeam: ${recargo_videobeam:,.0f}")
    print(f"  - TOTAL: ${costo_total:,.0f}")
    
    logging.info(f"Costo base: {costo_base}, Aire AC: {recargo_aire}, Internet: {recargo_internet}, Videobeam: {recargo_videobeam}, Total: {costo_total}")

except Exception as e:

    logging.error(e)

    print("Error:", e)


print("\n========================\n")


# ======================================================
# PRUEBA ALQUILER EQUIPO
# ======================================================

try:

    equipo1 = AlquilerEquipo(
        "Video Beam Epson",
        50000,
        "Proyector",
        2
    )

    equipo1.validar_disponibilidad(5)

except Exception as e:

    logging.error(e)

    print("Error:", e)


print("\n========================\n")


# ======================================================
# PRUEBA ASESORIA
# ======================================================

try:

    asesoria1 = Asesoria(
        "Consultoría TI",
        80000,
        "Ciberseguridad",
        experto_certificado=True
    )

    asesoria1.validar_disponibilidad()

    print(asesoria1.descripcion())

    print(
        "Costo:",
        asesoria1.calcular_costo(6)
    )

except Exception as e:

    logging.error(e)

    print("Error:", e)
