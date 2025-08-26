# 🤖 Projeto de Automação de Testes Web com Playwright

Projeto de portfólio que demonstra a automação de testes funcionais para o site de e-commerce de demonstração [SauceDemo](https://www.saucedemo.com/).

## ✨ Tecnologias Utilizadas

* **Linguagem:** ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
* **Framework de Automação:** ![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)
* **Framework de Testes:** ![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
* **CI/CD:** ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)

## 🧪 Cenários de Teste Automatizados

-   [x] **Login com sucesso:** Verifica se um usuário com credenciais válidas consegue acessar a página de produtos.
-   [x] **Login com falha:** Verifica se a mensagem de erro correta é exibida ao tentar logar com uma senha inválida.
-   [x] **Adicionar produto ao carrinho:** Verifica se é possível adicionar um item ao carrinho e se o contador é atualizado corretamente.

## ⚙️ Como Executar o Projeto Localmente

### Pré-requisitos
* Python 3.8+
* Git

### Passos para Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Caio-Aleixo/automacao_testes_saucedemo.git](https://github.com/Caio-Aleixo/automacao_testes_saucedemo.git)
    cd automacao_testes_saucedemo
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```
    > **Nota para usuários Windows:** Se encontrar um erro de execução de scripts ao ativar o venv, execute o seguinte comando no PowerShell (como administrador) e tente novamente:
    > `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`

3.  **Instale as dependências e os navegadores:**
    ```bash
    python -m pip install -r requirements.txt
    playwright install
    ```

### Executando os Testes

Para rodar todos os testes em modo "visível" (com o navegador abrindo):
```bash
python -m pytest
```

Para gerar o relatório HTML dos resultados:
```bash
python -m pytest --html=report.html
```

## 🚀 Pipeline de CI/CD

Este projeto utiliza GitHub Actions para integração contínua. Os testes são executados automaticamente a cada `push` ou `pull request` para a branch `main`. O relatório de testes fica disponível como um artefato para download ao final de cada execução bem-sucedida ou com falha.

Você pode ver as execuções na aba **[Actions](https://github.com/Caio-Aleixo/automacao_testes_saucedemo/actions)** do repositório.

---

*Projeto desenvolvido como guia e peça de portfólio na área de Quality Assurance.*
