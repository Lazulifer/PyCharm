import sys
from difflib import SequenceMatcher
from datetime import datetime
from http.client import responses
import Password_Generator_Mine

'''
HW
1. Add more responses
2. Add a way to exit the program through the chat
3. Add some cool features, like checking for the weather forecast.
4. Make it so that if the accuracy falls below 50%, it features a default response.
'''


class ChatBot:
    def __init__(self, name: str, responses: dict[str, str]) -> None:
        self.name = name
        self.responses = responses

    # Tells us how similar our input sentence is to our response sentence
    # Since we aren't using "self" in the actual method, the function throws a warning that it's
    # static. This means we can remove self from the arguments and instead annotate it as a
    # static method. This means that it can be used anywhere in the project without the class
    # or instance, but we want to include it in the function

    @staticmethod
    def calculate_similarity(input_sentence: str, response_sentence: str) -> float:

        # Compares input to output
        sequence: SequenceMatcher = SequenceMatcher(a=input_sentence, b=response_sentence)
        return sequence.ratio()

    # This function grabs the best response
    # The string is the response, while the float is the % similarity
    def get_best_response(self, user_input: str) -> tuple[str, float]:

        highest_similarity: float = 0.0
        best_match: str = 'Sorry, I didn\'t understand that' # Only triggers at 0% match

        for response in self.responses: # For each response in the full list

            # Calculate the similarity value between the user input and the response in question
            similarity: float = self.calculate_similarity(user_input, response)

            # If that value is higher than the current highest similarity (starts at 0)
            if similarity > highest_similarity:

                # Highest similarity is updated to be that value
                highest_similarity = similarity
                # A best match string response is decided.
                best_match: str = self.responses[response]

        # At the loop's end, the response with the highest similarity is what's decided on

        return best_match, highest_similarity

    def run(self) -> None:
        print(f'Hello! My name is {self.name}, how can I help you today?')

        while True: # Infinite
            user_input: str = input('You: ')

            # 2 returned values that are being unpacked with this syntax
            response, similarity = self.get_best_response(user_input)

            if similarity < 0.5:
                response = "Apologies. Please try again"

            elif response == 'GET_TIME':
                response = f'The time is: {datetime.now():%H:%M}'

            elif response == 'Goodbye! Have a great day!':
                print("Your session with this chat bot has ended. Please leave a review")
                sys.exit()

            elif response == 'GET_PASSWORD':
                password = Password_Generator_Mine
                password.main()
                response = 'Here are some ideas'

            print(f'{self.name}: {response} (Similarity: {similarity: .2%})')


def main() -> None:
    responses: dict[str, str] = {
        'hello': 'Hello! How are you today?',
        'how are you': 'Great, thanks! What about you?',
        'what time is it': 'GET_TIME',
        'I want to leave': 'Goodbye! Have a great day!',
        'do you have any family': 'You are my family',
        'what are your pronouns': 'As a machine, I have no pronouns. Call me whatever you like',
        'new password list': 'GET_PASSWORD',
    }

    chatbot: ChatBot = ChatBot(name='Bob', responses=responses)
    chatbot.run()

if __name__ == '__main__':
    main()


'''
HW
1. Add more responses
2. Add a way to exit the program through the chat 
3. Add some cool features, like checking for the weather forecast.
4. Make it so that if the accuracy falls below 50%, it features a default response.
'''