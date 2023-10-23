## Problemstellung: Bergwerk

Zitat aus dem Abgabesystem:

> Wir wollen lineare Programme benutzen, um Bergbau kostenminimal zu gestalten.
>
> Die Bergwerk AG betreibt mehrere Minen. Diese sind in der Liste `mines` gespeichert. In jeder Mine können verschiedene Erze abgebaut werden, welche in der Liste `ores` hinterlegt sind. Allerdings sind diese Ressourcen in jeder Mine begrenzt. Der Betrag der Einheiten, die für ein Erz $o \in$ `ores` in der Mine $m \in$ `mines` vorhanden sind bzw. abgebaut werden können, wird in einem Dictionary `available[m, o]` angegeben. Die Bergwerk AG kann nun in jeder Mine die vorhandenen Erze abbauen. Dabei entstehen allerdings Kosten, welche in `unit_costs[m, o]` in Euro pro Einheit des Erzes $o \in$ `ores` für jede Mine $m \in$ `mines` gespeichert ist. Die Bergwerk AG wird von der Regierung unterstützt, da Sie in ihren Minen bestimmte subventionierte Erze abbaut, welche in der Liste `subsidised_ores` ($\subseteq$ `ores`) angegeben sind. Teil des Vertrags ist allerdings auch die Regelung, dass in jeder Mine nur maximal $\frac{2}{3}$ der monatlichen Arbeitszeit mit Erzgewinnung verbracht werden darf, um anliegende Dörfer nicht mit dem Lärm der Sprengungen zu stören. Den Rest der Zeit soll jede Mine mit Verwaltungsaufgaben füllen. Die wichtigen Daten hierfür sind wie folgt angegeben: Die von Mine zu Mine unterschiedlichen monatlichen Arbeitsstunden sind im Dictionary `work_hours[m]` in Stunden für jede Mine $m \in$ `mines` erfasst, während die Stunden, die in Mine $m \in$ `mines` benötigt werden, um eine Einheit des Erzes $o \in$ `ores` zu gewinnen in `unit_time_needed[m,o]` angegeben sind. Für den nächsten Monat verbucht die Bergwerk AG Aufträge über eine gewisse Menge an Erzen. Diese Daten sind im Dictionary `demand[o]` in Einheiten eines Erzes $o \in$ `ores` erfasst.
>
> Der AG möchte nun für jede Mine die Menge an Einheiten bestimmen, die für jedes Erz im nächsten Monat abgebaut werden sollen, sodass die Kunden zufrieden sind und unter dem Aspekt, dass die Gesamtkosten minimal sind. Folgende Ziele sind ebenso zu beachten:
>
> - Für jedes Erz $o$ soll die gesamt abgebaute Menge der AG mindestens `demand[o]` decken
> - Pro Mine $m$ und pro Erz $o$ können nicht mehr Einheiten als `available[m,o]` Einheiten von $o$ in $m$ abgebaut werden
> - Für jede Mine $m$ darf die Zeit, die zum Abbau von Erzen verwendet wird, nicht höher als $\frac{2}{3}$ `work_hours[m]` Stunden sein
> - Ebenso soll für jede Mine $m$ mindestens ein Viertel der Einheiten abgebauter Erze zu subventionierten Erzen gehören, damit weitere Subventionierung gesichert ist
>
> Sie haben nun die Dateien `bergwerk.py`, `bergwerk-data1.py` und `bergwerk-data2.py` gegeben. Ergänzen Sie die Datei `bergwerk.py` so, dass das *Bergwerk*-Problem mit den gegebenen Bedingungen gelöst wird.
>
> Modellieren Sie das Problem als lineares Programm (LP) und ergänzen Sie die Datei `bergwerk.py` um die fehlenden Nebenbedingungen, sodass das *Bergwerk*-Problem gelöst wird. Ergänzen Sie dafür im gegebenen Modell gegebenenfalls Attribute für die vorgegebenen Entscheidungsvariablen (z. B. `lb`, `ub`, `obj`). Die Entscheidungsvariable `x_m_o` mit $m \in$ `mines` und $o \in$ `ores` entspricht dann dem Wert, wie viel Einheiten an Erz $o$ in Mine $m$ abgebaut werden soll. Wichtig: Es können auch nicht-ganzzahlige Mengen von Erz abgebaut werden. Sie können Ihr Modell (teilweise) testen, indem Sie den Code in `bergwerk-data1.py` oder `bergwerk-data2.py` ausführen. Dort wird die von Ihnen geschriebene `solve()`-Funktion aus `bergwerk.py` aufgerufen.
>
> Fügen Sie an den Stellen, an denen Sie `bergwerk.py` ergänzen, Kommentare hinzu, die die Bedeutung der entsprechenden Zeilen angeben. Das erhöht im Fall von falschen Bewertungen das Verständnis Ihres Modells und erleichtert Ihnen bei komplizierteren Modellen, den Überblick zu behalten.

## Optimale Zielfunktionswerte

| Datei               | ObjVal                        |
|---------------------|-------------------------------|
| `bergwerk-data1.py` | $2.081715686e+04$ ($20817.2$) |
| `bergwerk-data2.py` | $5.571891034e+04$ ($55718.9$) |