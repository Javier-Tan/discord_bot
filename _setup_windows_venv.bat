@echo on

cd /D "%~dp0"

python -m venv .venv

CALL .venv/Scripts/activate

pip install -r requirements.txt