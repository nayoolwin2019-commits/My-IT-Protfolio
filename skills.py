def display_portfolio():
    name = "Nay Oo Lwin"
    role = "Junior IT Specialist"
    
    # Skills dictionary to show data structure knowledge
    skills = {
        "Infrastructure": "Networking (Cisco Packet Tracer)",
        "Database": "SQL (Relational Design)",
        "Development": "HTML, CSS, Python",
        "Hardware": "IoT Prototype (Tinkercad)",
        "Academic": "Technical Research & Documentation"
    }
    
    print(f"--- {name}'s Technical Profile ---")
    print(f"Role: {role}\n")
    print("Core Competencies:")
    
    for category, detail in skills.items():
        print(f"[{category}]: {detail}")

    print("\nStatus: Actively seeking Junior IT opportunities.")

# Execute the function
display_portfolio()

