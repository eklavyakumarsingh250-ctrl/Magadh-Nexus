import time
import random
from rich.console import Console
from rich.progress import Progress

console = Console()

def run_simulation():
    console.print("[bold gold1]MAGADH NEXUS | BLOCKCHAIN SIMULATOR ACTIVE[/bold gold1]", style="on black")
    console.print(f"Network: [green]Magadh-Local-Node-v1[/green] | Port: 8545\n")

    with Progress() as progress:
        task1 = progress.add_task("[cyan]Processing Shipments...", total=100)

        while not progress.finished:
            time.sleep(random.uniform(0.5, 1.5))
            truck_id = f"BR-01-{random.randint(1000, 9999)}"
            material = random.choice(["Bijari", "Kankar"])

            console.log(f"TX-HASH: {random.getrandbits(128):x} | [green]VERIFIED[/green] | {truck_id} loaded with {material}")
            progress.update(task1, advance=random.randint(5, 15))

if __name__ == "__main__":
    run_simulation()
