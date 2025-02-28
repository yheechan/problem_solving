import os
import markdown
import pandas as pd
from datetime import datetime

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

def get_summary_status(problem_status):
    summary_status = {}
    
    for user in USERS:
        summary_status[user] = {}
        for source in SOURCES:
            summary_status[user][source] = {}
            if not os.path.exists(user + "/" + source):
                continue
            for level in os.listdir(user + "/" + source):
                summary_status[user][source][level] = {"solved": 0}
                
                level_path = os.path.join(user, source, level)
                if not os.path.isdir(level_path):
                    continue
                
                for problem in os.listdir(level_path):
                    if problem.endswith(".py"):
                        if problem_status[(source, level, problem)][user] == "✅":
                            summary_status[user][source][level]["solved"] += 1
    
    return summary_status

def update_readme():
    problem_status = get_problem_status()
    summary_status = get_summary_status(problem_status)
    
    # Convert problem dictionary to a DataFrame
    list_table_data = []
    for idx, ((source, level, problem), status) in enumerate(problem_status.items(), start=1):
        list_table_data.append([idx, source, level, problem, status["andy"], status["charlie"]])
    
    list_df = pd.DataFrame(list_table_data, columns=["Idx", "Source", "Level", "Problem", "Andy", "Charlie"])

    summary_table_data = []
    for source in SOURCES:
        if not os.path.exists("andy/" + source):
            continue
        for level in os.listdir("andy/" + source):
            summary_table_data.append(["Andy", source, level, summary_status["andy"][source][level]["solved"]])
            summary_table_data.append(["Charlie", source, level, summary_status["charlie"][source][level]["solved"]])

    summary_df = pd.DataFrame(summary_table_data, columns=["User", "Source", "Level", "Solved"])
    
    # Generate Markdown table
    list_md_table = list_df.to_markdown(index=False)
    summary_md_table = summary_df.to_markdown(index=False)

    
    # Read existing README.md content
    readme_content = ""
    if os.path.exists(README_PATH):
        with open(README_PATH, "r", encoding="utf-8") as f:
            readme_content = f.read()
    
    # Define the table update markers
    summary_table_start_marker = "<!-- START_TABLE_SUMMARY -->"
    summary_table_end_marker = "<!-- END_TABLE_SUMMARY -->"
    list_table_start_marker = "<!-- START_TABLE_LIST -->"
    list_table_end_marker = "<!-- END_TABLE_LIST -->"
    last_updated_start_marker = "<!-- START_LAST_UPDATED -->"
    last_updated_end_marker = "<!-- END_LAST_UPDATED -->"

    # Locate existing summary table
    if summary_table_start_marker in readme_content and summary_table_end_marker in readme_content:
        start_idx = readme_content.find(summary_table_start_marker) + len(summary_table_start_marker)
        end_idx = readme_content.find(summary_table_end_marker)
        new_readme_content = (
            readme_content[:start_idx]
            + "\n" + summary_md_table + "\n"
            + readme_content[end_idx:]
        )
    else:
        new_readme_content = readme_content + f"\n{summary_table_start_marker}\n{summary_md_table}\n{summary_table_end_marker}\n"
    
    # Locate existing table
    if list_table_start_marker in new_readme_content and list_table_end_marker in new_readme_content:
        start_idx = new_readme_content.find(list_table_start_marker) + len(list_table_start_marker)
        end_idx = new_readme_content.find(list_table_end_marker)
        new_new_readme_content = (
            new_readme_content[:start_idx]
            + "\n" + list_md_table + "\n"
            + new_readme_content[end_idx:]
        )
    else:
        new_readme_content = new_readme_content + f"\n{list_table_start_marker}\n{list_md_table}\n{list_table_end_marker}\n"
    
    # Update the last updated date
    current_date = datetime.now().strftime("%Y %b %d")
    if last_updated_start_marker in new_readme_content and last_updated_end_marker in new_readme_content:
        start_idx = new_readme_content.find(last_updated_start_marker) + len(last_updated_start_marker)
        end_idx = new_readme_content.find(last_updated_end_marker)
        new_new_readme_content = (
            new_new_readme_content[:start_idx]
            + "\nLast Update: " + current_date + "\n"
            + new_new_readme_content[end_idx:]
        )
    else:
        new_new_readme_content = new_new_readme_content + f"\n{last_updated_start_marker}\nLast Update {current_date}\n{last_updated_end_marker}\n"
    
    # Write updated content back to README.md
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_new_readme_content)
    
    print("README.md updated successfully!")


if __name__ == "__main__":
    update_readme()
