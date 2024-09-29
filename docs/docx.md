
# Документация #
## Общее описание проекта ##
### Файл circle.py ###
Содержит реализацию нахождения площади круга, периметра окружности
```
def area(r: int) -> float
def perimeter(r: int) -> float
```

### Файл square.py ###
Содержит реализацию нахождения площади квадрата, периметра квадрата
```
def area(a: int) -> int
def perimeter(a: int) -> int
```

## Примеры использования ##
### Примеры использования circle.py
```
import circle

def sphere_volume(r: int) -> float:
    return 2 / 3 * circle.area(r) * circle.perimeter(r)

print(sphere_volume(10))
```

### Пример использования square.py ###
```
import square

size = int(input())

area = square.area(size) # size ** 2
per  = square.perimeter(size) # 4 * size

print(area, per)
```
## История коммитов ##
