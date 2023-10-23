## Problemstellung: Tour

Zitat aus dem Abgabesystem:

> Wir möchten einem großen, mehrtägigen Radsport Event helfen, die Gesamtroute zu planen. Dabei müssen wir einiges Beachten, damit das Rennen ohne Probleme abgehalten werden kann und möchten die Gesamtanzahl der Zuschauerinnen und Zuschauer maximieren.
>
> Uns sind folgende Daten gegeben:
>
> - Ein (ganzzahliger) Zahlenwert `days`, welche die Anzahl der Tage angibt, die das Event andauern soll
> - Eine Liste `routes`, welche alle potenziellen Routen enthällt, die an maximal einem der Tage stattfinden können
> - Ein Dictionary `length`, welches für jede Route `route` $\in$ `routes` angibt, wie lange die Strecke in Kilometern ist
> - `visitors` ist ebenfalls ein Dictionary, welches die erwartete Anzahl an Zuschauern für jede Route `route` $\in$ `routes` enthält
> - Die natürliche Zahl `min_rest_days` gibt die minimale Anzahl an Ruhetagen an. Dies sind Tage innerhalb der Events, an denen keine Route befahren wird
> - `min_length` gibt die minimale Anzahl an Kilometern an, die während der `days` Tage zurückgelegt werden sollen
> - Und eine Liste `hard_routes` ($\subseteq$ `routes`), welche genau die Routen enthält, die von der Streckenplanung als schwierig erachtet werden
>
> Allerdings gibt es noch weitere Bedingungen: Es dürfen keine zwei schwere Routen an zwei aufeinander folgenden Tagen befahren werden (Ein Ruhetag oder eine nicht-schwere Route zwischen zwei schweren Routen ist erlaubt). Stellen Sie sicher, dass an einem Tag nur maximal eine Route gefahren werden kann und jeder Route nur maximal ein Tag zugeteilt werden kann. Ebenso ist es Tradition dieses ominösen Events, dass am letzten Tag die Route 'Les Champs' $\in$ `routes` gefahren wird. Modellieren Sie diese Notwendigkeit auch in Ihrem Modell. Allerdings soll am ersten Tag natürlich eine Route befahren werden (Stellen Sie sicher, dass Ihr Modell den ersten Tag nicht als Ruhetag einplant).
>
> Des weiteren haben wir Entscheidungsvariablen, welche uns beim Lösen dieses Problems unterstützen. Die Entscheidungsvariable `assignment[day, route]` $\in$ {$0, 1$} $\forall$ `day` $\in$ `range(days)` $\forall$ `route` $\in$ `routes` gibt an, ob das ob an einem Tag `day` die Route `route` gefahren werden soll (`assignment[day, route] = 1`) oder nicht. Falls eine Route `route` befahren wird, können Sie mit `visitors[route]` vielen Besuchern rechnen.
>
> Sie haben nun die Dateien `tour.py`, `tour-data1.py` und `tour-data2.py` gegeben. Ergänzen Sie die Datei `tour.py` so, dass das Tour-Problem mit den gegebenen Bedingungen gelöst wird.
>
> Modellieren Sie das Problem als ganzzahliges lineares Programm (LP) und ergänzen Sie die Datei `tour.py` um die fehlenden Nebenbedingungen, sodass das Tour-Problem gelöst wird und die Anzahl der Besucher maximiert wird. Ergänzen Sie dafür im gegebenen Modell gegebenenfalls Attribute für die vorgegebenen Entscheidungsvariablen (z. B. `vtype`, `lb`, `ub`, `obj`). Sie können Ihr Modell (teilweise) testen, indem Sie den Code in `tour-data1.py` oder `tour-data2.py` ausführen. Dort wird die von Ihnen geschriebene `solve()`-Funktion aus `tour.py` aufgerufen.
>
> Fügen Sie an den Stellen, an denen Sie `tour.py` ergänzen, Kommentare hinzu, die die Bedeutung der entsprechenden Zeilen angeben. Das erhöht im Fall von falschen Bewertungen das Verständnis Ihres Modells und erleichtert Ihnen bei komplizierteren Modellen, den Überblick zu behalten.
>
> **Tipp:** Mit dem Python-Code `for day in range(days)` erstellen Sie eine for-Schlefe, in der die Variable `day` die Werte `0` bis `days-1` annimmt. Mit `0` können Sie also den ersten Tag ansprechen und mit `days-1` den letzten Tag. Die Variable, welche angibt, ob die Route "Les Champs" am ersten Tag befahren werden soll, ist also: `assignment[0, 'Les Champs']`. Überlegen Sie sich genau, wie Sie in Python Paare von Tagen ansprechen können, um damit dann die Nebenbedingungen für zwei aufeinanderfolgende schwere Routen zu implementieren.

## Optimale Zielfunktionswerte

| Datei           | ObjVal   |
|-----------------|----------|
| `tour-data1.py` | $183000$ |
| `tour-data2.py` | $480345$ |