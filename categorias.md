# Categorias — regras e lista completa de produtos

Gerado a partir de `Planilha de Compras Domésticas (2).xlsx` (somente leitura). No app, qualquer item pode mudar de categoria (Itens → editar, ou na janela do item).

## Regras

| Categoria | Entra | Decisões / casos de fronteira |
|---|---|---|
| **Carne** | carnes bovinas, frango (inteiro, peito, coxa/sobrecoxa, fígado, empanado, a passarinho), peixe (sardinha), embutidos (calabresa, linguiça, mortadela, presunto), carne de lata e de hambúrguer | **Ovos ficam em Outros** (pedido do usuário). “Mistos de carnes e verduras” (R$ 100, compra mista de feira) ficou em Outros. “P. de frango” mantido como está (não dá para saber se é peito ou pé). |
| **Grãos** | arroz, feijão, milho (milho verde, ervilha/milho, flocão de milho para cuscuz, pipoca), ervilha, aveia, granola, sucrilhos (flocos), amendoim, **farinhas** (trigo, trigo c/ fermento, farinha de mandioca), **goma** (fécula de mandioca/tapioca) e **massas secas** (macarrão, lasanha, parafuso, miojo) | Farinhas e massas entraram por serem derivados diretos de cereais e comprados como “mercearia seca”. Ficaram em Outros: farinha láctea, pasta de amendoim, mistura para bolo, sopão, açúcar, café. |
| **Limpeza** | detergente, sabão (pó, barra, líquido, pasta), amaciante (“Amaciente” na planilha), água sanitária, desinfetante, Veja, polidor, bombril, esponja, flanela, pano de microfibra, rodo, vassoura, saco de lixo, pedra sanitária, aromatizadores (essência para difusor e refil) e **controle de pragas** (Baygon, Formitol, pasta mata-barata, veneno para mosca, naftalina) | **Higiene pessoal fica em Outros** (shampoo, sabonete, pasta de dente, desodorante, gilete, cotonete…). **Papel higiênico**: decidido que iria para Limpeza, mas a planilha não tem esse item — “P. Sanitária” custa ~R$ 2,60–4,20 por unidade, compra-se 4 e na planilha de 2024 aparece “Pedra Sanitária” com o mesmo padrão, então foi unificado como **Pedra sanitária**. “Essência” (R$ 12–35) é tratada como aromatizador de ambiente; “Essência de baunilha” (culinária) fica em Outros. |
| **Outros** | todo o resto (laticínios, ovos, hortifrúti, temperos, bebidas, biscoitos, higiene pessoal, utilidades), para nada se perder | Itens com nome incerto ficaram aqui: Quinó, Sentinela, Espok, Liga, Depósito (“4 em 1”), Misturinha, Lanche, Variados. |

## Normalização dos nomes

- Espaços extras removidos e maiúsculas/minúsculas padronizadas (só a 1ª letra maiúscula); variações de grafia foram unificadas (ex.: “Água sanitária”/“Água Sanitária”, “Carne moida”/“Carne muida”, “Lemon Piper”/“Limon Pepperr”).
- Erros de digitação óbvios corrigidos: Amaciente→Amaciante, Sabobete→Sabonete, Saso de lixo→Saco de lixo, Carbe mista→Carne mista, Cacal em pó→Cacau em pó, Cenosa→Cenoura, Phimichurri→Chimichurri, Contonete/Continente→Cotonete, Pegador se roupa→Prendedor de roupa, Bayggon→Baygon, Essência Balnilha→Essência de baunilha, Formitoo→Formitol, Cucuz→Flocão de milho (cuscuz), F. Teigo→Farinha de trigo.
- Unidades de medida no nome foram retiradas e passaram para o campo unidade (ex.: “Cebola (Kg)” → Cebola, unidade kg). Ovos 20 un e 30 un continuam separados (embalagens diferentes).
- O nome original de cada linha continua no CSV (coluna `produto_original`).

## Totais por categoria (dados da planilha)

