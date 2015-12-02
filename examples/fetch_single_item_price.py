from csgoprices.scraper import Scraper, Currencies
from csgoprices import entities

def main():
    scraper = Scraper(currency=Currencies.RUB)
    asiimov = entities.Skin('AWP', 'Asiimov', entities.Wears.FieldTested)
    print scraper.build_request(asiimov)


if __name__ == '__main__':
    main()
