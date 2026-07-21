# # | Метод         | Что делает                |
# # | ------------- | ------------------------- |
# # | `__init__`    | конструктор               |
# # | `__str__`     | вывод через `print()`     |
# # | `__repr__`    | отображение объекта       |
# # | `__len__`     | `len(obj)`                |
# # | `__getitem__` | `obj[key]`                |
# # | `__call__`    | вызов объекта как функции |
# # | `__eq__`      | `==`                      |
# # | `__lt__`      | `<`                       |
# # | `__gt__`      | `>`                       |
# from lessons.lesson3 import ardager
#
#
# # | Оператор | Магический метод | Пример   |
# # | -------- | ---------------- | -------- |
# # | `+`      | `__add__`        | `a + b`  |
# # | `-`      | `__sub__`        | `a - b`  |
# # | `*`      | `__mul__`        | `a * b`  |
# # | `/`      | `__truediv__`    | `a / b`  |
# # | `//`     | `__floordiv__`   | `a // b` |
# # | `%`      | `__mod__`        | `a % b`  |
#
# class Test:
#
#     def __init__(self, value):
#         self.value = value
#         self.view_count = 0
#
#     def __str__(self):
#         return str(self.value)
#
#     def __add__(self, other):
#
#         # if type(self) == type(other)
#        return self.value + other.value
#
#     def __lt__(self, other):
#         return self.value < other.value
#
#     def __call__(self):
#         self.view_count +=1
#         print('Меня вызвали')
#
# test_obj = Test(123)
# test_obj_2 = Test(12432)
# py_int = 123
# py_int_2 = 123
#
# # print(test_obj_2.view_count)
# # test_obj_2()
# # test_obj_2()
# # test_obj_2()
# # print(test_obj_2.view_count)
# # sum_int = test_obj == test_obj_2
# # print(sum_int)
#
#
# class Money:
#     def __init__(self, currency, sum):
#         self.currency = currency
#         self.sum = sum
#
#     def __convert_to_sum(self, money):
#         pass
#
#     # def __add__(self, other):
#     #     if self.currency != other.currency:
#     #
#
#
# som = Money('SOM', 100)
# usd = Money('USD', 100)
# # total_balance = som + usd
#
#
#
# class Add:
#
#     def __init__(self, value):
#         self.value = value
#
#
#     def get_value(self):
#         return self.value
#
#     @staticmethod
#     def add_int( a, b):
#         return a + b
#
#
# # test_1 = Add(123)
# # print(Add.add_int(123, 123))
#
# class BankAccount:
#     # Артибута класса
#     bank_name = "Kompanion"
#
#     def __init__(self, name, balance, bonus, total_balance):
#         # Артибуты экземпляра класса
#         self.name = name
#         self.first_name = name
#         self.last_name = name
#         self._balance = balance
#         self.__bonus = bonus
#     def get_name(self):
#         return self.name.
#
#     @classmethod
#     def get_bank_name(cls):
#         return cls.bank_name
#
#     @property
#     def balance(self):
#         return self._balance
#
#     @property
#     def total_balance(self):
#         return self._balance + self.__bonus
#
#     @property
#     def full_name(self):
#         return self.first_name + " " + self.last_name
#
#     @balance.setter
#     def balance(self, value):
#         self._balance = value
#
#
#
# ardager_1 = BankAccount('Name', 100, 50)
# ardager_2 = BankAccount(ardager_1, 100, 50)
# print(ardager_1.name)
# ardager_1.name = "Ардагер"
# print(ardager_1.name)
# print(ardager_1._balance)
# ardager_1.balance = 9999
# print(ardager_1._balance)
#
# column = (
#     'full_name' , '_balance', 'bonus', 'total_balance'
# )
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#


import asyncio
import sqlite3
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

# ─── CONFIG ───────────────────────────────────────
BOT_TOKEN = "8950234455:AAELXMOZv0bj-6eWf7wTwXolAjc06ZcrmJY"
DATABASE  = "tasks.db"

