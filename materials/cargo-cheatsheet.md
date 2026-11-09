# Памятка Cargo

| Команда из папки проекта | Результат |
|---|---|
| cargo check | Проверка сборки без создания итогового исполняемого файла |
| cargo run | Сборка и запуск программы |
| cargo test | Запуск тестовых функций |
| cargo test checks_parity | Запуск тестов, имя которых содержит checks_parity |
| cargo fmt | Форматирование кода; требуется компонент rustfmt |
| cargo clippy | Дополнительные подсказки по коду; требуется компонент clippy |

Из корня курса: `cargo test --manifest-path practice/03-loops-functions/Cargo.toml`.
У каждой работы отдельный Cargo.toml. Сохраняйте Cargo.lock приложений в Git.
target/ пересоздаётся при сборке. При изменении кода сначала сохраняйте src/main.rs.
