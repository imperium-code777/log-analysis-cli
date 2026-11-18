import sys
import os

def analyze_log_file(filepath):
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.")
        return

    total_lines = 0
    error_count = 0
    warning_count = 0
    errors = []

    with open(filepath, 'r') as file:
        for line in file:
            total_lines += 1
            if "ERROR" in line.upper():
                error_count += 1
                errors.append(line.strip())
            elif "WARNING" in line.upper():
                warning_count += 1

    print("=== LOG ANALYSIS REPORT ===")
    print(f"Total Lines Processed: {total_lines}")
    print(f"Total Warnings Found:  {warning_count}")
    print(f"Total Errors Found:    {error_count}")
    print("\n--- Error Summary ---")
    for err in errors[:5]:  # Show first 5 errors
        print(f" > {err}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyzer.py <path_to_log_file>")
    else:
        analyze_log_file(sys.argv[1])
      
