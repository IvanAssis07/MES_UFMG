import json

def load_problems(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def filter_and_sort_problems(problems, difficulty, limit):
    # Filter by difficulty
    filtered = [p for p in problems if p['difficulty'].lower() == difficulty.lower()]
    # Sort alphabetically by title
    filtered.sort(key=lambda x: x['titleSlug'])
    # Return the desired quantity
    return filtered[:limit]

def main():
    file_path = 'top_interview_150_clean.json'  # Update to your file's path
    difficulty = input("Enter difficulty (Easy, Medium, Hard): ").strip()
    limit = int(input("Enter number of problems to retrieve: "))

    try:
        problems = load_problems(file_path)
        selected = filter_and_sort_problems(problems, difficulty, limit)

        if not selected:
            print(f"No problems found with difficulty '{difficulty}'.")
        else:
            print(f"\nTop {len(selected)} {difficulty} problems:\n")
            for i, prob in enumerate(selected, 1):
                print(f"{i}. {prob['titleSlug']} - {prob['id']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
