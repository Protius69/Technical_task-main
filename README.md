Привет коллега, ты решил выполнить тестовое задание по созданию БД на Python
Минимальный курс по Python: https://stepik.org/course/67/syllabus
Так же желательно пройти хотя бы базовые курсы по GIT и Pandas (или прочитать про их базовые функции)
Первым делом тебе необходимо импортировать папку Technical Task в среду разработки
Ссылка на неё в github: https://github.com/Protius69/Technical_task-main
Далее установи следующие модули в свою среду разработки:
1.	Python 3.9
2.	Datetime
3.	Pandas
4.	Jira.client

Как это сделать ты можешь найти в гугле
В папке Technical Task ты найдешь следующие файлы:
Connection_test помогает подключится к jira, а также считает необходимые для запроса дни недели, где range_day дата ближайшего к текущей дате понедельника, а today – сегодняшняя дата, для его работы заполни в нём поля jira_token в массиве secrets. Номер строки 49
Так же в файле содержится информация о периоде выгрузки
Support_func – ограничивает jira на выгрузку не более чем 300 заявок за раз, может выполнять несколько проходов
Выгрузка полей заявки – поможет выгрузить все поля заявки и их имена , для этого в строке 3 введи номер интересующей заявки и запусти файл локально
Пример – файл который собирает отчет по СРТ и количеству заявок с этим СРТ созданным за период с range_day по today, сделан для помощи тебе с твоим тех заданием, код 100% рабочий и спокойно работает локально, если он выдает ошибку проверь установленные модули и заполнение логина и пароля jira в файле connection_test
Задание – файл с уже предзаполненым импортом модулей в котором ты можешь написать своё задание

Задание
Тебе необходимо создать отчет, который будет выгружать все закрытые заявки за период с range_day по today и проверять их на заполненность поля меток (labels) и суммировать это в БД по этим меткам. Должно быть 3 столбца:
1.	Labels – имя метки
2.	Count_sd – количество заявок с этой меткой
3.	Upload_date – должно содержать значение поля today и быть в формате даты
Обрати внимание, что количество заявок с пустым полем меток так же должно быть в отчете. Отчет должен выводится в среде разработки и сохранятся на рабочий стол в формате csv
Задание со звездочкой: Данные в таблице должны быть отсортированы по количеству заявок у лейбла от большего к меньшему, этого нет в файле Пример. 
По всем вопросам в первую очередь необходимо пользоваться гуглом и/или яндексом (если с английским туговато)
Ко мне можешь обращаться только после того как уверился что не нашел ответа и зашел в конечный тупик. По приходу ты должен сказать, что уже пробовал и что не получается.
По выполнению задания можешь прислать мне файл Задание.py на проверку 
И пожалуйста не забывай комментировать код, что бы мне было понятно по какому пути ты идешь. Коммент может быть в строке и начинаться с символа # либо быть заключенным в три одинарные кавычки с двух сторон
