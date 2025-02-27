import os
import markdown
import pandas as pd

# Define the directory structure
USERS = ["andy", "charlie"]
SOURCES = ["baekjoon", "programmers", "leetcode"]
README_PATH = "README.md"


def get_problem_status():
    problem_dict = {}
    
    for user in USERS:
        for source in SOURCES:
            source_path = os.path.join(user, source)
            if not os.path.exists(source_path):
                continue
            
            for level in os.listdir(source_path):
                level_path = os.path.join(source_path, level)
                if not os.path.isdir(level_path):
                    continue
                
                for problem in os.listdir(level_path):
                    if problem.endswith(".py"):  # Consider only Python files
                        problem_key = (source, level, problem)
                        if problem_key not in problem_dict:
                            problem_dict[problem_key] = {user: "✅"}
                        else:
                            problem_dict[problem_key][user] = "✅"
                        
                        for other_user in USERS:
                            if other_user not in problem_dict[problem_key]:
                                problem_dict[problem_key][other_user] = "❌"
    
    return problem_dict


def update_readme():
    problem_status = get_problem_status()
    
    # Convert problem dictionary to a DataFrame
    table_data = []
    for idx, ((source, level, problem), status) in enumerate(problem_status.items(), start=1):
        table_data.append([idx, source, level, problem, status["andy"], status["charlie"]])
    
    df = pd.DataFrame(table_data, columns=["Idx", "Source", "Level", "Problem", "Andy", "Charlie"])
    
    # Generate Markdown table
    md_table = df.to_markdown(index=False)
    
    # Read existing README.md content
    readme_content = ""
    if os.path.exists(README_PATH):
        with open(README_PATH, "r", encoding="utf-8") as f:
            readme_content = f.read()
    
    # Define the table update markers
    table_start_marker = "<!-- START_TABLE -->"
    table_end_marker = "<!-- END_TABLE -->"
    
    # Locate existing table
    if table_start_marker in readme_content and table_end_marker in readme_content:
        start_idx = readme_content.find(table_start_marker) + len(table_start_marker)
        end_idx = readme_content.find(table_end_marker)
        new_readme_content = (
            readme_content[:start_idx]
            + "\n" + md_table + "\n"
            + readme_content[end_idx:]
        )
    else:
        new_readme_content = readme_content + f"\n{table_start_marker}\n{md_table}\n{table_end_marker}\n"
    
    # Write updated content back to README.md
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_readme_content)
    
    print("README.md updated successfully!")


if __name__ == "__main__":
    update_readme()

