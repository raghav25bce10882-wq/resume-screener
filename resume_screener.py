import re
from datetime import datetime

# CONFIG SECTION - easy to modify settings
CONFIG = {
    'resume_file': 'resume.txt',
    'jd_file': 'job_description.txt',
    'log_file': 'screening_log.txt',
    'pass_threshold': 60,  # minimum percentage to pass
    'min_skill_length': 3  # ignore words shorter than this
}


# MODULE 1: FILE HANDLER
def read_file(filename):
    # reads text file and returns content
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = f.read()
        return data
    except FileNotFoundError:
        print(f"Error: Cannot find {filename} in current folder")
        return None
    except Exception as err:
        print(f"Something went wrong reading {filename}: {err}")
        return None


def validate_input(resume_txt, jd_txt):
    # making sure we got valid data to work with
    if not resume_txt or not resume_txt.strip():
        print("Resume file is empty or invalid")
        return False
    
    if not jd_txt or not jd_txt.strip():
        print("Job description file is empty or invalid")
        return False
    
    return True


def write_log(message):
    # keeping track of screening activities
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"
    
    try:
        with open(CONFIG['log_file'], 'a', encoding='utf-8') as log:
            log.write(log_entry)
    except:
        pass  # if logging fails, don't crash the program


# MODULE 2: SKILLS ANALYZER
def extract_keywords(text):
    # looking for REQUIRED_SKILLS tag in JD file
    text_lower = text.lower()
    
    # check if user provided skills list with tag
    if "required_skills:" in text_lower:
        # extract everything after the tag
        parts = text_lower.split("required_skills:")
        if len(parts) > 1:
            skills_section = parts[1]
            # get first line after tag (in case there's more text below)
            first_line = skills_section.split('\n')[0]
            # split by comma and clean up
            skills = [s.strip() for s in first_line.split(',')]
            # remove empty strings
            skills = [s for s in skills if s]
            return skills
    
    # if no tag found, show error message
    print("Error: Please add 'REQUIRED_SKILLS:' tag in job description file")
    print("Format: REQUIRED_SKILLS: python, java, sql, communication")
    return []


def match_skills(resume_txt, required_skills):
    # checking what's present vs what's missing
    resume_lower = resume_txt.lower()
    
    found_items = []
    missing_items = []
    
    for skill in required_skills:
        # case insensitive search
        if skill.lower() in resume_lower:
            found_items.append(skill)
        else:
            missing_items.append(skill)
    
    return found_items, missing_items


def calculate_score(matched, total):
    # computing match percentage
    if total == 0:
        return 0.0
    
    percent = (len(matched) / total) * 100
    return round(percent, 2)


def get_verdict(score):
    # deciding pass or fail based on threshold
    threshold = CONFIG['pass_threshold']
    
    if score >= threshold:
        status = "SELECTED"
        explanation = f"Candidate meets requirements with {score}% match"
    else:
        status = "REJECTED"
        explanation = f"Candidate below threshold with only {score}% match"
    
    return status, explanation


# MODULE 3: REPORT GENERATOR
def print_header():
    # displaying program title
    print("\n" + "="*55)
    print("          RESUME SCREENING SYSTEM")
    print("="*55)
    print("\nNote: JD file must contain 'REQUIRED_SKILLS:' tag")
    print("Example: REQUIRED_SKILLS: python, java, sql, teamwork\n")


def display_analysis(matched_skills, missed_skills, score_val, decision, reason):
    # showing complete screening report
    print("\n--- ANALYSIS RESULTS ---\n")
    
    print(f"Overall Match Score: {score_val}%")
    print()
    
    # showing what we found
    print("Skills Detected in Resume:")
    if len(matched_skills) > 0:
        for item in matched_skills:
            print(f"  ✓ {item}")
    else:
        print("  (none found)")
    
    print()
    
    # showing what's missing
    print("Skills Not Found:")
    if len(missed_skills) > 0:
        for item in missed_skills:
            print(f"  ✗ {item}")
    else:
        print("  (none)")
    
    print()
    print("="*55)
    print(f"FINAL DECISION: {decision}")
    print(f"Reason: {reason}")
    print("="*55)
    print()


# MAIN EXECUTION
def execute_screening():
    print_header()
    print("Loading files...\n")
    
    # step 1: read input files
    resume_data = read_file(CONFIG['resume_file'])
    jd_data = read_file(CONFIG['jd_file'])
    
    # step 2: validate inputs
    if not validate_input(resume_data, jd_data):
        write_log("Screening failed - invalid input files")
        return
    
    # step 3: extract required skills from JD
    required_keywords = extract_keywords(jd_data)
    
    if len(required_keywords) == 0:
        print("Error: No valid keywords found in job description")
        write_log("Screening failed - no keywords in JD")
        return
    
    # step 4: analyze resume against requirements
    found, missing = match_skills(resume_data, required_keywords)
    match_percentage = calculate_score(found, len(required_keywords))
    final_status, reasoning = get_verdict(match_percentage)
    
    # step 5: generate report
    display_analysis(found, missing, match_percentage, final_status, reasoning)
    
    # step 6: log the screening
    log_msg = f"Screening completed - {final_status} ({match_percentage}% match)"
    write_log(log_msg)


# program entry point
if __name__ == "__main__":
    execute_screening()