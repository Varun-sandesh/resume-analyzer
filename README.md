# Resume Analyzer

This is my final project for CS50P – Introduction to programming with python.

I built this tool to make resume screening faster and easier. Going through resumes manually can be slow and repetitive — especially when you're trying to check if someone has the right skills for a specific job. This report gives you a quick, clear summary of how well a candidate’s resume matches the job description.

#### Video Demo: https://youtu.be/lHbSeI7vkMA

#### Description: A Python tool that analyzes how well your resume matches a job description based on skills.

## What It Does

If you're a recruiter, this tool can help you quickly check how well a resume matches a job.

Instead of reading each resume manually, the tool looks for skill matches for you.

It shows:

What skills from the resume match the job description

What skills are missing

A match score to see how well the resume fits

And it saves everything in a results.csv file you can review or share

## How It Works

1. **You provide three files**:
   - A PDF of the applicant’s resume
   - A text file containing the job description
   - A list of known skills

2. **It reads the files**:
   - It uses `PyPDF2` to pull text from the resume
   - It also reads the job description and skills from the text files

3. **It cleans up the text**:
   - Everything is converted to lowercase
   - The text is split into individual words
   - Common words like “and”, “the”, and “is” are removed using NLTK so they don’t get in the way

4. **It compares the skills**:
   - It checks which skills appear in both the resume and the job description
   - Then it calculates a match score based on how many required skills are found in the resume

5. **It shows and saves the results**:
   - The terminal shows the matched skills, missing skills, and match percentage
   - It also saves everything into a `results.csv` file so you can keep or share the report

## ⚠️ What Happens If Something Goes Wrong?

Don't worry — this tool is built to handle common mistakes in a simple and helpful way. Here's how it responds if something isn't quite right:

- **Wrong file type?**
  If you accidentally enter a resume file that’s not a PDF (like a `.txt` or `.docx`), the program will kindly remind you to use a PDF instead.

- **Typed the wrong file name?**
  If the resume file name you enter doesn’t exist or can’t be opened, the program will tell you it couldn’t read the resume — no crashes, just a friendly message so you can fix it.

- **Job description or skills file missing?**
  If either `job_description.txt` or `skills.txt` isn’t found in the folder, the program will let you know exactly what’s missing and stop there until it's added.

- **Resume can’t be read properly?**
  If your PDF is scanned, corrupted, or doesn’t contain any real text, the program will say it couldn’t extract the content. This means you might need to use a different version of the resume.

- **Problem saving the CSV file?**
  If something goes wrong when trying to save the results — like a permission issue — the program will tell you what happened so you know how to fix it.


### In Short:
Even if something goes wrong, the tool won’t break or crash. It simply explains what’s missing or incorrect, so you can fix it and try again. No surprises — just helpful feedback.


## How to Use

1. **Make sure Python is installed**
   You can check this by running:
   `python --version` or `python3 --version`

2. **Install the libraries it needs**
   Run this in the terminal inside your project folder:
   ```bash
   pip install -r requirements.txt

## Acknowledgment

This project was completed by me as part of the CS50P final project. I used CS50 resources, official Python documentation, and tools like ChatGPT for help with ideas and code improvement. However, I wrote, tested, and fully understood all code myself, in accordance with CS50’s academic honesty policy.

I used libraries like nltk and PyPDF2 to handle text processing and PDF extraction.

This project has more comments and a cleaner structure than my earlier submissions. I made an effort to improve the readability and organization of my code for the final project, applying what I’ve learned throughout the course. I also used Black to keep the code clean and consistent style.
