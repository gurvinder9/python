# Makefile for Python Project Development
.PHONY: help install lint format test pre-commit-setup clean run-learning run-project

# Default target
help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Installation and setup
install: ## Install project dependencies
	python3 -m pip install -r src/requirements.txt

pre-commit-setup: ## Install pre-commit hooks
	pre-commit install

setup: install pre-commit-setup ## Full setup: install dependencies and pre-commit hooks

# Code quality
lint: ## Run linting (flake8)
	flake8 src/ basic/ --max-line-length=88 --extend-ignore=E203,W503

format: ## Format code with black and isort
	black src/ basic/ --line-length=88
	isort src/ basic/ --profile=black

format-check: ## Check if code needs formatting
	black src/ basic/ --line-length=88 --check
	isort src/ basic/ --profile=black --check-only

security-check: ## Run security check with bandit
	bandit -r src/ basic/ -f json || true

# Testing
test: ## Run tests
	python3 -m pytest src/tests/ -v

# Pre-commit
pre-commit: ## Run pre-commit hooks on all files
	pre-commit run --all-files

pre-commit-update: ## Update pre-commit hooks
	pre-commit autoupdate

# Running the project
run-learning: ## Run learning examples
	@echo "Running Python learning examples..."
	@for file in basic/0*.py; do \
		echo "\n=== Running $$file ==="; \
		python3 "$$file"; \
	done

run-project: ## Run the main project
	cd src && python3 main.py

# Cleanup
clean: ## Clean up temporary files
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name ".pytest_cache" -delete
	find . -type f -name ".mypy_cache" -delete

# Development workflow
dev-setup: setup format-check lint security-check ## Complete development setup with quality checks

check: format-check lint security-check ## Check code quality without making changes

# Quick development commands
quick-format: ## Quick format all Python files
	black . --line-length=88
	isort . --profile=black

quick-lint: ## Quick lint all Python files
	flake8 . --max-line-length=88 --extend-ignore=E203,W503
