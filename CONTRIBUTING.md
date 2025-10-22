# Contributing to DUK Transport Integration

Thank you for your interest in contributing to the DUK Transport Home Assistant integration! 

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- Home Assistant development environment
- Git

### Development Setup

1. **Fork the repository**
2. **Clone your fork:**
   ```bash
   git clone https://github.com/Peta01/ha-duk-transport.git
   cd ha-duk-transport
   ```

3. **Create development environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   # or
   .venv\Scripts\activate  # Windows
   ```

4. **Install development dependencies:**
   ```bash
   pip install -r requirements-dev.txt
   ```

## 🔧 Development Guidelines

### Code Style
- Follow [PEP 8](https://pep8.org/)
- Use [Black](https://black.readthedocs.io/) for formatting
- Use [isort](https://pycqa.github.io/isort/) for import sorting
- Type hints are encouraged

### Testing
- Write tests for new features
- Ensure all tests pass before submitting PR
- Test with Home Assistant development environment

### Documentation
- Update README.md if needed
- Add docstrings to new functions/classes
- Update CHANGELOG.md

## 📝 Pull Request Process

1. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
3. **Test thoroughly**
4. **Commit with clear messages:**
   ```bash
   git commit -m "feat: add support for real-time delays"
   ```

5. **Push and create PR:**
   ```bash
   git push origin feature/your-feature-name
   ```

## 🐛 Bug Reports

When reporting bugs, please include:

- Home Assistant version
- Integration version
- Steps to reproduce
- Expected behavior
- Actual behavior
- Log files (with debug enabled)

## 💡 Feature Requests

- Check existing issues first
- Describe the feature clearly
- Explain the use case
- Consider implementation complexity

## 📋 Code Review

All submissions require review. We use GitHub pull requests for this process.

## 🏷️ Commit Convention

We use [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` new features
- `fix:` bug fixes
- `docs:` documentation changes
- `style:` formatting changes
- `refactor:` code refactoring
- `test:` test additions/changes
- `chore:` maintenance tasks

## 🙏 Recognition

Contributors will be recognized in:
- README.md contributors section
- GitHub contributors page
- Release notes for significant contributions

Thank you for contributing! 🎉