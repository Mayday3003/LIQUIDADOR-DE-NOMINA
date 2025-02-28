JUAN JOSE CANO GIRALDO 
SIMON MUÑOZ MONTOYA 
PROYECTO


**Proyecto: Liquidador de Nómina**  

Se requiere una aplicación que calcule el total a pagar a un empleado que trabaja para una empresa, el cual corresponde a la diferencia entre los valores devengados y las deducciones de ley que le aplican.  



**Clasificación de los Casos de Prueba**  

**Normales**  

**Caso 1**  
**Descripción:**  
Un empleado con contrato a término indefinido recibe un salario fijo mensual sin horas extras ni deducciones adicionales fuera de las de ley.  

**Entradas:**  
- Salario base: $2.000.000  
- Horas extras: 0  
- Tarifa por hora extra: No aplica  
- Deducción por salud: 4% del salario base  
- Deducción por pensión: 4% del salario base  
- Otras deducciones: $0  

**Procedimiento:**  
1. **Calcular las deducciones:**  
   - Salud = 4% × $2.000.000 = $80.000  
   - Pensión = 4% × $2.000.000 = $80.000  
   - **Total deducciones** = $80.000 + $80.000 = $160.000  

2. **Calcular el total a pagar:**  
   - Total a pagar = Salario base - Total deducciones  
   - Total a pagar = $2.000.000 - $160.000 = $1.840.000  

**Salidas esperadas:**  
- **Total devengado:** $2.000.000  
- **Total deducciones:** $160.000  
- **Total a pagar:** $1.840.000  

---

**Caso 2**  
**Descripción:**  
Un empleado con salario fijo trabaja horas extra, lo que aumenta su devengado y su pago final.  

**Entradas:**  
- Salario base: $2.200.000  
- Horas extras: 10  
- Tarifa por hora extra: $15.000  
- Deducción por salud: 4% del salario base  
- Deducción por pensión: 4% del salario base  
- Otras deducciones: $0  

**Procedimiento:**  
1. **Calcular el valor de las horas extras:**  
   - Horas extras = 10 × $15.000 = $150.000  

2. **Calcular el salario total devengado:**  
   - Total devengado = Salario base + Horas extras  
   - Total devengado = $2.200.000 + $150.000 = $2.350.000  

3. **Calcular las deducciones:**  
   - Salud = 4% × $2.200.000 = $88.000  
   - Pensión = 4% × $2.200.000 = $88.000  
   - **Total deducciones** = $88.000 + $88.000 = $176.000  

4. **Calcular el total a pagar:**  
   - Total a pagar = Total devengado - Total deducciones  
   - Total a pagar = $2.350.000 - $176.000 = $2.174.000  

**Salidas esperadas:**  
- **Ingresos totales:** $2.350.000  
- **Total deducciones:** $176.000  
- **Total a pagar:** $2.174.000  

---

**Caso 3**  
**Descripción:**  
Un empleado con salario fijo trabaja horas extra durante el mes y tiene deducciones adicionales de un fondo de empleados.  

**Entradas:**  
- Salario base: $3.000.000  
- Horas extras trabajadas: 5  
- Tarifa por hora extra: $20.000  
- Deducción por salud: 4% del salario base  
- Deducción por pensión: 4% del salario base  
- Otras deducciones: $60.000  

**Procedimiento:**  
1. **Calcular el valor de las horas extras:**  
   - Horas extras = 5 × $20.000 = $100.000  

2. **Calcular el salario total devengado:**  
   - Ingresos totales = Salario base + Horas extras  
   - Ingresos totales = $3.000.000 + $100.000 = $3.100.000  

3. **Calcular las deducciones:**  
   - Salud = 4% × $3.000.000 = $120.000  
   - Pensión = 4% × $3.000.000 = $120.000  
   - **Total deducciones** = $120.000 + $120.000 + $60.000 = $300.000  

4. **Calcular el total a pagar:**  
   - Total a pagar = Total devengado - Total deducciones  
   - Total a pagar = $3.100.000 - $300.000 = $2.800.000  

**Salidas esperadas:**  
- **Ingresos totales:** $3.100.000  
- **Total deducciones:** $300.000  
- **Total a pagar:** $2.800.000  

---

**Extraordinarios**  

**Caso 4**  
**Descripción:**  
Un empleado con salario mínimo ha trabajado muchas horas extras, lo que incrementa significativamente sus ingresos.  

**Entradas:**  
- Salario base: $1.423.500  
- Horas extras trabajadas: 80 horas  
- Valor de la hora extra: $12.000  
- Deducción por salud: 4% del total devengado  
- Deducción por pensión: 4% del total devengado  

**Procedimiento para el cálculo:**  
1. **Cálculo del total devengado:**  
   - Salario base: $1.423.500  
   - Pago por horas extras: 80 × $12.000 = $960.000  
   - Ingresos totales = $1.423.500 + $960.000 = $2.383.500  

2. **Cálculo de las deducciones:**  
   - Salud: 4% × $2.383.500 = $95.340  
   - Pensión: 4% × $2.383.500 = $95.340  

3. **Cálculo del total a pagar:**  
   - Total a pagar = $2.383.500 - ($95.340 + $95.340)  
   - Total a pagar = $2.192.820  

**Salidas esperadas:**  
- **Ingresos totales:** $2.383.500  
- **Deducción de salud:** $95.340  
- **Deducción de pensión:** $95.340  
- **Total a pagar:** $2.192.820  

---

**Errores**  

**Caso 7**  
**Descripción:**  
Un usuario intenta ingresar un salario base negativo, lo cual es un valor inválido para el cálculo de la nómina.  

**Entradas:**  
- Salario base mensual: -$2.000.000  

**Procedimiento:**  
- Si el salario base es menor que $0, lanzar una excepción.  

**Salida esperada:**  
- **Error:** "El salario base no puede ser un valor negativo."  

---

**Caso 9**  
**Descripción:**  
Un trabajador registra horas extras excesivas, superando los límites establecidos por la ley laboral en Colombia.  

**Entradas:**  
- Salario base mensual: $2.500.000  
- Horas extras trabajadas: 150 (cuando el límite mensual es 80)  

**Procedimiento:**  
- Si las horas extras superan 80 horas al mes, lanzar una excepción.  

**Salida esperada:**  
- **Error:** "No se pueden registrar más de 80 horas extras en un mes según la legislación laboral."

  ---

  **Caso 10**
**Descripción:**
Un trabajador no tiene afiliación a salud o pensión, lo que impide realizar las deducciones obligatorias.

**Entradas:**
Salario base mensual: $3.000.000
Deducción por salud: 0% (sin afiliación)
Deducción por pensión: 0% (sin afiliación)

**Procedimiento:**
Verificar que el empleado tenga afiliación a salud y pensión.
Si no tiene afiliación, lanzar una excepción.


Salida esperada:
Error: "El trabajador debe estar afiliado a salud y pensión para calcular la nómina."
Ejecución interrumpida.
