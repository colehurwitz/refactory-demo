# Factory Configuration

## Project
- **Name:** refactory-demo
- **Type:** Python CLI application
- **Description:** A simple command-line calculator

## Eval
Run tests and check lint:
```bash
python -m pytest tests/ -v
python -m py_compile calculator.py
```

## Guards
- Do not modify .factory/ directory
- Keep all calculator functions in calculator.py
- Keep all tests in tests/test_calculator.py
