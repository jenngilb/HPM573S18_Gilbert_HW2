# HUI3 regression coefficients
Constant = 0.371
Coefficient = 1.371
dictCoefficients = {'Vision':       [1, 0.98, 0.89, 0.84, 0.75, 0.61],
                    'Hearing':      [1, 0.95, 0.89, 0.80, 0.74, 0.61],
                    'Speech':       [1, 0.94, 0.89, 0.81, 0.68], #there are only 5 levels for speech
                    'Ambulation':   [1, 0.93, 0.86, 0.73, 0.65, 0.58],
                    'Dexterity':    [1, 0.95, 0.88, 0.76, 0.65, 0.56],
                    'Emotion':      [1, 0.95, 0.85, 0.64, 0.46], #there are only 5 levels for emotion
                    'Cognition':    [1, 0.92, 0.95, 0.83, 0.6, 0.42],
                    'Pain':         [1, 0.96, 0.9, 0.77, 0.55]}; #there are only 5 levels for pain


def get_score(vision, hearing, speech, ambulation, dexterity, emotion, cognition, pain):
    """

    :param vision: level of vision dimension
    :param hearing: level of hearing dimension
    :param speech: level of speech dimension
    :param ambulation: level of ambulation dimension
    :param dexterity: level of dexterity dimension
    :param emotion: level of emotion dimension
    :param cognition: level of cognition dimension
    :param pain: level of pain dimension
    :return: HUI3 score
    """


    # ensure the entered health dimension levels are acceptable
    if not(vision in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Vision level can take only 1, 2, 3, 4, 5, or 6')
    if not(hearing in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Hearing level can take only 1, 2, 3, 4, 5, or 6')
    if not(speech in [1, 2, 3, 4, 5]):
        raise ValueError('Speech level can take only 1, 2, 3, 4, or 5')
    if not(ambulation in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Ambulation level can take only 1, 2, 3, 4, 5, or 6')
    if not(dexterity in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Dexterity level can take only 1, 2, 3, 4, 5, or 6')
    if not(emotion in [1, 2, 3, 4, 5]):
        raise ValueError('Emotion level can take only 1, 2, 3, 4, or 5')
    if not(cognition in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Cognition level can take only 1, 2, 3, 4, 5, or 6')
    if not(pain in [1, 2, 3, 4, 5]):
        raise ValueError('Pain level can take only 1, 2, 3, 4, or 5')

    score = Coefficient

    # subtract the coefficients of other dimensions
    score *= dictCoefficients['Vision'][vision - 1]
    score *= dictCoefficients['Hearing'][hearing - 1]
    score *= dictCoefficients['Speech'][speech - 1]
    score *= dictCoefficients['Ambulation'][ambulation - 1]
    score *= dictCoefficients['Dexterity'][dexterity - 1]
    score *= dictCoefficients['Emotion'][emotion - 1]
    score *= dictCoefficients['Cognition'][cognition - 1]
    score *= dictCoefficients['Pain'][pain - 1]

    score -= Constant

    return score
