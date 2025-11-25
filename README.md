# Холодный запуск
1. `pip install uv`
2. `uv sync`
3. `alembic upgrade head`
4. `python src/main.py`


# Модели
- Appeal - обращения/заявки
- Lead - лиды
- Operator - операторы
- Source - источники
- OperatorsToSources - ассоциативная таблица

![img.png](diagram.png)