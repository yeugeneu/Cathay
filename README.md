# Python Code Examples

This repository contains two Python scripts demonstrating different programming concepts.

## Environment
- Python 3

## 1. Print Triangle (triangle.py)
請設計一個函數，輸入為數字，輸出則為*符號為輸入數字邊長的空心正三角形。

輸入: 3

輸出：
```
  *
 * *
* * *
```

This script prints a triangle pattern of a specified size using star sign.

### Features:
- Prints a triangle with a user-defined size
- Handles edge cases (size <= 0 and size == 1)
- Creates a hollow triangle for sizes greater than 2

### Usage:
1. Run the script
2. Enter the desired size of the triangle when prompted
3. The script will print the triangle pattern

## 2. Reorder Odd and Even Numbers (reorder-odd-even-numbers.py)
國泰國中的老師出了一道題目給同學們練習，同學們自己設定一串奇偶混和地亂數，並將數字依照"奇數都在偶數前面"，且"偶數升冪排序"，"奇數降冪排序"。例如 '417324689435' 將會變成 '975331244468'。然而，班上有50位學生，每一個同學給出的數字長度不一，老師希望能用一段小程式來幫助他驗證答案，請你寫一個函數幫幫老師吧!

This script reorders the digits of a given number by placing odd digits in descending order followed by even digits in ascending order.

### Features:
- Separates odd and even digits
- Sorts odd digits in descending order
- Sorts even digits in ascending order
- Combines the sorted digits into a new number

### Usage:
1. Run the script
2. Enter a random number when prompted
3. The script will output the reordered number

## 3. POSTMAN Collection & Environment
This folder contains the POSTMAN colleciton and the environment file. Simply import them into POSTMAN to execute.

## 4. Pytest API Automation
This folder contains a Python script for automated API testing using pytest.

### Features:
- Tests the Star Wars API (SWAPI) endpoints
- Validates response status codes, schemas, and content
- Checks response times
- Verifies data formats and structures

### Requirements:
- Python 3.x
- pip (Python package installer)

### Installation:
1. Navigate to the "4. Pytest API Automation" directory
2. Install the required packages using pip:
   ```
   pip install -r requirements.txt
   ```

### Usage:
1. Navigate to the "4. Pytest API Automation" directory
2. Run the tests using pytest:
   ```
   pytest API_Automation.py
   ```

### Test Cases:
- Get all films API endpoint
- Get a specific film API endpoint
- Attempt to get a non-existent film with invalid ID

Each test case includes multiple assertions to thoroughly validate the API responses.

