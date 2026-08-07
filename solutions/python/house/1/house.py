def recite(start_verse, end_verse):
    pieces = [
        ("house that Jack built.", ""),
        ("malt", "that lay in the "),
        ("rat", "that ate the "),
        ("cat", "that killed the "),
        ("dog", "that worried the "),
        ("cow with the crumpled horn", "that tossed the "),
        ("maiden all forlorn", "that milked the "),
        ("man all tattered and torn", "that kissed the "),
        ("priest all shaven and shorn", "that married the "),
        ("rooster that crowed in the morn", "that woke the "),
        ("farmer sowing his corn", "that kept the "),
        ("horse and the hound and the horn", "that belonged to the "),
    ]

    song = []

    for verse in range(start_verse, end_verse + 1):
        lines = ["This is the " + pieces[verse - 1][0]]

        for i in range(verse - 1, 0, -1):
            lines.append(pieces[i][1] + pieces[i - 1][0])

        song.append(" ".join(lines))

    return song