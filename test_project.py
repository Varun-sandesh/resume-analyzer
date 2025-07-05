# import pytest
# Used black to make the code looks better
import pytest
from project import get_keywords, match_skills


def test_known_skills():
    # Test that it actually finds the skills and doesn’t miss anything
    text = (
        "I have experience working with Python, Django, and Flask in various projects."
    )
    skill_list = {"python", "django", "flask", "sql"}
    result = get_keywords(text, skill_list)
    assert result == {"python", "django", "flask"}


def test_keywords():
    # Check that it removes words that are not skills
    # Only "sql" should match from the valid skill set
    text = "He is a dedicated developer with good communication skills, but only familiar with SQL."
    valid = {"python", "sql", "django"}
    result = get_keywords(text, valid)
    assert result == {"sql"}


def test_match_skills():
    # Verify that the resume skills correctly match the job description requirements
    resume = {"python", "sql", "django"}
    job = {"python", "django", "flask", "aws"}

    # Check which skills from the resume match the job, and which are missing
    matched, missing, score = match_skills(resume, job)

    assert matched == {"python", "django"}

    assert missing == {"flask", "aws"}

    assert score == 50.0


def test_empty_text_returns_nothing():
    # Testing with empty
    result = get_keywords("", {"python", "sql"})
    assert result == set()


def test_no_matching_skills():
    # Testing with no relavent skills
    text = "I love photography and traveling."
    skills = {"python", "java", "sql"}
    result = get_keywords(text, skills)
    assert result == set()


def test_resume_with_all_unknown_skills():
    # Resume containing unrelated skills
    resume = {"dancing", "singing"}
    job = {"python", "sql"}
    matched, missing, score = match_skills(resume, job)
    assert matched == set()
    assert missing == {"python", "sql"}
    assert score == 0.0


def test_job_with_empty_skills():
    # testing if job as no skills
    resume = {"python", "sql"}
    job = set()
    matched, missing, score = match_skills(resume, job)
    assert matched == set()
    assert missing == set()
    assert score == 0.0


def test_case_insensitivity():
    # Testing capital and small letters
    text = "Experienced in PYTHON and Django."
    skills = {"python", "django"}
    result = get_keywords(text, skills)
    assert result == {"python", "django"}


def test_irrelevant_input_like_animals():
    # Testing with wrong skills
    text = "I have experience with cats, dogs, and parrots."
    skills = {"python", "sql", "aws"}
    result = get_keywords(text, skills)
    assert result == set()


def test_invalid_input_type():
    # Passing none instead of a string
    with pytest.raises(AttributeError):
        get_keywords(None, {"python"})
