import json
import random

datosCorrectos50 = []
datosCorrectos100 = []
datosIncoherentes50 = []
datosIncoherentes20 = []
datosIncoherentes10 = []
tiposDatosIncorrectos = []

tiposDatosIncorrectosPalabras = [{
    "serial_no": 479,
    "gre_score": "ඞ",
    "toefl_score": "hola",
    "university_rating": 4,
    "sop": 4,
    "lor": 2.77,
    "cgpa": 8.88,
    "research": 1
  },
  {
    "serial_no": 446,
    "gre_score": 301,
    "toefl_score": "si",
    "university_rating": 1,
    "sop": 1.85,
    "lor": "no",
    "cgpa": 7.71,
    "research": 0
  },
  {
    "serial_no": 336,
    "gre_score": 297,
    "toefl_score": 100,
    "university_rating": 1,
    "sop": "abc",
    "lor": 1.59,
    "cgpa": 7.89,
    "research": 0
  },
  {
    "serial_no": 20,
    "gre_score": 303,
    "toefl_score": 98,
    "university_rating": 3,
    "sop": 3.5,
    "lor": 3,
    "cgpa": 8.5,
    "research": "yo"
  }]

datosCorrectos = [{
    "serial_no": 479,
    "gre_score": 327,
    "toefl_score": 113,
    "university_rating": 4,
    "sop": 4,
    "lor": 2.77,
    "cgpa": 8.88,
    "research": 1
  },
  {
    "serial_no": 446,
    "gre_score": 301,
    "toefl_score": 92,
    "university_rating": 1,
    "sop": 1.85,
    "lor": 1.5,
    "cgpa": 7.71,
    "research": 0
  },
  {
    "serial_no": 336,
    "gre_score": 297,
    "toefl_score": 100,
    "university_rating": 1,
    "sop": 2.41,
    "lor": 1.59,
    "cgpa": 7.89,
    "research": 0
  },
  {
    "serial_no": 20,
    "gre_score": 303,
    "toefl_score": 98,
    "university_rating": 3,
    "sop": 3.5,
    "lor": 3,
    "cgpa": 8.5,
    "research": 0
  }]

datosIncoherentes= [
    {
        "serial_no": 0,
        "gre_score": 0,
        "toefl_score": 0,
        "university_rating": 0,
        "sop": 0,
        "lor": 0,
        "cgpa": 0,
        "research": 0
      }
]

for p in range(50):
  
    dic=({"serial_no": p,
    "gre_score": random.uniform(250, 340),
    "toefl_score": random.uniform(70, 120),
    "university_rating": random.uniform(0, 5),
    "sop": random.uniform(1, 5),
    "lor": random.uniform(1, 5),
    "cgpa": random.uniform(5, 10),
    "research": random.randint(0, 1)})
    datosCorrectos50.append(dic)

for p in range(100):
  
    dic=({"serial_no": p,
    "gre_score": random.uniform(250, 340),
    "toefl_score": random.uniform(70, 120),
    "university_rating": random.uniform(0, 5),
    "sop": random.uniform(1, 5),
    "lor": random.uniform(1, 5),
    "cgpa": random.uniform(5, 10),
    "research": random.randint(0, 1)})
    datosCorrectos100.append(dic)

for p in range(50):
  
    dic=({"serial_no": p,
    "gre_score": random.uniform(341, 500),
    "toefl_score": random.uniform(121, 300),
    "university_rating": random.uniform(6, 10),
    "sop": random.uniform(6, 10),
    "lor": random.uniform(6, 10),
    "cgpa": random.uniform(11, 20),
    "research": random.randint(2, 3)})
    datosIncoherentes50.append(dic)

for p in range(20):
  
    dic=({"serial_no": p,
    "gre_score": random.uniform(-400, -1),
    "toefl_score": random.uniform(-200, -1),
    "university_rating": random.uniform(-5, -1),
    "sop": random.uniform(-5, -1),
    "lor": random.uniform(-5, -1),
    "cgpa": random.uniform(-5, -1),
    "research": random.randint(-2, -1)})
    datosIncoherentes20.append(dic)

for p in range(10):
  
    dic=({"serial_no": p,
    "gre_score": random.uniform(0, 30),
    "toefl_score": random.uniform(0, 20),
    "university_rating": random.uniform(0, 1),
    "sop": random.uniform(0, 1),
    "lor": random.uniform(0, 1),
    "cgpa": random.uniform(0, 1),
    "research": random.randint(0, 1)})
    datosIncoherentes10.append(dic)


for p in range(10):
  
    dic=({"serial_no": p,
    "gre_score": str(random.uniform(250, 340)),
    "toefl_score": str(random.uniform(70, 120)),
    "university_rating": str(random.uniform(0, 5)),
    "sop": str(random.uniform(1, 5)),
    "lor": str(random.uniform(1, 5)),
    "cgpa": str(random.uniform(5, 10)),
    "research": str(random.randint(0, 1))})
    tiposDatosIncorrectos.append(dic)


with open('assets/datosCorrectos.json', 'w') as file:
    json.dump(datosCorrectos, file, indent=4)

with open('assets/datosCorrectos50.json', 'w') as file:
    json.dump(datosCorrectos50, file, indent=4)

with open('assets/datosCorrectos100.json', 'w') as file:
    json.dump(datosCorrectos100, file, indent=4)

with open('assets/datosIncoherentes.json', 'w') as file:
    json.dump(datosIncoherentes, file, indent=4)
    
with open('assets/datosIncoherentes50.json', 'w') as file:
    json.dump(datosIncoherentes50, file, indent=4)

with open('assets/datosIncoherentes20.json', 'w') as file:
    json.dump(datosIncoherentes20, file, indent=4)

with open('assets/datosIncoherentes10.json', 'w') as file:
    json.dump(datosIncoherentes10, file, indent=4)

with open('assets/tiposDatosIncorrectos.json', 'w') as file:
    json.dump(tiposDatosIncorrectos, file, indent=4)

with open('assets/tiposDatosIncorrectosPalabras.json', 'w') as file:
    json.dump(tiposDatosIncorrectosPalabras, file, indent=4)


