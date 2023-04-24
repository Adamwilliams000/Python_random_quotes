import random

# List of quotes
quotes = [
    "Be yourself; everyone else is already taken.― Oscar Wilde",
    "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",
    "Innovation distinguishes between a leader and a follower. - Steve Jobs",
    "The harder I work, the luckier I get. - Samuel Goldwyn",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "The secret of getting ahead is getting started. - Mark Twain",
    "The best revenge is massive success. - Frank Sinatra",
    "If you are going through hell, keep going. - Winston Churchill",
    "The best way to predict the future is to create it. - Peter Drucker",
    "You are never too old to set another goal or to dream a new dream. - C.S. Lewis"
]

def get_random_quote():
    """
    Function to get a random quote from the list of quotes.
    """
    return random.choice(quotes)

def main():
    """
    Main function to run the quote generator.
    """
    print("Welcome to the Random Quote Generator!")
    while True:
        print("\nHere's a quote for you:\n")
        print(get_random_quote())
        choice = input("\nWould you like to generate another quote? (Y/N): ")
        if choice.lower() != 'y':
            print("\nThank you for using the Random Quote Generator. Have a great day!")
            break

if __name__ == '__main__':
    main()
