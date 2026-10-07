# =====================================================================
# SUAS RESPOSTAS
# =====================================================================
# Escreva cada consulta SQL entre as aspas triplas, assim:
#
#   Q1 = """
#   SELECT ...
#   FROM ...
#   """
#
# Depois salve o arquivo (Ctrl+S) e veja o resultado no painel.
# Mexa só no que está ENTRE as aspas triplas.
# =====================================================================

# ---------------------------------------------------------------------
# NÍVEL 1 - AQUECIMENTO
# ---------------------------------------------------------------------

# Q1. Clientes no Centro
# Colunas do resultado: ClientesNoCentro
Q1 = """
SELECT COUNT(IdCliente) as Qtd_Clientes
From Clientes
where Bairro = 'Centro';
"""

# Q2. Hambúrgueres acima de R$ 30
# Colunas do resultado: NomeProduto, Preco
Q2 = """
SELECT 
NomeProduto,
Preco
From Produtos
WHERE Preco > 30.00
ORDER BY Preco desc;
"""

# Q3. Pedidos por status
# Colunas do resultado: Status, QuantidadePedidos
Q3 = """
SELECT
Status,
count(*) as Quantidade_Pedidos
FROM Pedidos
GROUP BY Status;
"""

# Q4. Nota média e pedidos sem avaliação
# Colunas do resultado: PedidosEntregues, PedidosAvaliados, PedidosSemAvaliacao, NotaMedia
Q4 = """
SELECT
COUNT (*) AS Pedidos_Entregues,
COUNT(CASE WHEN Avaliacao IS NOT NULL THEN 1 END) AS Entregas_Avaliadas,
COUNT(CASE WHEN Avaliacao IS NULL THEN 1 END) AS Entregas_Nao_Avaliadas,
AVG(CAST(Avaliacao AS DECIMAL(4,2)))
FROM Pedidos
WHERE Status = 'Entregue';
"""

# Q5. Delivery x Retirada por mês
# Colunas do resultado: Mes, TipoEntrega, QuantidadePedidos
Q5 = """
SELECT 
MONTH(DataPedido) AS Mes,
COUNT(CASE WHEN TipoEntrega = 'Delivery' THEN 1 END) AS Pedidos_Delivery,
COUNT(CASE WHEN TipoEntrega = 'Retirada' THEN 1 END) AS Pedidos_Retirada
FROM Pedidos
Group by MONTH(DataPedido)
Order by month(DataPedido);
"""

# ---------------------------------------------------------------------
# NÍVEL 2 - CRUZANDO TABELAS
# ---------------------------------------------------------------------

# Q6. Pedidos de janeiro com cliente
# Colunas do resultado: IdPedido, DataPedido, Nome, Bairro, Status
Q6 = """
SELECT
  P.IdPedido,
  P.DataPedido,
  C.Nome,
  C.Bairro,
  P.Status
from Pedidos as P
inner join Clientes as C
  on P.IdCliente = C.IdCliente
where P.DataPedido >= '2026-01-01'
AND P.DataPedido < '2026-02-01'
ORDER BY P.DataPedido;
"""

# Q7. Entregas por entregador
# Colunas do resultado: Nome, Entregas
Q7 = """
SELECT
e.IdEntregador,
e.Nome,
COUNT(p.IdPedido) as total_entregas
FROM Entregadores as e
INNER JOIN Pedidos as p
ON e.IdEntregador = p.IdEntregador
WHERE p.Status = 'Entregue'
GROUP BY e.IdEntregador, e.Nome
order by total_entregas DESC;
"""

# Q8. Unidades e faturamento por produto
# Colunas do resultado: NomeProduto, UnidadesVendidas, Faturamento
Q8 = """
SELECT 
P.NomeProduto,
SUM(I.Quantidade) AS Quantidade_Vendida,
SUM(I.Quantidade * I.PrecoUnitario) as Faturamento_Total
FROM ItensPedido AS I
INNER JOIN Produtos AS P
ON P.IdProduto = I.IdProduto
GROUP BY P.NomeProduto
ORDER BY Quantidade_Vendida DESC;
"""

# Q9. Faturamento por categoria
# Colunas do resultado: Categoria, Faturamento
Q9 = """
SELECT
P.Categoria,
SUM(I.Quantidade) as Quantidade_Vendida,
SUM(I.Quantidade * I.PrecoUnitario) as Faturamento_Total
FROM ItensPedido as I
INNER JOIN Produtos as P
ON P.IdProduto = I.IdProduto
GROUP BY P.Categoria
ORDER BY Faturamento_Total DESC;
"""

