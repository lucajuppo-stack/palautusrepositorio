from rich.console import Console
from rich.table import Table

from player_reader import PlayerReader
from player_stats import PlayerStats


def fetch_top_scorers(season, nationality):
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    stats = PlayerStats(PlayerReader(url))
    return stats.top_scorers_by_nationality(nationality)


def build_table(season, nationality, players):
    table = Table(title=f"{nationality} {season}")
    table.add_column("Nimi")
    table.add_column("Joukkue")
    table.add_column("Maalit", justify="right")
    table.add_column("Syötöt", justify="right")
    table.add_column("Pisteet", justify="right")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.points),
        )

    return table


def main():
    console = Console()

    season = input("Kausi (esim. 2024-25): ")
    nationality = input("Maan koodi (esim. FIN): ").upper()

    try:
        players = fetch_top_scorers(season, nationality)
    except ValueError as error:
        console.print(f"[bold red]Virhe:[/bold red] {error}")
        return

    console.print(build_table(season, nationality, players))


if __name__ == "__main__":
    main()
