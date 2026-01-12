-- Estrutura de Banco de Dados PostgreSQL
CREATE TABLE entregas (
    id_entrega SERIAL PRIMARY KEY,
    endereco VARCHAR(255),
    status VARCHAR(20) DEFAULT 'pendente'
);

-- Simulação de atualização de baixa no sistema
UPDATE entregas SET status = 'concluido' WHERE id_entrega = 1;
