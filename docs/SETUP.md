# Установка Rust и редактора

## Windows 10/11

1. Установите [Visual Studio Code](https://code.visualstudio.com/) и [Git for Windows](https://git-scm.com/downloads/win).
2. Откройте [официальную установку Rust](https://rust-lang.org/install/), скачайте и запустите `rustup-init.exe` для вашей системы.
3. Для сборки Rust с MSVC требуются инструменты C++ и Windows SDK. Если установщик предлагает установить их,
   выполните этот шаг. В Visual Studio Installer выберите рабочую нагрузку **Desktop development with C++**
   («Разработка классических приложений на C++»). Подойдёт [Build Tools for Visual Studio](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio).
4. Завершите стандартную установку stable через rustup. Закройте и снова откройте VS Code.
5. В расширениях VS Code установите **rust-analyzer**, издатель **rust-lang**.

Терминал VS Code открывается через меню **Terminal → New Terminal**. Выполните:

```powershell
rustup --version
rustc --version
cargo --version
git --version
```

Команды должны вывести версии установленных инструментов. Проекты курса используют edition 2024,
для которой требуется Rust 1.85 или новее. `stable` устанавливает актуальный стабильный выпуск.

## macOS и Linux

Следуйте [официальной инструкции Rust](https://rust-lang.org/install/) для вашей системы.
Нужен системный компоновщик: на macOS инструменты Xcode Command Line Tools, на Linux пакет
с инструментами C/C++ для вашего дистрибутива. Затем установите VS Code, Git и rust-analyzer.

## Первая проверка

Откройте корень своей копии репозитория:

```powershell
cargo check --manifest-path practice/01-variables/Cargo.toml
cargo run --manifest-path practice/01-variables/Cargo.toml
```

`cargo check` проверяет сборку; `cargo run` собирает и запускает программу.
Первый запуск может загрузить компоненты выбранного toolchain.
Выполните [ДЗ 0](../homework/00-first-project/README.md) и запишите результат в отчёт.

## Частые ситуации

| Сообщение или ситуация | Что сделать |
|---|---|
| `cargo` или `rustc` не распознаны | Перезапустить VS Code после установки, проверить завершение rustup; инструменты находятся в `%USERPROFILE%\.cargo\bin` |
| `link.exe not found` | Установить инструменты C++ и Windows SDK через Visual Studio Installer |
| `could not find Cargo.toml` | Перейти в папку работы либо указать `--manifest-path` |
| rust-analyzer не нашёл проект | Открыть отдельную папку работы, содержащую Cargo.toml |
| Изменения кода не появились в выводе | Сохранить файл и проверить, какой Cargo.toml используется |
| Ошибка типов или синтаксиса | Прочитать первую ошибку, номер строки и подсказку компилятора |

Источники: [Rust](https://rust-lang.org/install/), [Microsoft — Rust в Windows](https://learn.microsoft.com/en-us/windows/dev-environment/rust/setup),
[VS Code — Rust](https://code.visualstudio.com/docs/languages/rust), [Rust 2024](https://blog.rust-lang.org/releases/1.85.0/).