# ─── DB ───────────────────────────────────────────
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER NOT NULL UNIQUE,
            username    TEXT
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title   TEXT NOT NULL,
            is_done BOOLEAN NOT NULL DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
    ''')
    conn.commit()
    conn.close()

# ─── USER FUNCTIONS ───────────────────────────────
def get_user(telegram_id):
    conn = get_db()
    user = conn.execute(
        'SELECT * FROM users WHERE telegram_id = ?', (telegram_id,)
    ).fetchone()
    conn.close()
    return dict(user) if user else None

def create_user(telegram_id, username):
    conn = get_db()
    conn.execute(
        'INSERT OR IGNORE INTO users (telegram_id, username) VALUES (?, ?)',
        (telegram_id, username)
    )
    conn.commit()
    conn.close()
    return get_user(telegram_id)

# ─── TASK FUNCTIONS ───────────────────────────────
def get_tasks(user_id):
    conn = get_db()
    rows = conn.execute(
        'SELECT * FROM tasks WHERE user_id = ? ORDER BY id',
        (user_id,)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]

def add_task(user_id, title):
    conn = get_db()
    conn.execute(
        'INSERT INTO tasks (user_id, title) VALUES (?, ?)',
        (user_id, title)
    )
    conn.commit()
    conn.close()

def mark_done(task_id, user_id):
    conn = get_db()
    cursor = conn.execute(
        'UPDATE tasks SET is_done = 1 WHERE id = ? AND user_id = ?',
        (task_id, user_id)
    )
    conn.commit()
    affected = cursor.rowcount  # 0 если задача не найдена или чужая
    conn.close()
    return affected > 0

def delete_task(task_id, user_id):
    conn = get_db()
    cursor = conn.execute(
        'DELETE FROM tasks WHERE id = ? AND user_id = ?',
        (task_id, user_id)
    )
    conn.commit()
    affected = cursor.rowcount
    conn.close()
    return affected > 0

def get_stats(user_id):
    conn = get_db()
    row = conn.execute('''
        SELECT
            COUNT(*)         AS total,
            SUM(is_done)     AS done,
            SUM(1 - is_done) AS not_done
        FROM tasks
        WHERE user_id = ?
    ''', (user_id,)).fetchone()
    conn.close()
    return dict(row) if row else {'total': 0, 'done': 0, 'not_done': 0}

# ─── BOT SETUP ────────────────────────────────────
bot = Bot(token=BOT_TOKEN)
dp  = Dispatcher(storage=MemoryStorage())

# ─── FSM STATES ───────────────────────────────────
class AddTask(StatesGroup):
    waiting_title = State()

class DoneTask(StatesGroup):
    waiting_number = State()

class DeleteTask(StatesGroup):
    waiting_number = State()

# ─── HELPERS ──────────────────────────────────────
def format_tasks(tasks):
    if not tasks:
        return "У тебя пока нет задач. Добавь через /add"
    lines = []
    for i, t in enumerate(tasks, 1):
        mark = "✅" if t['is_done'] else "⬜"
        lines.append(f"{i}. {mark} {t['title']}")
    return "\n".join(lines)

def tasks_keyboard(tasks):
    """Inline-кнопки для невыполненных задач"""
    buttons = []
    for i, t in enumerate(tasks, 1):
        if not t['is_done']:
            buttons.append([InlineKeyboardButton(
                text=f"✅ Выполнить №{i} — {t['title'][:20]}",
                callback_data=f"done_{t['id']}"
            )])
    if not buttons:
        return None
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# ─── HANDLERS ─────────────────────────────────────

@dp.message(Command('start'))
async def cmd_start(message: Message):
    user = create_user(
        telegram_id=message.from_user.id,
        username=message.from_user.username or 'Аноним'
    )
    await message.answer(
        f"Привет, {message.from_user.first_name}! 👋\n"
        f"Я помогу вести список задач.\n\n"
        f"/add — добавить задачу\n"
        f"/tasks — мои задачи\n"
        f"/done — отметить выполненной\n"
        f"/stats — статистика\n"
        f"/delete — удалить задачу"
    )

@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(
        "/add — добавить задачу\n"
        "/tasks — список задач\n"
        "/done — отметить выполненной\n"
        "/delete — удалить задачу\n"
        "/stats — статистика"
    )

# ── /add ──────────────────────────────────────────
@dp.message(Command('add'))
async def cmd_add(message: Message, state: FSMContext):
    await state.set_state(AddTask.waiting_title)
    await message.answer("Введи название задачи:")

@dp.message(AddTask.waiting_title)
async def add_title(message: Message, state: FSMContext):
    user = get_user(message.from_user.id)
    add_task(user['id'], message.text)
    await state.clear()
    await message.answer(f"✅ Задача добавлена: {message.text}")

# ── /tasks ────────────────────────────────────────
@dp.message(Command('tasks'))
async def cmd_tasks(message: Message):
    user = get_user(message.from_user.id)
    if not user:
        await message.answer("Сначала напиши /start")
        return
    tasks = get_tasks(user['id'])
    text  = format_tasks(tasks)
    kb    = tasks_keyboard(tasks)
    await message.answer(text, reply_markup=kb)

# ── Inline-кнопка "Выполнить" ─────────────────────
@dp.callback_query(F.data.startswith('done_'))
async def inline_done(callback: CallbackQuery):
    await callback.answer()
    task_id = int(callback.data.split('_')[1])
    user    = get_user(callback.from_user.id)
    success = mark_done(task_id, user['id'])
    if success:
        await callback.message.answer("✅ Задача отмечена как выполненная!")
    else:
        await callback.message.answer("❌ Задача не найдена.")

# ── /done (FSM) ───────────────────────────────────
@dp.message(Command('done'))
async def cmd_done(message: Message, state: FSMContext):
    user  = get_user(message.from_user.id)
    tasks = get_tasks(user['id'])
    if not tasks:
        await message.answer("У тебя нет задач.")
        return
    await state.update_data(tasks=tasks)
    await state.set_state(DoneTask.waiting_number)
    await message.answer(
        f"{format_tasks(tasks)}\n\n"
        f"Введи номер задачи которую хочешь отметить выполненной:"
    )

@dp.message(DoneTask.waiting_number)
async def done_number(message: Message, state: FSMContext):
    data  = await state.get_data()
    tasks = data['tasks']
    await state.clear()

    if not message.text.isdigit():
        await message.answer("❌ Введи число.")
        return

    num = int(message.text)
    if num < 1 or num > len(tasks):
        await message.answer(f"❌ Номер должен быть от 1 до {len(tasks)}.")
        return

    task    = tasks[num - 1]
    user    = get_user(message.from_user.id)
    success = mark_done(task['id'], user['id'])

    if success:
        await message.answer(f"✅ Задача выполнена: {task['title']}")
    else:
        await message.answer("❌ Не удалось отметить задачу.")

# ── /delete (FSM) ─────────────────────────────────
@dp.message(Command('delete'))
async def cmd_delete(message: Message, state: FSMContext):
    user  = get_user(message.from_user.id)
    tasks = get_tasks(user['id'])
    if not tasks:
        await message.answer("У тебя нет задач.")
        return
    await state.update_data(tasks=tasks)
    await state.set_state(DeleteTask.waiting_number)
    await message.answer(
        f"{format_tasks(tasks)}\n\n"
        f"Введи номер задачи которую хочешь удалить:"
    )

@dp.message(DeleteTask.waiting_number)
async def delete_number(message: Message, state: FSMContext):
    data  = await state.get_data()
    tasks = data['tasks']
    await state.clear()

    if not message.text.isdigit():
        await message.answer("❌ Введи число.")
        return

    num = int(message.text)
    if num < 1 or num > len(tasks):
        await message.answer(f"❌ Номер должен быть от 1 до {len(tasks)}.")
        return

    task    = tasks[num - 1]
    user    = get_user(message.from_user.id)
    success = delete_task(task['id'], user['id'])

    if success:
        await message.answer(f"🗑 Задача удалена: {task['title']}")
    else:
        await message.answer("❌ Не удалось удалить задачу.")

# ── /stats ────────────────────────────────────────
@dp.message(Command('stats'))
async def cmd_stats(message: Message):
    user = get_user(message.from_user.id)
    if not user:
        await message.answer("Сначала напиши /start")
        return
    s = get_stats(user['id'])
    await message.answer(
        f"📊 Твоя статистика:\n\n"
        f"Всего задач:    {s['total'] or 0}\n"
        f"✅ Выполнено:   {s['done'] or 0}\n"
        f"⬜ Не выполнено: {s['not_done'] or 0}"
    )

# ─── MAIN ─────────────────────────────────────────
async def main():
    init_db()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
