import textract
import os

# convert any type of files into txt files
cwd = os.getcwd()
input_dir_path = os.path.join(cwd, 'Resumes/collected_resumes/')
result_dir_path = os.path.join(cwd, 'Resumes/extracted_resumes/')

for file in os.listdir(input_dir_path):
    cur_resume_path = os.path.join(input_dir_path, file)

    #convert existing resume to txt format
    content = textract.process(cur_resume_path, encoding='utf-8')
    resume_name = os.path.basename(cur_resume_path).split(".", 1)[0] 
    result_resume_path = result_dir_path+resume_name+'.txt'
    
    with open(result_resume_path, 'wb') as f:
        f.write(content)
