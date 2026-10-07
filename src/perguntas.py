"""As 17 perguntas da Dona Marta: textos, colunas e tipo de gráfico.



Os alunos não precisam mexer aqui. As respostas ficam em src/respostas.py.

"""

from src import respostas



NIVEIS = {

  1: ("Nível 1 - Aquecimento", "Uma tabela só: WHERE, COUNT, AVG, GROUP BY."),

  2: ("Nível 2 - Cruzando tabelas", "JOIN com 2 e 3 tabelas, WHERE, GROUP BY e HAVING."),

  3: ("Nível 3 - Desafio", "Tudo junto: COUNT(DISTINCT), TOP, HAVING duplo e LEFT JOIN."),

}



PERGUNTAS = [

  # ----- Nível 1 - Aquecimento -----

  {

   "numero": 1,

   "nivel": 1,

   "titulo": "Clientes no Centro",

   "enunciado": "A Dona Marta quer saber quantos clientes cadastrados moram no bairro **Centro**.",

   "colunas_esperadas": ["ClientesNoCentro"],

   "visual": {"tipo": "metricas"},

   "conceitos": ["WHERE", "COUNT"],

   "dica": "`COUNT(*)` com `WHERE`.",

   "moeda": [],

  },

  {

   "numero": 2,

   "nivel": 1,

   "titulo": "Hambúrgueres acima de R$ 30",

   "enunciado": "Liste o **nome e o preço** dos produtos da categoria **Hambúrguer** que custam **mais de R$ 30,00**, do mais caro para o mais barato.",

   "colunas_esperadas": ["NomeProduto", "Preco"],

   "visual": {"tipo": "barra", "x": "NomeProduto", "y": "Preco", "horizontal": True},

   "conceitos": ["WHERE", "AND", "ORDER BY"],

   "dica": "Duas condições no `WHERE`, ligadas por `AND`. Atenção: \"mais de 30\" é `>` e não `>=`.",

   "moeda": ["Preco"],

  },

  {

   "numero": 3,

   "nivel": 1,

   "titulo": "Pedidos por status",

   "enunciado": "Quantos pedidos foram **entregues** e quantos foram **cancelados** no trimestre? Mostre as duas contagens numa consulta só.",

   "colunas_esperadas": ["Status", "QuantidadePedidos"],

   "visual": {"tipo": "barra", "x": "Status", "y": "QuantidadePedidos"},

   "conceitos": ["GROUP BY", "COUNT"],

   "dica": "Agrupe pela coluna `Status`.",

   "moeda": [],

  },

  {

   "numero": 4,

   "nivel": 1,

   "titulo": "Nota média e pedidos sem avaliação",

   "enunciado": "Considerando só os pedidos **entregues**: quantos foram, quantos receberam avaliação, quantos ficaram **sem avaliação** e qual a **nota média** (com casas decimais)?",

   "colunas_esperadas": ["PedidosEntregues", "PedidosAvaliados", "PedidosSemAvaliacao", "NotaMedia"],

   "visual": {"tipo": "metricas"},

   "conceitos": ["COUNT(*) x COUNT(coluna)", "AVG", "CAST", "NULL"],

   "dica": "`COUNT(*)` conta linhas; `COUNT(coluna)` ignora os `NULL`. E, no SQL Server, `AVG` de uma coluna inteira devolve um número inteiro: converta com `CAST(Avaliacao AS DECIMAL(4,2))`.",

   "moeda": [],

  },

  {

   "numero": 5,

   "nivel": 1,

   "titulo": "Delivery x Retirada por mês",

   "enunciado": "A Dona Marta acha que o delivery está crescendo. Mostre, **mês a mês**, quantos pedidos **entregues** foram de **Delivery** e quantos de **Retirada**.",

   "colunas_esperadas": ["Mes", "TipoEntrega", "QuantidadePedidos"],

   "visual": {"tipo": "barra_agrupada", "x": "Mes", "y": "QuantidadePedidos", "grupo": "TipoEntrega"},

   "conceitos": ["MONTH", "GROUP BY com 2 colunas"],

   "dica": "`MONTH(DataPedido)` devolve o número do mês. Agrupe por duas colunas: o mês e o `TipoEntrega`.",

   "moeda": [],

  },

  # ----- Nível 2 - Cruzando tabelas -----

  {

   "numero": 6,

   "nivel": 2,

   "titulo": "Pedidos de janeiro com cliente",

   "enunciado": "Liste todos os pedidos de **janeiro de 2026** com número do pedido, data, **nome do cliente**, bairro e status, em ordem de data.",

   "colunas_esperadas": ["IdPedido", "DataPedido", "Nome", "Bairro", "Status"],

   "visual": {"tipo": "tabela"},

   "conceitos": ["INNER JOIN", "BETWEEN"],

   "dica": "Primeiro JOIN: `Pedidos` com `Clientes` pela coluna `IdCliente`. Filtre a data com `BETWEEN`.",

   "moeda": [],

  },

  {

   "numero": 7,

   "nivel": 2,

   "titulo": "Entregas por entregador",

   "enunciado": "Para escolher o entregador do trimestre, a Dona Marta quer ver **quantas entregas cada entregador fez** (só pedidos entregues), de quem mais entregou para quem menos entregou.",

   "colunas_esperadas": ["Nome", "Entregas"],

   "visual": {"tipo": "barra", "x": "Nome", "y": "Entregas", "horizontal": True},

   "conceitos": ["INNER JOIN", "GROUP BY", "ORDER BY"],

   "dica": "JOIN entre `Pedidos` e `Entregadores`. Os pedidos de retirada têm `IdEntregador` NULL: o que o `INNER JOIN` faz com eles?",

   "moeda": [],

  },

  {

   "numero": 8,

   "nivel": 2,

   "titulo": "Unidades e faturamento por produto",

   "enunciado": "Quantas **unidades** de cada produto foram vendidas e quanto cada um **faturou** (só pedidos entregues)? Ordene pelas unidades. O campeão em unidades é também o campeão em faturamento?",

   "colunas_esperadas": ["NomeProduto", "UnidadesVendidas", "Faturamento"],

   "visual": {"tipo": "barras_duplas", "x": "NomeProduto", "y1": "UnidadesVendidas", "y2": "Faturamento"},

   "conceitos": ["JOIN com 3 tabelas", "SUM", "Quantidade x PrecoUnitario"],

   "dica": "São 3 tabelas: `ItensPedido`, `Produtos` e `Pedidos`. Faturamento = `SUM(Quantidade * PrecoUnitario)`, usando o preço de `ItensPedido`.",

   "moeda": ["Faturamento"],

  },

  {

   "numero": 9,

   "nivel": 2,

   "titulo": "Faturamento por categoria",

   "enunciado": "Qual o **faturamento de produtos por categoria** (só pedidos entregues), da maior para a menor?",

   "colunas_esperadas": ["Categoria", "Faturamento"],

   "visual": {"tipo": "barra", "x": "Categoria", "y": "Faturamento"},

   "conceitos": ["JOIN com 3 tabelas", "GROUP BY", "SUM"],

   "dica": "Mesmo JOIN da questão anterior, agrupando por `Categoria`.",

   "moeda": ["Faturamento"],

  },

  {

   "numero": 10,

   "nivel": 2,

   "titulo": "Bairros com 7+ pedidos entregues",

   "enunciado": "Em quais **bairros** houve **pelo menos 7 pedidos entregues**? Mostre o bairro e a quantidade.",

   "colunas_esperadas": ["Bairro", "PedidosEntregues"],

   "visual": {"tipo": "barra", "x": "Bairro", "y": "PedidosEntregues"},

   "conceitos": ["JOIN", "WHERE x HAVING"],

   "dica": "O bairro está em `Clientes`, o status em `Pedidos`. `WHERE` filtra antes de agrupar; `HAVING` filtra depois.",

   "moeda": [],

  },

  {

   "numero": 11,

   "nivel": 2,

   "titulo": "Preços praticados do X-Bacon",

   "enunciado": "O X-Bacon teve **reajuste de preço** durante o trimestre. Por quais preços ele foi vendido, quantas unidades saíram **a cada preço** e quanto isso faturou?",

   "colunas_esperadas": ["PrecoUnitario", "Unidades", "Faturamento"],

   "visual": {"tipo": "barra", "x": "PrecoUnitario", "y": "Unidades"},

   "conceitos": ["JOIN", "GROUP BY", "preço histórico"],

   "dica": "Agrupe pelo `PrecoUnitario` de `ItensPedido`. Compare com o preço que aparece em `Produtos`: por que são diferentes?",

   "moeda": ["PrecoUnitario", "Faturamento"],

  },

  # ----- Nível 3 - Desafio -----

  {

   "numero": 12,

   "nivel": 3,

   "titulo": "Top 3 clientes (fidelidade)",

   "enunciado": "A Dona Marta vai criar um **programa de fidelidade** para os **3 clientes que mais gastaram** em produtos (só pedidos entregues). Mostre o nome, **quantos pedidos** cada um fez e o total gasto.",

   "colunas_esperadas": ["Nome", "Pedidos", "TotalGasto"],

   "visual": {"tipo": "barra", "x": "Nome", "y": "TotalGasto", "horizontal": True},

   "conceitos": ["COUNT(DISTINCT)", "TOP", "JOIN com 3 tabelas"],

   "dica": "Ao juntar `Pedidos` com `ItensPedido`, cada pedido vira várias linhas (uma por item). `COUNT(*)` vai contar itens, não pedidos. Pesquise `COUNT(DISTINCT ...)`. Use `TOP 3`.",

   "moeda": ["TotalGasto"],

  },

  {

   "numero": 13,

   "nivel": 3,

   "titulo": "Faturamento mês a mês",

   "enunciado": "O faturamento de produtos **cresceu ou caiu** ao longo do trimestre? Mostre, para cada mês, a quantidade de pedidos entregues e o faturamento de produtos.",

   "colunas_esperadas": ["Mes", "PedidosEntregues", "Faturamento"],

   "visual": {"tipo": "linha", "x": "Mes", "y": "Faturamento"},

   "conceitos": ["MONTH", "COUNT(DISTINCT)", "SUM"],

   "dica": "Combine `MONTH()`, JOIN com `ItensPedido` e `COUNT(DISTINCT ...)`.",

   "moeda": ["Faturamento"],

  },

  {

   "numero": 14,

   "nivel": 3,

   "titulo": "Entregador do trimestre",

   "enunciado": "O **entregador do trimestre** precisa ter feito **pelo menos 4 entregas** e ter **nota média de pelo menos 4**. Quem se qualifica? Mostre entregas e nota média (com decimais).",

   "colunas_esperadas": ["Nome", "Entregas", "NotaMedia"],

   "visual": {"tipo": "barra", "x": "Nome", "y": "NotaMedia", "horizontal": True},

   "conceitos": ["HAVING com 2 condições", "AVG", "CAST"],

   "dica": "Duas condições no `HAVING`, ligadas por `AND`. Lembre do `CAST` na média.",

   "moeda": [],

  },

  {

   "numero": 15,

   "nivel": 3,

   "titulo": "Valor total dos pedidos de março",

   "enunciado": "Mostre o **valor total** de cada pedido **entregue em março** (produtos + taxa de entrega), com o nome do cliente, do maior para o menor.",

   "colunas_esperadas": ["IdPedido", "Nome", "ValorProdutos", "TaxaEntrega", "ValorTotal"],

   "visual": {"tipo": "empilhada", "x": "IdPedido", "partes": ["ValorProdutos", "TaxaEntrega"], "rotulo": "Nome"},

   "conceitos": ["GROUP BY", "SUM sem duplicar a taxa"],

   "dica": "Some os itens de cada pedido e **depois** some a taxa uma única vez. A taxa está em `Pedidos`, que se repete para cada item no JOIN.",

   "moeda": ["ValorProdutos", "TaxaEntrega", "ValorTotal"],

  },

  {

   "numero": 16,

   "nivel": 3,

   "titulo": "Clientes sem nenhum pedido",

   "enunciado": "Há clientes que se cadastraram e **nunca fizeram nenhum pedido**. Quem são e em que bairro moram? O que isso sugere para a Dona Marta?",

   "colunas_esperadas": ["Nome", "Bairro", "DataCadastro"],

   "visual": {"tipo": "tabela"},

   "conceitos": ["LEFT JOIN", "IS NULL"],

   "dica": "Um `INNER JOIN` só mostra quem tem par na outra tabela. Pesquise `LEFT JOIN` + `IS NULL`.",

   "moeda": [],

  },

  {

   "numero": 17,

   "nivel": 3,

   "titulo": "Produto que nunca foi vendido",

   "enunciado": "Existe algum produto do cardápio que **nunca apareceu em nenhum pedido**, nem cancelado? Ele é candidato a sair do cardápio.",

   "colunas_esperadas": ["NomeProduto", "Categoria", "Preco"],

   "visual": {"tipo": "tabela"},

   "conceitos": ["LEFT JOIN", "IS NULL"],

   "dica": "Mesma técnica da questão anterior, agora entre `Produtos` e `ItensPedido`.",

   "moeda": ["Preco"],

  },

]





def resposta(p):

  """O SQL que o aluno escreveu em src/respostas.py para a pergunta p."""

  return getattr(respostas, f"Q{p['numero']}", "").strip()





def por_nível(nivel):

  return [p for p in PERGUNTAS if p["nivel"] == nivel]


