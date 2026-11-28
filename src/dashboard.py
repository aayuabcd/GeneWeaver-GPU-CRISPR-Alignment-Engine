from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widgets import Header, Footer, Static, ProgressBar
from pathlib import Path

from numba import cuda


class GeneWeaverDashboard(App):
    """Interactive GeneWeaver terminal dashboard."""

    CSS = """
    Screen {
        background: #101820;
        color: white;
    }

    #title {
        color: cyan;
        text-align: center;
        text-style: bold;
        padding: 1;
    }

    .panel {
        border: round cyan;
        padding: 1;
        margin: 1;
        height: auto;
    }

    ProgressBar {
        margin: 1;
    }
    """

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("r", "refresh_status", "Refresh"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()

        with Vertical():
            yield Static(
                "GENEWEAVER - CRISPR ALIGNMENT ENGINE",
                id="title"
            )

            with Horizontal():
                yield Static(
                    "CPU ALIGNMENT\nStatus: Available\n"
                    "Algorithm: Mismatch Detection",
                    classes="panel"
                )

                yield Static(
                    "GPU ACCELERATION\nStatus: Checking...",
                    id="gpu_status",
                    classes="panel"
                )

            with Vertical(classes="panel"):
                yield Static("GENOME INFORMATION")
                yield Static(
                    "Sample: data/sample_genome.fasta"
                )
                yield Static(
                    "Processing: Ready",
                    id="processing_status"
                )

            with Vertical(classes="panel"):
                yield Static("PROJECT DEVELOPMENT")
                yield ProgressBar(total=20, progress=9)
                yield Static(
                    "Development milestone: Day 9 / 20"
                )

            yield Static(
                "Press R to refresh status | Q to exit"
            )

        yield Footer()

    def on_mount(self) -> None:
        self.refresh_status()

    def action_refresh_status(self) -> None:
        gpu = (
            "Available"
            if cuda.is_available()
            else "Unavailable - CPU mode"
        )

        self.query_one("#gpu_status", Static).update(
            f"GPU ACCELERATION\nStatus: {gpu}"
        )

        fasta_path = Path("data/sample_genome.fasta")

        status = (
            "Sample FASTA file found"
            if fasta_path.exists()
            else "Sample FASTA file not found"
        )

        self.query_one("#processing_status", Static).update(
            f"Processing: {status}"
        )


if __name__ == "__main__":
    GeneWeaverDashboard().run()
