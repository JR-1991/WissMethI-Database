# R Tutorial für Datenbankabfragen und Visualisierung

## Installation von R und RStudio

Bevor Sie mit diesem Tutorial beginnen können, müssen Sie R und RStudio auf Ihrem Computer installieren.

### Installation für Windows

1. Laden Sie R von der offiziellen Website herunter: [R für Windows](https://cran.r-project.org/bin/windows/base/)
2. Führen Sie die heruntergeladene .exe Datei aus und folgen Sie den Installationsanweisungen
3. Laden Sie anschließend RStudio Desktop von [rstudio.com](https://www.rstudio.com/products/rstudio/download/) herunter
4. Installieren Sie RStudio durch Ausführen der heruntergeladenen .exe Datei

### Installation für macOS

1. Laden Sie R von der offiziellen Website herunter: [R für macOS](https://cran.r-project.org/bin/macosx/)
2. Öffnen Sie die heruntergeladene .pkg Datei und folgen Sie den Installationsanweisungen
3. Laden Sie RStudio Desktop von [rstudio.com](https://www.rstudio.com/products/rstudio/download/) herunter
4. Ziehen Sie die heruntergeladene RStudio-App in Ihren Applications-Ordner

## Installation der benötigten Pakete

Für dieses Tutorial benötigen Sie einige R-Pakete. Diese können Sie mit den folgenden Befehlen in RStudio installieren:

```r
install.packages("DBI")
install.packages("RMySQL")
install.packages("ggplot2")
```

> Für die Installation des Pakets `RMySQL` auf MacOS benötigen sie [xcode](https://developer.apple.com/xcode/). Dieses können Sie über den App Store installieren.

---

## Ausführung der Übungen

Folgende Schritte werden in diesem Tutorial durchgeführt:

- **Datenbankverbindung:** Verwendet `DBI` und `RMySQL` zur Verbindung mit einer MySQL-Datenbank. Ersetzen Sie die Verbindungsparameter durch Ihre eigenen.
- **Datenabruf:** Führt eine SQL-Abfrage mit `dbGetQuery` aus und speichert das Ergebnis in einem Dataframe.
- **Visualisierung:** Nutzt `ggplot2` zur Erstellung eines Streudiagramms der Daten, mit `temperature` auf der x-Achse und `density` auf der y-Achse.

### Datenbankverbindung

In diesem Abschnitt stellen Sie eine Verbindung zu einer MySQL-Datenbank mit R her. Bearbeiten Sie die Argumente innerhalb der `dbConnect`-Funktion mit Ihren Datenbankzugangsdaten und führen Sie die Zelle aus.

> **WICHTIG:** Die Verbindungsdaten für die Datenbankverbindung (host, user, port, password) finden Sie im ILIAS-Kurs. Die folgenden Werte sind nur *Platzhalter*.

```r
# Laden der benötigten Pakete
library(DBI)
library(RMySQL)

# Verbindung zur MySQL-Datenbank herstellen
db_connection <- dbConnect(
  MySQL(),
  host = "127.0.0.1",
  user = "user",
  port = 3307,
  password = "supersecurepassword",
  dbname = "mixtures"
)
```

### Ausführen einer Abfrage

Geben Sie Ihren SQL-Befehl in die folgende Zelle ein und führen Sie diese aus. Das Ergebnis Ihrer Abfrage wird angezeigt und in der Variable `data` gespeichert.

Sie können die Abfrage beliebig anpassen, um verschiedene Daten aus der Datenbank zu extrahieren. Hier sind einige Beispiele:

- Alle Spalten anzeigen: `SELECT * FROM density LIMIT 10`
- Nach Temperatur filtern: `SELECT * FROM density WHERE temperature > 20`
- Join mit anderer Tabelle `SELECT * FROM density JOIN mixtures ON density.mixture_id = mixtures.id`

Experimentieren Sie mit verschiedenen SQL-Befehlen, um sich mit den Daten vertraut zu machen.

```r
# Ausführen einer Abfrage
query <- "
SELECT temperature, density FROM density LIMIT 10
"

data <- dbGetQuery(db_connection, query)
print(data)
```

### Visualisierung

In diesem Abschnitt können Sie die abgerufenen Daten visualisieren. Passen Sie die Argumente der Plotting-Funktion entsprechend an.

Die nachfolgende Visualisierung erstellt ein Streudiagramm (Scatter Plot) der Dichte in Abhängigkeit von der Temperatur. Dabei wird die Temperatur auf der x-Achse und die Dichte auf der y-Achse aufgetragen. Das Diagramm wird mit ggplot2 erstellt, einer leistungsstarken Visualisierungsbibliothek in R.

Sie können die Darstellung nach Ihren Wünschen anpassen, zum Beispiel durch:

- Änderung der Farben und Formen der Datenpunkte
- Hinzufügen einer Trendlinie
- Anpassung der Achsenbeschriftungen
- Modifikation des Themes

```r
# Laden von ggplot2 für die Visualisierung
library(ggplot2)

# Erstellen eines Streudiagramms
p <- ggplot(data, aes(x = temperature, y = density)) +
  geom_point() +
  labs(title = "density vs. temperature",
       x = "temperature",
       y = "density") +
  theme_minimal()

# Anzeigen des Plots
print(p)
```
