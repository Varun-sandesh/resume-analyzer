# Importing necessary libraries
# Used black to make code looks better
import PyPDF2
import csv
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# setup for NLTK
nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)


def main():
    print("---Resume Analyser---")

    # Taking input from the user
    resume_file = input("Enter resume pdf file name: ").strip()

    if not resume_file.endswith(".pdf"):
        print("Please enter a pdf file.")
        return

    resume_text = read_pdf(resume_file)
    if not resume_text:
        print("Could not extract from the resume.")
        return

    try:
        with open("job_description.txt") as f:
            job_text = f.read()
    except FileNotFoundError:
        print("Missing job_description.txt, Please add it!.")
        return

    try:
        with open("skills.txt") as f:
            req_skills = set(line.strip().lower() for line in f if line.strip())
    except FileNotFoundError:
        print("Missing skills.txt! Please add it!.")
        return

    resume_skills = get_keywords(resume_text, req_skills)
    job_skills = get_keywords(job_text, req_skills)

    matched, missing, score = match_skills(resume_skills, job_skills)

    print("\n--- Analysis Result for Applicant ---")
    print("Matched Skills:", matched)
    print("Missing Skills:", missing)
    print(f"Score: {score}%")

    save_csv("Varun sandesh", matched, missing, score)


def read_pdf(resume_file):
    # Reads and all text from pdf file. and also returns text
    text = ""
    try:
        with open(resume_file, "rb") as file:
            pdf = PyPDF2.PdfReader(file)
            for page_num, page in enumerate(pdf.pages):
                content = page.extract_text()
                if content:
                    text += content + "\n"
    except Exception as exp:
        print(f"Error reading PDF file: {exp}")
    return text


def get_keywords(text, skillset=None):
    # removes unwanted letters and returns skills
    tokens = word_tokenize(text.lower())
    words = [word for word in tokens if word.isalpha()]
    filtered_words = [word for word in words if word not in stopwords.words("english")]

    if skillset:
        # returns only the skills that match the required skill set
        return set(word for word in filtered_words if word in skillset)
    return set(filtered_words)


def match_skills(resume_skills, job_skills):
    matched = resume_skills & job_skills
    missing = job_skills - resume_skills
    score = (len(matched) / len(job_skills)) * 100 if job_skills else 0
    return matched, missing, round(score, 2)


def save_csv(name, matched, missing, score, filename="results.csv"):
    try:
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(
                ["applicant_name", "Matched Skills", "Missing Skills", "Score (%)"]
            )
            writer.writerow(
                [
                    name,
                    ", ".join(sorted(matched)),
                    ", ".join(sorted(missing)),
                    score,
                ]
            )
        print(f"Results saved to {filename}")
    except Exception as exp:
        print(f"Error saving results: {exp}")


if __name__ == "__main__":
    main()
