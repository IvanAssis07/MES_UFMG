import os
import json

'''
** This script creates a directory structure for LeetCode problems categorized by difficulty levels.
** It creates folders for each difficulty level (EASY, MEDIUM, HARD) and subfolders for each problem.
** Each problem folder contains subfolders for different AI models (deepseek, gpt, claude).
** Inside each subfolder, it creates two JSON files for C and Python solutions.
** Usage:
    Substitute "base_dir" with your desired base directory name.
    Put your LeetCode problem names in the `difficulties` dictionary with the format: <number>_<problem-name>.
'''

def create_leetcode_folders_and_files():
    base_dir = "henrique_problems"
    difficulties = {
        "EASY": [
            "67_add-binary",
            "637_average-of-levels-in-binary-tree",
            "121_best-time-to-buy-and-sell-stock",
            "70_climbing-stairs",
            "219_contains-duplicate-ii"
        ],
        "MEDIUM": [
            "15_3sum",
            "2_add-two-numbers",
            "122_best-time-to-buy-and-sell-stock-ii",
            "173_binary-search-tree-iterator",
            "102_binary-tree-level-order-traversal"
        ],
        "HARD": [
            "224_basic-calculator",
            "123_best-time-to-buy-and-sell-stock-iii",
            "188_best-time-to-buy-and-sell-stock-iv",
            "124_binary-tree-maximum-path-sum",
            "135_candy"
        ]
    }

    subfolders = ["deepseek", "gpt", "claude"]

    # Cria a pasta base
    os.makedirs(base_dir, exist_ok=True)
    print(f"Pasta '{base_dir}' criada ou já existe.")

    for difficulty, problems in difficulties.items():
        difficulty_path = os.path.join(base_dir, difficulty.lower())
        os.makedirs(difficulty_path, exist_ok=True)
        print(f"  Pasta '{difficulty_path}' criada ou já existe.")

        for problem_folder_name_with_number in problems:
            file_name_base = problem_folder_name_with_number

            problem_path = os.path.join(difficulty_path, problem_folder_name_with_number)
            os.makedirs(problem_path, exist_ok=True)
            print(f"    Pasta '{problem_path}' criada ou já existe.")

            for sf in subfolders:
                final_path = os.path.join(problem_path, sf)
                os.makedirs(final_path, exist_ok=True)
                print(f"      Pasta '{final_path}' criada ou já existe.")

                c_file_path = os.path.join(final_path, f"{file_name_base}_C.json")
                py_file_path = os.path.join(final_path, f"{file_name_base}_Py.json")

                with open(c_file_path, 'w') as f:
                    json.dump({}, f)
                print(f"        Arquivo '{c_file_path}' criado.")

                with open(py_file_path, 'w') as f:
                    json.dump({}, f)
                print(f"        Arquivo '{py_file_path}' criado.")

if __name__ == "__main__":
    create_leetcode_folders_and_files()