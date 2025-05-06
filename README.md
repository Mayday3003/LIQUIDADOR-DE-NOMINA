Autores 
Juan jose cano giraldo
Simon muñoz lopez

Entrega 3:
Juan Fernando Castañeda Agudelo--
Maria Isabel Zuluaga

PROYECTO

¿Qué es?

El proyecto es una aplicación para la liquidación de nómina que permite calcular de manera automática el pago de empleados, considerando factores como horas trabajadas, salario base y deducciones. Facilita la gestión de pagos y ayuda a reducir errores en los cálculos.

✅ Propósito:

Automatizar el cálculo de nómina.
Generar reportes precisos de los pagos realizados.
Validar datos mediante pruebas unitarias para asegurar la fiabilidad del cálculo.
¿Para qué es?

El objetivo es garantizar que el cálculo del salario neto sea preciso, rápido y conforme a las normativas laborales. La aplicación permitirá a las empresas:
✅ Automatizar el proceso de liquidación de nómina.
✅ Reducir errores humanos en los cálculos.
✅ Generar reportes detallados de los pagos realizados.
✅ Facilitar la gestión de pagos a empleados.

✅ Prerrequisitos
Antes de ejecutar el proyecto, asegúrate de tener instalados los siguientes componentes:

Python 3.10 o superior

▶️ Ejecución de la interfaz por consola
Hay dos formas de ejecutar la aplicación desde la consola:

1.Desde la terminal

-Abre una terminal y Navega hasta el directorio raíz del proyecto:

<img width="688" alt="image" src="https://github.com/user-attachments/assets/0c62d875-92ce-45cb-8207-5888c4b144bf" />

-Ejecuta el archivo consola.py con el siguiente comando:

<img width="677" alt="image" src="https://github.com/user-attachments/assets/d6d18456-19f4-4b47-a167-4af3e196a108" />

2.Desde el archivo directamente

-Abre el archivo consola.py desde un editor de texto o IDE (como VSCode o PyCharm).

-En la parte superior de la ventana, haz clic en "Run" o "Ejecutar".

-También puedes hacer clic derecho en el archivo y seleccionar "Ejecutar archivo Python".

🧪 Ejecución de las pruebas

Hay dos formas de ejecutar las pruebas unitarias para verificar que el código funciona correctamente:

1.Desde la terminal

Abre una terminal y ejecuta el siguiente comando desde el directorio raíz:

<img width="679" alt="image" src="https://github.com/user-attachments/assets/b6e539be-5712-41b9-ace0-2520635653df" />

2.Desde el archivo directamente

-Abre el archivo test_nom.py desde un editor de texto o IDE.

-En la parte superior de la ventana, haz clic en "Run" o "Ejecutar".

-También puedes hacer clic derecho en el archivo y seleccionar "Ejecutar archivo Python".

✅ Consejo:
Si tienes problemas para importar módulos al ejecutar los archivos, añade esta línea al principio de consola.py y test_nom.py:

<img width="676" alt="image" src="https://github.com/user-attachments/assets/aab2e442-63a2-4eeb-8df6-8b1a84785d5a" />

Estructura sugerida 

<img width="545" alt="image" src="https://github.com/user-attachments/assets/c3aadfd8-fba8-46c5-b70f-e3de275693cf" />

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

  ---

 **Cómo ejecutar la interfaz gráfica (GUI)**
**Requisitos previos**
Antes de ejecutar la aplicación, asegúrate de tener instalado Python y los siguientes módulos:


pip install kivy
 Si estás usando un archivo requirements.txt, también puedes instalar todo con:


pip install -r requirements.txt

 **Ejecutar la GUI**

Abre una terminal en la raíz del proyecto.

Asegúrate de tener el archivo main.py (o el nombre del archivo que contiene el código GUI).

Ejecuta el siguiente comando:


python main.py