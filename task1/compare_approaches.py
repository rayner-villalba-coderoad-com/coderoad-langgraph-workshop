"""
Task 1: Compare Approaches - Simple Table
Shows the key differences in a clear table format
"""

def main():
    print("\n📊 COMPARISON: SEQUENTIAL vs STATEFUL")
    print("=" * 50)
    
    # Simple comparison table
    print("""
┌─────────────────┬────────────────┬────────────────┐
│ Feature         │ Sequential     │ Stateful       │
├─────────────────┼────────────────┼────────────────┤
│ Memory          │ ❌ None        │ ✅ Preserved   │
│ Between Steps   │ Independent    │ Connected      │
│ Complexity      │ Simple         │ Flexible       │
│ Use Case        │ One-time tasks │ Conversations  │
└─────────────────┴────────────────┴────────────────┘
    """)
    
    print("Key Insight:")
    print("• Sequential: Each step starts fresh (no memory)")
    print("• Stateful: Steps share state (full memory)")
    print()

if __name__ == "__main__":
    main()
    