import pandas as pd

def reduce_data_points(input_file, output_file, target_points=300):
    # Datei einlesen und sicherstellen, dass der Header übersprungen wird
    df = pd.read_csv(input_file, delimiter=';', decimal=',', encoding='latin1', header=None)

    # Entferne die erste Zeile mit Einheiten (die Zeile, die als Header zu betrachten ist)
    df = df.iloc[1:].reset_index(drop=True)

    # Entferne die erste Zeile mit Einheiten (die Zeile, die als Header zu betrachten ist)
    df = df.iloc[1:].reset_index(drop=True)

    # Entferne leere Spalten, falls vorhanden
    df = df.dropna(axis=1, how='all')

    # Berechnen des Schrittes zur Reduktion der Datenpunkte
    total_points = len(df)
    step = total_points // target_points if total_points > target_points else 1

    # Neue reduzierte Daten auswählen
    reduced_df = df.iloc[::step]

    # Lösche die 4. Spalte (Index 3)
    reduced_df = reduced_df.drop(reduced_df.columns[3], axis=1)

    # Tausche die 2. und 3. Spalte (Index 1 und 2)
    reduced_df = reduced_df[[reduced_df.columns[0], reduced_df.columns[2], reduced_df.columns[1]] + list(reduced_df.columns[3:])]

    # Ersetze alle Kommas mit Punkten und alle Semikolons mit Kommas
    reduced_df = reduced_df.applymap(lambda x: str(x).replace(',', '.'))

    # Datei speichern, Dezimalstellen mit Punkt und Komma als Delimiter
    reduced_df.to_csv(output_file, index=False, header=False, sep=',', decimal='.')

    print(f'Reduzierte Datei gespeichert als {output_file}')

# Beispielaufruf
def main():
    input_file = 'C:/Users/39334/CTM/ct7/SES/Bending Tests/3.Runde/27_03_2025_Versuche/Aramid_03_3.csv'
    output_file = 'C:/Users/39334/CTM/ct7/SES/Bending Tests/3.Runde/27_03_2025_Versuche/Aramid_03_3_resampled.csv'
    reduce_data_points(input_file, output_file)

if __name__ == "__main__":
    main()
