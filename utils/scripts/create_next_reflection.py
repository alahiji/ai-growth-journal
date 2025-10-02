#!/usr/bin/env python3
"""
Script to generate next month's reflection file based on the current month's reflection.
Includes a summary of the previous month and carries forward uncompleted goals.
"""

import re
from datetime import datetime, timedelta
from pathlib import Path
from calendar import monthrange


def parse_reflection_file(file_path):
    """Parse the current reflection file and extract key information."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    data = {
        'content': content,
        'concepts': [],
        'projects': [],
        'achievements': [],
        'knowledge_gaps': [],
        'learning_goals': [],
        'project_goals': [],
        'skill_goals': [],
        'resources': [],
        'rating': '',
        'personal_notes': ''
    }
    
    # Extract completed concepts
    concept_matches = re.findall(r'- \[x\] (.+?) - Confidence level', content)
    data['concepts'] = concept_matches
    
    # Extract completed projects
    project_section = re.search(r'### Projects Completed\n(.*?)(?=###|\n##)', content, re.DOTALL)
    if project_section:
        project_matches = re.findall(r'\d+\.\s\*\*(.+?)\*\*', project_section.group(1))
        data['projects'] = project_matches
    
    # Extract completed achievements
    achievement_matches = re.findall(r'- \[x\] (.+?)(?:\n|$)', content)
    data['achievements'] = achievement_matches
    
    # Extract uncompleted knowledge gaps
    gaps_section = re.search(r'## Knowledge Gaps Identified\n(.*?)(?=\n##)', content, re.DOTALL)
    if gaps_section:
        gap_matches = re.findall(r'- \[ \] (.+?)(?:\n|$)', gaps_section.group(1))
        data['knowledge_gaps'] = gap_matches
    
    # Extract uncompleted goals from "Goals for Next Month"
    goals_section = re.search(r'## Goals for Next Month\n(.*?)(?=\n## |\Z)', content, re.DOTALL)
    if goals_section:
        goals_content = goals_section.group(1)
        
        # Learning goals
        learning_section = re.search(r'### Learning Goals\n(.*?)(?=###|\n## |\Z)', goals_content, re.DOTALL)
        if learning_section:
            data['learning_goals'] = re.findall(r'- \[ \] (.+)', learning_section.group(1))
        
        # Project goals
        project_section = re.search(r'### Project Goals\n(.*?)(?=###|\n## |\Z)', goals_content, re.DOTALL)
        if project_section:
            data['project_goals'] = re.findall(r'- \[ \] (.+)', project_section.group(1))
        
        # Skill goals
        skill_section = re.search(r'### Skill Goals\n(.*?)(?=###|\n## |\Z)', goals_content, re.DOTALL)
        if skill_section:
            data['skill_goals'] = re.findall(r'- \[ \] (.+)', skill_section.group(1))
    
    # Extract resources
    resources_section = re.search(r'## Resources to Explore\n(.*?)(?=\n##)', content, re.DOTALL)
    if resources_section:
        data['resources'] = re.findall(r'- \[ \] (.+?)(?:\n|$)', resources_section.group(1))
    
    # Extract rating
    rating_match = re.search(r'\*\*Overall Rating\*\*: (.+?)(?:\n|$)', content)
    if rating_match:
        data['rating'] = rating_match.group(1)
    
    # Extract personal growth notes
    notes_section = re.search(r'## Personal Growth Notes\n(.*?)(?=\n---)', content, re.DOTALL)
    if notes_section:
        data['personal_notes'] = notes_section.group(1).strip()
    
    return data


def get_next_month_info(current_file_path):
    """Extract current month info and calculate next month."""
    file_name = Path(current_file_path).stem
    
    # Try to parse month from filename (e.g., "september-reflection")
    month_match = re.search(r'([a-z]+)-reflection', file_name.lower())
    if month_match:
        month_name = month_match.group(1)
        
        # Get current year from file path
        year_match = re.search(r'(\d{4})', str(current_file_path))
        year = int(year_match.group(1)) if year_match else datetime.now().year
        
        # Convert month name to number
        month_names = ['january', 'february', 'march', 'april', 'may', 'june',
                      'july', 'august', 'september', 'october', 'november', 'december']
        
        try:
            current_month_num = month_names.index(month_name) + 1
        except ValueError:
            # Fallback to current date
            current_month_num = datetime.now().month
            year = datetime.now().year
        
        # Calculate next month
        if current_month_num == 12:
            next_month_num = 1
            next_year = year + 1
        else:
            next_month_num = current_month_num + 1
            next_year = year
        
        current_month_name = month_names[current_month_num - 1].capitalize()
        next_month_name = month_names[next_month_num - 1].capitalize()
        
        return {
            'current_month': current_month_name,
            'current_month_num': current_month_num,
            'current_year': year,
            'next_month': next_month_name,
            'next_month_num': next_month_num,
            'next_year': next_year
        }
    
    return None


def create_summary(data, month_info):
    """Create a brief summary of the previous month."""
    summary_parts = []
    
    if data['concepts']:
        summary_parts.append(f"Mastered {len(data['concepts'])} new concepts including {', '.join(data['concepts'][:2])}")
    
    if data['projects']:
        summary_parts.append(f"Completed {len(data['projects'])} projects")
    
    if data['achievements']:
        summary_parts.append(f"Achieved {len(data['achievements'])} milestones")
    
    summary = f"**Previous Month ({month_info['current_month']} {month_info['current_year']})**: " + ". ".join(summary_parts) + "."
    
    if data['rating']:
        summary += f" Overall rating: {data['rating']}"
    
    return summary


def generate_next_reflection(current_file_path, output_path=None):
    """Generate the next month's reflection file."""
    
    # Parse current file
    data = parse_reflection_file(current_file_path)
    
    # Get month information
    month_info = get_next_month_info(current_file_path)
    if not month_info:
        print("Error: Could not parse month information from filename")
        return
    
    # Create summary
    summary = create_summary(data, month_info)
    
    # Calculate date range for next month
    next_year = month_info['next_year']
    next_month = month_info['next_month_num']
    last_day = monthrange(next_year, next_month)[1]
    
    start_date = f"{next_year}-{next_month:02d}-01"
    end_date = f"{next_year}-{next_month:02d}-{last_day}"
    
    # Calculate review dates
    review_date = f"{next_year}-{next_month:02d}-{last_day}"
    
    # Next review date (first day of month after next)
    if next_month == 12:
        next_review_month = 1
        next_review_year = next_year + 1
    else:
        next_review_month = next_month + 1
        next_review_year = next_year
    next_review_date = f"{next_review_year}-{next_review_month:02d}-1"
    
    # Generate new file content
    content = f"""# Monthly Reflection - {month_info['next_month']} {next_year}

## Date Range
From: {start_date}  
To: {end_date}

## Previous Month Summary
{summary}

## Learning Summary

### New Concepts Mastered
- [ ] [Concept name] - Confidence level (1-10)
- [ ] [Concept name] - Confidence level (1-10)

### Projects Completed
1. **[Project Name]** - [Brief description of what you built and learned]
2. **[Project Name]** - [Brief description of what you built and learned]

### Skills Developed
- **Technical Skills**: [List technical skills you improved or learned]
- **Soft Skills**: [List soft skills like communication, time management, etc.]
- **Tools/Frameworks**: [List new tools or frameworks you learned]

## Challenges & Solutions

### Biggest Challenge
[Describe the main challenge you faced this month]

### How You Overcame It
[Explain your approach to solving the challenge]

### Lessons Learned
[Key takeaways and insights from this month's experiences]

## Achievements & Milestones
- [ ] [Achievement or milestone]
- [ ] [Achievement or milestone]

## Knowledge Gaps Identified
"""
    
    # Add carried-over knowledge gaps
    if data['knowledge_gaps']:
        for gap in data['knowledge_gaps']:
            content += f"- [ ] {gap}\n"
    else:
        content += "- [ ] [Knowledge gap] - Priority level (High/Medium/Low)\n"
        content += "- [ ] [Knowledge gap] - Priority level (High/Medium/Low)\n"
    
    content += "\n## Goals for Next Month\n\n### Learning Goals\n"
    
    # Add carried-over learning goals
    if data['learning_goals']:
        for goal in data['learning_goals']:
            # Update dates if they exist in the goal
            updated_goal = re.sub(r'\d{4}-\d{2}-\d{2}', f'{next_year}-{next_month:02d}-15', goal)
            content += f"- [ ] {updated_goal}\n"
    else:
        content += f"- [ ] [Learning goal] - Target completion date: {next_year}-{next_month:02d}-15\n"
        content += f"- [ ] [Learning goal] - Target completion date: {next_year}-{next_month:02d}-{last_day}\n"
    
    content += "\n### Project Goals\n"
    
    # Add carried-over project goals
    if data['project_goals']:
        for goal in data['project_goals']:
            content += f"- [ ] {goal}\n"
    else:
        content += "- [ ] [Project goal]\n"
        content += "- [ ] [Project goal]\n"
    
    content += "\n### Skill Goals\n"
    
    # Add carried-over skill goals
    if data['skill_goals']:
        for goal in data['skill_goals']:
            content += f"- [ ] {goal}\n"
    else:
        content += "- [ ] [Skill to develop]\n"
    
    content += "\n## Resources to Explore\n"
    
    # Add carried-over resources
    if data['resources']:
        for resource in data['resources']:
            content += f"- [ ] {resource}\n"
    else:
        content += "- [ ] [Resource name or link]\n"
    
    content += f"""
## Personal Growth Notes
[Reflect on your overall progress, mindset, challenges, and what you're learning about yourself as you grow in AI/ML and your career]

---
**Overall Rating**: ⭐⭐⭐⭐⭐ (Rate your month: 1-5 stars with brief comment)
**Review Completed On**: {review_date}
**Next Review Date**: {next_review_date}
"""
    
    # Determine output path
    if output_path is None:
        current_path = Path(current_file_path)
        next_month_lower = month_info['next_month'].lower()
        output_path = current_path.parent / f"{next_month_lower}-reflection.md"
    
    # Write the new file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Created new reflection file: {output_path}")
    print(f"📅 Month: {month_info['next_month']} {next_year}")
    print(f"📋 Carried over {len(data['knowledge_gaps'])} knowledge gaps")
    print(f"🎯 Carried over {len(data['learning_goals'])} learning goals")
    print(f"🚀 Carried over {len(data['project_goals'])} project goals")
    
    return output_path


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python create_next_reflection.py <path_to_current_reflection.md> [output_path]")
        print("\nExample:")
        print("  python create_next_reflection.py reflections/2025/september-reflection.md")
        sys.exit(1)
    
    current_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    if not Path(current_file).exists():
        print(f"Error: File not found: {current_file}")
        sys.exit(1)
    
    generate_next_reflection(current_file, output_file)
