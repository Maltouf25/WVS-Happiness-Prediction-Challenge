import zipfile
from pathlib import Path
import shutil

ROOT_DIR = Path(__file__).parent.parent

PAGES_DIR = ROOT_DIR / "pages"
INGESTION_DIR = ROOT_DIR / "ingestion_program"
SCORING_DIR = ROOT_DIR / "scoring_program"
PHASE_DATA = ROOT_DIR / "dev_phase"
SOLUTION_DIR = ROOT_DIR / "solution"

BUILD_DIR = ROOT_DIR / "build"


def zip_directory(source_dir: Path, zip_path: Path):
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for file in source_dir.rglob("*"):
            if file.is_file() and not file.name.startswith(".") and not file.name.endswith(".pyc"):
                z.write(file, file.relative_to(source_dir))


if __name__ == "__main__":

    # Clean build directory
    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)
    BUILD_DIR.mkdir()

    print("Creating component ZIP files...")

    # 1️⃣ Ingestion
    zip_directory(INGESTION_DIR, BUILD_DIR / "ingestion_program.zip")

    # 2️⃣ Scoring
    zip_directory(SCORING_DIR, BUILD_DIR / "scoring_program.zip")

    # 3️⃣ Input Data
    zip_directory(PHASE_DATA / "input_data", BUILD_DIR / "input_data.zip")

    # 4️⃣ Reference Data
    zip_directory(PHASE_DATA / "reference_data", BUILD_DIR / "reference_data.zip")

    # 5️⃣ Solution (starting kit)
    zip_directory(SOLUTION_DIR, BUILD_DIR / "solution.zip")

    print("Creating final competition bundle...")

    # 6️⃣ Final bundle
    with zipfile.ZipFile("competition_bundle.zip", "w", zipfile.ZIP_DEFLATED) as bundle:

        # Root files
        bundle.write(ROOT_DIR / "competition.yaml", "competition.yaml")
        bundle.write(ROOT_DIR / "logo.png", "logo.png")

        # Pages
        for file in PAGES_DIR.rglob("*"):
            if file.is_file():
                bundle.write(file, file.relative_to(ROOT_DIR))

        # Add component zips
        for zip_file in BUILD_DIR.glob("*.zip"):
            bundle.write(zip_file, zip_file.name)

    print("✅ competition_bundle.zip created successfully.")