"""
Task 1: Stateful Graph - Simple Demo
Shows that LangGraph maintains state across steps
"""

import os
from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI

# Define state structure
class ConversationState(TypedDict):
    name: str
    greeting: str
    farewell: str

def main():
    print("\n🕸️ STATEFUL GRAPH DEMO")
    print("=" * 40)
    
    # Setup LLM
    llm = ChatGoogleGenerativeAI(
        model=os.getenv("GOOGLE_MODEL", "gemini-2.5-flash"),
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )
    
    # Input
    name = "Rayner Villalba"
    print(f"Input: {name}\n")
    
    # Define nodes that use state
    def greet_person(state: ConversationState):
        """Step 1: Greet and save name to state"""
        prompt = f"Say hello to {state['name']} in 5 words or less"
        greeting = llm.invoke(prompt).content
        print(f"Step 1: {greeting} (saved name to state)")
        return {"greeting": greeting}
    
    def say_farewell(state: ConversationState):
        """Step 2: Use saved name from state"""
        prompt = f"Say goodbye to {state['name']} mentioning their name in 5 words or less"
        farewell = llm.invoke(prompt).content
        print(f"Step 2: {farewell} (used name from state)")
        return {"farewell": farewell}
    
    def check_memory(state: ConversationState):
        """Test: Can access saved state"""
        print(f"\nMemory Test: The person's name is {state['name']}")
        print("→ State preserved! Graph remembers everything.\n")
        return {}
    
    # Build the graph
    workflow = StateGraph(ConversationState)
    workflow.add_node("greet", greet_person)
    workflow.add_node("farewell", say_farewell)
    workflow.add_node("memory", check_memory)
    
    # Define flow
    workflow.set_entry_point("greet")
    workflow.add_edge("greet", "farewell")
    workflow.add_edge("farewell", "memory")
    workflow.add_edge("memory", END)
    
    # Compile and run
    app = workflow.compile()
    result = app.invoke({"name": name})
    
    print("Stateful graph completed.\n")
    print("Stateful Graph: Memory preserved across steps\n")
    print(f"Input: {name}")
    print(f"Output: {result.get('greeting', '')} → {result.get('farewell', '')}")
    print(f"Memory: {name} (preserved in state)\n")

if __name__ == "__main__":
    main()