def wave(people):
    people = list(people)
    result = []
    for i in range(len(people)):
        if people[i].isalpha():
            wave_person = people[:]
            wave_person[i] = wave_person[i].upper()
            result.append("".join(wave_person))
    return result

print(wave("dff"))
