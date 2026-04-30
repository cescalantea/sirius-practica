-- Simulando la base de datos inicial de Sirius
CREATE TABLE IF NOT EXISTS eventos_codigo_azul (
    id SERIAL PRIMARY KEY,
    tipo_paciente VARCHAR(50),
    ubicacion VARCHAR(100),
    estado VARCHAR(50),
    fecha_activacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Datos de prueba
INSERT INTO eventos_codigo_azul (tipo_paciente, ubicacion, estado)
VALUES 
    ('Adulto', 'Piso 2 - UTI', 'Atendido'),
    ('Adulto Mayor', 'Piso 1 - Emergencias', 'Cerrado'),
    ('Adulto', 'Piso 3 - Medicina', 'Activo');