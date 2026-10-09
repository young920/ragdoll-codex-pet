"""Extract preview frames from the exact final atlas and render review loops."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parent
ATLAS = ROOT / "final" / "spritesheet-clean.png"
FRAMES = ROOT / "qa" / "encoded_frames"
PREVIEWS = ROOT / "qa" / "previews"
STATES = [
    ("idle", 6),
    ("running-right", 8),
    ("running-left", 8),
    ("waving", 4),
    ("jumping", 5),
    ("failed", 8),
    ("waiting", 6),
    ("running", 6),
    ("review", 6),
]


def main() -> None:
    sheet = Image.open(ATLAS).convert("RGBA")
    PREVIEWS.mkdir(parents=True, exist_ok=True)
    all_frames = []
    for row, (state, count) in enumerate(STATES):
        directory = FRAMES / state
        directory.mkdir(parents=True, exist_ok=True)
        for column in range(count):
            frame = sheet.crop((column * 192, row * 208, (column + 1) * 192, (row + 1) * 208))
            frame.save(directory / f"{column:02d}.png")
            all_frames.append(frame)

    def save_gif(name: str, frames: list[Image.Image], duration: int) -> None:
        frames[0].save(PREVIEWS / name, save_all=True, append_images=frames[1:], duration=duration, loop=0, disposal=2)

    save_gif("all-states.gif", all_frames, 150)
    jump = [sheet.crop((c * 192, 4 * 208, (c + 1) * 192, 5 * 208)) for c in range(5)]
    idle = sheet.crop((0, 0, 192, 208))
    save_gif("idle-jump-idle.gif", [idle, idle, *jump, idle, idle], 160)
    looks = [sheet.crop((c * 192, r * 208, (c + 1) * 192, (r + 1) * 208)) for r in (9, 10) for c in range(8)]
    save_gif("look-directions.gif", looks, 180)
    print(FRAMES)


if __name__ == "__main__":
    main()
