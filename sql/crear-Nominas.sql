CREATE TABLE nominas (
    id SERIAL PRIMARY KEY,
    empleado_id INTEGER REFERENCES empleados(id),
    horas_extras INTEGER DEFAULT 0,
    tarifa_hora_extra NUMERIC(10, 2) DEFAULT 0,
    otras_deducciones NUMERIC(10, 2) DEFAULT 0,
    deduccion_salud NUMERIC(10, 2),
    deduccion_pension NUMERIC(10, 2),
    total_deducciones NUMERIC(12, 2),
    total_devengado NUMERIC(12, 2),
    total_a_pagar NUMERIC(12, 2)
);