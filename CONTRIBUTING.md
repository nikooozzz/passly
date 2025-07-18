# Contributing to Passly

Thank you for considering contributing to Passly! We welcome all kinds of contributions, from bug reports to feature requests and code contributions.

---

## How to Contribute

### Report Issues

- Please check existing issues before reporting a new one to avoid duplicates.
- Provide clear descriptions and steps to reproduce bugs.

### Suggesting Features

- Open an issue describing your idea.
- Explain the use case and benefits.

### Submitting Code

1. Fork the repository and clone it locally.
2. Create a new branch for your feature or bugfix:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. Write clear, concise commit messages.
4. Ensure your code follows the existing style and includes tests if applicable.
5. Submit a pull request describing your changes and motivation.


---

## Setup

1. Clone the repo and navigate into it:
    ```bash
    git clone https://github.com/nikooozzz/passly.git
    cd passly
    ```
2. Run the setup to create a virtual environment and install dependencies:
    ```bash
    make setup
    ```
3. Activate the virtual environment:
    ```bash
    source .venv/bin/activate
    ```

---

## Code Style
- Follow PEP 8 for Python code.
- Keep code modular and well-documented.

---

## Running Tests
- Tests use pytest.
- Run them with:
    ```bash
    make test
    ```

---

## Adding New Checks
Passly uses a modular check system:
1. Create a new check in `src/passly/checks/`.
2. Inherit from the base `Check` class in base.py
3. Register your check in `src/passly/checks/__init__.py` by adding it to the CHECKS dictionary.
4. Add corresponding tests in the `tests/` directory.

---

## Communication
- Use GitHub issues and pull requests for discussions.
- Be respectful and constructive.

---

## License
By contributing, you agree that your contributions will be licensed under the MIT License.