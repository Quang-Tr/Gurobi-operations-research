#!/usr/bin/python

from gurobipy import *


def solve(mines, ores, available, unit_costs, unit_time_needed, work_hours, subsidised_ores, demand):

    model = Model('bergwerk')

    x = {}
    for m in mines:
        for o in ores:
            x[m, o] = model.addVar(obj = unit_costs[m, o], name=f'x_{m}_{o}')

    model.modelSense = GRB.MINIMIZE

    model.update()

    # 1. Nebenbedingung:
    # Bedeutung: Für jedes Erz o soll die gesamt abgebaute Menge der AG mindestens demand[o] decken
    # Ungleichung: x_m1_o + x_m2_o + ... >= demand[o] für jedes o
    for o in ores:
        model.addConstr(quicksum(x[m, o] for m in mines) >= demand[o])

    # 2. Nebenbedingung:
    # Bedeutung: Pro Mine m und pro Erz o können nicht mehr Einheiten als available[m, o] Einheiten von o in m abgebaut werden
    # Ungleichung: x_m_o <= available[m, o] pro m und pro o
    model.addConstrs(x[m, o] <= available[m, o] for m in mines for o in ores)
    # Oder fügen ub = available[m, o] in model.addVar() hinzu

    # 3. Nebenbedingung:
    # Bedeutung: Für jede Mine m darf die Zeit, die zum Abbau von Erzen verwendet wird, nicht höher als 2/3 work_hours[m] Stunden sein
    # Ungleichung: x_m_o1 * unit_time_needed[m, o1] + x_m_o2 * unit_time_needed[m, o2] + ... <= 2/3 * work_hours[m] für jede m
    for m in mines:
        model.addConstr(quicksum(x[m, o] * unit_time_needed[m, o] for o in ores) <= 2/3 * work_hours[m])

    # 4. Nebenbedingung:
    # Bedeutung: Für jede Mine m soll mindestens ein Viertel der Einheiten abgebauter Erze zu subventionierten Erzen gehören, damit weitere Subventionierung gesichert ist
    # Ungleichung: x_m_so1 + x_m_so2 + ... >= 1/4 * (x_m_o1 + x_m_o2 + ...) für jede m
    for m in mines:
        model.addConstr(quicksum(x[m, so] for so in subsidised_ores) >= 1/4 * quicksum(x[m, o] for o in ores))

    # optimize
    model.optimize()

    # Ausgabe der Loesung.
    if model.status == GRB.OPTIMAL:
        print('\nOptimaler Zielfunktionswert: %g\n' % model.ObjVal)
        for m in mines:
            for o in ores:
                print(f"Mine {m} baut {str(x[m,o].x)} Einheiten {o} ab")
            print("")
    else:
        print('Keine Optimalloesung gefunden. Status: %i' % (model.status))
    return model

