import os
import yaml
import sys

def check_file(path):
    exists = os.path.exists(path)
    status = "✅ FOUND" if exists else "❌ MISSING"
    print(f"[{status}] {path}")
    return exists

def validate_yaml(path):
    if not os.path.exists(path):
        return False
    try:
        with open(path, 'r') as f:
            yaml.safe_load(f)
        print(f"[✅ VALID] {path} syntax is correct.")
        return True
    except Exception as e:
        print(f"[❌ ERROR] {path} has YAML syntax errors: {e}")
        return False

print("--- CYSE 411 Assignment Pre-Flight Check ---")
print("Targeting directory: /vulnerable-app\n")

# 1. Check Directory Structure
critical_files = [
    ".github/workflows/starter-sast.yml",
    ".github/workflows/starter-sca.yml",
    ".github/workflows/starter-sbom.yml",
    "vulnerable-app/package.json"
]

results = [check_file(f) for f in critical_files]
yaml_results = [validate_yaml(f) for f in critical_files if f.endswith('.yml')]

print("\n--- Summary ---")
if all(results) and all(yaml_results):
    print("PASS: Your repository structure and YAML syntax are ready for submission.")
    print("NOTE: This does not verify if your security logic or 'gates' are functional.")
else:
    print("FAIL: Please fix the missing files or syntax errors listed above.")

if not all(results):
    sys.exit(1)