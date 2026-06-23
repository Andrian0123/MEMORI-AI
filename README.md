# 🏗️ Смета-А — Нейронная база знаний

Date: 2026-06-23
Time: 20:40 UTC
@see Obsidian: https://obsidian.md
@see Engram: https://github.com/engram-memory/engram

Единый мозг проекта: Obsidian + Git + Engram ML-память.

## 🚀 Быстрый старт

```bash
# 1. Клонируйте репозиторий
git clone https://github.com/Andrian0123/MEMORI-AI.git
cd MEMORI-AI

# 2. Откройте папку как Vault в Obsidian

# 3. Установите плагины Obsidian:
#    - Dataview (живые таблицы)
#    - Templater (шаблоны)
#    - Git (синхронизация)
#    - Shell Commands (интеграция)

# 4. Запустите Engram сервер
docker-compose up -d

# 5. Настройте MCP для Claude Code
bash scripts/setup-mcp.sh
```

## 📁 Структура проекта

| Папка | Описание |
|-------|----------|
| `01-ARCHITECTURE/` | Архитектурные решения (ADR) |
| `02-FEATURES/` | Функциональные спецификации |
| `03-UI-UX/` | Экраны и пользовательские сценарии |
| `04-LEGAL/` | Юридические документы |
| `05-MEETINGS/` | Логи обсуждений |
| `templates/` | Шаблоны Templater |
| `scripts/` | Скрипты для интеграции |

## 🤖 Интеграция с AI

- Engram MCP сервер: автоматическая память
- Obsidian MCP сервер: доступ к заметкам
- CI/CD: синхронизация при коммите

## 📝 Команды

```bash
# Ручная синхронизация памяти
bash scripts/sync-engram.sh

# Поиск по памяти
engram search --query "архитектура"

# Тестовый прогон извлечения знаний
python scripts/extract-knowledge.py --dry-run
```

---
*Последнее обновление: 2026-06-23*