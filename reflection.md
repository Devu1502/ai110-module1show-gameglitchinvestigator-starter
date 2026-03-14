# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

When I first ran the game, the interface loaded correctly and I was able to enter guesses. However, I noticed two parts of the game behavior did not work as expected. First, after correctly guessing the number, the game displayed the message saying I already won, but pressing the New Game button did not properly reset the game and the message remained. Second, the high/low feedback logic appeared incorrect because when I guessed a number lower than the secret number, the game sometimes said Go Lower instead of Go Higher.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude VSCode Extension

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
One helpful suggestion from AI was about the New Game button not resetting the game. Claude explained that the problem was that the status in session state was still set to "won" even after pressing New Game. Because of this, the program kept showing the message saying the player had already won and stopped the game from starting again. The AI suggested adding st.session_state.status = "playing" in the New Game logic so the game state resets. I added that line to the code and ran the game again. After guessing the correct number and pressing New Game, the game restarted normally, which confirmed the fix worked.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
I thought the Show Hint button was broken because when I clicked it nothing new appeared. I asked Claude to look at the code and it explained that the hint was not saved in session state and suggested changing the code to store the hint. The explanation sounded correct but after testing the game again I realized the hint was actually the Go Higher or Go Lower message from the guess result. The feature was already working and I had misunderstood how the hint worked. This showed me that AI can give confident explanations even when there is no real bug, so it is important to test things yourself before changing the code.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
To decide if a bug was fixed I ran the Streamlit game and tested the behavior again. For the New Game bug I guessed the correct number and then clicked New Game to see if the game reset. After adding the status reset line the game started a new round correctly, so I knew the fix worked. I also tested the high and low logic by entering numbers above and below the secret number to check that the hints said Go Higher or Go Lower correctly. I also ran pytest tests for the check_guess function, which confirmed the function returned the correct result for different guesses. AI helped explain what the test should check and helped generate a simple pytest test, but I still verified the behavior by running the program myself.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns the entire script every time a user interacts with the app. Because of this, the program needs session state to remember important values between reruns. Session state is like memory for the app and stores things like the secret number, number of attempts, and game status. Without session state the game would reset every time the page reruns.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
One habit I want to reuse in future projects is marking suspected bugs in the code with comments like FIXME so I know where to focus when debugging. I would also run tests more often while making changes so I can quickly confirm that the logic still works. Next time I work with AI on a coding task I will test the behavior more carefully before assuming something is broken, because I initially thought the hint button was not working when it actually was. This project showed me that AI generated code can be very helpful for debugging and explaining problems, but developers still need to test and verify the results themselves.