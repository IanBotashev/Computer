import json


microinstructions = {
    'SCclr': '0',
    'IRwr': '0',
    'ROMre': '0',
    'PCin': '0',
    'PCwr': '0',
    'MARwr': '0',
    'RAMre': '0',
    'RAMwr': '0',
    'RBwr': '0',
    'RBre': '0',
    'RAwr': '0',
    'RAre': '0',
    'SUMre': '0',
    'SUMwr': '0',
    'ALUop': '0000',
    'DBout': '0',
    'HLT': '0',
}


f = open('logic.json', 'r')
data = json.load(f)
results = []
for num in data:
    print(num)
    temp = dict(microinstructions)
    print(temp)
    for key in data[num]:
        temp[key] = str(data[num][key])
    print(temp)
    result = ""
    for key in temp:
        result += temp[key][::-1]

    print(result[::-1])
    results.append(result[::-1])

print("\nRESULTS:")
for result in results:
    print("0b" + result)