# Q10. Bairros com 7+ pedidos entregues
# Colunas do resultado: Bairro, PedidosEntregues
Q10 = """
SELECT
C.Bairro,
COUNT(P.IdPedido) as Total_Pedidos_Entregues
FROM Clientes as C
INNER JOIN Pedidos as P
ON C.IdCliente = P.IdCliente
WHERE P.Status = 'Entregue'
GROUP BY C.Bairro
HAVING count(P.IdPedido) >=7
ORDER BY Total_Pedidos_Entregues DESC;
"""

# Q11. Preços praticados do X-Bacon
# Colunas do resultado: PrecoUnitario, Unidades, Faturamento
Q11 = """
SELECT
P.NomeProduto,
I.PrecoUnitario,
SUM(I.Quantidade) as Unidades_Vendida_Preco,
SUM(I.Quantidade * I.PrecoUnitario) AS Faturamento_Por_Preco,
COUNT(I.IdPedido) AS Qtd_Pedidos
FROM ItensPedido AS I
JOIN Produtos as P
ON I.IdProduto = P.IdProduto
WHERE I.IdProduto = 2
GROUP BY P.NomeProduto, I.PrecoUnitario
ORDER BY I.PrecoUnitario;
"""

# ---------------------------------------------------------------------
# NÍVEL 3 - DESAFIO
# ---------------------------------------------------------------------

# Q12. Top 3 clientes (fidelidade)
# Colunas do resultado: Nome, Pedidos, TotalGasto
Q12 = """
SELECT TOP 3
C.Nome,
COUNT(DISTINCT P.IdPedido) AS Qtd_Pedidos,
SUM(I.Quantidade * I.PrecoUnitario) AS Total_Gasto
FROM Clientes AS C
JOIN Pedidos AS P
ON C.IdCliente = P.IdCliente
JOIN ItensPedido AS I
ON P.IdPedido = I.IdPedido
GROUP BY C.IdCliente, C.Nome
ORDER BY Total_Gasto DESC;
"""

# Q13. Faturamento mês a mês
# Colunas do resultado: Mes, PedidosEntregues, Faturamento
Q13 = """
SELECT
DATENAME(MONTH, P.DataPedido) AS Nome_Mes,
COUNT(DISTINCT P.IdPedido) AS Qtd_Pedidos_Entregues,
SUM(I.Quantidade * I.PrecoUnitario) AS Faturamento_Total
FROM Pedidos as P
JOIN ItensPedido AS I
ON P.IdPedido = I.IdPedido
GROUP BY DATENAME(MONTH, P.DataPedido)
ORDER BY Faturamento_Total DESC
"""

# Q14. Entregador do trimestre
# Colunas do resultado: Nome, Entregas, NotaMedia
Q14 = """
SELECT
E.Nome,
COUNT(P.IdPedido) AS Total_Entregas,
ROUND(AVG(P.Avaliacao), 2) AS Media_Nota
FROM Entregadores E
JOIN Pedidos P
ON E.IdEntregador =P.IdEntregador
GROUP BY E.IdEntregador, E.Nome
HAVING COUNT(P.IdPedido) >=4 AND AVG(P.Avaliacao) >=4
ORDER BY Media_Nota DESC;
"""

# Q15. Valor total dos pedidos de março
# Colunas do resultado: IdPedido, Nome, ValorProdutos, TaxaEntrega, ValorTotal
Q15 = """
SELECT
C.Nome,
P.IdPedido,
P.DataPedido,
SUM(I.Quantidade * I.PrecoUnitario + P.TaxaEntrega) AS Faturamento_Total
FROM Pedidos AS P
JOIN ItensPedido AS I
ON P.IdPedido = I.IdPedido
JOIN Clientes AS C
ON C.IdCliente = P.IdCliente
WHERE MONTH(P.DataPedido) = 3
GROUP BY C.Nome, P.IdPedido, P.DataPedido
ORDER BY Faturamento_Total DESC;
"""

# Q16. Clientes sem nenhum pedido
# Colunas do resultado: Nome, Bairro, DataCadastro
Q16 = """
SELECT
C.IdCliente,
C.Nome,
C.Bairro
FROM Clientes AS C
LEFT JOIN Pedidos AS P
ON C.IdCliente = P.IdCliente
WHERE P.IdCliente IS NULL
"""

# Q17. Produto que nunca foi vendido
# Colunas do resultado: NomeProduto, Categoria, Preco
Q17 = """
SELECT 
IdProduto,
NomeProduto
FROM Produtos as P
WHERE NOT EXISTS (SELECT 1
FROM ItensPedido as I
WHERE I.IdProduto = P.IdProduto);
"""