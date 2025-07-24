import os
import random
import string
import subprocess
from pathlib import Path

COMPONENTS_DIR = Path("src/components")
NUM_COMPONENTS = 10  # Customize how many components to add

def random_component_name():
    return ''.join(random.choices(string.ascii_uppercase, k=1)) + ''.join(random.choices(string.ascii_lowercase, k=6))

def generate_tsx_component(name):
    return f"""import React from 'react';

const {name} = () => {{
  return (
    <div>
      <h2>{name} says hi 👋</h2>
      <p>{random.choice(["Lorem", "Ipsum", "Dolor", "Sit", "Amet"])} {random.randint(1, 100)}</p>
    </div>
  );
}}

export default {name};
"""

def write_component_file(name):
    COMPONENTS_DIR.mkdir(parents=True, exist_ok=True)
    path = COMPONENTS_DIR / f"{name}.tsx"
    with open(path, "w") as f:
        f.write(generate_tsx_component(name))
    return path

def git_commit(file_path, message):
    subprocess.run(["git", "add", str(file_path)], check=True)
    subprocess.run(["git", "commit", "-m", message], check=True)

def git_push():
    subprocess.run(["git", "push", "origin", "main"], check=True)

def main():
    for _ in range(NUM_COMPONENTS):
        name = random_component_name()
        file_path = write_component_file(name)
        git_commit(file_path, f"Add {name} component")
    
    git_push()

if __name__ == "__main__":
    main()
