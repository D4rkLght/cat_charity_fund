# QRKot

## Оглавление

* [Стек технологий](#stack)
* [Описание проекта](#description)
* [Запуск проекта](#start_project)
* [Документация](#dock)
* [Автор проекта](#author)


## Стек технологий <a name="stack"></a>

[![Python](https://img.shields.io/badge/-Python-464641?style=flat-square&logo=Python)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-464646?style=flat-square&logo=pytest)](https://docs.pytest.org/en/6.2.x/)
[![FastAPI](https://img.shields.io/badge/-FastAPI-464641?style=flat-square&logo=FastAPI)](https://fastapi.tiangolo.com/)
[![SQLite](https://img.shields.io/badge/-SQLite-464641?style=flat-square&logo=SQLite)](https://www.sqlite.org/index.html)


## Описание проекта <a name="description"></a>

Проект предоставлет сервис для пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.

Каждый пользователь может сделать пожертвование и сопроводить его комментарием. Пожертвования не целевые: они вносятся в фонд, а не в конкретный проект. Каждое полученное пожертвование автоматически добавляется в первый открытый проект, который ещё не набрал нужную сумму. Если пожертвование больше нужной суммы или же в Фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта. При создании нового проекта все неинвестированные пожертвования автоматически вкладываются в новый проект.


## Запуск проекта <a name="start_project"></a>

```
git clone git@github.com:D4rkLght/cat_charity_fund.git
```

```
cd cat_charity_fund
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Миграции

```
alembic upgrade head
```

Запустить проект:

```
uvicorn app.main:app
```


## Документация <a name="dock"></a>


* http://127.0.0.1:8000/docs/


## Над проектом работал: <a name="author"></a>

Разработчик [Ярослав Андреев](https://github.com/D4rkLght).