def make_greetings(people, course, keys):
    greetings = []
    for person in people:
        if course in person[keys.courses]:
            greetings.append(f"Hello {person[keys.name]}\n")
    return greetings
