## The process of Test Driven Development (TDD)
- **Write a failing test first** define your desired behavior, and ensure a failing test first. When it fails the initial write you know it is a good test. Avoids false positives (example if you write a test that has no fail condition)
- **Write minimal code to pass** before building onto the function we want to ensure a tests exists for new behavior.
- **Refactor** potentially identify complexity in code that you can now refactor and then you have the tests to ensure behavior is consistent.

## Why we test

- **Catch regressions.** Change code later without breaking what worked.
- **Document behavior.** A test says what a function is *supposed* to do.
- **Refactor with confidence.** Green tests mean you didn't break anything.


## Arrange, Act, Assert

- **Arrange** Setup expected data, input data to test, any other variables you might need
- **Act** Execute and capture code output. Run your code with test input.
- **Assert** Assert the actual output matches your expected output.

## Project Setup

# 2. install pytest
`pip install pytest`

# 3. confirm it works
`pytest`