| Categoria | Produtos | Linhas | Total R$ |
|---|---:|---:|---:|
| Carne | 22 | 185 | R$ 2.869,02 |
| Grãos | 19 | 240 | R$ 2.420,94 |
| Limpeza | 26 | 199 | R$ 1.946,71 |
| Outros | 107 | 752 | R$ 6.905,97 |
| **Total** | 174 | 1376 | R$ 14.142,64 |

## Lista completa produto → categoria

### Carne

| Produto | Unidade | Nomes na planilha | Linhas | Total R$ |
|---|---|---|---:|---:|
| Calabresa | un | Calabresa | 23 | R$ 705,04 |
| Capa de filé | un | Capa de Filé | 1 | R$ 23,69 |
| Carne alcatra | kg | Carne alcatra | 2 | R$ 65,54 |
| Carne de hambúrguer | un | Carne Hanbur. | 23 | R$ 252,46 |
| Carne de lata | un | Carne de Lata, Carne de lata, Carne enlatada | 18 | R$ 173,94 |
| Carne mista 2,5kg | un | Carbe mista 2,5kg | 8 | R$ 60,00 |
| Carne moída | kg | Carne moida, Carne muida | 3 | R$ 71,35 |
| Costela bovina | kg | Costela Bovina | 7 | R$ 33,50 |
| Coxa e sobrecoxa | kg | Coxa/SobreC | 7 | R$ 137,42 |
| Empanado | un | Empanado | 11 | R$ 18,08 |
| Frango | kg | Frango(Kg) | 4 | R$ 4,00 |
| Frango a passarinho | un | Frango a passarinho | 1 | R$ 13,96 |
| Fígado bovino | kg | Figado, Figado B. (Kg) | 16 | R$ 13,79 |
| Fígado de frango | kg | Figado Frango | 4 | R$ 12,96 |
| Linguiça | un | Linguiça | 1 | R$ 63,73 |
| Mortadela | un | Mortadela, mortadela | 22 | R$ 712,02 |
| Mortadela 1,5kg | un | Mortadela 1,5kg | 4 | R$ 0,00 |
| Mortadela 1kg | un | Mortadela 1kg | 1 | R$ 13,29 |
| P. de frango | un | P. de frango | 13 | R$ 274,31 |
| Peito de frango | kg | Peito de Frango | 6 | R$ 157,36 |
| Presunto | un | Presunto | 2 | R$ 7,00 |
| Sardinha | un | Sardinha | 8 | R$ 55,58 |

### Grãos

| Produto | Unidade | Nomes na planilha | Linhas | Total R$ |
|---|---|---|---:|---:|
| Amendoim | un | Amendoim | 11 | R$ 167,92 |
| Arroz | kg | Arroz | 29 | R$ 535,66 |
| Aveia | un | Aveia | 4 | R$ 45,46 |
| Ervilha | un | Ervilha | 5 | R$ 5,70 |
| Ervilha/milho | un | Ervilha/milho, M e Ervilha | 13 | R$ 74,99 |
| Farinha (mandioca) | un | Farinha | 11 | R$ 51,88 |
| Farinha de trigo | kg | F.Trigo, Farinha de trigo | 27 | R$ 152,18 |
| Farinha de trigo c/ fermento | kg | F. Teigo c/ F., F.Trigo C/ Ferm, Farinha de Trigo c/Ferm | 9 | R$ 55,58 |
| Feijão | kg | Feijao | 15 | R$ 144,75 |
| Flocão de milho (cuscuz) | pct | Cucuz | 18 | R$ 188,25 |
| Goma | kg | Goma | 23 | R$ 193,96 |
| Granola | un | Granola | 5 | R$ 171,18 |
| Macarrão | pct | Macarrão | 16 | R$ 249,94 |
| Macarrão lasanha | un | Macarrão Lasanha | 5 | R$ 9,89 |
| Macarrão parafuso | un | Macarrão Parafuso | 2 | R$ 4,00 |
| Milho verde | un | Milho Verde | 20 | R$ 180,84 |
| Miojo | pct | Miojo, Nissin Miojo | 20 | R$ 151,68 |
| Pipoca | un | Pipoca | 6 | R$ 25,10 |
| Sucrilhos | un | Sucrilhos | 1 | R$ 11,98 |

