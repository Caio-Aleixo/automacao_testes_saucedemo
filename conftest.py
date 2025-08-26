# conftest.py

import pytest
from playwright.sync_api import sync_playwright, Page

@pytest.fixture(scope="function")
def page() -> Page:
    """
    Esta fixture cria uma nova página do navegador para cada teste.
    'scope="function"' garante que cada teste receba uma página limpa e isolada.
    """
    with sync_playwright() as p:
        # headless=False faz com que o navegador seja aberto com interface gráfica,
        # para que possamos ver a execução. Mude para True para rodar em modo "invisível".
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        # 'yield' entrega a página para o teste que a solicitou.
        yield page
        # O código após o 'yield' é executado ao final do teste, garantindo
        # que o navegador seja sempre fechado.
        browser.close()