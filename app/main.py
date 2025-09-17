class Car:
    """Representa um carro com suas propriedades."""

    def __init__(
        self, comfort_class: int, clean_mark: int, brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    """Representa uma estação de lava-rápido e suas operações."""

    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        """
        Lava uma lista de carros se a sua marca de limpeza for inferior
        ao poder de limpeza da estação e retorna o rendimento total.
        """
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                wash_cost = self.calculate_washing_price(car)
                total_income += wash_cost
                self.wash_single_car(car)
        return round(total_income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        """
        Calcula o custo de lavagem para um único carro com base na fórmula.
        """
        price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        """
        Lava um único carro, atualizando a sua marca de limpeza para o poder
        de limpeza da estação.
        """
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, new_rate: int) -> None:
        """
        Adiciona uma nova avaliação e recalcula a avaliação média da estação.
        """
        current_total_rating = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        new_average_rating = (
            current_total_rating + new_rate
        ) / self.count_of_ratings
        self.average_rating = round(new_average_rating, 1)
