# Testing Guide for Flask Application

## Overview
This Flask application uses pytest for testing with comprehensive test coverage and VS Code integration.

## Test Structure

```
tests/
├── __init__.py
├── conftest.py          # Test configuration and fixtures
├── test_models.py       # Unit tests for models
├── test_auth.py         # Integration tests for authentication
└── test_main.py         # Integration tests for main routes
```

## Test Categories

### Unit Tests
- **test_models.py**: Tests for database models (User model, password hashing, etc.)

### Integration Tests
- **test_auth.py**: Tests for authentication flows (login, register, logout)
- **test_main.py**: Tests for main application routes and navigation

## Running Tests

### Command Line

```bash
# Run all tests
./venv/bin/python -m pytest tests/

# Run with verbose output
./venv/bin/python -m pytest tests/ -v

# Run specific test file
./venv/bin/python -m pytest tests/test_models.py -v

# Run specific test method
./venv/bin/python -m pytest tests/test_models.py::TestUserModel::test_user_creation -v

# Run with coverage report
./venv/bin/python -m pytest tests/ --cov=app --cov-report=html

# Run tests with specific markers
./venv/bin/python -m pytest tests/ -m "not slow"
./venv/bin/python -m pytest tests/ -m "integration"
```

### VS Code Integration

1. **Test Explorer**: Use the Test Explorer in VS Code to run and debug tests
2. **Python Testing**: Tests are automatically discovered by the Python extension
3. **Coverage**: View coverage reports in the generated `htmlcov/` directory

## Test Configuration

### pytest.ini (in pyproject.toml)
```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py", "*_test.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = [
    "--verbose",
    "--tb=short",
    "--cov=app",
    "--cov-report=term-missing",
    "--cov-report=html:htmlcov",
    "--cov-fail-under=80"
]
```

### VS Code Settings
```json
{
    "python.testing.pytestEnabled": true,
    "python.testing.unittestEnabled": false,
    "python.testing.pytestArgs": ["tests"],
    "python.testing.autoTestDiscoverOnSaveEnabled": true
}
```

## Test Fixtures

### Available Fixtures (from conftest.py)
- **app**: Flask application instance with test configuration
- **client**: Test client for making HTTP requests
- **auth**: Helper for authentication actions (login, logout, register)
- **test_user**: Pre-created test user in the database

### Usage Example
```python
def test_login(client, test_user):
    """Test user login."""
    response = client.post('/auth/login', data={
        'email': 'test@example.com',
        'password': 'testpass'
    })
    assert response.status_code == 302
```

## Writing New Tests

### Test Naming Convention
- Test files: `test_*.py`
- Test classes: `Test*`
- Test methods: `test_*`

### Example Test
```python
class TestNewFeature:
    """Test cases for new feature."""
    
    def test_feature_works(self, client, app):
        """Test that the feature works correctly."""
        with app.app_context():
            # Test implementation
            pass
    
    @pytest.mark.integration
    def test_feature_integration(self, client, auth):
        """Test feature integration."""
        # Integration test implementation
        pass
```

## Test Markers

- `@pytest.mark.slow`: For slow-running tests
- `@pytest.mark.integration`: For integration tests
- `@pytest.mark.unit`: For unit tests

## Coverage Reports

After running tests with coverage, open `htmlcov/index.html` in your browser to view detailed coverage reports.

## Best Practices

1. **Test Independence**: Each test should be independent and not rely on other tests
2. **Use Fixtures**: Leverage pytest fixtures for common setup
3. **Clear Test Names**: Test names should clearly describe what is being tested
4. **Test Both Success and Failure**: Test both positive and negative cases
5. **Mock External Dependencies**: Use mocks for external services
6. **Keep Tests Fast**: Unit tests should run quickly

## Troubleshooting

### Common Issues
1. **Database Errors**: Make sure test database is properly isolated
2. **Import Errors**: Ensure all required packages are installed
3. **Configuration Issues**: Check that test configuration is correct

### Debug Tests
```bash
# Run with pdb debugger
./venv/bin/python -m pytest tests/ --pdb

# Run with detailed output
./venv/bin/python -m pytest tests/ -vvv --tb=long
```
