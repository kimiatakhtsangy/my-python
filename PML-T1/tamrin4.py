class Car:
    def __init__(self, company, color, year):
        self.company = company
        self.color = color
        self.year = year

    def details(self, company, color, year):
        company2 = {"sazande": company}
        color2 = {"rang": color}
        year2 = {"salesakht": year}
        print(company2.keys(), "\t", company2.values())
        print(color2.keys(), "\t", color2.values())
        print(year2.keys(), "\t", year2.values())

    def worked(self, year):
        how_old = float(2021 - year)
        print("your car age:", how_old)


Benz_sls = Car("Benz", "black", 2018)
Benz_sls.details("Benz", "black", 2018)
Benz_sls.worked(2018)

BMW_528 = Car("BMW", "white", 2015)
BMW_528.details("BMW", "white", 2015)
BMW_528.worked(2015)
