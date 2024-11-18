CREATE TABLE usuario_empresa (
    id SERIAL PRIMARY KEY,
    usuario_id INT NOT NULL REFERENCES usuario (id),
    empresa_id INT NOT NULL REFERENCES empresa (id),
    permissao VARCHAR(50) NOT NULL,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_modificacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);