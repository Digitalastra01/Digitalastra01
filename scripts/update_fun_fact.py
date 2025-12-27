import requests
import re
import os

def get_random_fact():
    try:
        response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
        if response.status_code == 200:
            return response.json()['text']
    except Exception as e:
        print(f"Error fetching fact: {e}")
    return "Did you know? Python is named after Monty Python's Flying Circus, not the snake!"

def update_readme(fact):
    readme_path = "README.md"
    try:
        with open(readme_path, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Regex to find the content between markers
        pattern = r"(<!-- FUN_FACT_START -->)(.*?)(<!-- FUN_FACT_END -->)"
        replacement = f"\\1\n> {fact}\n\\3"
        
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        with open(readme_path, "w", encoding="utf-8") as file:
            file.write(new_content)
            
        print("README.md updated successfully.")
        
    except FileNotFoundError:
        print("README.md not found.")

if __name__ == "__main__":
    fact = get_random_fact()
    print(f"Fetched Fact: {fact}")
    update_readme(fact)
