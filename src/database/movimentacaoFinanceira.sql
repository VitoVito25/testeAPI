CREATE TABLE movimentacao_financeira (
    id SERIAL PRIMARY KEY,
    conta_id INT NOT NULL REFERENCES conta (id),
    categoria_movimentacao_financeira_id INT NOT NULL REFERENCES categoria_movimentacao_financeira (id),
    valor DECIMAL(15, 2) NOT NULL,
    descricao TEXT,
    beneficiario_origem_id INT REFERENCES pessoas (id),
    tipo_movimentacao VARCHAR(10) CHECK (tipo_movimentacao IN ('Entrada', 'Saída')) NOT NULL,
    data_movimentacao TIMESTAMP NOT NULL
);