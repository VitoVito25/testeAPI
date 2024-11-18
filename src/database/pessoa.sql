CREATE TABLE pessoas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf_cnpj VARCHAR(18) UNIQUE,
    categoria_pessoa_id INT NOT NULL REFERENCES categoria_pessoa (id),
    cep VARCHAR(10),
    endereco_rua VARCHAR(100),
    endereco_numero VARCHAR(10),
    endereco_bairro VARCHAR(50),
    endereco_cidade VARCHAR(50),
    endereco_estado VARCHAR(2),
    email VARCHAR(100),
    celular VARCHAR(15),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_modificacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);