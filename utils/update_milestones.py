#!/usr/bin/env python3
"""
Script to update time calculations in milestones.md
Automatically calculates and updates the "X years ago" lines under each important date.
"""

import re
from datetime import datetime, date
import os

def calculate_time_since(date_str):
    """Calculate time since a given date and return formatted string."""
    try:
        # Parse the date (assuming YYYY-MM-DD format)
        start_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        current_date = date.today()
        
        # Calculate difference
        diff = current_date - start_date
        years = diff.days / 365.25
        
        # Format the result
        if years < 1:
            months = diff.days / 30.44  # Average days per month
            if months < 1:
                return f"{diff.days} days ago"
            else:
                return f"{months:.1f} months ago"
        else:
            return f"{years:.2f} years ago"
            
    except ValueError:
        return "Invalid date format"

def update_milestones_file(file_path):
    """Update the milestones.md file with current time calculations."""
    
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found")
        return False
    
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    updated_lines = []
    i = 0
    in_important_dates = False
    
    while i < len(lines):
        line = lines[i]
        updated_lines.append(line)
        
        # Check if we're entering the Important Dates section
        if line.strip() == "## Important Dates":
            in_important_dates = True
        # Check if we're leaving the Important Dates section (next ## header)
        elif line.startswith("## ") and line.strip() != "## Important Dates":
            in_important_dates = False
        
        # Only process dates if we're in the Important Dates section
        if in_important_dates:
            # Look for lines with dates in the format "Name: YYYY-MM-DD"
            date_match = re.search(r'(\d{4}-\d{2}-\d{2})', line)
            
            if date_match and ':' in line:
                date_str = date_match.group(1)
                time_ago = calculate_time_since(date_str)
                
                # Check if the next line is already a time calculation line
                if i + 1 < len(lines):
                    next_line = lines[i + 1].strip()
                    # If next line contains "ago" or is mostly whitespace with time info
                    if 'ago' in next_line or re.match(r'^\s*\d+\.?\d*\s*(years?|months?|days?)\s+ago\s*$', next_line):
                        # Skip the old time calculation line
                        i += 1
                
                # Add the updated time calculation line with proper indentation
                spaces = ' ' * 44  # Match the indentation from your example
                updated_lines.append(f"{spaces}{time_ago}\n")
        
        i += 1
    
    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(updated_lines)
    
    print(f"Successfully updated {file_path}")
    return True

def main():
    """Main function to run the milestone updater."""
    # Get the script directory and go up one level since we're now in utils/
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Path to milestones.md
    milestones_path = os.path.join(script_dir, 'career', 'milestones.md')
    
    print("Updating milestones.md with current time calculations...")
    
    if update_milestones_file(milestones_path):
        print("Update completed successfully!")
    else:
        print("Update failed. Please check the file path and format.")

if __name__ == "__main__":
    main()
