import asyncio, sys
from playwright.async_api import async_playwright
URL = sys.argv[1] if len(sys.argv) > 1 else 'file:///workspace/controle-compras/index.html'
OUT = '/workspace/controle-compras/shots/'
errs = []
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox','--lang=pt-BR'])
        async def page_for(vp, mobile):
            ctx = await b.new_context(viewport=vp, device_scale_factor=2 if mobile else 1, is_mobile=mobile, has_touch=mobile, locale='pt-BR', timezone_id='America/Fortaleza')
            pg = await ctx.new_page()
            pg.on('console', lambda m: errs.append(f'[{m.type}] {m.text}') if m.type in ('error', 'warning') else None)
            pg.on('pageerror', lambda e: errs.append(f'[pageerror] {e}'))
            return pg
        # ---------- celular ----------
        m = await page_for({'width': 390, 'height': 844}, True)
        await m.goto(URL); await m.wait_for_timeout(500)
        # limite
        await m.goto(URL + '#gastos'); await m.click('[data-tab="gastos:limites"]')
        await m.fill('#lim-g', '500'); await m.fill('#lim-Carne', '120'); await m.click('[data-form=limites] button[type=submit]'); await m.wait_for_timeout(200)
        await m.evaluate("document.querySelectorAll('.toast').forEach(t=>t.remove())"); await m.screenshot(path=OUT + 'm_gastos.png', full_page=True)
        await m.goto(URL + '#painel'); await m.wait_for_timeout(300)
        await m.evaluate("document.querySelectorAll('.toast').forEach(t=>t.remove())"); await m.screenshot(path=OUT + 'm_painel.png', full_page=True)
        await m.goto(URL + '#cat/Carne'); await m.wait_for_timeout(300)
        await m.evaluate("document.querySelectorAll('.toast').forEach(t=>t.remove())"); await m.screenshot(path=OUT + 'm_categoria_carne.png', full_page=True)
        # feira passo 1
        await m.goto(URL + '#feira'); await m.wait_for_timeout(200)
        await m.evaluate("document.querySelectorAll('.toast').forEach(t=>t.remove())"); await m.screenshot(path=OUT + 'm_feira_inicio.png')
        await m.click('[data-a="feira-new"][data-m="ultima"]'); await m.wait_for_timeout(300)
        await m.click('[data-a="fonly"]'); await m.wait_for_timeout(200)  # mostrar todos
        btns = await m.query_selector_all('[data-a="fplan"][data-d="1"]')
        for bt in btns[:3]: await bt.click(); await bt.click()
        await m.evaluate("document.querySelectorAll('.toast').forEach(t=>t.remove())"); await m.screenshot(path=OUT + 'm_feira_1_planejar.png')
        # passo 2
        await m.click('[data-a="feira-market"]'); await m.wait_for_timeout(300)
        inputs = await m.query_selector_all('[data-f="mpreco"]')
        prices = ['3,99', '12.50', '7', '2,49', '15,9', '1,25']
        for inp, pr in zip(inputs, prices): await inp.fill(pr)
        minus = await m.query_selector_all('[data-a="fqtd"][data-d="-1"]')
        await minus[0].click()
        nao = await m.query_selector_all('[data-a="fnao"]'); await nao[-1].click(); await m.wait_for_timeout(200)
        await m.fill('#madd', 'vela'); await m.wait_for_timeout(200)
        await m.evaluate("document.querySelectorAll('.toast').forEach(t=>t.remove())"); await m.screenshot(path=OUT + 'm_feira_2_mercado_busca.png')
        await m.click('#madd-s button'); await m.wait_for_timeout(300)
        await m.keyboard.type('3,15'); await m.wait_for_timeout(200)
        await m.evaluate('window.scrollTo(0,0)')
        await m.evaluate("document.querySelectorAll('.toast').forEach(t=>t.remove())"); await m.screenshot(path=OUT + 'm_feira_2_mercado.png')
        # reload: feira deve persistir
        await m.reload(); await m.wait_for_timeout(300)
        st = await m.evaluate("JSON.parse(localStorage.getItem('controleCompras.v1')).feira.status")
        print('feira após reload:', st)
        await m.click('[data-a="feira-finish"]'); await m.wait_for_timeout(300)
        await m.evaluate("document.querySelectorAll('.toast').forEach(t=>t.remove())"); await m.screenshot(path=OUT + 'm_feira_3_finalizar.png')
        await m.click('[data-a="feira-save"]'); await m.wait_for_timeout(400)
        await m.evaluate("document.querySelectorAll('.toast').forEach(t=>t.remove())"); await m.screenshot(path=OUT + 'm_compras_historico.png')
        await m.click('[data-a="compra-new"]'); await m.wait_for_timeout(300)
        dval = await m.input_value('#cf-data'); print('data padrão form:', dval)
        lines = await m.query_selector_all('#cf-lines [data-l=item]')
        await lines[0].fill('Arroz'); q = await m.query_selector_all('#cf-lines [data-l=qtd]'); await q[0].fill('2'); pr = await m.query_selector_all('#cf-lines [data-l=preco]'); await pr[0].fill('4,59')
        await m.evaluate("document.querySelectorAll('.toast').forEach(t=>t.remove())"); await m.screenshot(path=OUT + 'm_compras_form.png', full_page=True)
        await m.click('[data-form=compra] button[type=submit]'); await m.wait_for_timeout(300)
        await m.click('[data-a="more"]'); await m.wait_for_timeout(200)
        await m.evaluate("document.querySelectorAll('.toast').forEach(t=>t.remove())"); await m.screenshot(path=OUT + 'm_menu_mais.png')
        # ---------- desktop ----------
        d = await page_for({'width': 1366, 'height': 900}, False)
        await d.goto(URL + '#painel'); await d.wait_for_timeout(500)
        await d.evaluate("document.querySelectorAll('.toast').forEach(t=>t.remove())"); await d.screenshot(path=OUT + 'painel.png', full_page=True)
        await d.goto(URL + '#cat/Grãos'); await d.wait_for_timeout(300)
        await d.evaluate("document.querySelectorAll('.toast').forEach(t=>t.remove())"); await d.screenshot(path=OUT + 'categoria_graos.png')
        rows = await d.query_selector_all('tr.click'); await rows[0].click(); await d.wait_for_timeout(300)
        await d.evaluate("document.querySelectorAll('.toast').forEach(t=>t.remove())"); await d.screenshot(path=OUT + 'item_historico.png')
        await d.keyboard.press('Escape')
        await d.goto(URL + '#compras'); await d.click('[data-tab="compras:nova"]'); await d.wait_for_timeout(300)
        await d.evaluate("document.querySelectorAll('.toast').forEach(t=>t.remove())"); await d.screenshot(path=OUT + 'compras_form.png')
        await d.goto(URL + '#relatorios'); await d.wait_for_timeout(300)
        await d.evaluate("document.querySelectorAll('.toast').forEach(t=>t.remove())"); await d.screenshot(path=OUT + 'relatorios.png')
        for v in ['itens', 'fornecedores', 'backup', 'gastos', 'feira']:
            await d.goto(URL + '#' + v); await d.wait_for_timeout(200)
        await d.click('[data-a="theme"]'); await d.goto(URL + '#painel'); await d.wait_for_timeout(300)
        await d.evaluate("document.querySelectorAll('.toast').forEach(t=>t.remove())"); await d.screenshot(path=OUT + 'painel_tema_claro.png')
        await b.close()
asyncio.run(main())
print('ERROS:' if errs else 'sem erros de console'); print('\n'.join(errs))
