import json
from collections import defaultdict
d=json.load(open('dados.json')); iss=json.load(open('issues.json'))['issues']
it={i['id']:i for i in d['itens']}
agg=defaultdict(lambda:{'n':0,'t':0.0,'orig':set()})
for c in d['compras']:
    for l in c['linhas']:
        a=agg[l['itemId']]; a['n']+=1; a['t']+=l['total'] or 0; a['orig'].add(l['original'])
br=lambda v:('R$ {:,.2f}'.format(v)).replace(',','X').replace('.',',').replace('X','.')
CATS=['Carne','Grãos','Limpeza','Outros']
L=['# Categorias — regras e lista completa de produtos','',
'Gerado a partir de `Planilha de Compras Domésticas (2).xlsx` (somente leitura). No app, qualquer item pode mudar de categoria (Itens → editar, ou na janela do item).','',
'## Regras','',
'| Categoria | Entra | Decisões / casos de fronteira |','|---|---|---|',
'| **Carne** | carnes bovinas, frango (inteiro, peito, coxa/sobrecoxa, fígado, empanado, a passarinho), peixe (sardinha), embutidos (calabresa, linguiça, mortadela, presunto), carne de lata e de hambúrguer | **Ovos ficam em Outros** (pedido do usuário). “Mistos de carnes e verduras” (R$ 100, compra mista de feira) ficou em Outros. “P. de frango” mantido como está (não dá para saber se é peito ou pé). |',
'| **Grãos** | arroz, feijão, milho (milho verde, ervilha/milho, flocão de milho para cuscuz, pipoca), ervilha, aveia, granola, sucrilhos (flocos), amendoim, **farinhas** (trigo, trigo c/ fermento, farinha de mandioca), **goma** (fécula de mandioca/tapioca) e **massas secas** (macarrão, lasanha, parafuso, miojo) | Farinhas e massas entraram por serem derivados diretos de cereais e comprados como “mercearia seca”. Ficaram em Outros: farinha láctea, pasta de amendoim, mistura para bolo, sopão, açúcar, café. |',
'| **Limpeza** | detergente, sabão (pó, barra, líquido, pasta), amaciante (“Amaciente” na planilha), água sanitária, desinfetante, Veja, polidor, bombril, esponja, flanela, pano de microfibra, rodo, vassoura, saco de lixo, pedra sanitária, aromatizadores (essência para difusor e refil) e **controle de pragas** (Baygon, Formitol, pasta mata-barata, veneno para mosca, naftalina) | **Higiene pessoal fica em Outros** (shampoo, sabonete, pasta de dente, desodorante, gilete, cotonete…). **Papel higiênico**: decidido que iria para Limpeza, mas a planilha não tem esse item — “P. Sanitária” custa ~R$ 2,60–4,20 por unidade, compra-se 4 e na planilha de 2024 aparece “Pedra Sanitária” com o mesmo padrão, então foi unificado como **Pedra sanitária**. “Essência” (R$ 12–35) é tratada como aromatizador de ambiente; “Essência de baunilha” (culinária) fica em Outros. |',
'| **Outros** | todo o resto (laticínios, ovos, hortifrúti, temperos, bebidas, biscoitos, higiene pessoal, utilidades), para nada se perder | Itens com nome incerto ficaram aqui: Quinó, Sentinela, Espok, Liga, Depósito (“4 em 1”), Misturinha, Lanche, Variados. |','',
'## Normalização dos nomes','',
'- Espaços extras removidos e maiúsculas/minúsculas padronizadas (só a 1ª letra maiúscula); variações de grafia foram unificadas (ex.: “Água sanitária”/“Água Sanitária”, “Carne moida”/“Carne muida”, “Lemon Piper”/“Limon Pepperr”).',
'- Erros de digitação óbvios corrigidos: Amaciente→Amaciante, Sabobete→Sabonete, Saso de lixo→Saco de lixo, Carbe mista→Carne mista, Cacal em pó→Cacau em pó, Cenosa→Cenoura, Phimichurri→Chimichurri, Contonete/Continente→Cotonete, Pegador se roupa→Prendedor de roupa, Bayggon→Baygon, Essência Balnilha→Essência de baunilha, Formitoo→Formitol, Cucuz→Flocão de milho (cuscuz), F. Teigo→Farinha de trigo.',
'- Unidades de medida no nome foram retiradas e passaram para o campo unidade (ex.: “Cebola (Kg)” → Cebola, unidade kg). Ovos 20 un e 30 un continuam separados (embalagens diferentes).',
'- O nome original de cada linha continua no CSV (coluna `produto_original`).','',
'## Totais por categoria (dados da planilha)','','| Categoria | Produtos | Linhas | Total R$ |','|---|---:|---:|---:|']
tot=defaultdict(lambda:[0,0,0.0])
for i in d['itens']:
    a=agg[i['id']]; t=tot[i['categoria']]; t[0]+=1; t[1]+=a['n']; t[2]+=a['t']
