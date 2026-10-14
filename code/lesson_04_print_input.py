
"""Collect business details and create an AI prompt."""

# Personal details make the welcome message more relevant.
name = input("Your name: ")
business = input("Business type: ")
problem = input("Biggest problem: ")

print(f"\nWelcome, {name}!")

# A focused prompt helps the AI suggest solutions to a real problem.
prompt = f"Suggest 3 AI solutions for a {business} that struggles with {problem}."

print("--- Your AI Prompt ---")
print(prompt)
