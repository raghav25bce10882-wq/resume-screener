 Project Statement: Simple Resume Screening System

1. Problem Statement
Companies receive too many resumes, making manual initial screening slow and inefficient. Human Resources (HR) teams need a fast, automated way to filter candidates who clearly do not meet the minimum job requirements.

 2. Scope of the Project
The project is a command-line application (CLI) built in Python that performs *keyword-based matching* between a single candidate's resume (text file) and a defined list of required job skills (text file). It calculates a match score and provides a final "SELECTED" or "REJECTED" verdict based on a configurable threshold. The project focuses solely on *text analysis* and *scoring logic*, not complex PDF parsing.

3. Target Users
HR Departments: Teams responsible for the initial application screening process.
Recruitment Agencies: Staff who need to quickly shortlist candidates for clients.
Hiring Managers: Users seeking fast, objective data on candidate qualification.

 4. High-Level Features
File Input: Reads resume and job description content from simple text files.
Keyword Matching: Identifies and counts specific required skills present in the resume.
Match Scoring: Calculates a percentage score and applies a pass/fail verdict.
Detailed Reporting: Displays a clear list of found skills (✓) and missing skills (✗).
Logging: Records all screening activities for tracking.
