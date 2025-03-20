import os
import datetime

# Define valid DSA solution categories
VALID_CATEGORIES = [
    "Arrays", "String", "Hash Table", "Dynamic Programming", "Math", "Sorting",
    "Greedy", "Depth-First Search", "Binary Search", "Database", "Matrix", "Tree",
    "Breadth-First Search", "Bit Manipulation", "Two Pointers", "Prefix Sum",
    "Heap (Priority Queue)", "Binary Tree", "Simulation", "Stack", "Graph",
    "Counting", "Sliding Window", "Design", "Enumeration", "Backtracking",
    "Union Find", "Linked List", "Number Theory", "Ordered Set", "Monotonic Stack",
    "Segment Tree", "Trie", "Combinatorics", "Bitmask", "Queue", "Recursion",
    "Divide and Conquer", "Memoization", "Binary Indexed Tree", "Geometry",
    "Binary Search Tree", "Hash Function", "String Matching", "Topological Sort",
    "Shortest Path", "Rolling Hash", "Game Theory", "Interactive", "Data Stream",
    "Monotonic Queue", "Brainteaser", "Randomized", "Merge Sort",
    "Doubly-Linked List", "Counting Sort", "Iterator", "Concurrency",
    "Probability and Statistics", "Quickselect", "Suffix Array", "Bucket Sort",
    "Line Sweep", "Minimum Spanning Tree", "Shell", "Reservoir Sampling",
    "Strongly Connected Component", "Eulerian Circuit", "Radix Sort",
    "Rejection Sampling", "Biconnected Component"
]

# Paths
script_dir = os.path.dirname(os.path.abspath(__file__))  # Path to Scripts folder
repo_dir = os.path.dirname(script_dir)  # Root directory of the repo
readme_path = os.path.join(repo_dir, "README.md")  # Path to README.md

# Read existing README content
if os.path.exists(readme_path):
    with open(readme_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
else:
    print("README.md not found!")
    exit(1)

# Find the start of the table
header_index = None
for i, line in enumerate(lines):
    if line.strip().startswith("| # "):  # Detect table header
        header_index = i
        break

if header_index is None:
    print("Table header not found in README.md!")
    exit(1)

# Extract existing problems
existing_problems = set()
last_index = 0  # To track the last used serial number

for line in lines[header_index + 2:]:  # Skip header & separator
    parts = line.strip().split("|")
    if len(parts) >= 5:
        try:
            num = int(parts[1].strip())  # Extract serial number
            last_index = max(last_index, num)  # Track the highest number
        except ValueError:
            continue
        problem_name = parts[3].strip()
        existing_problems.add(problem_name.lower())  # Store in lowercase for case-insensitive matching

# Detect new problems
new_entries = []
today = datetime.date.today().strftime("%Y-%m-%d")

for category in VALID_CATEGORIES:
    category_path = os.path.join(repo_dir, category)
    if not os.path.isdir(category_path):  
        continue  # Skip if the category folder doesn't exist

    for filename in sorted(os.listdir(category_path)):  # Sort files alphabetically
        if filename.endswith((".py", ".cpp", ".java", ".js", ".ts")):  # Filter solution files
            problem_name = filename.replace("_", " ").rsplit(".", 1)[0].title()
            problem_path = f"{category}/{filename}"  # Convert to forward-slash format
            
            if problem_name.lower() not in existing_problems:  # Add only if not already present
                last_index += 1  # Increment serial number
                new_entries.append(
                    f"| {last_index} | {today} | {problem_name} | {category} | [{filename}]({problem_path}) |\n"
                )

# Append new problems at the end of the table
if new_entries:
    lines.extend(new_entries)
    with open(readme_path, "w", encoding="utf-8") as file:
        file.writelines(lines)
    print(f"✅ Added {len(new_entries)} new problem(s) to README.md")
else:
    print("✅ No new problems found.")
