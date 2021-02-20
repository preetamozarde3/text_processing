import re
import pandas as pd

def square_brackets(string_to_process):
    dp = []
    flag = False
    processed_string = ""
    for char in string_to_process:
        if char == "[":
            flag = True
        if char == "]" and flag:
            flag = False
            dp.append(processed_string)
            processed_string = ""
        if flag and char != "[":
            processed_string = processed_string + char
    return dp

def exclamation(string_to_process):
    ij = []
    str_beg = False
    processed_string = ""
    for char in string_to_process:
        if char == "!":
            if not processed_string:
                str_beg = True
            else:
                str_beg = False
                ij.append(processed_string)
                processed_string = ""

        if str_beg and char != "!":
            processed_string = processed_string + char
    return ij

def round_brackets(string_to_process):
    fls = []
    flag = False
    processed_string = ""
    for char in string_to_process:
        if char == "(":
            flag = True
        if char == ")" and flag:
            flag = False
            if processed_string not in phenomena:
                fls.append(processed_string)
            processed_string = ""
        if flag and char != "(":
            processed_string = processed_string + char
    return fls

def hashes(string_to_process):
    fl = []
    str_beg = False
    processed_string = ""
    for char in string_to_process:
        if char == "#":
            if not processed_string:
                str_beg = True
            else:
                str_beg = False
                fl.append(processed_string)
                processed_string = ""

        if str_beg and char != "#":
            processed_string = processed_string + char
    return fl

filename = "3000-1.csv"
df = pd.read_csv(filename)
discourse_particles = []
fillers = []
interjections = []
foreign_language = []
unclear_words = []
short_pauses = []
invalid = []
non_english_utterances = []
contains_fil = []
paralinguistic_phenomena = []
unknown_words = []
background_sound = []
phenomena = ["ppb", "ppc", "ppl", "ppo"]
for i in df['3']:
    if "[" in i:
        dp = square_brackets(i)
        if dp:
            discourse_particles.append(dp)
        else:
            discourse_particles.append(0)
    else:
        discourse_particles.append(0)
    if "!" in i:
        ij = exclamation(i)
        if ij:
            interjections.append(ij)
        else:
            interjections.append(0)
    else:
        interjections.append(0)
    if "(" in i:
        fls = round_brackets(i)
        if fls:
            fillers.append(fls)
        else:
            fillers.append(0)
    else:
        fillers.append(0)
    if "#" in i:
        fl = hashes(i)
        if fl:
            foreign_language.append(fl)
        else:
            foreign_language.append(0)
    else:
        foreign_language.append(0)
    if "<UNK>" in i:
        unclear_words.append(1)
    else:
        unclear_words.append(0)
    if "<S>" in i:
        short_pauses.append(1)
    else:
        short_pauses.append(0)
    if "<Z>" in i:
        invalid.append(1)
    else:
        invalid.append(0)
    if "<NEN>" in i:
        non_english_utterances.append(1)
    else:
        non_english_utterances.append(0)
    if "<FIL/>" in i:
        contains_fil.append(1)
    else:
        contains_fil.append(0)
    if "<SPK/>" in i:
        paralinguistic_phenomena.append(1)
    else:
        paralinguistic_phenomena.append(0)
    if "**" in i:
        unknown_words.append(1)
    else:
        unknown_words.append(0)
    if "<NON/>" in i:
        background_sound.append(1)
    else:
        background_sound.append(0)
    if "<NON/>" in i:
        background_sound.append(1)
    else:
        background_sound.append(0)

df['discourse_particles'] = discourse_particles
df['fillers'] = fillers
df['interjections'] = interjections
df['foreign_language'] = foreign_language
df['unclear_words'] = unclear_words
df['short_pauses'] = short_pauses
df['invalid'] = invalid
df['non_english_utterances'] = non_english_utterances
df['contains_fil'] = contains_fil
df['paralinguistic_phenomena'] = paralinguistic_phenomena
df['unknown_words'] = unknown_words

df.to_csv(filename)
