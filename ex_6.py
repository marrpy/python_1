while True:
    day = 1
    start_km = float(input('Начальный результат - '))
    last_km = float(input('Финальный результат - '))
    if start_km <= 0 or last_km < 0:
        print('Результаты должны быть больше нуля! Стартовое значение != 0')
    else:
        while start_km < last_km:
            start_km *= 1.1
            day += 1
        print(f'Спортмен добьется результат за {day} дней')