import random
import re


class ReactionManager:

    def __init__(self):

        self.rules = {

            "😂": [
                "lol",
                "lmao",
                "lmfao",
                "haha",
                "funny"
            ],

            "💀": [
                "dead",
                "bro",
                "nah",
                "crazy",
                "wtf"
            ],

            "😭": [
                "sad",
                "cry",
                "rip",
                "pain",
                "lost"
            ],

            "🔥": [
                "fire",
                "clean",
                "nice",
                "cool",
                "goated",
                "insane"
            ],

            "👀": [
                "look",
                "watch",
                "see",
                "proof",
                "show"
            ],

            "❤️": [
                "love",
                "thanks",
                "thank you",
                "appreciate"
            ],

            "👍": [
                "ok",
                "okay",
                "yes",
                "sure",
                "done"
            ]

        }

    def choose(self, text):

        text = text.lower()

        for emoji, words in self.rules.items():

            for word in words:

                if re.search(rf"\b{re.escape(word)}\b", text):
                    return emoji

        if random.random() < 0.30:
            return random.choice(
                ["😂", "💀", "😭", "🔥", "👀", "👍"]
            )

        return None
