# Scripts

Utility scripts to help manage your AI growth journal.

## create_next_reflection.py

Automatically generates next month's reflection file based on the current month's reflection.

### Features
- ✅ Creates a summary of the previous month at the top
- ✅ Carries forward uncompleted knowledge gaps
- ✅ Carries forward uncompleted goals (learning, project, and skill goals)
- ✅ Carries forward unexplored resources
- ✅ Updates dates automatically for the next month
- ✅ Maintains consistent structure and formatting

### Usage

```bash
# Basic usage - creates next month's file in the same directory
python scripts/create_next_reflection.py reflections/2025/september-reflection.md

# Specify custom output path
python scripts/create_next_reflection.py reflections/2025/september-reflection.md reflections/2025/october-reflection.md
```

### Example

If you run this on `september-reflection.md`, it will:
1. Parse all your September achievements, projects, and concepts
2. Create a summary like: "Mastered 3 new concepts including GUI Automation, Git Version Control. Completed 3 projects. Achieved 5 milestones."
3. Generate `october-reflection.md` with:
   - The September summary at the top
   - All uncompleted goals carried forward
   - Dates updated to October
   - Empty sections ready to fill in as you progress

**Sample Output:**
```
✅ Created new reflection file: reflections\2025\october-reflection.md
📅 Month: October 2025
📋 Carried over 2 knowledge gaps
🎯 Carried over 3 learning goals
🚀 Carried over 2 project goals
```

### What Gets Carried Forward
- ✅ Uncompleted knowledge gaps
- ✅ Uncompleted learning goals (with updated target dates)
- ✅ Uncompleted project goals
- ✅ Uncompleted skill goals
- ✅ Unexplored resources

### What Starts Fresh
- New concepts mastered (empty checkboxes)
- Projects completed (empty list)
- Skills developed (empty)
- Challenges & solutions (empty)
- Achievements & milestones (empty)
- Personal growth notes (empty)
