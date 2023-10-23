from gurobipy import quicksum, Model, GRB
from gurobipy import *

def solve(days, routes, length, visitors, min_rest_days, min_length, hard_routes):
    
    model = Model('tour')

    model.modelSense = GRB.MAXIMIZE

    assignment = {}
    for day in range(days): # Achtung: day nimmt alle Werte von 0 bis days-1 an.
        for route in routes:
            assignment[day, route] = model.addVar(obj = visitors[route], vtype = GRB.BINARY, name=f"assignment_{day}_{route}")

    model.update()

    # 1. Nebenbedingung(en):
    # Bedeutung: Am letzten Tag genau 'Les Champs' gefahren
    model.addConstr(assignment[days - 1, 'Les Champs'] == 1)

    # 2. Nebenbedingung(en):
    # Bedeutung: Am ersten Tag genau eine Route gefahren
    model.addConstr(quicksum(assignment[0, route] for route in routes) == 1)

    # 3. Nebenbedingung(en):
    # Bedeutung: Jeden Tag maximal eine Route gefahren
    for day in range(days):
        model.addConstr(quicksum(assignment[day, route] for route in routes) <= 1)

    # 4. Nebenbedingung(en):
    # Bedeutung: Jeder Route maximal ein Tag zugeteilt
    for route in routes:
        model.addConstr(quicksum(assignment[day, route] for day in range(days)) <= 1)

    # 5. Nebenbedingung(en):
    # Bedeutung: Minimale Anzahl an Ruhetagen
    model.addConstr(quicksum(model.getVars()) <= days - min_rest_days)

    # 6. Nebenbedingung(en):
    # Bedeutung: Minimale Anzahl an Kilometern
    model.addConstr(quicksum(assignment[day, route] * length[route] for route in routes for day in range(days)) >= min_length)

    # 7. Nebenbedingung(en):
    # Bedeutung: Keine zwei schwere Routen an zwei aufeinander folgenden Tagen
    for day in range(days - 1):
        model.addConstr(quicksum(assignment[day, route] + assignment[day + 1, route] for route in hard_routes) <= 1)

    # ...

    model.optimize()

    if model.status == GRB.OPTIMAL:
        print(f"\nObjective value: {model.ObjVal}\n")
        for day in range(days):
            assign = None
            for route in routes:
                if (assignment[day, route].x > 0.1):
                    assign = route
            if assign == None:
                print(f'Day {day+1} will be a rest day')
            else:
                print(f'Day {day+1} will include the route: {assign}')
    else:
        print(f"No solution was found. Status {model.status}")

    return model
