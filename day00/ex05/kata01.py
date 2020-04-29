languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

if __name__ == "__main__":
    s = ""
    for key, value in languages.items():
        s += key + " was created by " + value + "\n"
    s = s.rstrip('\n')
    print(s)
