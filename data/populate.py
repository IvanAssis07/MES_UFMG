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
    base_dir = "ivan_problems"
    difficulties = {
        "EASY": [
            "108_convert-sorted-array-to-binary-search-tree",
            "222_count-complete-tree-nodes",
            "28_find-the-index-of-the-first-occurrence-in-a-string",
            "202_happy-number",
            "226_invert-binary-tree"
        ],
        "MEDIUM": [
            "199_binary-tree-right-side-view",
            "103_binary-tree-zigzag-level-order-traversal",
            "201_bitwise-and-of-numbers-range",
            "133_clone-graph",
            "322_coin-change"
        ],
        "HARD": [
            "295_find-median-from-data-stream",
            "502_ipo",
            "149_max-points-on-a-line",
            "4_median-of-two-sorted-arrays",
            "23_merge-k-sorted-lists"
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
