### Armstrong Number Checker

This Python script identifies **Armstrong numbers** within a user-specified range. Armstrong numbers (also known as narcissistic numbers) are numbers that are equal to the sum of their digits raised to the power of the number of digits. For example, `153` is an Armstrong number because (1^3 + 5^3 + 3^3 = 153).

---

#### **Features**
- **Single Number Check**: The script defines a function to determine whether a given number is an Armstrong number.
- **Range Search**: Allows users to find all Armstrong numbers in a given range.
- **Exception Handling**: Validates user inputs and handles errors gracefully, such as:
  - Input that isn't a valid integer.
  - Ranges where the starting number is greater than the ending number.
- **User-Friendly Interaction**: Provides clear error messages and ensures a smooth user experience.

---

#### **How It Works**
1. **Core Functions**:
   - `is_armstrong(num)`: Checks if a single number is an Armstrong number.
   - `check_armstrong(start, end)`: Identifies all Armstrong numbers within the range `[start, end]`.

2. **User Input**:
   - Prompts the user to enter the starting and ending numbers of the range.

3. **Output**:
   - Displays the list of Armstrong numbers in the specified range.
   - If no Armstrong numbers are found, notifies the user.

4. **Error Handling**:
   - Detects invalid inputs, such as non-integer values or incorrectly ordered ranges.
   - Provides informative error messages for easy debugging.

5. **Finally Block**:
   - Ensures a "Thank You" message is displayed after execution, regardless of success or error.

---

#### **Sample Execution**

**Input**:
```
Enter the first number: 1
Enter the last number: 500
```

**Output**:
```
Armstrong numbers between 1 and 500: [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]

Thank you for using the Armstrong number checker!
```

---

#### **Technologies Used**
- **Python**: Core programming language.
- **List Comprehensions**: Simplifies logic for filtering Armstrong numbers.
- **Exception Handling**: Ensures robustness and user-friendly behavior.

---

#### **Usage**
Clone or download the script and run it using Python:
```bash
python armstrong_checker.py
```

---

Feel free to use or modify this description as needed! Let me know if you'd like help refining it further.
