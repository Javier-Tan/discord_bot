@echo on

cd /D "%~dp0"

python -m venv .venv

.venv/Scripts/activate

pip install -r requirements.txt