for c in CATS: L.append(f'| {c} | {tot[c][0]} | {tot[c][1]} | {br(tot[c][2])} |')
L.append(f'| **Total** | {sum(t[0] for t in tot.values())} | {sum(t[1] for t in tot.values())} | {br(sum(t[2] for t in tot.values()))} |')
L+=['','## Lista completa produto → categoria','']
for c in CATS:
    L+=[f'### {c}','','| Produto | Unidade | Nomes na planilha | Linhas | Total R$ |','|---|---|---|---:|---:|']
    for i in sorted([i for i in d['itens'] if i['categoria']==c],key=lambda i:i['nome'].lower()):
        a=agg[i['id']]; L.append(f"| {i['nome']} | {i['unidade']} | {', '.join(sorted(a['orig']))} | {a['n']} | {br(a['t'])} |")
    L.append('')
L+=['## Problemas de dados e suposições','',
'- A planilha tem estilos inválidos (o openpyxl padrão falha); a leitura foi feita em modo somente leitura ignorando estilos — valores não são afetados.',
'- Uma aba = uma compra. Para cada aba, a soma das linhas extraídas confere com o total da linha 2 da aba (todas as 37 bateram, diferença < R$ 0,01).',
'- Linhas incluídas: quantidade > 0, ou preço, ou marca de comprado (👌, X, x, -, e marcas avulsas como A, &, ♥️, 🔒, y, feito, g, X30, não). Itens com 👌/X sem preço entram com total vazio (“comprado, preço não anotado”) e **não** somam nos valores.',
'- Linhas com quantidade preenchida mas sem preço também foram incluídas (muitas abas funcionam como lista de compras). Duas abas têm total 0: “1 AGOSTO 2026 ELIAS” e “04 de Outubro Elias” (só quantidades).',
'- Ano inferido pela ordem das abas (mais nova primeiro) para as abas sem ano: Dezembro, Novembro, Outubro, Setembro, Agosto, “JUNLO” e Junho → 2025.',
'- Meses com erro de digitação: “JUNLO” → julho (fica entre Agosto/2025 e Junho/2025), “MAIL” → maio, “JANEIROS” → janeiro.',
'- “31 MAIO 2026 ELIAS - FEIRA JUNH”: data 31/05/2026, com observação “feira de junho”. Não há aba de fevereiro/2026 (a compra de 31/01 cobriu o mês).',
'- “7 JULHO 2026 ELIAS + CLAUDIA” → comprador “Elias + Claudia”. Quatro abas antigas (20/04, 04/05, 18/05 e 08/06/2024) não têm comprador → vazio.',
'- Em “08 de Junho-2024” o cabeçalho da coluna A diz “Alho” em vez de PRODUTO e há uma linha “Alho” 10 × R$ 3,88 (provavelmente outro produto) — mantida como está.',
'- Fornecedor: a planilha não tem essa coluna → vazio em todas as compras importadas.',
'','Ocorrências registradas pelo extrator:','']+['- '+x for x in iss]
open('../categorias.md','w').write('\n'.join(L)+'\n')
print(len(L))
