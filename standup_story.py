#!/usr/bin/env python3
"""
Standup Story Generator - Because "still debugging" sounds sad.
"""

import random
import sys

def generate_story():
    """
    Generates a plausible-sounding standup update.
    Returns: A string that sounds productive but means "I'm stuck".
    """
    
    # The building blocks of corporate storytelling
    activities = [
        "investigating", "researching", "analyzing", "documenting",
        "refactoring", "optimizing", "benchmarking", "prototyping"
    ]
    
    issues = [
        "edge case", "race condition", "memory leak", "performance bottleneck",
        "dependency conflict", "API inconsistency", "caching issue", "null pointer"
    ]
    
    next_steps = [
        "write a test to reproduce it", "consult the documentation",
        "pair with someone after lunch", "create a proof of concept",
        "update the ticket with findings", "try a different approach"
    ]
    
    blockers = [
        "waiting on CI", "need clarification from PM",
        "environment issue", "awaiting code review"
    ]
    
    # The classic standup formula
    yesterday = f"Continued {random.choice(activities)} the {random.choice(issues)}."
    today = f"Will {random.choice(next_steps)}."
    blocked = f"Blocked by: {random.choice(blockers)}." if random.random() > 0.7 else "No blockers."
    
    return f"\n📊 STANDUP STORY:\n\nYesterday: {yesterday}\nToday: {today}\nBlockers: {blocked}"

def main():
    """Main function - generates standup stories until you feel productive."""
    print("\n🤖 Standup Story Generator")
    print("=" * 30)
    print("Press Enter for a new story, 'q' to quit\n")
    
    while True:
        print(generate_story())
        
        user_input = input("\nAnother? (press Enter for more, 'q' to quit): ").strip().lower()
        if user_input == 'q':
            print("\nGood luck in standup! Remember: confidence is key. 🚀")
            break
        print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nStory generation interrupted. Your actual productivity remains unchanged.")
        sys.exit(0)
