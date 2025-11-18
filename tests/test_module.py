import pytest
from project_template.module import module

def test_function_pass():
    """Test the function"""
    result = module.function()
    assert result == module.function()

def test_function_fail():
    """Test the function"""
    result = module.function()
    assert result != module.function()