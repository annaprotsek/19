import shelve

D1 = {
    "Tesla Model S": 1020,
    "Ford Mustang": 450,
    "Chevrolet Camaro": 455,
    "BMW M3": 473,
    "Audi RS6": 591,
    "Toyota Supra": 382,
    "Porsche 911": 473
}

D1.update({
    "Honda Civic": 158,
    "Nissan GT-R": 565,
    "Lamborghini Huracan": 631
})

with shelve.open("file1") as db:
    db["D1"] = D1

with shelve.open("file1") as db:
    saved_data = db["D1"]
    print("Вміст словника D1 з файлу:")
    for model, power in saved_data.items():
        print(f"{model}: {power} HP")
