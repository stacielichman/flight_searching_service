import os
import time


def main_menu():
    """
    Базовая функция с пунктами меню
    :param user_choice: пользовательский ввод
    """
    print(
        '\nГлавное меню:\n\n1 - ввод рейса\n2 - вывод всех рейсов\n3 - поиск рейса по номеру\n0 - завершение работы\n')
    while True:
        try:
            menu_choice = int(input('Введите номер пункта меню: '))
            if menu_choice == 1:
                make_new_flight()
                return
            elif menu_choice == 2:
                display_all_flights()
                return
            elif menu_choice == 3:
                flight_search_by_number()
                return
            elif menu_choice == 0:
                break
            else:
                print('Вы не выбрали пункт меню')
        except ValueError:
            print('Вы ввели несуществующий номер пункта меню')


def check_sym_amount(curr_sym_amnt: int, req_sym_amnt: int) -> bool:
    """
    Функция проверки количества введенных пользователем символов
    :param сurr_sym_amnt: количество символов, веденных пользователем
    :param req_sym_amnt: установленное количество символов
    :return: bool
    """
    if curr_sym_amnt != req_sym_amnt:
        return False
    return True


def add_to_database(text: str) -> None:
    """
    Функция сохранения данных в текстовый файл
    """
    with open('flights_datebase.txt', 'a') as flights_base:
        flights_base.write(text + '\n')
        return


def get_flight_num() -> str:
    """
    Функция возвращает номер рейса
    """
    while True:
        flight_num = input('XXXX - номер рейса: ').upper()
        if check_sym_amount(len(flight_num), 4):
            return flight_num
        print('Неверно введен номер рейса.\nВведите номер рейса согласно указанному формату.')


def format_date_is_valid(date: str) -> bool:
    """
    Функция проверяет валиден ли формат даты
    """
    try:
        time.strptime(date, '%d/%m/%Y')
    except ValueError:
        return False
    return True


def get_flight_date() -> str:
    """
    Функция возвращает дату рейса
    """
    while True:
        flight_date = input('ДД/ММ/ГГГГ - дата рейса: ')
        if check_sym_amount(len(flight_date), 10) and format_date_is_valid(flight_date):
            return flight_date
        print('Неверно введена дата рейса.\nВведите дату рейса согласно указанному формату.')


def format_time_is_valid(flight_time: str) -> bool:
    """
    Функция проверяет валиден ли формат времени
    """
    try:
        time.strptime(flight_time, '%H:%M')
    except ValueError:
        return False
    return True


def get_flight_time() -> str:
    """
    Функция возвращает время вылета
    """
    while True:
        flight_time = input('ЧЧ:ММ - время вылета: ')
        if check_sym_amount(len(flight_time), 5) and format_time_is_valid(flight_time):
            return flight_time
        print('Неверно введено время вылета.\nВведите время вылета согласно указанному формату.')


def check_travel_time_is_valid(time: float) -> bool:
    """
    Функция проверяет является ли переменная длительности перелета валидной
    """
    if len(str(time)) != 5:
        return False
    return True


def get_travel_time() -> str:
    """
    Функция возвращает время перелета
    :param travel_time: пользовательский ввод
    :return float: время перелета
    """
    while True:
        try:
            time = input('XX.XX - длительность перелета: ')
            if check_travel_time_is_valid(time) and time[2] == ".":
                return time
            print('Неверно введена длительность перелета.\nВведите длительность перелета согласно указанному формату.')
        except ValueError:
            print('Неверно введена длительность перелета.')


def get_departure_airport() -> str:
    """
    Функция возвращает аэропорт вылета
    """
    while True:
        dep_airport_iata = input('ХХХ - аэропорт вылета: ').upper()
        if check_sym_amount(len(dep_airport_iata), 3):
            return dep_airport_iata
        print('Неверно введен аэропорт вылета.\nВведите аэропорт вылета согласно указанному формату.')


def get_arrival_airport() -> str:
    """
    Функция возвращает аэропорт прибытия
    """
    while True:
        arr_airport_iata = input('ХХХ - аэропорт назначения: ').upper()
        if check_sym_amount(len(arr_airport_iata), 3):
            return arr_airport_iata
        print('Неверно введен аэропорт назначения.\nВведите аэропорт назначения согласно указанному формату.')


def get_ticket_price() -> float:
    """
    Функция возвращает стоимость билета
    param: ticket_price: пользовательский ввод
    return: float: стоимость билета
    """
    while True:
        try:
            price = float(input('.XX - стоимость билета (>0): '))
            if price > 0:
                return price
            print('Неверно введена стоимость билета.\nВведите стоимость билета согласно указанному формату.')
        except ValueError:
            print('Неверно введена стоимость билета.')


def make_new_flight():
    """
    Функция сохраняет данные по рейсу в общую переменную
    :return str: строка, подтверждающая добавление рейса в хранилище
    """
    print('\nВведите данные рейса:')
    flight_num = get_flight_num()
    flight_date = get_flight_date()
    flight_time = get_flight_time()
    travel_time = get_travel_time()
    dep_airport_iata = get_departure_airport()
    arr_airport_iata = get_arrival_airport()
    ticket_price = get_ticket_price()

    result_text = f"Информация о рейсе {flight_num} {flight_date} {flight_time} {travel_time} {dep_airport_iata} {arr_airport_iata} {ticket_price}"
    add_to_database(result_text)
    print(f'\n{result_text}* добавлена\n\n')
    main_menu()


def display_all_flights():
    """
    Функция, которая выводит все рейсы
    :return str: выводит все рейсы
    """
    with open('flights_datebase.txt', 'r') as flights_data:
        if os.stat('flights_datebase.txt').st_size == 0:
            print('Информация о рейсах отсутствует\n\n')
        else:
            data = flights_data.read()
            print(data)
    main_menu()


def flight_search_by_number():
    """
    Функция, которая выводит рейс по введенному пользователем номеру
    :param user_choice: пользовательский ввод номера рейса
    :return str: рейс по введенному пользователем номеру
    """
    no_flight_is_found = True
    flight_search_num = input('Введите номер рейса в формате ХХХХ: ').upper()
    with open('flights_datebase.txt', 'r') as flights_data:
        for i_flight in flights_data.readlines():
            if flight_search_num in i_flight.split()[3]:
                print(f'{i_flight}')
                no_flight_is_found = False
    if no_flight_is_found:
        print(f'Рейс {flight_search_num} не найден')
    main_menu()


print('Сервис поиска авиабилетов\n\n')
main_menu()