### Limpeza

| Produto | Unidade | Nomes na planilha | Linhas | Total R$ |
|---|---|---|---:|---:|
| Amaciante | un | Amaciente | 18 | R$ 259,85 |
| Baygon (inseticida) | un | Bayggon | 27 | R$ 429,56 |
| Bombril | un | Bombril | 5 | R$ 4,81 |
| Desinfetante | L | Desinfetante | 5 | R$ 14,96 |
| Detergente | un | Detergente | 24 | R$ 84,24 |
| Esponja | un | Esponja | 10 | R$ 12,99 |
| Essência (aromatizador) | un | Essência, essência | 13 | R$ 176,46 |
| Flanela | un | Flanela | 3 | R$ 14,99 |
| Formitol (veneno formiga) | un | Formitol - Veneno, Formitoo | 2 | R$ 15,00 |
| Naftalina | un | Naftalina | 1 | R$ 12,50 |
| Pano de microfibra | un | Pano micro Fibra | 1 | R$ 17,00 |
| Pasta mata barata | un | Pasta Mata Barata | 1 | R$ 15,99 |
| Pedra sanitária | un | P. Sanitária, Pedra Sanitária | 27 | R$ 178,17 |
| Polidor | un | Polidor | 2 | R$ 2,99 |
| Refil difusor essência | un | Refil Difusor Essência | 5 | R$ 87,00 |
| Rodo | un | Rodo | 1 | R$ 0,00 |
| Sabão em barra | un | Sabão em Barra | 1 | R$ 2,98 |
| Sabão em pó | un | Sabão em pó | 2 | R$ 20,25 |
| Sabão em pó Ypê | un | Sabão em pó Ypê | 23 | R$ 393,56 |
| Sabão líquido | un | Sabão Líquido, Sabão líquido | 3 | R$ 31,27 |
| Sabão pasta | un | Sabão Pasta | 3 | R$ 14,98 |
| Saco de lixo | pct | Saso de lixo | 7 | R$ 58,98 |
| Vassoura | un | Vassoura, vassoura | 9 | R$ 83,21 |
| Veja | un | Veja | 1 | R$ 10,99 |
| Veneno para mosca | un | veveno mosca | 1 | R$ 0,00 |
| Água sanitária | L | Água Sanitária, Água sanitária | 4 | R$ 3,98 |

### Outros

