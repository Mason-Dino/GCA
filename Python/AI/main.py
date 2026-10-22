import json
import ollama

def get_current_weather(city: str) -> str:
    mock_database = {
        "new york": "Cold and rainy, 8°C",
        "london": "Overcast and windy, 12°C",
        "tokyo": "Clear skies, 18°C"
    }
    return mock_database.get(city.lower(), "Weather data unavailable for this location.")

available_tools = {
    "get_current_weather": get_current_weather
}
userInput = input("What is your message: ")
messages = [
    {"role": "user", "content": userInput}
]

print("Sending initial prompt to Llama 3.2...")

response = ollama.chat(
    model="llama3.2",
    messages=messages,
    tools=[get_current_weather]
)

if response.message.tool_calls:
    print("\nLlama 3.2 decided to call a tool!")
    
    for tool_call in response.message.tool_calls:
        func_name = tool_call.function.name
        func_args = tool_call.function.arguments
        
        print(f"-> Tool Name: {func_name}")
        print(f"-> Arguments: {func_args}")
        
        if func_name in available_tools:
            tool_to_call = available_tools[func_name]
            tool_output = tool_to_call(**func_args)
            print(f"-> Tool Output: {tool_output}")
            
            messages.append(response.message)
            messages.append({
                "role": "tool",
                "content": str(tool_output),
                "name": func_name
            })
            
            print("\nSending tool results back to Llama 3.2...")
            final_response = ollama.chat(
                model="llama3.2",
                messages=messages
            )
            
            print("\nFinal Answer:")
            print(final_response.message.content)
else:
    print("\nNo tool was called.")
    print(response.message.content)
