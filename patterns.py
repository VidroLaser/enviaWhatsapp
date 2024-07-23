import re


def remove_after_at(text):
    # Define a regex que remove tudo após ".AT" (inclusive ".AT")
    regex = r'\.?AT.*'
    cleaned_text = re.sub(regex, "", text)
    return cleaned_text


def remove_after_ic_r(text):
    # Define the regex pattern
    pattern = r'(IÇ|\.IÇ|R|\.R).*'
    # Replace the matched pattern with an empty string
    result = re.sub(pattern, "", text)
    return result


def contains_ic_r(text):
    # Define the regex pattern to search for "IÇ" or "R" case-insensitive
    pattern = r'IÇ|R'
    # Search the text for the pattern with case-insensitive flag
    if re.search(pattern, text, re.IGNORECASE):
        return True
    else:
        return False


def remover_letras(string):
    # Substitui todas as letras (a-z, A-Z) por uma string vazia
    resultado = re.sub(r'[a-zA-Z]', '', string)
    return resultado


def filter_words(words):
    final_list = []
    for word in words:
        cleaned_word = remove_after_at(word)
        if len(cleaned_word.replace('.', '')) != 5:
            final_list.append(cleaned_word)
    return final_list
