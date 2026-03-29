import time


def get_recommendations():
    resources = {
        "Business with AI": {
            "YouTube": ["The AI Advantage", "Dan Martell (AI Strategy)", "Edureka (AI for Business Course)"],
            "Website": ["Analytics Vidhya", "MIT Sloan - AI in Business", "Coursera - IBM BI Analyst"]
        },
        "Finance with AI": {
            "YouTube": ["Career Principles (AI for Finance)", "Fintool AI Reviews", "Bloomberg Technology"],
            "Website": ["Microsoft Learn (Dynamics 365 Finance)", "AlphaSense AI", "Quadratic.co"]
        },
        "Robotics": {
            "YouTube": ["Boston Dynamics", "Unitree Robotics", "PRO Robots", "Cornell University Research"],
            "Website": ["ABB Robotics", "VEX Robotics Education", "KUKA Robotics Group"]
        },
        "Mindset & Growth": {
            "YouTube": ["The Mindset Mentor (Rob Dial)", "Ali Abdaal", "Mel Robbins", "Sadhguru"],
            "Website": ["Thomas Frank (College Info Geek)", "James Clear (Atomic Habits)", "The Muse"]
        },
        "Personality & Soft Skills": {
            "YouTube": ["Charisma on Command", "The Art of Improvement", "Science of People (Vanessa Van Edwards)"],
            "Website": ["SessionLab (Soft Skills Games)", "BusinessBalls.com", "FutureLearn Professional Skills"]
        }
    }

    print("--- Welcome to the Student Resource Navigator ---")
    print("Helping you find the best Academic and Personal growth resources.\n")


    print("\nWhich field are you interested in today?")
    fields = list(resources.keys())
    for i, field in enumerate(fields, 1):
        print(f"{i}. {field}")

    while True:
        try:
            choice_input = input("\nEnter the number of your choice: ")
            choice = int(choice_input) - 1
            if 0 <= choice < len(fields):
                selected_field = fields[choice]
                break
            else:
                print(f"Invalid choice. Please enter a number between 1 and {len(fields)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


    print(f"\nGreat choice! How do you prefer to learn about {selected_field}?")
    print("1. Video (YouTube)\n2. Interactive/Reading (Websites)")

    platform_choice = input("Enter 1 or 2: ")
    platform = "YouTube" if platform_choice == "1" else "Website"


    print(f"\nAnalysing the best {platform} resources for {selected_field}...")
    time.sleep(1.5)

    results = resources[selected_field][platform]

    print(f"\n--Your Personalized Recommendations --")
    print(f"Target Field: {selected_field}")
    print(f"Platform: {platform}")
    for item in results:
        print(f"-> {item}")
    print("\nHappy learning! Remember: Small steps lead to big changes.")

if __name__ == "__main__":
    get_recommendations()