| Produto | Unidade | Nomes na planilha | Linhas | Total R$ |
|---|---|---|---:|---:|
| Adoçante em pó | un | Adoçante Po | 7 | R$ 120,63 |
| Adoçante gotas | un | Adoçante Gota | 5 | R$ 57,69 |
| Alho | kg | Alho, Alho kg | 17 | R$ 56,00 |
| Alho (lata) | un | Alho lata | 1 | R$ 4,39 |
| Antitranspirante | un | Antitranspirante | 10 | R$ 113,83 |
| Azeitona verde | un | Azeitona Verde | 2 | R$ 11,38 |
| Açafrão | un | Açafrão | 1 | R$ 10,00 |
| Açúcar | kg | Açucar | 20 | R$ 203,88 |
| Batata | kg | Batata | 7 | R$ 7,88 |
| Batata palha | un | Batata Palha | 6 | R$ 18,98 |
| Batata-doce | kg | Batata Doce | 4 | R$ 6,39 |
| Biscoito recheado | pct | Recheado, Recheado 4un | 11 | R$ 96,99 |
| Bolacha | un | Bolacha | 18 | R$ 179,68 |
| Cacau em pó | un | Cacal em Po | 1 | R$ 24,37 |
| Café | un | Cafe | 31 | R$ 748,10 |
| Cebola | kg | Cebola (Kg) | 22 | R$ 42,32 |
| Cenoura | kg | Cenosa(Kg) | 1 | R$ 0,00 |
| Chimichurri | un | Chimichurri, Phimichurri | 10 | R$ 23,62 |
| Chinelo | un | Chinelo | 1 | R$ 50,00 |
| Cotonete | un | Continente, Contonete | 4 | R$ 12,49 |
| Creme capilar | un | Creme Capilar | 7 | R$ 44,28 |
| Creme de barbear | un | Creme Barbear, Creme de Barbear | 6 | R$ 32,08 |
| Creme de leite | un | C. de Leite | 30 | R$ 320,89 |
| Depósito | un | Depósito | 1 | R$ 31,99 |
| Doce de goiaba | un | Doce de Goiaba | 1 | R$ 4,05 |
| Escova de dente | un | Escova de dente | 3 | R$ 21,18 |
| Espok | un | Espok | 1 | R$ 6,32 |
| Essência de baunilha | un | Essência Balnilha | 7 | R$ 24,48 |
| Farinha láctea | un | farinha lactea | 16 | R$ 143,30 |
| Fermento químico | un | Fermento Químico | 4 | R$ 17,48 |
| Filtro de café | un | Filtro de Café | 1 | R$ 7,98 |
| Frisco | pct | Frisco | 12 | R$ 126,38 |
| Funil | un | Funil | 1 | R$ 0,00 |
| Gelatina | un | Gelatina | 10 | R$ 61,80 |
| Gilete | un | gilete | 3 | R$ 33,68 |
| H2OH limão | un | H2OH Limão | 3 | R$ 43,36 |
| Hidratante | un | hidratante | 13 | R$ 20,59 |
| Iogurte | un | Iogurte, iogurte | 13 | R$ 148,90 |
| Ketchup | un | catchup | 7 | R$ 18,98 |
| Kinnor | un | Kinnor | 12 | R$ 26,74 |
| Lanche | un | lanche | 1 | R$ 37,78 |
| Laranja | un | Laranja | 5 | R$ 4,00 |
| Leite | L | Leite | 2 | R$ 21,96 |
| Leite condensado | un | Leite Cond., leite condensado | 28 | R$ 395,75 |
| Leite em pó | un | Leite em po | 15 | R$ 648,06 |
| Lemon pepper | un | Lemon Piper, Limon Pepperr | 10 | R$ 19,31 |
| Liga | un | Liga | 1 | R$ 0,00 |
| Listerine | un | Listerine | 6 | R$ 48,10 |
| Maionese | un | Maionese | 16 | R$ 38,08 |
| Manteiga | un | Manteiga | 19 | R$ 308,91 |
| Maçã | un | Maçã | 8 | R$ 20,00 |
| Mistos de carnes e verduras | un | mistos de carnes e verduras | 1 | R$ 100,00 |
| Mistura bolo | un | Mistura Bolo | 9 | R$ 22,71 |
| Misturinha | un | Misturinha | 4 | R$ 25,96 |
| Molho de pimenta | un | Molho de Pimenta | 1 | R$ 2,50 |
| Molho de tomate | un | M. de Tomate | 22 | R$ 149,36 |
| Molho shoyu | un | Molho Shoyu | 1 | R$ 2,89 |
| Nescafe | un | Nescafe | 2 | R$ 13,99 |
| Nescau | un | Nescau | 5 | R$ 52,28 |
| Nesquik | un | Nesquik | 1 | R$ 14,50 |
| Ovos (20 un) | cart | Ovos(20un) | 11 | R$ 193,59 |
| Ovos (30 un) | cart | Ovos(30un) | 16 | R$ 254,64 |
| Papel alumínio | un | PAPEL alumínio | 1 | R$ 7,00 |
| Pasta de amendoim | un | Pasta de Amendoim | 1 | R$ 28,00 |
| Pasta de dente M | un | P. de Dente M, Pasta de Dente | 16 | R$ 116,52 |
| Pasta de dente P | un | P. de Dente P | 3 | R$ 20,76 |
| Pimenta calabresa | un | Pimenta Calabresa | 1 | R$ 2,99 |
| Pimentão | un | Pimentao, Pimentao(Un) | 20 | R$ 11,08 |
| Piraquê | un | Piraquê | 4 | R$ 60,29 |
| Porta filtro | un | Porta filtro | 1 | R$ 11,49 |
| Prendedor de roupa | un | Pegador se roupa | 6 | R$ 8,98 |
| Prestobarba | un | Prestobarba | 1 | R$ 17,90 |
| Pão de hambúrguer | un | Pão amburger | 1 | R$ 11,99 |
| Queijo | un | Queijo | 10 | R$ 203,26 |
| Quinó | un | Quinó | 7 | R$ 24,04 |
| Rapadura | un | Rapadura | 2 | R$ 8,99 |
| Sabonete | un | Sabobete | 23 | R$ 216,47 |
| Sabonete líquido | un | Sabonete líquido | 7 | R$ 58,78 |
| Sabores (para dindin) | un | sabores | 1 | R$ 0,00 |
| Sal | un | Sal, sal | 16 | R$ 14,02 |
| Salgadinho | un | Salgadinho | 8 | R$ 35,16 |
| Salgado | un | Salgado | 2 | R$ 6,76 |
| Salsa | un | salsa | 1 | R$ 1,25 |
| Sazon | un | Sazon | 1 | R$ 5,79 |
| Sentinela | un | sentinela | 4 | R$ 9,18 |
| Shampoo | un | shampoo | 11 | R$ 86,32 |
| Sopão | un | Sopão | 2 | R$ 17,78 |
| Sorvete | un | sorvete | 1 | R$ 19,88 |
| Tang | un | Tang | 6 | R$ 79,99 |
| Tempero | un | Tempero | 1 | R$ 6,00 |
| Tempero baiano | un | Temp. Baiano | 5 | R$ 16,74 |
| Tempero chefe | un | Tempero Chefe | 1 | R$ 5,19 |
| Tempero Edu | un | Temp Edu | 6 | R$ 26,20 |
| Tempero folhas verdes caseiro | un | Temp. FolVer. Caseiro | 5 | R$ 5,24 |
| Tempero Gourmet | un | Temp Gurme | 6 | R$ 16,15 |
| Tempero regional frango | un | Temp. Reg. Feango | 4 | R$ 13,73 |
| Toddy | un | Toddy | 1 | R$ 13,89 |
| Todinho | un | Todinho | 1 | R$ 18,00 |
| Tomate | kg | Tomate | 2 | R$ 5,98 |
| Tênis Pé Baruel (talco) | un | TÊNIS PÉ BARUEL | 4 | R$ 8,99 |
| Uva | un | Uva | 2 | R$ 0,00 |
| Variados | un | Variados | 1 | R$ 100,00 |
| Vela | un | Vela | 1 | R$ 3,50 |
| Vinagre | un | Vinagre | 3 | R$ 3,34 |
| Wafer | un | Waffer, waffer | 11 | R$ 45,89 |
| Óleo de cozinha | un | Oleo, Óleo | 22 | R$ 207,01 |
| Óleo Mobil | un | Óleo Mobile | 5 | R$ 28,00 |

