# Controle de Compras

Abra **index.html** com dois cliques — funciona no navegador sem instalar nada e sem internet (sem bibliotecas externas).
Os dados ficam salvos no próprio navegador (localStorage). Na 1ª abertura o app carrega as 37 compras extraídas da planilha.

## Fluxo da feira (tela "Feira")
1. **Planejar** (em casa): todos os itens por categoria (Carne, Grãos, Limpeza, Outros), botões grandes de +/−; dicas com a última quantidade, o último preço e a sugestão (média por mês nos últimos 6 meses); atalhos "Repetir última feira" e "Sugestões"; estimativa (quantidade × último preço) comparada com o limite do mês.
2. **No mercado**: só os itens planejados; digite o preço pago (teclado numérico, aceita vírgula), ajuste a quantidade final com +/−, marque "Não comprei", adicione itens fora do plano; mostra se o preço subiu (▲ vermelho) ou caiu (▼ verde) desde a última vez; total do carrinho ao vivo, comparado com o limite (amarelo a partir de 80%, vermelho acima do limite).
3. **Finalizar**: data (hoje, no horário local), comprador e mercado (opcional). Grava cada linha com quantidade planejada, quantidade final, preço unitário e total.
A feira em andamento é salva automaticamente e continua lá se você fechar o app.

## Instalar no celular (PWA / offline)
Publique a pasta inteira (index.html, manifest.json, sw.js, icon-192.png, icon-512.png) em um endereço https (ex.: GitHub Pages, Netlify) e abra no Chrome do celular → "Adicionar à tela inicial". O service worker guarda o app para uso offline. Quando aberto como arquivo (file://) o app funciona igual, mas não é instalável — limitação do navegador.
Atenção: os dados de cada endereço/navegador são separados. Use Backup → Exportar/Importar JSON para levar os dados de um para outro.

## Arquivos
- `index.html` — o app inteiro (HTML + CSS + JS + dados da planilha embutidos)
- `dados_extraidos.csv` — todas as linhas extraídas (separador `;`, decimal com vírgula, UTF-8, abre direto no Excel em pt-BR)
- `categorias.md` — regras das categorias, lista completa produto → categoria, problemas de dados encontrados
- `manifest.json`, `sw.js`, `icon-*.png` — instalação como app (PWA)
- `shots/` — capturas de tela do teste automático
- `ferramentas/` — scripts usados para extrair a planilha e montar o app
