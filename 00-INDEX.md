# Смета-А — Живой индекс

> Проект для создания строительных смет и BIM-моделей

## Последние обновления

```dataview
TABLE date, status
FROM "01-ARCHITECTURE"
SORT date DESC
LIMIT 5
```

## Активные функции в разработке

```dataview
TABLE status, owner
FROM "02-FEATURES"
WHERE status = "in-progress"
```

## Структура проекта

- [[01-ARCHITECTURE/INDEX|Архитектурные решения (ADR)]]
- [[02-FEATURES/INDEX|Функции проекта]]
- [[03-UI-UX/INDEX|Описание экранов и flow]]
- [[04-LEGAL/INDEX|Юридические документы]]
- [[05-MEETINGS/INDEX|Логи обсуждений]]

## Быстрые ссылки

- Репозиторий: TODO
- CI/CD: TODO
- Актуальная версия: 0.1.0-alpha