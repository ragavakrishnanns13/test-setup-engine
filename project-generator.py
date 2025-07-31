import os
import sys
import subprocess

def install_packages(requirements_path):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_path])
        print("Packages installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install packages: {e}")

def create_file(path, content=""):
    with open(path, 'w') as f:
        f.write(content)

def create_project_structure(base_path, framework_type, browser_type="Chrome", headless=False, reporting_tool="pytest-html", ci_cd_tool=None):
    folders = ['tests', 'pages', 'locators', 'data', 'utils', 'reports', 'features', 'features/steps']
    for folder in folders:
        os.makedirs(os.path.join(base_path, folder), exist_ok=True)

    # Requirements
    requirements_content = "selenium\npytest\n"
    if reporting_tool == "allure":
        requirements_content += "allure-pytest\n"
    else:
        requirements_content += "pytest-html\n"
    requirements_content += "python-dotenv\n"
    if framework_type == "BDD":
        requirements_content += "pytest-bdd\n"
    if browser_type.lower() == "firefox":
        requirements_content += "selenium-firefox\n"
    create_file(os.path.join(base_path, 'requirements.txt'), requirements_content)

    # .env file
    create_file(os.path.join(base_path, '.env'), "BASE_URL=https://example.com\n")

    # config.py
    config_content = (
        "from dotenv import load_dotenv\n"
        "import os\n\n"
        "load_dotenv()\n"
        "BASE_URL = os.getenv(\"BASE_URL\")\n"
        f"BROWSER_TYPE = '{browser_type}'\n"
        f"HEADLESS = {str(headless).lower()}\n"
    )
    create_file(os.path.join(base_path, 'utils', 'config.py'), config_content)

    # logger.py
    logger_content = (
        "import logging\n\n"
        "logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')\n"
        "logger = logging.getLogger(__name__)\n"
    )
    create_file(os.path.join(base_path, 'utils', 'logger.py'), logger_content)
    # conftest.py
    conftest_content = (
        "import pytest\n"
        "from selenium import webdriver\n"
        "from utils.config import BROWSER_TYPE, HEADLESS\n\n"
        "def pytest_configure(config):\n"
        f"    config.option.htmlpath = 'reports/report.html'\n"
        "@pytest.fixture\n"
        "def driver():\n"
        f"    if BROWSER_TYPE.lower() == 'firefox':\n"
        "        options = webdriver.FirefoxOptions()\n"
        "        if HEADLESS:\n"
        "            options.add_argument('--headless')\n"
        "        driver = webdriver.Firefox(options=options)\n"
        "    else:\n"
        "        options = webdriver.ChromeOptions()\n"
        "        if HEADLESS:\n"
        "            options.add_argument('--headless')\n"
        "        driver = webdriver.Chrome(options=options)\n"
        "    yield driver\n"
        "    driver.quit()\n"
    )
    create_file(os.path.join(base_path, 'conftest.py'), conftest_content)

    # README.md
    readme_content = (
        "# Selenium Test Automation Framework\n\n"
        "## Features\n"
        "- Supports Keyword-driven, Data-driven, Hybrid, and BDD frameworks\n"
        "- Page Object Model (POM) structure\n"
        "- Logging and environment configuration using dotenv\n"
        f"- HTML test reports with {reporting_tool}\n"
        "- BDD support with pytest-bdd\n\n"
        "## Setup Instructions\n"
        "1. Create a virtual environment:\n"
        "   python -m venv venv\n\n"
        "2. Activate the virtual environment:\n"
        "   - Windows: venv\\Scripts\\activate\n"
        "   - macOS/Linux: source venv/bin/activate\n\n"
        "3. Install dependencies:\n"
        "   pip install -r requirements.txt\n\n"
        "4. Run tests:\n"
        "   pytest\n"
    )
    create_file(os.path.join(base_path, 'README.md'), readme_content)

    # Base page
    base_page_content = (
        "from selenium.webdriver.support.ui import WebDriverWait\n"
        "from selenium.webdriver.support import expected_conditions as EC\n\n"
        "class BasePage:\n"
        "    def __init__(self, driver):\n"
        "        self.driver = driver\n\n"
        "    def find_element(self, locator, timeout=10):\n"
        "        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))\n"
    )
    create_file(os.path.join(base_path, 'pages', 'base_page.py'), base_page_content)

    # Sample test
    test_sample_content = (
        "import pytest\n"
        "from selenium import webdriver\n\n"
        "@pytest.fixture\n"
        "def driver():\n"
        "    driver = webdriver.Chrome()\n"
        "    yield driver\n"
        "    driver.quit()\n\n"
        "def test_sample(driver):\n"
        "    driver.get(\"https://example.com\")\n"
        "    assert \"Example Domain\" in driver.title\n"
    )
    create_file(os.path.join(base_path, 'tests', 'test_sample.py'), test_sample_content)

    # BDD feature file
    if framework_type == "BDD":
        feature_content = (
            "Feature: Example feature\n"
            "  Scenario: Open example.com and check title\n"
            "    Given the browser is open\n"
            "    When I navigate to \"https://example.com\"\n"
            "    Then the page title should be \"Example Domain\"\n"
        )
        create_file(os.path.join(base_path, 'features', 'example.feature'), feature_content)

        # BDD step definitions
        steps_content = (
            "from pytest_bdd import scenarios, given, when, then\n"
            "from selenium import webdriver\n\n"
            "scenarios('../example.feature')\n\n"
            "@given(\"the browser is open\")\n"
            "def browser_open():\n"
            "    driver = webdriver.Chrome()\n"
            "    return driver\n\n"
            "@when('I navigate to \"https://example.com\"')\n"
            "def navigate(driver):\n"
            "    driver.get(\"https://example.com\")\n\n"
            "@then('the page title should be \"Example Domain\"')\n"
            "def check_title(driver):\n"
            "    assert \"Example Domain\" in driver.title\n"
            "    driver.quit()\n"
        )
        create_file(os.path.join(base_path, 'features', 'steps', 'test_example_steps.py'), steps_content)

    # Framework-specific additions
    if framework_type == "Keyword-driven":
        keyword_engine = (
            "class KeywordEngine:\n"
            "    def __init__(self, driver):\n"
            "        self.driver = driver\n\n"
            "    def execute_keyword(self, keyword, *args):\n"
            "        if keyword == \"open_url\":\n"
            "            self.driver.get(args[0])\n"
            "        elif keyword == \"click\":\n"
            "            self.driver.find_element(*args).click()\n"
            "        elif keyword == \"type\":\n"
            "            self.driver.find_element(*args[:2]).send_keys(args[2])\n"
        )
        create_file(os.path.join(base_path, 'utils', 'keyword_engine.py'), keyword_engine)

    elif framework_type == "Data-driven":
        data_sample = (
            "import csv\n"
            "def read_test_data(file_path):\n"
            "    with open(file_path, newline='') as csvfile:\n"
            "        reader = csv.DictReader(csvfile)\n"
            "        return [row for row in reader]\n"
        )
        create_file(os.path.join(base_path, 'data', 'test_data.csv'), "url,title\nhttps://example.com,Example Domain\n")
        create_file(os.path.join(base_path, 'utils', 'data_reader.py'), data_sample)

    elif framework_type == "Hybrid":
        hybrid_note = "# Hybrid framework combines keyword and data-driven approaches.\n"
        create_file(os.path.join(base_path, 'utils', 'hybrid_note.txt'), hybrid_note)

    # CI/CD Integration
    if ci_cd_tool:
        if ci_cd_tool == "github":
            os.makedirs(os.path.join(base_path, '.github', 'workflows'), exist_ok=True)
            github_actions_content = (
                "name: CI\n\n"
                "on: [push]\n\n"
                "jobs:\n"
                "  build:\n"
                "    runs-on: ubuntu-latest\n"
                "    steps:\n"
                "    - uses: actions/checkout@v2\n"
                "    - name: Set up Python\n"
                "      uses: actions/setup-python@v2\n"
                "      with:\n"
                "        python-version: '3.8'\n"
                "    - name: Install dependencies\n"
                "      run: |\n"
                "        python -m pip install --upgrade pip\n"
                "        pip install -r requirements.txt\n"
                "    - name: Test with pytest\n"
                "      run: pytest\n"
            )
            create_file(os.path.join(base_path, '.github', 'workflows', 'ci.yml'), github_actions_content)

    # Optional Git initialization
    os.system(f'cd "{base_path}" && git init')

