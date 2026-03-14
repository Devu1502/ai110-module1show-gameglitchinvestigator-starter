# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

-  When I first ran the game, the interface loaded correctly and I was able to enter guesses. However, I noticed two parts of the game behavior did not work as expected. First, after correctly guessing the number, the game displayed the message saying I already won, but pressing the New Game button did not properly reset the game and the message remained. Second, the high/low feedback logic appeared incorrect because when I guessed a number lower than the secret number, the game sometimes said Go Lower instead of Go Higher.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Claude VSCode Extension

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- One helpful suggestion from AI was about the New Game button not resetting the game. Claude explained that the problem was that the status in session state was still set to "won" even after pressing New Game. Because of this, the program kept showing the message saying the player had already won and stopped the game from starting again. The AI suggested adding st.session_state.status = "playing" in the New Game logic so the game state resets. I added that line to the code and ran the game again. After guessing the correct number and pressing New Game, the game restarted normally, which confirmed the fix worked.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
- I thought the Show Hint button was broken because when I clicked it nothing new appeared. I asked Claude to look at the code and it explained that the hint was not saved in session state and suggested changing the code to store the hint. The explanation sounded correct but after testing the game again I realized the hint was actually the Go Higher or Go Lower message from the guess result. The feature was already working and I had misunderstood how the hint worked. This showed me that AI can give confident explanations even when there is no real bug, so it is important to test things yourself before changing the code.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
