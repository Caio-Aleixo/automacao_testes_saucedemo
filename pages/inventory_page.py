# pages/inventory_page.py

from playwright.sync_api import Page, expect

class InventoryPage:
    """
    Esta classe representa a página de inventário (produtos) e contém
    os elementos e ações relevantes.
    """
    def __init__(self, page: Page):
        self.page = page

        # --- Localizadores (Locators) ---
        self.page_title = page.locator('.title')
        # Localizador específico para o botão de adicionar a mochila ao carrinho
        self.add_to_cart_button = page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')
        # Localizador para o ícone do carrinho que mostra a quantidade de itens
        self.shopping_cart_badge = page.locator('.shopping_cart_badge')

    # --- Ações da Página (Actions) ---

    def assert_on_inventory_page(self):
        """
        Verifica se o usuário está de fato na página de inventário,
        checando o título e a URL.
        """
        expect(self.page_title).to_have_text("Products")
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")

    def add_backpack_to_cart(self):
        """
        Ação de clicar no botão "Add to cart" da mochila.
        """
        self.add_to_cart_button.click()

    def assert_cart_item_count(self, count: int):
        """
        Verifica se o número exibido no ícone do carrinho
        corresponde à contagem esperada.
        """
        expect(self.shopping_cart_badge).to_have_text(str(count))