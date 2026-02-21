import time
import random
from rich.live import Live
from rich.table import Table
from rich.console import Console

console = Console()

def generate_table() -> Table:
    # Subtitle removed to fix TypeError; moved to caption
    table = Table(
        title="🏛️  MAGADH NEXUS: RWA LOGISTICS ORACLE",
        caption="[bold gold1][SHARK PROTOCOL ACTIVE][/bold gold1]",
        border_style="yellow" # Using standard yellow for maximum compatibility
    )

    table.add_column("Truck ID", style="cyan", no_wrap=True)
    table.add_column("Material", style="magenta")
    table.add_column("TX Hash", style="green")
    table.add_column("Status", style="bold green")

    # Simulating the elite flow
    for _ in range(5):
        table.add_row(
            f"BR-01-{random.randint(1000, 9999)}",
            random.choice(["Bijari", "Kankar"]),
            f"0x{random.getrandbits(64):x}"[:14] + "...",
            "VERIFIED"
        )
    return table

with Live(generate_table(), refresh_per_second=1) as live:
    while True:
        time.sleep(1)
        live.update(generate_table())
