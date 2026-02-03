# AI Growth Journal

A personal repository to track learning, projects, and growth in the AI field over multiple years.

## Recent Highlights
- 💍 **Married** (January 17, 2026) - Major life milestone
- 🌍 **Evaluating International Relocation** - Considering move to GCC country (Oman)
- 🎓 **Azure AI-102 Certification** (December 2025) - Cloud AI and Machine Learning
- 🎓 **FHIR Fundamentals Certificate** (November 2025) - Healthcare interoperability standards
- 💼 **Associate AI Automation Engineer** at DHR (September 2025) - 1.2 years at DHR
- 📊 **6+ Production Projects** - Including HL7 messaging systems, data pipelines, and automation tools
- 🚀 **Luigi AI** - Side business (currently evaluating future direction)

## Repository Structure

```
ai-growth-journal/
├── README.md                    # This file
├── _SHARED_CONTEXT.md          # Consolidated context for therapist & career counselor
├── learning/                    # Organized learning materials
│   ├── 2025/                   # Year-based organization
│   │   ├── courses/            # Online courses, tutorials
│   │   ├── papers/             # Research papers and notes
│   │   ├── concepts/           # Key concept explanations
│   │   └── skills/             # Specific skill development
│   ├── languages/              # Language-specific learning
│   │   ├── python/             # Primary focus
│   │   ├── javascript/         # Web development
│   │   ├── r/                  # Statistics and data science
│   │   └── sql/                # Database queries
│   ├── tools/                  # Tools and frameworks
│   │   ├── libraries/          # Library-specific notes
│   │   ├── frameworks/         # Framework learning
│   │   └── platforms/          # Cloud platforms, MLOps
│   └── resources/              # General resources and references
├── projects/                   # Hands-on projects
│   └── 2025/                   # Year-based organization
│       ├── experiments/        # Quick experiments and prototypes
│       ├── tutorials/          # Following tutorials
│       └── personal/           # Personal projects
├── career/                     # Career development
│   └── portfolio-and-certifications/  # Certificates and portfolio items
├── reflections/                # Personal growth tracking
│   ├── 2025/                   # Year-based reflections
│   └── milestones/             # Major achievements
├── therapy/                    # Therapy session notes (private)
│   └── _SESSION_INDEX.md       # Session log and running themes
├── career-counseling/          # Career counseling and assessments
│   └── 20251118-career-counselor-assessment.md
├── memories/                   # Screenshots and memorable moments
└── templates/                  # Reusable templates
```

## Usage Guidelines

### Daily Learning
- Add new concepts to `learning/YYYY/concepts/`
- Document experiments in `projects/YYYY/experiments/`
- Track progress in `reflections/YYYY/`

### Project Organization
- Use descriptive folder names with dates
- Include README.md in each project folder
- Tag projects by difficulty and topic

### File Naming Conventions
- Use lowercase with hyphens: `machine-learning-basics.md`
- Include dates for time-sensitive content: `2025-01-15-transformer-paper.md`
- Use consistent prefixes for similar content types

## Getting Started

1. Create your first learning entry in `learning/2025/concepts/`
2. Start a project in `projects/2025/experiments/`
3. Document your progress in `reflections/2025/`

## Templates

See the `templates/` directory for:
- Project README template
- Learning note template
- Reflection template

## Automation Scripts

The `scripts/` directory contains helpful automation tools:

### Generate Next Month's Reflection
Automatically create next month's reflection file based on the current month:

```bash
python scripts/create_next_reflection.py reflections/2025/september-reflection.md
```

This will:
- ✅ Create a summary of the previous month
- ✅ Carry forward uncompleted goals and knowledge gaps
- ✅ Update all dates automatically
- ✅ Maintain consistent formatting

See `scripts/README.md` for more details.
