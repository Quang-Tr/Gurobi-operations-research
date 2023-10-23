## Problemstellung: Lummerland

Zitat aus dem Abgabesystem:

> Der kleine *Jim KnORpf* wohnt mit seinem Freund Lukas dem Lokomotivführer auf der kleinen Insel Lummerland. Über Lummerland erzählt man sich vieles:
>
> Eine Insel mit zwei Bergen und dem tiefen weiten Meer
Mit viel Tunnels und Geleisen und dem Eisenbahnverkehr
Nun, wie mag die Insel heißen, ringsherum ist schöner Strand
Jeder sollte einmal reisen in das schöne Lummerland.
>
> Einer ihrer Aufgaben ist es, Güter und andere Gegenstände zwischen den verschiedenen Bewohnern und den Geschäften auf der Insel zu transportieren. Diese Güter und andere Gegenstände sind als Menge $goods$ gegeben. Beim Transport einer Charge von Gut $g$ fallen `costs[g]` Euro pro Kilometer Wegstecke an. Da die Lok sehr klein ist, kann sie immer nur eine Charge gleichzeitig transportieren.
>
> Es gibt zudem eine Menge an $places$, an der die Lok halten kann. Dies können entweder die Bewohner sein, aber auch die Geschäfte auf der Insel. Jeder Ort $p$ hat `availabilities[p, g]` Chargen des Gutes $g$ vorrätig, welche transportiert werden können und zudem einen Bedarf von `demands[p, g]` Chargen des Gutes $g$. Jeder Ort kann jedoch ein Gut nur vorrätig haben oder nur benötigen (oder nichts von beidem), aber nicht ein gut benötigen und gleichzeitig vorrätig haben.
>
> Die Kilometeranzahl zwischen Ort $p$ und Ort $q$ beträgt `travel_distance[p,q]` Kilometer. Außerdem können insgesamt höchstens `capacities[p,q]` Chargen von Ort $p$ zu Ort $q$ transportiert werden.
>
> Zudem hat die Lokomotive Emma nicht eine unendliche Reichweite und kann deshalb nicht beliebig viele Kilometer zurücklegen. Aus diesem Grund darf die maximal zurückgelegte Strecke nicht `max_travel` überschreiten.
>
> Es ist nun zu entscheiden, wie viele Chargen von Gut $g$ jeweils von Ort $p$ zu Ort $q$ transportiert werden sollen. Gehen Sie davon aus, dass die Güter nur direkt von einem Ort zum anderen Ort (d.h. ohne Umwege über andere Städte) transportiert werden. Dabei sollen die insgesamt anfallenden Transportkosten minimiert, aber alle Bedarfe gedeckt und die vorhandenen Kapazitäten nicht überschritten werden. Zur Einfachheit sind auch nicht ganzzahlige Chargen erlaubt.
>
> Sie haben nun die Dateien `lummerland.py`, `lummerland-data1.py` und `lummerland-data2.py` gegeben. Ergänzen Sie die Datei `lummerland.py` so, dass das *lummerland*-Problem mit den gegebenen Bedingungen gelöst wird.
>
> Modellieren Sie Problem als lineares Programm (LP) und ergänzen Sie die Datei `lummerland.py` um die fehlende Nebenbedingung, sodass das *lummerland*-Problem gelöst wird. Ergänzen Sie dafür im gegebenen Modell gegebenenfalls Attribute für die vorgegebenen Entscheidungsvariablen (z.B. `lb`, `ub`, `obj`). Die Entscheidungsvariable `x_g_p_q` soll als Wert die Anzahl an Chargen von Gut $g \in goods$ erhalten, die von Ort $p \in places$ zu Ort $q \in places$ transportiert werden. Sie können Ihr Modell (teilweise) testen, indem Sie den Code in `lummerland-data1.py` oder `lummerland-data2.py` ausführen. Dort wird die von Ihnen ergänzte `solve()`-Funktion aus `lummerland.py` aufgerufen.
>
> Fügen Sie an den Stellen, an denen Sie `lummerland.py` ergänzen, Kommentare hinzu, was die entsprechenden Zeilen bedeuten. Das erhöht im Fall von falschen Bewertungen das Verständnis Ihres Modells und erleichtert Ihnen bei komplizierteren Modellen, den Überblick zu behalten.

## Optimale Zielfunktionswerte

| Datei                 | ObjVal   |
|-----------------------|----------|
| `lummerland-data1.py` | $3514$   |
| `lummerland-data2.py` | $3041.5$ |