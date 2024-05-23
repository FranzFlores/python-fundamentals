# Herencia: Es la posibilidad de compartir atributos y métodos entre clases.
# Para ello, se define una clase padre y se define una clase hija.
import person
import developer

person_object = person.Person()
person_object.set_name("Franz")
person_object.set_lastname("Flores")
person_object.set_height(1.70)
person_object.set_age(30)

print(f"La persona se llama {person_object.get_name()} {person_object.get_lastname()} y tiene {person_object.get_age()} años.")
print(person_object.talk())

person_developer = developer.Developer()
person_developer.set_name("Juan")
person_developer.set_lastname("Perez")
person_developer.set_height(1.70)
person_developer.set_age(20)

print(f"La persona informática se llama {person_developer.get_name()} {person_developer.get_lastname()} y tiene {person_developer.get_age()} años.")
print(person_developer.program())
print(person_developer.get_languages())