"""
Task 1: Sequential Chain - Simple Demo
Shows that LangChain processes steps independently with no memory
"""

import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

def main():
    print("\n🔗 SEQUENTIAL CHAIN DEMO")
    print("=" * 40)
    
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    # Setup LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=GOOGLE_API_KEY
    )
    
    # Input
    name = "Rayner"
    print(f"Input: {name}\n")
    
    # Step 1: Create greeting
    prompt1 = ChatPromptTemplate.from_template("Say hello to {name} in 5 words or less")
    chain1 = prompt1 | llm
    greeting = chain1.invoke({"name": name}).content
    print(f"Step 1: {greeting}")
    
    # Step 2: Create farewell (independent - doesn't know the name)
    prompt2 = ChatPromptTemplate.from_template("Say a friendly goodbye in 5 words or less")
    chain2 = prompt2 | llm
    farewell = chain2.invoke({}).content
    print(f"Step 2: {farewell}")
    
    # Test memory: Ask about the name
    prompt3 = ChatPromptTemplate.from_template("What was the person's name from our conversation?")
    chain3 = prompt3 | llm
    memory_test = chain3.invoke({}).content
    print(f"\nMemory Test: {memory_test}")
    print("→ No memory! Each step is independent.\n")
    
if __name__ == "__main__":
    main()