# Computational Chemistry: Guess The Element Game 🧪

**Group-2 Project** **By:** Samarth Shukla & Dhruv Bajpai  
**Course:** Introduction To Computational Chemistry    
**Faculty:** Dr. Saurav Prasad Sir

## 📖 Overview

This is a Python-based graphical user interface (GUI) application designed to test your knowledge of the Periodic Table. Built using `tkinter` and the `mendeleev` chemical database, the game challenges users to guess a randomly selected element based on atomic properties.

The application features a modern "dark mode" UI, real-time feedback logic (Higher/Lower atomic numbers), and a progressive hint system based on electron configuration, groups, and periods.

## ✨ Features

* **Dynamic Database:** Uses the `mendeleev` library to fetch real-time data for all 118 elements.
* **Fallback Mode:** Includes a robust fallback system (Mock Database) if the required libraries are not installed, ensuring the game always runs.
* **Smart Feedback:** Tells you to go "Higher" or "Lower" based on atomic number and alerts you if you match the correct Group or Period.
* **Progressive Hints:** Unlocks specific chemical clues (Block, Series, Electron Config, Atomic Mass) as you use up your attempts.
* **Modern UI:** A clean, dark-themed interface designed for readability.

## ⚙️ Prerequisites & Installation

To enjoy the full experience with the complete database of elements, you need Python installed on your system.

### 1. Install Python
Ensure you have Python 3.x installed. You can check this by typing:
```bash
python --version
```

### 2. Install Required Library
The game relies on the mendeleev library for chemical data. Open your terminal or command prompt and run:
```bash
pip install mendeleev
```
> ⚠️ If `mendeleev` is not available, the game will automatically switch to **Fallback Mode**  
> and provide a small built-in database (H, He, C, O, Fe, Au).

### 3. Tkinter
Tkinter is included with most Python installations. 

---

## 🚀 How to Run

1. Download or clone the project.
   ```bash
   git clone https://github.com/samarthshukla20/guess-the-element
   ```
2. Navigate to the folder containing the file.
   ```bash
   cd guess-the-element
   ```
3. Run the application
   ```bash
   python main.py
   ```
   
   ---

   ## 🎮 How to Play

1.  **The Objective:**
    The computer selects a random chemical element (from Hydrogen to Oganesson). You have **6 attempts** to guess the correct one.

2.  **Making a Guess:**
    Type an element's **Name** (e.g., "Carbon") or **Symbol** (e.g., "C") into the input box and press **ENTER** or click the **ANALYZE** button.

3.  **Analyze the Feedback:**
    The game provides feedback based on the Atomic Number ($Z$) of your guess compared to the target:
    * **Go HIGHER:** The target element is heavier (Higher $Z$).
    * **Go LOWER:** The target element is lighter (Lower $Z$).
    * **MATCH Group:** Your guess is in the same vertical column (Group) as the target.
    * **MATCH Period:** Your guess is in the same horizontal row (Period) as the target.

4.  **Unlock Hints:**
    A new hint appears at the bottom of the screen after specific incorrect attempts:
    * *Attempt 1:* Reveal the **Block** (s, p, d, f).
    * *Attempt 2:* Reveal the **Chemical Series** (e.g., Alkali Metal, Noble Gas).
    * *Attempt 3:* Reveal the valence **Electron Configuration**.
    * *Attempt 4:* Reveal the approximate **Atomic Mass**.

---

## 📝 Credits

Developed by **Group-2** for the Introduction To Computational Chemistry class project.

* **Samarth Shukla (25BAI11027)**
* **Dhruv Bajpai (25BAI10926)**

---
*Powered by Python and the Mendeleev Database.*
