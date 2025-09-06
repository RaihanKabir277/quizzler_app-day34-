# Quizzler App 🎯

A Python-based **True/False Quiz Application** built with **Object-Oriented Programming (OOP)** and **Tkinter GUI**.  
The app fetches live trivia questions from the **Open Trivia Database API** and presents them in a clean, interactive interface.

---

## 🚀 Features
- Fetches **real-time questions** from the [Open Trivia Database](https://opentdb.com/).
- **Multiple components** designed with OOP:
  - `Question` → data model for each question  
  - `QuizBrain` → logic engine for quiz control  
  - `QuizInterface` → graphical user interface with Tkinter  
- **Dynamic score tracking** during the quiz.  
- **Instant feedback** (green for correct, red for wrong).  
- **Auto progress** to the next question after a short delay.  
- Disables buttons once the quiz ends with a final score display.  

---

## 📂 Project Structure

Quizzler-App/
- │── main.py # Entry point, initializes the quiz
- │── data.py # Fetches trivia questions from API
- │── question_model.py # Defines Question class
- │── quiz_brain.py # Quiz logic (score, question handling)
- │── ui.py # Tkinter interface
- │── images/
- │ ├── true.png
- │ └── false.png
- │── README.md # Project documentation

# Install dependencies:

pip install requests

# How It Works

1.data.py → Fetches 15 computer science True/False questions from the OpenTDB API.
2.question_model.py → Wraps each question into a Question object.
3.quiz_brain.py → Controls quiz flow, scoring, and answer validation.
4.ui.py → Displays questions in a Tkinter window, handles user interaction, and provides feedback.
5.main.py → Ties everything together

# Demo Question Flow

1.Question is displayed in the canvas.
2.User clicks ✅ True or ❌ False.
3.Background flashes:

    - '🟩 Green → Correct
    - '🟥 Red → Incorrect

4.After 1 second, the next question appears automatically.
5.Once all questions are answered → final score displayed & buttons are disabled.

## 🕹️ Tech Stack

This project utilizes the following technologies:

* **Python 3:** The core programming language.
* **Tkinter:** A standard Python library for creating the graphical user interface (GUI).
* **Requests:** A library used to make HTTP requests for fetching questions from the API.
* **Open Trivia DB API:** The source for all trivia questions used in the application.

***

## ✨ Future Enhancements

* **Diverse Question Types:** Expand beyond True/False to include multiple-choice questions.
* **Customizable Quizzes:** Allow users to select different categories and difficulty levels.
* **Local High Scores:** Implement a feature to save and display high scores locally.
* **Progress Tracking:** Add a progress bar to show the number of remaining questions.

***

## 👨‍💻 Author

**Raihan Kabir**

A Computer Science student passionate about Python projects, Data Science, and Machine Learning.
