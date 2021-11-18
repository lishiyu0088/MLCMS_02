import json

def load_scenario(filename):
    with open(filename) as json_file:
        scenario = json.load(json_file)
        return scenario

def save_scenario(scenario, filename):
    with open(filename, 'w') as outfile:
        json.dump(scenario, outfile)

def add_pedestrian(scenario, x, y):
    with open("pedestrian.json") as json_file:
        pedestrian = json.load(json_file)
        pedestrian["position"]["x"] = x
        pedestrian["position"]["y"] = y
        for target in scenario["scenario"]["topography"]["targets"]:
            pedestrian["targetIds"].append(target["id"])
        scenario["scenario"]["topography"]["dynamicElements"].append(pedestrian)


scenario = load_scenario("../scenarios/rimea6_optimal_step_pedestrian.scenario")
add_pedestrian(scenario, 8.4, 1.5)
save_scenario(scenario, "../scenarios/rimea6_optimal_step_pedestrian.scenario")