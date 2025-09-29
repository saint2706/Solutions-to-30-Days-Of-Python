# AGENTS

## setup

- description: Prepare the environment and install dependencies.
- run: |
  apt-get update && apt-get install -y git-lfs
  git lfs install
  if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

## run

- description: Automatically detect and run the latest lesson script.
- run: |
  latest_day=$(ls -d Day\_\* 2>/dev/null | sort -V | tail -n 1)
  if [ -n "$latest_day" ] && [ -f "$latest_day/lesson.py" ]; then
  echo "Running $latest_day/lesson.py ..."
  python "$latest_day/lesson.py"
  elif [ -f Day_01/lesson.py ]; then
  echo "No latest lesson found, running Day_01/lesson.py ..."
  python Day_01/lesson.py
  else
  echo "No lesson.py scripts found in any Day_xx folder."
  fi

## test

- description: Run the test suite if available.
- run: |
  if compgen -G "tests/test\_\*.py" > /dev/null; then
  pytest -q
  else
  echo "No tests directory found."
  fi

## lint

- description: Run code quality checks.
- run: |
  pip install black ruff || true
  black --check . || true
  ruff check . || true

## format

- description: Auto-format Python files.
- run: |
  pip install black ruff || true
  black .
  ruff --fix .

## notebook

- description: Launch Jupyter Notebook for interactive coding.
- run: |
  pip install notebook
  jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root
