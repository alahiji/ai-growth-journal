@echo off
echo Updating milestones with current time calculations...
cd /d "%~dp0"
py update_milestones.py
pause
