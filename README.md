Liquidador de Nómina
Descripción del Proyecto
El Liquidador de Nómina es una aplicación diseñada para calcular el salario neto de un empleado, teniendo en cuenta los ingresos y deducciones de ley aplicables. Su objetivo es proporcionar un cálculo preciso, automatizado y conforme a la normatividad vigente, facilitando la gestión de nómina en empresas de cualquier tamaño.

Características Principales
Cálculo automático del salario neto con base en el salario base, horas extras, bonificaciones y otros ingresos.
Aplicación de deducciones legales, como aportes a seguridad social, fondo de solidaridad pensional y retención en la fuente.
Manejo de casos especiales, como descuentos por préstamos, embargos judiciales o aportes voluntarios.
Validación de datos de entrada, garantizando que la información ingresada sea correcta y evitando errores en la liquidación.
Interfaz intuitiva, que permite el uso fácil y accesible para los usuarios sin conocimientos técnicos avanzados.

Clasificación de los Casos de prueba
Normales

Caso 1 
Descripción:
Un empleado con contrato a término indefinido recibe un salario fijo mensual sin horas extras ni deducciones adicionales fuera de las de ley.

Entradas:
Salario base: $2.000.000
Horas extras: 0
Tarifa por hora extra: No aplica
Deducción por salud: 4% del salario base
Deducción por pensión: 4% del salario base
Otras deducciones: $0
Procedimiento:

Calcular las deducciones:
Salud = 4% × $2.000.000 = $80.000
Pensión = 4% × $2.000.000 = $80.000
Total, deducciones = $80.000 + $80.000 = $160.000

Calcular el total a pagar:
Total, a pagar = Salario base - Total deducciones
Total, a pagar = $2.000.000 - $160.000 = $1.840.000
Salidas esperadas:
Total, devengado: $2.000.000
Total, deducciones: $160.000
Total, a pagar: $1.840.000

Caso 2
Descripción:
Un empleado con salario fijo trabaja horas extra, lo que aumenta su devengado y su pago final.

Entradas:
Salario base: $2.200.000 (antes era $1.800.000)
Horas extras: 10
Tarifa por hora extra: $15.000
Deducción por salud: 4% del salario base
Deducción por pensión: 4% del salario base
Otras deducciones: $0

Procedimiento:
Calcular el valor de las horas extras:
Horas extras = 10 × $15.000 = $150.000
Calcular el salario total devengado:
Total, devengado = Salario base + Horas extras
Total, devengado = $2.200.000 + $150.000 = $2.350.000
Calcular las deducciones:
Salud = 4% × $2.200.000 = $88.000
Pensión = 4% × $2.200.000 = $88.000
Total, deducciones = $88.000 + $88.000 = $176.000
Calcular el total a pagar:
Total, a pagar = Total devengado - Total deducciones
Total, a pagar = $2.350.000 - $176.000 = $2.174.000
Salidas esperadas:
Ingresos totales: $2.350.000
Total, deducciones: $176.000
Total, a pagar: $2.174.000

Caso 3 
Descripción:
Un empleado con salario fijo trabaja horas extra durante el mes y tiene deducciones adicionales de un fondo de empleados.
Entradas:
Salario base: $3.000.000
Horas extras trabajadas: 5
Tarifa por hora extra: $20.000
Deducción por salud: 4% del salario base
Deducción por pensión: 4% del salario base
Otras deducciones: 60.000 del salario base

Procedimiento:
Calcular el valor de las horas extras:
Horas extras = 5 × $20.000 = $100.000
Calcular el salario total devengado:
Ingresos totales = Salario base + Horas extras
Ingresos totales = $3.000.000 + $100.000 = $3.100.000

Calcular las deducciones:
Salud = 4% × $3.000.000 = $120.000
Pensión = 4% × $3.000.000 = $120.000
Total, deducciones = $120.000 + $120.000 + $60.000 = $300.000

Calcular el total a pagar:
Total, a pagar = Total devengado - Total deducciones
Total, a pagar = $3.100.000 - $300.000 = $2.800.000

Salidas esperadas:
Ingresos totales: $3.100.000
Total, deducciones: $300.000
Total, a pagar: $2.800.000
