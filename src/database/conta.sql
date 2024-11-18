CREATE TABLE conta (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    descricao TEXT,
    saldo_inicial DECIMAL(15, 2) DEFAULT 0.00 NOT NULL,
    empresa_id INT NOT NULL REFERENCES empresa (id),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_modificacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);