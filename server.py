from flask import Flask, jsonify, request

app = Flask(__name__)

class Person:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

people = [
    Person(1, 'Vyacheslav Terekhov', 21),
    Person(2, 'Mariya Smirnova', 25),
    Person(3, 'Petr Petrov', 40),
    Person(4, 'Anna Ivanova', 35),
    Person(5, 'Sergey Kuznetsov', 28),
    Person(6, 'Ekaterina Kozlova', 33),
    Person(7, 'Aleksandr Novikov', 45),
    Person(8, 'Yelena Morozova', 22),
    Person(9, 'Andrey Pavlov', 38),
    Person(10, 'Olga Volkova', 29),
]

@app.route('/', methods=['GET'])
def get_people():
    response = [{'id': person.id, 'name': person.name, 'age': person.age} for person in people]
    return jsonify(response), 200

@app.route('/check', methods=['GET'])
def check_service():
    return jsonify({'message': 'Service is running...'}), 200

@app.route('/person/<int:id>', methods=['GET'])
def get_person(id):
    person = next((person for person in people if person.id == id), None)
    if person:
        return jsonify({'id': person.id, 'name': person.name, 'age': person.age}), 200
    else:
        return jsonify({'error': 'Person not found'}), 404

# Получение статистики
@app.route('/person/stats', methods=['GET'])
def get_people_stats():
    total_people = len(people)
    ages_distribution = {age: sum(1 for person in people if person.age == age) for age in set(person.age for person in people)}
    return jsonify({'total_people': total_people, 'ages_distribution': ages_distribution}), 200

# Сортировка
@app.route('/person/sort/<string:criteria>', methods=['GET'])
def sort_people(criteria):
    if criteria == 'name':
        sorted_people = sorted(people, key=lambda person: person.name)
    elif criteria == 'age':
        sorted_people = sorted(people, key=lambda person: person.age)
    else:
        return jsonify({'error': 'Invalid sorting criteria. Use "name" or "age"'}), 400
    return jsonify([{'id': person.id, 'name': person.name, 'age': person.age} for person in sorted_people]), 200

if __name__ == '__main__':
    app.run(debug=True)
