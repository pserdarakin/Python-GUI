import random

words = [
    "potato", "perpetual", "screeching", "man", "advertisement", "grateful", "fanatical", "theory", "skillful", "erratic",
    "shape", "print", "meeting", "four", "steel", "standing", "weigh", "minute", "force", "amount", "whip", "clover", "wave",
    "nonstop", "detailed", "aspiring", "shock", "play", "bashful", "long", "quarter", "six", "charge", "dock", "crabby",
    "dime", "wry", "story", "wiry", "rampant", "return", "dare", "open", "shame", "many", "brush", "babies", "stem", "squeeze",
    "judge", "heavenly", "defeated", "optimal", "invention", "object", "change", "sink", "verdant", "jaded", "adjoining",
    "muddled", "switch", "helpless", "motionless", "skirt", "shrug", "trip", "haircut", "oven", "lip", "habitual", "yielding",
    "bag", "wheel", "attach", "ticket", "visit", "reflect", "suppose", "present", "wound", "voyage", "real", "aunt", "religion",
    "redundant", "necessary", "fail", "flower", "unpack", "join", "gamy", "tired", "welcome", "rightful", "jeans", "obscene",
    "spring", "basket", "battle", "utter", "descriptive", "caring", "pies", "drawer", "station", "soothe", "year", "agreeable",
    "seemly", "button", "encourage", "reduce", "bed", "wave", "nosy", "zoo", "hateful", "flaky", "work", "ear", "uneven",
    "cumbersome", "languid", "box", "devilish", "yawn", "ablaze", "lake", "harbor", "legs", "glow", "glossy", "cruel", "warn",
    "hard", "unique", "card", "hug", "tangible", "hook", "label", "exotic", "account", "imagine", "grain", "tranquil", "book",
    "pickle", "whistle", "sack", "scissors", "trashy", "puzzled", "bottle", "smile", "neighborly", "eatable", "admit", "picayune",
    "type", "fast", "shy", "anger", "open", "add", "curly", "free", "aftermath", "cherry", "daily", "heal", "rose", "abhorrent",
    "short", "fine", "guarded", "vase", "fascinated", "fresh", "chickens", "mine", "stare", "boring", "include", "ajar",
    "gorgeous", "trade", "selective", "reading", "snakes", "sneeze", "spill", "helpful", "alleged", "numerous", "note", "acoustics",
    "fry", "resonant", "supply", "geese", "pets", "impulse", "scintillating", "tame", "release", "tail", "depend", "lively",
    "nondescript", "punishment", "sore", "statuesque", "stupendous", "aromatic", "thin", "coil", "serve", "rinse", "gusty",
    "swim", "save", "guttural", "attend", "shoes", "used", "periodic", "minor", "dysfunctional", "ragged", "sisters", "receptive",
    "railway", "decay", "meek", "crooked", "representative", "twist", "manage", "bored", "grotesque", "demonic", "camp",
    "temporary", "coil", "passenger", "appliance", "clam", "smoggy", "tasteless", "guess", "verse", "drab", "peep", "business",
    "paper", "female", "admire", "way", "moor", "breezy", "opposite", "comparison", "tank", "suit"]


def choose_words():
    selected_words = random.choices(words, k=40)
    return ' '.join(selected_words)