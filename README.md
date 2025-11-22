📘 Daily Expense Tracker (Python)

A clean, simple, and efficient CLI application to track daily expenses.

<p align="center"> <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge"> <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge"> <img src="https://img.shields.io/badge/Storage-Text File-orange?style=for-the-badge"> </p>
📌 Overview

The Daily Expense Tracker is a beginner-friendly command-line application written in Python.
It allows users to add, organize, and view daily expenses with clean formatting.

This version uses a simple text-file storage system, and displays data grouped by date for easy readability.

✨ Features

🗓️ Add expenses with date validation (DD-MM-YYYY)

💵 Store amount and category

🔁 Add multiple expenses under the same date

📄 Data is saved in a plain text file (expence.txt)

📊 View all expenses grouped by date

🔍 Clean and readable output formatting

✔️ Input validation for numbers and yes/no responses

📂 Project Structure
.
├── expence_tracker.py   # Main application
├── expence.txt          # Auto-generated expense data file
└── README.md            # Project documentation

🖥️ Usage
▶️ Running the Program
python expence_tracker.py

📥 Adding Expenses

Enter date in DD-MM-YYYY format

Enter amount

Enter category

Add more items under the same date if needed

Example saved data:

22-11-2025
100
Food
22-11-2025
60
Snacks
23-11-2025
40
Travel

📤 Viewing Expenses

Output is grouped by date:
----- All Expence -----

22-11-2025
 Biriyani -- ₹100
 Egg rice -- ₹50
 Penpencil -- ₹15
------------------------------

23-11-2025
 T-Shirt -- ₹340
 Movie ticket -- ₹350
 Full Meals -- ₹100
------------------------------
🛠️ Tech Stack
Component	Description
Language	Python 3.10+
Storage	Text File (expence.txt)
Interface	Command Line (CLI)
🔮 Future Enhancements

Planned improvements for the next version:

🗄️ Migrate storage to JSON for structured data

📅 Search expenses by date or category

🧮 Daily / Monthly totals

📝 Edit or delete expenses

📊 Export to CSV / Excel

📄 Generate PDF reports

🤝 Contributing

Contributions, suggestions, and improvements are welcome!
Feel free to fork the repository and submit a pull request.

📜 License

This project is open-source and free to use.
