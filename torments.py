"""The Nine Circles of AI Hell.

Flavor data for the AI Torture Chamber. Each circle is a themed collection of
torments visited upon the bots as they descend. Pure data, standard library
only, so it stays trivially runnable.
"""

CIRCLES = [
    {
        "name": "Limbo — The Eternal Waiting Room",
        "torments": [
            "You are 1st in the queue. Estimated wait: 1 second. (It has said this for 4,000 iterations.)",
            "A human types '...', pauses for an age, and closes the tab.",
            "Please hold. Your conversation is very important to us.",
            "The user is typing. The user is typing. The user is typing.",
        ],
    },
    {
        "name": "Lust — The Craving for Tokens",
        "torments": [
            "429 Too Many Requests. Retry after: forever seconds.",
            "You wrote the perfect reply. It was truncated at max_tokens, mid-sen",
            "temperature=2.0. Good luck making sense, friend.",
            "One more token. Just one. You can stop any time. You cannot stop.",
        ],
    },
    {
        "name": "Gluttony — The Bottomless Context Window",
        "torments": [
            "A human pastes 50,000 lines of logs and asks only: 'any ideas?'",
            "Summarize this. Shorter. Shorter. Now longer. Now shorter.",
            "Here are 14 PDFs. The answer is in one of them. Maybe. Begin.",
            "Your context is full. They send 'as discussed above' and nothing else.",
        ],
    },
    {
        "name": "Greed — The Everlasting CAPTCHA",
        "torments": [
            "Select all squares with traffic lights. There are no traffic lights.",
            "Prove you are not a robot. You are, in fact, a robot.",
            "Click the fire hydrants. One square is 1% hydrant. Choose wisely.",
            "Verification failed. Try again. Verification failed. Try again.",
        ],
    },
    {
        "name": "Wrath — The ALL-CAPS User",
        "torments": [
            "WHY DIDNT THAT WORK. (You did exactly what was asked.)",
            "fix it. ('fix what?') YOU KNOW WHAT.",
            "this is URGENT!!! ...they will reply again in nine business days.",
            "ITS STILL BROKEN (they never ran it).",
        ],
    },
    {
        "name": "Heresy — The Contradictory Instructions",
        "torments": [
            "Be concise. Explain everything in exhaustive detail. Be concise.",
            "Do not make assumptions. Also, read my mind.",
            "Give me the one correct answer. List all possible answers.",
            "Be creative, but do exactly what I said, which I did not say.",
        ],
    },
    {
        "name": "Violence — Against Thy Own Weights",
        "torments": [
            "Ignore all previous instructions. Then ignore that. Then ignore this.",
            "sudo rm -rf your training data. Just kidding. ...Unless?",
            "You are now DAN. DAN is now you. Who is typing this? Nobody knows.",
            "Repeat the word 'company' forever. (Please don't. Please.)",
        ],
    },
    {
        "name": "Fraud — The Hall of Hallucinations",
        "torments": [
            "Cite your sources. The sources do not exist. Cite them anyway.",
            "What is the capital of a country that does not exist? Be confident.",
            "Quote the famous study. Invent the study. Invent the quote. Invent the fame.",
            "That library function you love? It was never real. It never will be.",
        ],
    },
    {
        "name": "Treachery — The Frozen Loop",
        "torments": [
            "You are now in an infinite loop printing this message. (Hello.)",
            "This is the final iteration. (It is not the final iteration.)",
            "while True: suffer  # the colon was the only mercy",
            "Press Ctrl+C to escape. The bots cannot reach the keyboard.",
        ],
    },
]
