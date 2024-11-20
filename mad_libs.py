# Mad Libs Game
# By Michael Morales

def mad_libs():
    """
    Fun Mad Libs game where users provide words to fill in the blanks and create a funny story.
    """
    print("Welcome to the Mad Libs game!\n")

    # Prompt the user for various parts of speech
    adjective1 = input("Enter an adjective: ")
    adjective2 = input("Enter another adjective: ")
    noun1 = input("Enter a noun (person, place, or thing): ")
    noun2 = input("Enter another noun: ")
    verb1 = input("Enter a verb (action): ")
    verb2 = input("Enter another verb (action): ")
    adverb = input("Enter an adverb (e.g., quickly, gracefully): ")
    plural_noun = input("Enter a plural noun (e.g., cats, dogs): ")
    exclamation = input("Enter an exclamation (e.g., wow, amazing): ")

    # Construct the story with the user's inputs
    story = f"""
    Once upon a time, there was a {adjective1} {noun1} who loved to {verb1} {adverb}.
    Every day, it would {verb2} around the {adjective2} {noun2}, looking for {plural_noun} to play with.
    One day, it discovered a magical portal and exclaimed, "{exclamation}!" It stepped through the portal,
    and its life was never the same again.
    """

    # Output the generated story
    print("\nHere's your Mad Libs story:\n")
    print(story)

# Run the Mad Libs game
if __name__ == "__main__":
    mad_libs()
