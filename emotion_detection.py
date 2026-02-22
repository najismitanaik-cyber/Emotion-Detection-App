def emotion_detector(text):
    if text is None or text.strip() == "":
        return {"error": "Invalid input"}, 400

    text = text.lower()

    emotions = {
        "happy": 0,
        "sad": 0,
        "angry": 0,
        "fear": 0,
        "surprise": 0
    }

    if "happy" in text or "joy" in text:
        emotions["happy"] = 1
    if "sad" in text:
        emotions["sad"] = 1
    if "angry" in text:
        emotions["angry"] = 1
    if "fear" in text:
        emotions["fear"] = 1
    if "surprise" in text:
        emotions["surprise"] = 1

    return emotions