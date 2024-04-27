import importlib
from typing import List
from pathlib import Path
from types import ModuleType

from pylint.lint import Run
from docstr_coverage import analyze
from docstr_coverage.cli import collect_filepaths
from docstr_coverage.printers import LegacyPrinter
from docstr_coverage.ignore_config import IgnoreConfig
from mypy.main import main as mypy_main

MODULES = [
    "qosst_core",
    "qosst_hal",
    "qosst_alice",
    "qosst_bob",
    "qosst_sim",
    "qosst_skr",
]

MODULES_LOADED = [importlib.import_module(mod) for mod in MODULES]


def check_pylint(modules):
    print("============")
    print("== pylint ==")
    print("============")
    for module in modules:
        print("------------")
        print(module.__name__)
        print("------------")
        Run([module.__name__], exit=False)


def check_mypy(modules):
    print("============")
    print("=== mypy ===")
    print("============")
    for module in modules:
        print("------------")
        print(module.__name__)
        print("------------")
        try:
            mypy_main(
                args=["--disable-error-code", "import", "--disable-error-code", "no-redef", "-p", module.__name__],
                clean_exit=True,
            )
        except SystemExit:
            pass


def check_docstring(modules: List[ModuleType]):
    print("============")
    print("== docstr ==")
    print("============")
    ignore_config = IgnoreConfig(
        skip_magic=True,
    )
    for module in modules:
        print("------------")
        print(module.__name__)
        print("------------")
        paths = collect_filepaths(str(Path(module.__file__).parent))
        results = analyze(paths, ignore_config=ignore_config, show_progress=False)
        LegacyPrinter(verbosity=3, ignore_config=ignore_config).print(results)


def main():
    check_pylint(MODULES_LOADED)
    check_mypy(MODULES_LOADED)
    check_docstring(MODULES_LOADED)


if __name__ == "__main__":
    main()
