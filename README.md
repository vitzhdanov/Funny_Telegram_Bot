# Telegram_Bot

Возможности:
* Игра на двоих в кости, выводит победителя, играть можно параллельно в нескольких чатах.
* По запросу сохраняет текст в БД, сохраняет время, юезар и текст. (Для каждого чата своя таблица создаётся автоматически по ID чата)
* По запросу выводит сохранённые фразы.
* Поиск гугл по запросу.
* Аналог подбрось монетку, только возвращает гифки. ('да','нет' и с очень маленькой вероятностью 'может быть')
* ШЕСТЬ видов гороскопа на сегодня.
* Погода на сегодня.
* Курс валют на сегодня. (BTC, USD, EUR) 
* Совет от Бота. (запрос к веб-сервису по генерации случайных советов)
* Каждый день выводит "Цитату дня" в указанное время.
* Каждый понедельник, среду и пятницу отправляет картинку связанную с этим днём.

Для работы заполнить файлик 'config', вставить свои данные.
Для полноценной работы лучше сделать бота админом, он удаляет некоторые команды типа '/weather' чтобы не засорять чат.
