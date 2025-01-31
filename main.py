from urllib.parse import urlparse, parse_qs


def parse(query: str) -> dict:
    parsed_url = urlparse(query)
    query_params = parse_qs(parsed_url.query, keep_blank_values=True)  # Теперь пустые значения сохраняются!

    return {key: values[0] if len(values) == 1 else values for key, values in query_params.items()}


# ✅ Тесты
if __name__ == '__main__':
    assert parse('http://example.com/?') == {}  # Нет параметров
    assert parse('http://example.com/') == {}  # Пустой URL
    assert parse('http://example.com/?name=Alex') == {'name': 'Alex'}  # Один параметр
    assert parse('http://example.com/?name=Alex&age=25') == {'name': 'Alex', 'age': '25'}  # Несколько параметров
    assert parse('http://example.com/?name=Alex&name=John') == {'name': ['Alex', 'John']}  # Один ключ - несколько значений
    assert parse('http://example.com/?name=') == {'name': ''}  # ✅ Теперь пустое значение сохраняется
    assert parse('http://example.com/?name=Alex&age=') == {'name': 'Alex', 'age': ''}  # ✅ Один параметр с пустым значением
    assert parse('http://example.com/?color=red&color=blue&color=green') == {'color': ['red', 'blue', 'green']}  # Повторяющийся параметр
    assert parse('http://example.com/?a=1&b=2&c=3&d=4&e=5') == {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5'}  # Много параметров
    assert parse('http://example.com/?a=hello%20world') == {'a': 'hello world'}  # Кодировка пробела (%20)
    print("✅ Все тесты пройдены успешно!")
