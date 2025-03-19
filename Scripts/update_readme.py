import os
from datetime import date

README_PATH = "README.md"

PROBLEM_DIRS = [
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

TABLE_HEADER = "| #  | Date       | Problem        | Topic  | Solution |\n|----|------------|---------------|--------|----------|\n"

if os.path.exists(README_PATH):
    with open(README_PATH, "r") as f:
        lines = f.readlines()

start_idx = next((i for i, line in enumerate(lines) if "| #  |" in line), len(lines))
table_content = "".join(lines[start_idx + 1:]) if start_idx < len(lines) else ""

new_entries = []
SUPPORTED_EXTENSIONS = (".js", ".py", ".cpp", ".java")  

problem_count = 1  # Counter for problem numbers
for topic in PROBLEM_DIRS:
    if os.path.exists(topic):
        for file in os.listdir(topic):
            if file.endswith(SUPPORTED_EXTENSIONS):
                problem_name = file.replace("_", " ").rsplit(".", 1)[0].title()  # Convert to title case
                solution_path = f"[{file}]({topic}/{file})"
                new_entries.append(f"| {problem_count:<2} | {date.today()} | {problem_name:<15} | {topic:<10} | {solution_path} |\n")
                problem_count += 1

if new_entries:
    with open(README_PATH, "w") as f:
        f.writelines(lines[:start_idx + 1] if start_idx < len(lines) else lines)
        f.write(TABLE_HEADER)
        f.writelines(new_entries + [table_content])
    print("✅ README updated with new problems!")
else:
    print("No new problems found.")
