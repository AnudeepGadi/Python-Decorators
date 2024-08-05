# Python Decorators Repository

This repository contains various types of decorators in Python. Decorators are a powerful feature in Python that allows you to modify the behavior of a function or method. Below are the different types of decorators included in this repository:

## Types of Decorators

### 1. Non-Parameterized Decorator
A basic decorator that logs the function name and execution time of any function it decorates.

### 2. Parameterized Decorator
A decorator that takes arguments. In this repository, we have a parameterized decorator that checks if the user has the necessary permissions to execute the function based on their role.

### 3. Class Decorator
A decorator that modifies class behavior. Here, we have a singleton pattern implementation ensuring that a class has only one instance.

### 4. Chaining Multiple Decorators
Decorators that can be chained together to preprocess data, including logging, validation, and data transformation.

### 5. Call Limiting Decorator
A decorator that limits the number of times a function can be called.

## File Structure

- **1_non_parameterized_decorator.py**: Contains the non-parameterized logging decorator.
- **2_parameterized_decorator.py**: Contains the parameterized role-checking decorator.
- **3_class_decorator.py**: Contains the singleton pattern class decorator.
- **4_decorator_chaining.py**: Demonstrates chaining multiple decorators for a data processing pipeline.
- **5_call_limiting_decorator.py**: Contains the decorator that limits the number of times a function can be called.

## Usage

Each Python file in this repository can be run independently to see the decorators in action. Simply clone the repository and run the desired file.

```bash
git clone https://github.com/AnudeepGadi/Python-Decorators.git
cd python-decorators
python 1_non_parameterized_decorator.py
