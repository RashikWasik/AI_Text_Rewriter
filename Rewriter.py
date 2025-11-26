from google import genai          # Import the Google GenAI library

# Create a client object using your API key
client = genai.Client(api_key="MY API KEY") # Replace with your own Google API key

# Ask the user to enter the text that needs to be rewritten
text = input("Enter text to rewrite: ")

# Send the text to the Gemini model along with the instruction
resp = client.models.generate_content(
    model="gemini-2.0-flash",                       # AI model you want to use
    contents=f"Rewrite this text in simple English:\n\n{text}"  # What the model should do
)

print("\nRewritten Text:\n")   # Print a title
print(resp.text)              # Print the simplified output from the model
