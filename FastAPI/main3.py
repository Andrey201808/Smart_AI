import uuid
from fastapi import FastAPI, Body, status
from fastapi.responses import JSONResponse, FileResponse
 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id = str(uuid.uuid4())
 
# условная база данных - набор объектов Person
people = [Person("город Павловск, Пязелево, Школьная улица, дом 5, литера А", 196641),
          Person("Санкт-Петербург город Красное Село Дудергоф Театральная улица дом 9 литера А", 198325),
          Person("г.Санкт-Петербург улица Верности дом 28 корпус 2 литера А", 195256),
          Person("г. Смоленск, 3 Марта улица, дом 22", 154685),
          Person("г.Санкт-Петербург  Взлётная улица  дом 5  корпус 2  литера Д", 324846),
          Person("г.Санкт-Петербург  Большая Морская улица  дом 67  литера Я", 548735),
          Person("г.Санкт-Петербург  Старо-Паново  Поселковая улица  дом 32  литера А а", 154385),
          Person("г.Санкт-Петербург  Белградская улица  дом 42  корпус 1", 154342),
          Person("г.Санкт-Петербург  Большая Озерная улица  дом 39а", 487345),
          Person("город Кронштадт  Тулонская аллея  дом 3", 158435),
          Person("город Сестрорецк  улица Николая Соколова  дом 9", 154145),
          Person("поселок Белоостров  Александровское шоссе  дом 59", 554466),
          Person("город Красное Село  улица Освобождения  дом 15  корпус 2", 798987),
          Person("город Зеленогорск  Кавалерийская улица  дом 14а", 198543),
          Person("поселок Песочный  Центральная улица  дом 12", 796546),
          Person("г.Санкт-Петербург  улица Белоусова  дом 24/32", 847165),
          Person("посёлок Ушково  Приморское шоссе  дом 619/2  литера О", 847516),
          Person("поселок Лисий Нос  Новоцентральная улица  дом 46", 004841),
          Person("г.Санкт-Петербург  улица Лизы Чайкиной  дом 26  литера Б", 567451),
          Person("г.Санкт-Петербург  улица Электропультовцев  дом 7  корпус 5", 411165),
          Person("г.Санкт-Петербург  Петергофское шоссе  корпус 7", 654665),
          Person("поселок Комарово  Северная улица  дом 2/6", 119448),
          Person("город Петергоф  Собственный проспект  дом 4", 798652),
          Person("город Зеленогорск  1-я Лесная улица  дом 37  литера И", 184855),
          Person("г.Санкт-Петербург  проспект Обуховской Обороны  дом 120  литера АТ", 300135),
          Person("поселок Тярлево  Колхозная улица  дом 7", 115546),
          Person("город Сестрорецк  садоводство Разлив  11-я дорожка  дом 58  литера Б", 133554),
          Person("г.Санкт-Петербург  деревня Рыбацкое  дом 10", 884465),
          Person("город Пушкин  улица Красной Звезды  дом 8", 184644),
          Person("город Петергоф  Егерская улица  дом 1/7", 114554),
          Person("г.Санкт-Петербург  проспект Обуховской Обороны  дом 45", 546566)      
         ]
 
# для поиска пользователя в списке people
def find_person(id):
   for person in people: 
        if person.id == id:
           return person
   return None
 
app = FastAPI()
 
@app.get("/")
async def main():
    return FileResponse("public/index.html")
 
@app.get("/api/users")
def get_people():
    return people
 
@app.get("/api/users/{id}")
def get_person(id):
    # получаем пользователя по id
    person = find_person(id)
    print(person)
    # если не найден, отправляем статусный код и сообщение об ошибке
    if person==None:  
        return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND, 
                content={ "message": "Пользователь не найден" }
        )
    #если пользователь найден, отправляем его
    return person
 
 
@app.post("/api/users")
def create_person(data  = Body()):
    person = Person(data["name"], data["age"])
    # добавляем объект в список people
    people.append(person)
    return person
 
@app.put("/api/users")
def edit_person(data  = Body()):
  
    # получаем пользователя по id
    person = find_person(data["id"])
    # если не найден, отправляем статусный код и сообщение об ошибке
    if person == None: 
        return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND, 
                content={ "message": "Пользователь не найден" }
        )
    # если пользователь найден, изменяем его данные и отправляем обратно клиенту
    person.age = data["age"]
    person.name = data["name"]
    return person
 
 
@app.delete("/api/users/{id}")
def delete_person(id):
    # получаем пользователя по id
    person = find_person(id)
  
    # если не найден, отправляем статусный код и сообщение об ошибке
    if person == None:
        return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND, 
                content={ "message": "Пользователь не найден" }
        )
  
    # если пользователь найден, удаляем его
    people.remove(person)
    return person
