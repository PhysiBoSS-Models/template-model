import os
short_name = ""
dirs = [dir for dir in os.listdir("sample_projects")  if os.path.isdir(os.path.join("sample_projects", dir)) and dir != "template_BM"]
if len(dirs) == 1:
    short_name = dirs[0]
    print("Found exactly one sample project:", short_name)
else:
    print("Error: Expected exactly one sample project, found:", dirs)
with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'model_short_name={short_name}', file=fh)