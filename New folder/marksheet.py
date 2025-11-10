# ### **Question Title:**  
# **Create a Marksheet Program with Grade Calculation**


# ### **Problem Statement:**

# Write a Python program that:

# 1. Takes input for a student's details:
#    - Name
#    - Roll Number
#    - Class
#    - Marks in 5 subjects (out of 100 each):
#      - English
#      - Math
#      - Science
#      - Social Studies
#      - Second Language

# 2. Calculates:
#    - **Total marks** (out of 500)
#    - **Percentage**
#    - **Grade** based on the following criteria:
#      ```
#      90% and above → A+
#      80% to 89%   → A
#      70% to 79%   → B+
#      60% to 69%   → B
#      50% to 59%   → C
#      Below 50%    → F (Fail)
#      ```

# 3. Checks if the student **passed** (must score ≥ 40 in each subject).

# 4. Displays a **formatted marksheet** like this:

# ```
# ========================================
#            STUDENT MARKSHEET
# ========================================
# Name           : John Doe
# Roll No        : 101
# Class          : 10th

# Subject          Marks
# -------------------------
# English          85
# Math             92
# Science          78
# Social Studies   88
# Second Language  75

# Total          : 418 / 500
# Percentage     : 83.60%
# Grade          : A
# Result         : PASS
# ========================================
# ```

# ---

# ### **Requirements:**

# - Use **dictionary** or **list** to store subject marks.
# - Use **functions** for:
#   - Input
#   - Calculate total & percentage
#   - Determine grade
#   - Check pass/fail
#   - Print marksheet
# - Input validation: marks should be between 0 and 100.
# - Handle invalid input gracefully.

# ---

# ### **More Requiremnts:**
# - Allow input for **multiple students** and generate marksheets for all.

# ---

# ### **Sample Input:**
# ```
# Enter Name: Alice
# Enter Roll No: 205
# Enter Class: 9th
# Enter marks for English: 95
# Enter marks for Math: 88
# Enter marks for Science: 91
# Enter marks for Social Studies: 79
# Enter marks for Second Language: 85
# ```

# ---

# **Test your code with edge cases:**
# - All 100s → A+
# - Marks = 0 or 101 → Invalid input

# ---

# *(You can use functions, loops, conditionals, formatting, and file handling.)*