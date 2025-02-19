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

Caso 4

Descripción:

Un empleado con salario mínimo ha trabajado muchas horas extras, lo que incrementa significativamente sus ingresos.
Entradas:

Salario base: $1.423.500 (salario mínimo actualizado)

Horas extras trabajadas: 80 horas

Valor de la hora extra: $12.000

Deducción por salud (4% del total devengado)

Deducción por pensión (4% del total devengado)

Procedimiento para el cálculo:

Cálculo del total devengado:

Salario base: $1.423.500

Pago por horas extras: 80 × $12.000 = $960.000

Ingresos totales = $1.423.500 + $960.000 = $2.383.500

Cálculo de las deducciones:

Salud: 4% × $2.383.500 = $95.340

Pensión: 4% × $2.383.500 = $95.340

Cálculo del total a pagar: $2.383.500 - ($95.340 + $95.340) = $2.192.820

Salidas esperadas:

Ingresos totales: $2.383.500

Deducción de salud: $95.340

Deducción de pensión: $95.340

Total, a pagar: $2.192.820

Caso 5

Descripción:

El empleado tomó una licencia no remunerada de todo el mes, por lo que no genera ingresos en este período.
Entradas:

Salario base: $3.000.000

Días trabajados en el mes: 0

Deducciones de ley: Salud y pensión siguen aplicando si el contrato lo exige.

Procedimiento para el cálculo:

Cálculo del total devengado:

Como el empleado no trabajó, su salario devengado es $0.

Cálculo de las deducciones:
Si el contrato exige que el empleado siga pagando salud y pensión, se calculan sobre el salario base:

Salud: 4% × $3.000.000 = $120.000

Pensión: 4% × $3.000.000 = $120.000

Cálculo del total a pagar:

$0 - ($120.000 + $120.000) = -$240.000

Salidas esperadas:

Ingresos totales: $0

Deducción de salud: $120.000

Deducción de pensión: $120.000

Total, a pagar: -$240.000 (deuda con la empresa, debe compensarlo en el futuro o pagar por su cuenta)

Caso 6 

Descripción:

El empleado tiene un salario tan alto que se le debe descontar retención en la fuente, además de las deducciones de ley.
Entradas:

Salario base: $15.000.000

Retención en la fuente: 10% (aplicable a salarios altos según la legislación fiscal)
Deducciones de ley: Salud y pensión.

Procedimiento para el cálculo:

Cálculo del total devengado:

Salario base: $15.000.000

Cálculo de las deducciones:

Salud: 4% × $15.000.000 = $600.000

Pensión: 4% × $15.000.000 = $600.000

Retención en la fuente: 10% × $15.000.000 = $1.500.000

Cálculo del total a pagar:

$15.000.000 - ($600.000 + $600.000 + $1.500.000) = $12.300.000
Salidas esperadas:

Ingresos totales: $15.000.000

Deducción de salud: $600.000

Deducción de pensión: $600.000

Retención en la fuente: $1.500.000

Total, a pagar: $12.300.000

Error 
Caso 7
Descripción:
Un usuario intenta ingresar un salario base negativo, lo cual es un valor inválido para el cálculo de la nómina.
Entradas:

Salario base mensual: -$2.000.000

Deducción por salud: 4%

Deducción por pensión: 4%

Procedimiento:

Verificación inicial:

Si el salario base es menor que $0, lanzar una excepción indicando que el salario no puede ser negativo.
Salida esperada:

Error: "El salario base no puede ser un valor negativo."
Ejecución interrumpida.

Caso 8 
Descripción:

Un usuario ingresa un porcentaje de deducción mayor al 100%, lo cual es un error ya que las deducciones de ley no pueden superar el total del salario.
Entradas:

Salario base mensual: $3.000.000

Deducción por salud: 110%

Deducción por pensión: 4%

Procedimiento:

Verificación inicial:
Si cualquier porcentaje de deducción es mayor al 100%, lanzar una excepción.

Salida esperada:

Error: "El porcentaje de deducción no puede ser mayor al 100% del salario."
Ejecución interrumpida.

Caso 9

Descripción:

Un trabajador registra horas extras excesivas, superando los límites establecidos por la ley laboral en Colombia.
Entradas:

Salario base mensual: $2.500.000

Horas extras trabajadas: 150 (cuando el límite mensual es 80)

Tarifa por hora extra: $15.000

Procedimiento:

Verificar que el número de horas extras no exceda el máximo legal permitido.
Si las horas extras superan 80 horas al mes, lanzar una excepción.

Salida esperada:
Error: "No se pueden registrar más de 80 horas extras en un mes según la legislación laboral."
Ejecución interrumpida.

Caso 10

Descripción:

Un trabajador no tiene afiliación a salud o pensión, lo que impide realizar las deducciones obligatorias.
Entradas:

Salario base mensual: $3.000.000

Deducción por salud: 0% (sin afiliación)

Deducción por pensión: 0% (sin afiliación)

Procedimiento:

Verificar que el empleado tenga afiliación a salud y pensión.
Si no tiene afiliación, lanzar una excepción.


Salida esperada:

Error: "El trabajador debe estar afiliado a salud y pensión para calcular la nómina."
Ejecución interrumpida.




