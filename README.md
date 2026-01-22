# Bookish-Quiz

This is a simple console-based quiz program written in Python.  
The quiz tests the user's knowledge of popular fantasy books and provides immediate feedback for each answer.

---

## Program Description

The program works as follows:

- Reads questions from a CSV file named `questions.csv`.
- Each question has four options and a correct answer.
- All questions are related to popular fantasy books.
- Questions are shuffled randomly for each quiz attempt.
- Displays one question at a time with options labeled A, B, C, D.
- The user enters their answer and receives immediate feedback.
- The score is updated for each correct answer.
- The quiz continues until all questions are answered or the user chooses to exit.

---

## Code Explanation

1. The `csv` module is used to read questions from a CSV file.
2. The `random` module is used to shuffle the order of questions.
3. Each question is stored as a dictionary containing:
   - question text
   - four options
   - the correct answer
4. User input is taken for each question and validated.
5. The program checks the selected answer against the correct answer and updates the score.
6. The user can exit at any time by pressing N or n.
7. At the end, the program displays a thank you message.

---

## How to Run

1. Install Python 3 on your system.
2. Make sure `bookish_quiz.py` and `questions.csv` are in the same folder.
3. Open terminal or command prompt in that folder.
4. Run the program using:

```bash
python bookish_quiz.py