import json

# Example prompt
prompt = "Extract skills from this resume text: Python, Java, SQL, React, Spring Boot."

print("Prompt sent to LLM:")
print(prompt)
print()

# Simulated LLM JSON response (free/offline demo)
llm_response = """
{
  "skills": ["Python", "Java", "SQL", "React", "Spring Boot"]
}
"""

# Parse structured output
parsed = json.loads(llm_response)

print("Structured output:")
print(json.dumps(parsed, indent=2))