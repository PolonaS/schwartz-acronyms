import spacy
from spacy.lang.en import English

nlp = spacy.blank("en")
tokenizer = English().Defaults.create_tokenizer(nlp)


def is_valid_short_form(string):
    return has_letter(string) and (string[0].isalpha() or string[0].isdigit() or string[0] == '(')


def has_letter(string):
    return any(c.isalpha() for c in string)


def has_capital(string):
    return any(c.isupper() for c in string)


def extract_pairs(sentence):
    acronym = ""
    definition = ""
    pairs = []
    c = -1

    o = sentence.find(" (")  # find open parenthesis

    while True:
        if o > -1:
            o += 1  # skip white space, i.e. " (" -> "("

            c = sentence.find(")", o)  # find closed parenthesis
            if c > -1:
                # find the start of the previous clause based on punctuation
                cutoff = max(sentence.rfind(". ", o), sentence.rfind(", ", o))
                if cutoff == -1:
                    cutoff = -2

                definition = sentence[(cutoff + 2):o]
                acronym = sentence[(o + 1):c]

        if len(acronym) > 0 or len(definition) > 0:
            if len(acronym) > 1 or len(definition) > 1:

                next_c = sentence.find(")", c + 1)
                if acronym.find("(") > -1 and next_c > -1:
                    acronym = sentence[(o + 1):next_c]
                    c = next_c

                # if separator found within parentheses, then trim everything after it
                tmp = acronym.find(", ")
                if tmp > -1:
                    acronym = acronym[0:tmp]

                tmp = acronym.find("; ")
                if tmp > -1:
                    acronym = acronym[0:tmp]

                if len(tokenizer(acronym)) > 2 or len(acronym) > len(definition):
                    # extract the last token before "(" as a candidate for acronym
                    tmp = sentence.rfind(" ", o - 2)
                    str = sentence[(tmp + 1):(o - 1)]

                    # swap acronym & definition
                    definition = acronym
                    acronym = str

                    if not has_capital(acronym):
                        acronym = ""  # delete invalid acronym

                _acronym = acronym.strip()
                _definition = definition.strip()

                if is_valid_short_form(acronym) and match_pair(_acronym, _definition):
                    pairs.append({"acronym": _acronym, "definition": _definition})

            # prepare to process the rest of the sentence after ")"
            sentence = sentence[(c + 1):]
        elif o > -1:
            sentence = sentence[(o + 1):]

        acronym = ""
        definition = ""

        o = sentence.find(" (")
        if o == -1:
            break

    return pairs


def best_long_form(acronym, definition):
    print("best_long_form:\n \tacronym: " + acronym + "\n \tdefinition: " + definition)
    return True


def match_pair(acronym, definition):
    print("match_pair:\n \tacronym: " + acronym + "\n \tdefinition: " + definition)
    return True
