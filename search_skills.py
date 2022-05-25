import os
import argparse
import sys 
from xlwt import Workbook


def update_survery_result():
    global skills, condidate_skills
    # Workbook is created
    wb = Workbook()
    # add_sheet is used to create sheet.
    sheet1 = wb.add_sheet('Sheet 1')
    row = 1
    col = 1
    # column headings
    sheet1.write(0, 0, 'Name')

    # update skills
    for skill in skills:
        sheet1.write(0, col, skill)
        col +=1
    col =1
    for name,skills in condidate_skills.items():
        sheet1.write(row, 0, name)
        for skill in skills.values():
            sheet1.write(row, col,skill)
            col +=1
        col = 1
        row +=1
    # save records
    wb.save('condidates_skills_survey.xls')
    #print("Please check updated condidates_skills_survey.xls sheet")

def search_skills_in_resume():
    global dir_path, condidate_skills

    # iterate each file in a directory
    for file in os.listdir(dir_path):
        cur_resume_path = os.path.join(dir_path, file)

        with open(cur_resume_path, 'r') as f:
            condidate_name = f.readline().strip()
            condidate_skills[condidate_name] = {}
            resume = f.read()
        # Iterate list to find each skill
        for skill in skills:
            condidate_skills[condidate_name][skill] = 'n'
            if skill.lower() in resume.lower():
                condidate_skills[condidate_name][skill] = 'y'
        print(condidate_skills)
def list_skills():
    parser = argparse.ArgumentParser(description="cdata plugins")
    parser.add_argument("--skills", nargs='?') # 
    parser.parse_known_args(['--skills']) # valid cmd arguments

    if "--skills" in sys.argv:
        global skills
        args = parser.parse_args()
        skills = args.skills.split(',')
    else:
        print("Invalid Argument !!.\nPlease specify the skill/s separated by commas that you are looking for :\nEx: search_skills.py --skills Python, AWS, Linux ")
  
if __name__ == "__main__":

    condidate_skills  = {}
    skills = []
    dir_path = "/home/vidya/ReadResume/Resumes/extracted_resumes/"
    cwd = os.getcwd()
    dir_path = os.path.join(cwd, 'Resumes/extracted_resumes/')
    list_skills()
    search_skills_in_resume()
    update_survery_result()