def main():
    print("Welcome to Selenium Project Generator")
    print("Select the framework type:")
    print("1. Keyword-driven")
    print("2. Data-driven")
    print("3. Hybrid")
    print("4. BDD")
    choice = input("Enter your choice (1/2/3/4): ").strip()
    framework_map = {"1": "Keyword-driven", "2": "Data-driven", "3": "Hybrid", "4": "BDD"}
    framework_type = framework_map.get(choice)
    if not framework_type:
        print("Invalid choice. Exiting.")
        sys.exit(1)

    project_name = input("Enter the project name: ").strip()
    project_location = input("Enter the full path where the project should be created: ").strip()
    browser_type = input("Enter the browser type (Chrome/Firefox): ").strip() or "Chrome"
    headless_input = input("Run in headless mode? (y/n): ").strip().lower()
    headless = headless_input == 'y'
    reporting_tool = input("Choose reporting tool (pytest-html/allure): ").strip().lower() or "pytest-html"
    ci_cd_input = input("Add CI/CD configuration? (github/none): ").strip().lower() or "none"
    ci_cd_tool = ci_cd_input if ci_cd_input != "none" else None

    base_path = os.path.join(project_location, project_name)
    if os.path.exists(base_path):
        print("Project directory already exists. Exiting.")
        sys.exit(1)

    os.makedirs(base_path)
    create_project_structure(base_path, framework_type, browser_type, headless, reporting_tool, ci_cd_tool)

    # Install packages
    requirements_path = os.path.join(base_path, 'requirements.txt')
    install_packages(requirements_path)

    print(f"\n {framework_type} Selenium project '{project_name}' created successfully at {base_path}")

if __name__ == "__main__":
    main()

# test engine setup
