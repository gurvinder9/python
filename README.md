# Python Project with Learning Materials

This repository contains a Python project with two main components:

## 📁 Project Structure

```
python/
├── src/                    # Main project source code
│   ├── main.py            # Entry point for the application
│   ├── requirements.txt   # Project dependencies
│   ├── __init__.py        # Package initialization
│   └── .gitignore         # Git ignore rules for src
├── basic/                  # Python learning materials for beginners
│   ├── 01_variables_and_types.py
│   ├── 02_input_output.py
│   ├── 03_operators.py
│   ├── 04_control_flow.py
│   ├── 05_loop.py
│   ├── 06_dict.py
│   ├── 06_dict-method.py
│   ├── 07_list.py
│   ├── 07_list-method.py
│   ├── 08_list-comprehension.py
│   ├── 09_dict-comprehension.py
│   ├── 10_tuple.py
│   ├── 11_sets.py
│   └── README.md          # Learning guide
├── .pre-commit-config.yaml # Pre-commit hooks configuration
├── .cursorrules            # Cursor IDE rules and guidelines
├── Makefile               # Development commands
├── CONTRIBUTING.md         # Contributing guidelines
└── README.md              # This file - project overview
```

## 🚀 Getting Started

### For Learning Python (Beginners)

1. **Navigate to the basic folder:**
   ```bash
   cd basic
   ```

2. **Start with the learning sequence:**
   - `01_variables_and_types.py` - Learn about variables and data types
   - `02_input_output.py` - Understand input and output operations
   - `03_operators.py` - Master Python operators
   - `04_control_flow.py` - Learn conditional statements and loops
   - `05_loop.py` - Comprehensive loop tutorial with examples
   - `06_dict.py` - Dictionary basics and concepts
   - `06_dict-method.py` - Dictionary methods and advanced patterns
   - `07_list.py` - List basics and concepts
   - `07_list-method.py` - List methods and advanced patterns
   - `08_list-comprehension.py` - List comprehensions tutorial
   - `09_dict-comprehension.py` - Dictionary comprehensions tutorial
   - `10_tuple.py` - Tuple basics and when to use them
   - `11_sets.py` - Set basics and when to use them

3. **Run the examples:**
   ```bash
   python basic/01_variables_and_types.py
   # or
   cd basic && python 01_variables_and_types.py
   ```

### For Development (Main Project)

#### Quick Setup

```bash
# Install all dependencies and setup pre-commit hooks
make setup

# Or manually:
pip install -r src/requirements.txt
pre-commit install
```

#### Running the Project

```bash
# Using Makefile (recommended)
make run-project

# Or manually
cd src
python main.py
```

## 📚 Learning Path

The `basic/` folder provides a structured learning path:

1. **Variables & Data Types** - Foundation of Python variables
2. **Input/Output** - User interaction basics
3. **Operators** - Mathematical and logical operations
4. **Control Flow** - Conditional statements and loops
5. **Loops** - Comprehensive loop tutorial with practical examples
6. **Dictionaries** - Key-value pairs and data organization
7. **Dictionary Methods** - Advanced dictionary operations and patterns
8. **Lists** - Ordered collections and data manipulation
9. **List Methods** - Advanced list operations and patterns
10. **List Comprehensions** - Concise list creation and transformation
11. **Dictionary Comprehensions** - Concise dictionary creation and transformation
12. **Tuples** - Immutable sequences and when to use them
13. **Sets** - Unique collections and fast membership testing

## 🛠️ Development Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Git
- Make (optional, for using Makefile commands)

### Code Quality Tools

This project uses several tools to maintain code quality:

- **pre-commit**: Automated hooks that run before each commit
- **Black**: Code formatting
- **flake8**: Code linting
- **isort**: Import sorting
- **bandit**: Security checks

#### Commands

```bash
# Complete setup (dependencies + pre-commit hooks)
make setup

# Run all quality checks
make check

# Format code
make format

# Run pre-commit hooks on all files
make pre-commit

# Complete development setup with all checks
make dev-setup

# See all available commands
make help
```

## 📖 Documentation

- **Learning Materials**: See `basic/README.md` for detailed learning instructions
- **Source Code**: Check `src/` folder for the main project files
- **Development Guidelines**: See `CONTRIBUTING.md` for contribution guidelines
- **IDE Configuration**: `.cursorrules` file provides Cursor IDE with project-specific rules
- **Main README**: This file provides project overview and setup instructions

## 🤝 Contributing

1. For learning materials: Add new examples to the `basic/` folder
2. For main project: Enhance the `src/` folder with your application logic
3. Follow Python best practices and PEP 8 style guidelines

## 📝 License

This project is open source and available under the MIT License.

---

**Happy Coding!** 🐍 Whether you're learning Python or developing with it, this project structure supports both paths.