## Problemas de dados e suposições

- A planilha tem estilos inválidos (o openpyxl padrão falha); a leitura foi feita em modo somente leitura ignorando estilos — valores não são afetados.
- Uma aba = uma compra. Para cada aba, a soma das linhas extraídas confere com o total da linha 2 da aba (todas as 37 bateram, diferença < R$ 0,01).
- Linhas incluídas: quantidade > 0, ou preço, ou marca de comprado (👌, X, x, -, e marcas avulsas como A, &, ♥️, 🔒, y, feito, g, X30, não). Itens com 👌/X sem preço entram com total vazio (“comprado, preço não anotado”) e **não** somam nos valores.
- Linhas com quantidade preenchida mas sem preço também foram incluídas (muitas abas funcionam como lista de compras). Duas abas têm total 0: “1 AGOSTO 2026 ELIAS” e “04 de Outubro Elias” (só quantidades).
- Ano inferido pela ordem das abas (mais nova primeiro) para as abas sem ano: Dezembro, Novembro, Outubro, Setembro, Agosto, “JUNLO” e Junho → 2025.
- Meses com erro de digitação: “JUNLO” → julho (fica entre Agosto/2025 e Junho/2025), “MAIL” → maio, “JANEIROS” → janeiro.
- “31 MAIO 2026 ELIAS - FEIRA JUNH”: data 31/05/2026, com observação “feira de junho”. Não há aba de fevereiro/2026 (a compra de 31/01 cobriu o mês).
- “7 JULHO 2026 ELIAS + CLAUDIA” → comprador “Elias + Claudia”. Quatro abas antigas (20/04, 04/05, 18/05 e 08/06/2024) não têm comprador → vazio.
- Em “08 de Junho-2024” o cabeçalho da coluna A diz “Alho” em vez de PRODUTO e há uma linha “Alho” 10 × R$ 3,88 (provavelmente outro produto) — mantida como está.
- Fornecedor: a planilha não tem essa coluna → vazio em todas as compras importadas.

