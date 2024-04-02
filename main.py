from generator import createLetter

if __name__ == "__main__":
    company_name = input("Input Company Name: ")
    applicant_name = "Noah Beidelman"
    school_name = "Cal State University Fullerton"
    github = "github.com/noahbei"
    skills = [
        "HTML", "CSS", "JavaScript", "React", "React Native", "C/C++", "Python",
        "SQL", "MySQL", "Firebase", "Git", "GitHub", "Bootstrap", "EJS", "Figma",
        "Linux", "Docker", "Selenium", "Agile methodologies"
    ]
    createLetter(applicant_name, company_name, school_name, github, skills)