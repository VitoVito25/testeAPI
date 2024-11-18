CREATE TABLE categoria_movimentacao_financeira (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    tipo VARCHAR(10) CHECK (tipo IN ('Entrada', 'Saída')) NOT NULL,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_modificacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);