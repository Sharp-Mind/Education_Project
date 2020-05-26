import json

collector = [{}, {}]
counter, total = 0, 0

with open('007.txt') as file:
    lines = file.readlines()

for line in lines:
    collector[0][line.split()[0]] = float(line.split()[2]) - float(line.split()[3])

    # print(f'Итог: {float(line.split()[2]) - float(line.split()[3])}')
    if float(line.split()[2]) - float(line.split()[3]) >= 0:
        total += float(line.split()[2]) - float(line.split()[3])
        counter += 1
    else:
        if len(collector) == 2:
            collector.append({})
        collector[2][line.split()[0]] = float(line.split()[2]) - float(line.split()[3])

collector[1]['average_profit'] = total / counter

# print(f'Средняя прибыль: {collector[1]["average_profit"]}')

with open('007.json', 'w') as file:
    # file.write(json.dumps(l))
    json.dump(collector, file)

