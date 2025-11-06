import random

def show_intro():
    print("="*50)
    print("🎨 Welcome to Art Assistant! 🎨")
    print("="*50)
    print("This program helps you find creative drawing ideas!")
    print()

def get_art_style():
    print("Choose your art style:")
    print("1. Realistic")
    print("2. Fantasy")
    print("3. Cartoon")
    print("4. Abstract")
    print("5. Random Mix")
    choice = input("Enter your choice (1-5): ").strip()

    styles = {
        "1": "Realistic",
        "2": "Fantasy",
        "3": "Cartoon",
        "4": "Abstract",
        "5": "Mixed"
    }

    return styles.get(choice, "Mixed")

def generate_idea(style):
    realistic = [
        "A portrait of an old man under soft sunlight",
        "A still life with fruits and a glass of water",
        "A rainy street in the city at night"
    ]

    fantasy = [
        "A dragon flying over a floating island",
        "A princess holding a magical sword in a misty forest",
        "A castle made of clouds under the moonlight"
    ]

    cartoon = [
        "A funny cat wearing sunglasses",
        "Two best friends on an adventure",
        "A superhero with a donut power"
    ]

    abstract = [
        "Shapes that represent chaos and peace",
        "Lines forming a mysterious face",
        "A swirl of colors showing emotions"
    ]

    all_styles = realistic + fantasy + cartoon + abstract

    if style == "Realistic":
        return random.choice(realistic)
    elif style == "Fantasy":
        return random.choice(fantasy)
    elif style == "Cartoon":
        return random.choice(cartoon)
    elif style == "Abstract":
        return random.choice(abstract)
    else:
        return random.choice(all_styles)

def main():
    show_intro()
    name = input("Enter your name, artist: ").strip().title()
    print(f"\nWelcome, {name}! Let's find your next art idea ✨\n")

    while True:
        style = get_art_style()
        idea = generate_idea(style)
        print("\n🎨 Your art idea:")
        print(f"👉 {idea}\n")

        again = input("Do you want another idea? (yes/no): ").lower()
        if again != "yes":
            print(f"\nGoodbye, {name}! Keep drawing and stay creative ❤️")
            break


main()
