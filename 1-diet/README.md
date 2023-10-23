## Problemstellung: Diät Problem

Zitat aus dem Abgabesystem:

> Betrachten Sie erneut das Diät-Problem aus der Vorlesung: Sie haben eine Liste mit Lebensmitteln $s \in S$ und deren Werte für Kalorien $k_s$, Fett $f_s$ und Kosten $c_s$ gegeben. Weiterhin sind einige Speisen $S_0 \subseteq S$ als Obst deklariert. Es soll nun festgelegt werden, welche Speisen in welcher Menge gekauft werden sollen. Dabei sollen Speisen für mindestens $K$ Kalorien, aber nur maximal $F$ Mengeneinheiten Fett gekauft werden. Zudem dürfen von jeder Speise nur höchstens 8 Einheiten gekauft werden und mindestens ein Drittel der Menge soll Obst sein.
>
> Ziel ist die Kostenminimierung unter Einhaltung aller Nebenbedingungen.
>
> Im Lernraum finden Sie die Dateien `diet-data1.py`, `diet-data2.py` und `diet.py`. Ergänzen Sie die Datei `diet.py` um die fehlende Nebenbedingung zum Fett und beschränken Sie die maximale Menge von jeder Speise durch 8, sodass das Diät-Problem gelöst wird. Ergänzen Sie dafür im gegebenen Modell gebenenfalls Attribute für die vorgegebenen Entscheidungsvariablen (z.B. `lb`, `ub`, `obj`). Die Variable $x_s$ soll in Ihrem Modell angeben, wie viele Mengeneinheiten von Speise $s \in S$ gekauft werden sollen. Sie können Ihr Modell (teilweise) testen, indem Sie den Code in `diet-data1.py` oder `diet-data2.py` ausführen. Dort wird die von Ihnen ergänzte `solve()`-Funktion aus `diet.py` aufgerufen.

## Optimale Zielfunktionswerte

| Datei           | ObjVal    |
|-----------------|-----------|
| `diet-data1.py` | $4.3341$  |
| `diet-data2.py` | $5.39688$ |