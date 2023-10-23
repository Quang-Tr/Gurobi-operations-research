# coding=utf-8

from gurobipy import *


def solve(places, goods, travel_distance, costs, capacities, availabilities, demands, max_travel):
    model = Model("lummerland")

    # Ziel (Minimieren oder Maximieren?)
    model.modelSense = GRB.MINIMIZE

    # Variablen erzeugen.
    x = {}
    for g in goods:
        for p in places:
            for q in places:
                x[g, p, q] = model.addVar(obj = costs[g] * travel_distance[p, q], name="x_" + g + "_" + p + "_" + q)

    # Variablen dem Modell bekannt machen.
    model.update()


    # Erste Nebenbedingung:
    # Bedeutung: Vorrat am Anfangsort ist beschraenkt
    # Ungleichung: x[g, p, q1] + x[g, p, q2] + ... <= availabilities[p, g]
    for g in goods:
        for p in places:
            model.addConstr(quicksum(x[g, p, q] for q in places) <= availabilities[p, g])

    # Zweite Nebenbedingung (falls noetig):
    # Bedeutung: Bedarf am Zielort ist gedeckt
    # Ungleichung: x[g, p1, q] + x[g, p2, q] + ... >= demands[q, g]
    for g in goods:
        for q in places:
            model.addConstr(quicksum(x[g, p, q] for p in places) >= demands[q, g])

    # Dritte Nebenbedingung (falls noetig):
    # Bedeutung: Chargenanzahl von p zu q ist beschraenkt
    # Ungleichung: x[g1, p, q] + x[g2, p, q] + ... <= capacities[p, q]
    for p in places:
        for q in places:
            model.addConstr(quicksum(x[g, p, q] for g in goods) <= capacities[p, q])

    # Vierte Nebenbedingung (falls noetig):
    # Bedeutung: Gesamtreichweite ist bschraenkt
    # Ungleichung: Summe((x[g1, p, q] + x[g2, p, q] + ...) * travel_distance[p, q]) <= max_travel
    model.addConstr(quicksum(quicksum(x[g, p, q] for g in goods) * travel_distance[p, q] for p in places for q in places) <= max_travel)

    # Fuenfte Nebenbedingung (falls noetig):
    # Bedeutung: ...
    # Ungleichung: ...

    # Nebenbedingungen hinzugefuegt? LP loesen lassen!
    model.optimize()

    # Transportmengen ausgeben.
    if model.status == GRB.OPTIMAL:
      print('\nOptimalloesung hat Kosten von %g.\n' % (model.ObjVal))
      for k in goods:
        for s1 in places:
          for s2 in places:
            if x[k, s1, s2].x > 0.0001:
              print('Von %s nach %s werden %g Chargen von %s transportiert.' % (s1, s2, x[k, s1, s2].x, k))
    else:
      print('Keine Optimalloesung gefunden. Status: %i' % (model.status))

    return model

