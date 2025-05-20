# bootstrap.py
import pathlib, textwrap

BASE = pathlib.Path(".")

dirs = [
    "src",
    "src/utils",
    "assets",
    "outputs/frames",
    "outputs/viewport",
    "tests",
]

files = [
    "src/__init__.py",
    "src/main.py",
    "src/frame_processor.py",
    "src/motion_detector.py",
    "src/viewport_tracker.py",
    "src/visualizer.py",
    "src/utils/__init__.py",
    "src/utils/io.py",
    "tests/__init__.py",
    "tests/test_motion.py",
    "requirements.txt",
    "README.md",
    ".gitignore",
    "pyproject.toml",
]

# create directories
for d in dirs:
    (BASE / d).mkdir(parents=True, exist_ok=True)

# touch files (with a friendly header for empty .py files)
header = textwrap.dedent("""\
    \"\"\"Placeholder created by bootstrap.py.
    Replace with implementation.
    \"\"\"
    """)
for f in files:
    path = BASE / f
    if not path.exists():
        path.write_text(header if path.suffix == ".py" else "")

print(f"✅  Scaffolding created under {BASE.resolve()}")
