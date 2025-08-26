# pages/login_page.py

from playwright.sync_api import Page, expect

class LoginPage:
    """
    Esta classe representa a página de login e contém todos os elementos
    e ações relacionadas a ela.
    """
    def __init__(self, page: Page):
        # O construtor __init__ recebe a 'page' do Playwright como argumento
        # para que possamos interagir com o navegador dentro da classe.
        self.page = page

        # --- Localizadores (Locators) ---
        # Mapeamos os elementos da página que vamos usar.
        # Usar atributos como 'data-test' é uma ótima prática pois eles são feitos para testes
        # e raramente mudam.
        self.username_input = page.locator('[data-test="username"]')
        self.password_input = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')
        self.error_message = page.locator('[data-test="error"]')

    # --- Ações da Página (Actions) ---

    def navigate(self):
        """
        Ação de navegar para a URL de login.
        """
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        """
        Ação de preencher o formulário de login e clicar no botão.
        """
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def assert_error_message(self, expected_message: str):
        """
        Verificação (assertion) para garantir que a mensagem de erro
        correta está visível na tela.
        """
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_have_text(expected_message)