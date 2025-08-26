# tests/test_saucedemo.py

from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# --- Casos de Teste ---

def test_successful_login(page: Page):
    """
    Caso de teste: Login com credenciais válidas.
    Verifica se o usuário é redirecionado para a página de produtos.
    """
    # 1. Preparação: Instanciar as Page Objects
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    # 2. Execução: Realizar as ações
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # 3. Verificação: Checar o resultado esperado
    inventory_page.assert_on_inventory_page()


def test_failed_login_with_wrong_password(page: Page):
    """
    Caso de teste: Login com senha inválida.
    Verifica se a mensagem de erro correta é exibida.
    """
    # 1. Preparação
    login_page = LoginPage(page)

    # 2. Execução
    login_page.navigate()
    login_page.login("standard_user", "wrong_password")

    # 3. Verificação
    expected_error = "Epic sadface: Username and password do not match any user in this service"
    login_page.assert_error_message(expected_error)


def test_add_item_to_cart(page: Page):
    """
    Caso de teste: Adicionar um item ao carrinho.
    Verifica se o contador do carrinho é atualizado para 1.
    """
    # 1. Preparação
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    # Pré-condição: Estar logado para poder adicionar itens ao carrinho
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.assert_on_inventory_page()

    # 2. Execução
    inventory_page.add_backpack_to_cart()

    # 3. Verificação
    inventory_page.assert_cart_item_count(1)