# 0x07. Python - Test-driven development

Test-driven development (TDD) is a software development approach in which tests are written before the actual code. The TDD cycle typically involves the following steps:

1. Write a Test: In this step, you write a test that describes a small piece of functionality of your program. This test should initially fail since you haven't implemented the functionality yet.

2. Run the Test: Execute all the tests, including the new one you just wrote. The new test should fail, indicating that the functionality it describes hasn't been implemented yet.

3. Write Code: Now, write the minimum amount of code necessary to make the test pass. Don't worry about writing the most elegant or efficient code at this stage; the goal is just to make the test pass.

4. Run the Test Suite: Once you've implemented the code, run all the tests again. Ensure that the new test and all existing tests pass. If any test fails, go back and make adjustments to your code.

5. Refactor Code: If all tests pass, you can refactor your code to make it more readable, maintainable, or efficient. After each refactoring, run the test suite again to ensure you haven't introduced any errors.

6. Repeat: Repeat this cycle for each new piece of functionality you want to add or modify.
