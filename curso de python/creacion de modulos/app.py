import reporte

ventas_reporte = reporte.generar_informe_ventas('octubre', 100000)
informacion_gastos = reporte.generar_reporte_gastos('octubre', 5000000)

print(ventas_reporte)
print(informacion_gastos)