Ocorrências registradas pelo extrator:

- "1 AGOSTO 2026 ELIAS": total da planilha = 0 (lista de compras sem preços anotados)
- "09 MAIL 2026 Elias": mês com erro de digitação "MAIL"→Maio
- "31 JANEIROS 2026 Elias": mês com erro de digitação "JANEIROS"→Janeiro
- "06 de Dezembro Elias": ano não consta no nome → inferido 2025 pela ordem das abas
- "04 de Novembro Elias": ano não consta no nome → inferido 2025 pela ordem das abas
- "04 de Novembro Elias" / Alho kg: quantidade "600g" convertida para 0.6 kg
- "04 de Outubro Elias": ano não consta no nome → inferido 2025 pela ordem das abas
- "04 de Outubro Elias": total da planilha = 0 (lista de compras sem preços anotados)
- "06 de Setembro Elias": ano não consta no nome → inferido 2025 pela ordem das abas
- "02 de Agosto Elias": ano não consta no nome → inferido 2025 pela ordem das abas
- "05 de JUNLO Elias": ano não consta no nome → inferido 2025 pela ordem das abas
- "05 de JUNLO Elias": mês com erro de digitação "JUNLO"→Julho
- "04 de JUNHO Elias": ano não consta no nome → inferido 2025 pela ordem das abas
- "02 de março -2025 Elias" / Adoçante: só marca "!" sem quantidade/preço → ignorada
- "20 de outubro-2024 Juliano" / M. de Tomate: preço unitário digitado como texto "2.35" → 2.35; total não somado (planilha marca 👌)
- Aba "Planilha1" vazia — ignorada
- "08 de Junho-2024": sem nome de comprador na aba → comprador vazio
- "18 de Maio-2024": sem nome de comprador na aba → comprador vazio
- "04 de Maio-2024": sem nome de comprador na aba → comprador vazio
- "20 Abril de 2024": sem nome de comprador na aba → comprador vazio
- "04 ABRIL 2026 Elias" / Alho kg: quantidade 200 interpretada como gramas → 0.2 kg
- "06 de Setembro Elias" / Alho: quantidade 300 interpretada como gramas → 0.3 kg
- "06 de Setembro Elias" / Cebola (Kg): quantidade 500 interpretada como gramas → 0.5 kg
- "03 de MAIO -2025 Elias  (2)" / Alho: quantidade 500 interpretada como gramas → 0.5 kg
- "21 de Setembro-2024 Juliano" / Alho: quantidade 500 interpretada como gramas → 0.5 kg
