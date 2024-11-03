import pytest
from solution import MinStack
from command_processor import process_commands

def test_example_case():
    commands = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
    values = [None, 1, 2, 0, None, None, None, None]
    expected = [None, None, None, None, 0, None, 2, 1]
    
    assert process_commands(commands, values) == expected

def test_single_element():
    commands = ["MinStack", "push", "getMin", "top"]
    values = [None, 42, None, None]
    expected = [None, None, 42, 42]
    
    assert process_commands(commands, values) == expected

def test_negative_numbers():
    commands = ["MinStack", "push", "push", "push", "getMin", "pop", "getMin"]
    values = [None, -2, 0, -3, None, None, None]
    expected = [None, None, None, None, -3, None, -2]
    
    assert process_commands(commands, values) == expected

def test_duplicate_values():
    commands = ["MinStack", "push", "push", "push", "getMin", "pop", "getMin"]
    values = [None, 1, 1, 1, None, None, None]
    expected = [None, None, None, None, 1, None, 1]
    
    assert process_commands(commands, values) == expected

def test_ascending_order():
    commands = ["MinStack", "push", "push", "push", "getMin", "top"]
    values = [None, 1, 2, 3, None, None]
    expected = [None, None, None, None, 1, 3]
    
    assert process_commands(commands, values) == expected

def test_descending_order():
    commands = ["MinStack", "push", "push", "push", "getMin", "top"]
    values = [None, 3, 2, 1, None, None]
    expected = [None, None, None, None, 1, 1]
    
    assert process_commands(commands, values) == expected