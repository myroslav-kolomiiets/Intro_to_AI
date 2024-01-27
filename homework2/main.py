from logic_solver import Symbol, Not, And, Implication, model_check

milan = Symbol("Мілан")
real = Symbol("Реал")
metalist = Symbol("Металіст")

antonio = Symbol("Антоніо")
rodrigo = Symbol("Родріго")
mykola = Symbol("Микола")

# а) Металіст не тренується в Антоніо.
constraint1 = Not(Implication(metalist, antonio))

# б) Реал обіцяв ніколи не брати Миколу головним тренером.
constraint2 = Not(Implication(real, mykola))

knowledge = And(constraint1, constraint2)

query = metalist

result = model_check(knowledge, query)

if result:
    print("Тренер команди Металіст визначений.")
else:
    print("Не вдалося визначити тренера команди Металіст.")
