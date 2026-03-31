# 📄 Simple Resume Screening System (Python)

### Project Title: Simple Resume Screening System

## 🌟 1. Overview

This project is a command-line tool built using *Python* designed to automate the initial screening of job applicants. It helps recruiters quickly determine if a candidate's resume meets the minimum requirements for a job opening.

The system works by comparing a candidate's resume text against a list of required skills specified in a job description file, providing a clear *match score* and a final *selection verdict (SELECTED/REJECTED)*.

---

## ✨ 2. Key Features

* *File-Based Input:* Reads input cleanly from resume.txt and job_description.txt files.
* *Keyword Matching:* Searches for specific skills defined by the recruiter in the JD file.
* *Configurable Threshold:* The minimum passing score (e.g., 60%) can be easily adjusted.
* *Detailed Reporting:* Shows exactly which skills were *Found (✓)* and which are *Missing (✗)*.
* *Activity Logging:* Automatically records all screening actions in a screening_log.txt file.
* *Robust Error Handling:* Alerts the user if input files are missing or empty.

---

## 🛠 3. Technologies Used

* *Programming Language:* Python 3
* *Libraries:*
    * **re:** Used for text processing and basic pattern matching.
    * **datetime:** Used for timestamping log entries.

---

## 🚀 4. Installation and Setup

### Prerequisites
You only need to have *Python 3* installed on your system.

### Steps to Run

1.  *Clone the Repository:* (If applicable, when hosted on GitHub)
    bash
    git clone [your_repo_link_here]
    cd resume-screening-system
    
2.  *Create Input Files:* In the project folder, create two plain text files:
    * resume.txt (Paste the candidate's resume content here.)
    * job_description.txt (Paste the job requirements here, including the skills.)
3.  *Run the Script:* Execute the main Python file from your terminal:
    bash
    python resume_screener.py
    

### Important Input Instruction

The job description file (job_description.txt) *must* include the skills list using the tag REQUIRED_SKILLS: for the program to successfully extract keywords.

Example format in job_description.txt:
> 
> REQUIRED_SKILLS: python, java, sql, teamwork
> We are looking for a developer...
> 

---

## 🧪 5. Instructions for Testing

To test the different outcomes of the system:

1.  *Test Case 1 (SELECTED):* Ensure resume.txt contains most of the skills listed under REQUIRED_SKILLS: in the JD (e.g., matching 4 out of 6 skills for a 66.67% score).
2.  *Test Case 2 (REJECTED):* Update resume.txt to only contain 1 or 2 of the required skills (e.g., matching 2 out of 6 skills for a low score).
3.  *Test Case 3 (Error Handling):* Delete either resume.txt or job_description.txt and run the script to confirm the Error: Cannot find [filename] message appears.

---

## 🖥 6. Sample Output

Here is an example of the program's result displayed in the terminal:


=============================================== RESUME SCREENING SYSTEM
Loading files...

--- ANALYSIS RESULTS ---

Overall Match Score: 66.67%

Skills Detected in Resume: ✓ python ✓ sql ✓ communication ✓ leadership

Skills Not Found: ✗ java ✗ teamwork ✗ problem solving

=============================================== FINAL DECISION: SELECTED Reason: Candidate meets requirements with 66.67% match
