import csv


def write(data_dict):
    # generate the list of opening names
    print("Getting opening names...")
    opening_names = []
    for year in data_dict:
        for opening in data_dict[year]:
            if opening not in opening_names:
                opening_names.append(opening)
    opening_names.sort()
    print("Finished getting opening names!")

    with open("white.csv", 'w', newline='') as whiteFile, open("black.csv", 'w', newline='') as blackFile, \
            open("draw.csv", 'w', newline='') as drawFile, open("popularity.csv", 'w', newline='') as popularityFile:

        fieldnames = ['Year'] + opening_names

        whiteWriter = csv.DictWriter(whiteFile, fieldnames=fieldnames)
        blackWriter = csv.DictWriter(blackFile, fieldnames=fieldnames)
        drawWriter = csv.DictWriter(drawFile, fieldnames=fieldnames)
        popularityWriter = csv.DictWriter(popularityFile, fieldnames=fieldnames)

        whiteWriter.writeheader()
        blackWriter.writeheader()
        drawWriter.writeheader()
        popularityWriter.writeheader()

        whiteRow = {}
        blackRow = {}
        drawRow = {}
        popularityRow = {}

        for year in data_dict:
            whiteRow["Year"] = year
            blackRow["Year"] = year
            drawRow["Year"] = year
            popularityRow["Year"] = year
            total_games_in_year = sum([sum(data_dict[year][i].values()) for i in data_dict[year]])

            for opening in opening_names:
                if opening not in data_dict[year]:
                    whiteRow[opening] = 0
                    blackRow[opening] = 0
                    drawRow[opening] = 0
                    popularityRow[opening] = 0
                else:
                    whiteRow[opening] = data_dict[year][opening]["white"]
                    blackRow[opening] = data_dict[year][opening]["black"]
                    drawRow[opening] = data_dict[year][opening]["draw"]
                    total_games_of_opening_in_year = sum(data_dict[year][opening].values())
                    popularityRow[opening] = total_games_of_opening_in_year / total_games_in_year

            whiteWriter.writerow(whiteRow)
            blackWriter.writerow(blackRow)
            drawWriter.writerow(drawRow)
            popularityWriter.writerow(popularityRow)

# write({'1834': {'C24': {'white': 1, 'draw': 0, 'black': 0}, 'C42': {'white': 1, 'draw': 0, 'black': 0}, 'B21': {'white': 1, 'draw': 0, 'black': 1}, 'D20': {'white': 4, 'draw': 1, 'black': 3}, 'C37': {'white': 1, 'draw': 0, 'black': 0}, 'C53': {'white': 0, 'draw': 1, 'black': 0}, 'D32': {'white': 1, 'draw': 0, 'black': 0}, 'C25': {'white': 0, 'draw': 0, 'black': 1}, 'C38': {'white': 1, 'draw': 0, 'black': 1}, 'C33': {'white': 0, 'draw': 0, 'black': 1}, 'C23': {'white': 0, 'draw': 1, 'black': 1}, 'C51': {'white': 0, 'draw': 0, 'black': 1}}})
# write({'1834': {'C24': {'white': 1, 'draw': 0, 'black': 0}, 'B21': {'white': 0, 'draw': 0, 'black': 1}, 'D32': {'white': 1, 'draw': 0, 'black': 0}, 'D20': {'white': 2, 'draw': 0, 'black': 3}, 'C25': {'white': 0, 'draw': 0, 'black': 1}, 'C38': {'white': 1, 'draw': 0, 'black': 1}, 'C33': {'white': 0, 'draw': 0, 'black': 1}, 'C51': {'white': 0, 'draw': 0, 'black': 1}}, '1835': {'C42': {'white': 1, 'draw': 0, 'black': 0}}, '1837': {'D20': {'white': 1, 'draw': 0, 'black': 0}}, '1832': {'B21': {'white': 1, 'draw': 0, 'black': 0}}, '1831': {'C37': {'white': 1, 'draw': 0, 'black': 0}}, '1840': {'C53': {'white': 0, 'draw': 1, 'black': 0}}, '1852': {'D20': {'white': 1, 'draw': 1, 'black': 0}, 'C23': {'white': 0, 'draw': 1, 'black': 1}}})