# Contributing Guide

Thank you for your interest in contributing to this Python project! This guide will help you get started with development and ensure your contributions follow our standards.

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Git

### Setup

1. **Clone the repository** (if you haven't already)
   ```bash
   git clone <repository-url>
   cd python-project
   ```

2. **Install dependencies and pre-commit hooks**
   ```bash
   make setup
   # or manually:
   # pip install -r src/requirements.txt
   # pre-commit install
   ```

3. **Verify the setup**
   ```bash
   make dev-setup
   ```

## 🛠️ Development Workflow

### Code Quality Standards

This project uses several tools to maintain code quality:

- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Code linting
- **bandit**: Security checks
- **pre-commit**: Git hooks for automated quality checks

### Running Quality Checks

```bash
# Run all quality checks
make check

# Format code
make format

# Run linting
make lint

# Security check
make security-check

# Run pre-commit hooks on all files
make pre-commit
```

### Development Commands

```bash
# Run learning examples
make run-learning

# Run main project
make run-project

# Run tests
make test

# Clean temporary files
make clean
```

## 📝 Contributing Guidelines

### For Learning Materials (`basic/` folder)

1. **Code Examples**: Create clear, well-commented examples
2. **File Naming**: Use descriptive names like `05_functions_and_classes.py`
3. **Documentation**: Include docstrings and comments explaining concepts
4. **Consistency**: Follow the existing pattern in numbered files

### For Main Project (`src/` folder)

1. **Code Style**: Follow PEP 8 guidelines
2. **Type Hints**: Use type hints where appropriate
3. **Documentation**: Add docstrings for functions and classes
4. **Tests**: Include unit tests for new functionality

### Commit Guidelines

- Use descriptive commit messages
- Keep commits focused on a single change
- Reference issues in commit messages when applicable
- The pre-commit hooks will run automatically and must pass

### Pull Request Process

1. **Create a feature branch** from `main`
2. **Make your changes** following the guidelines above
3. **Ensure all checks pass**:
   ```bash
   make dev-setup
   ```
4. **Create a pull request** with a clear description
5. **Wait for review** and address any feedback

## 🧪 Testing

### Running Tests

```bash
# Run all tests
make test

# Run specific test file
python -m pytest src/tests/test_specific.py -v
```

### Writing Tests

- Place tests in `src/tests/` directory
- Use descriptive test names
- Test both success and failure cases
- Aim for good test coverage

## 🐛 Bug Reports

When reporting bugs, please include:

1. **Description**: Clear description of the bug
2. **Steps to Reproduce**: Step-by-step instructions
3. **Expected Behavior**: What should happen
4. **Actual Behavior**: What actually happens
5. **Environment**: Python version, OS, etc.

## 💡 Feature Requests

For feature requests:

1. **Check existing issues** to avoid duplicates
2. **Describe the feature** clearly
3. **Explain the use case** and benefits
4. **Include examples** if possible

## 📚 Style Guide

### Python Code Style

- Follow PEP 8
- Use Black for formatting (line length: 88)
- Use meaningful variable and function names
- Write clear docstrings following Google style

### Learning Materials Style

- Include clear explanations with examples
- Use comments to explain complex concepts
- Provide progressive difficulty levels
- Include "Try it yourself" sections

## 🤝 Community Guidelines

- Be respectful and inclusive
- Help others learn and grow
- Provide constructive feedback
- Follow the project's code of conduct

## 📞 Getting Help

- **Documentation**: Check the README files
- **Issues**: Open an issue for questions or bugs
- **Discussions**: Use GitHub discussions for general questions

## 🎉 Recognition

Contributors will be recognized in:
- CONTRIBUTORS.md file
- Release notes
- Project README

Thank you for contributing! 🐍✨
