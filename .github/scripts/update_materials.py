"""Обновляет материалы курса, сохраняя существующие решения студента.

Запуск: python update_materials.py <папка шаблона> <папка копии студента>
Пути с символическими ссылками пропускаются. Файлы никогда не удаляются.
"""
import os
from pathlib import Path
import shutil
import sys


TEACHER_DIRS = {"lectures", "materials", "docs"}
TEACHER_FILES = {".gitignore", ".gitattributes", "rust-toolchain.toml"}
WORK_DIRS = {"practice", "homework", "exams"}
SKIP_NAMES = {".git", "target", "__pycache__", ".venv"}


def is_teacher(relative):
    parts = Path(relative).parts
    if parts[0] in TEACHER_DIRS or relative in TEACHER_FILES:
        return True
    if len(parts) >= 3 and parts[:2] == (".github", "scripts"):
        return True
    if parts[0] in WORK_DIRS:
        if len(parts) == 2 and parts[-1] == "README.md":
            return True
        if len(parts) == 3 and parts[-1] in {"README.md", "tasks.md"}:
            return True
    return False


def has_symlink(root, relative):
    current = root
    for part in Path(relative).parts:
        current = current / part
        if current.is_symlink():
            return True
    return False


def template_files(root):
    for current, dirs, files in os.walk(root, followlinks=False):
        here = Path(current)
        dirs[:] = sorted(
            name for name in dirs
            if name not in SKIP_NAMES
            and not (here / name).is_symlink()
            and (here / name).relative_to(root).as_posix() != ".github/workflows"
        )
        for name in sorted(files):
            path = here / name
            if not path.is_symlink():
                yield path.relative_to(root).as_posix()


def update(template, student):
    template, student = Path(template).resolve(), Path(student).resolve()
    if not template.is_dir() or not student.is_dir() or template == student:
        raise ValueError("Нужны две разные существующие папки: шаблон и копия студента")
    result = {"added": [], "updated": [], "skipped": []}
    for relative in template_files(template):
        source, destination = template / relative, student / relative
        if has_symlink(student, relative):
            result["skipped"].append(relative + " (символическая ссылка)")
            continue
        if destination.exists() and not destination.is_file():
            result["skipped"].append(relative + " (занято папкой)")
            continue
        if not destination.exists():
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
            result["added"].append(relative)
        elif is_teacher(relative) and source.read_bytes() != destination.read_bytes():
            shutil.copy2(source, destination)
            result["updated"].append(relative)
    return result


def main():
    if len(sys.argv) != 3:
        sys.exit("Запуск: python update_materials.py <шаблон> <копия студента>")
    result = update(sys.argv[1], sys.argv[2])
    lines = [f"Добавлено: {len(result['added'])}, обновлено: {len(result['updated'])}."]
    for key, label in [("added", "добавлен"), ("updated", "обновлён"), ("skipped", "пропущен")]:
        lines.extend(f"- {label} `{path}`" for path in result[key])
    report = "\n".join(lines)
    print(report)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as stream:
            stream.write("## Обновление материалов курса\n\n" + report + "\n")


if __name__ == "__main__":
    main()
