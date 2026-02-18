from backend.scrapers.bayer_ua_dekalb import BayerUADekalbScraper


def test_parse_product_extracts_expected_fields():
    html = """
    <html><body>
      <h1>ДКС 3747</h1>
      <div>ФАО: 260</div>
      <div>Тип зерна: зубовидний</div>
      <div>Група стиглості: середньорання</div>
      <div>ОСНОВНІ ПЕРЕВАГИ\nСтабільний врожай</div>
      <div>ПОЗИЦІОНУВАННЯ ГІБРИДА\nЗона вирощування: усі зони\nРівень мінерального живлення: середній, високий</div>
      <div>ГУСТОТА НА ЧАС ЗБИРАННЯ\nПосушливі умови: 50 000–55 000 шт./га</div>
      <div>ХАРАКТЕРИСТИКА ГІБРИДА\nХолодостійкість ● ● ● ● ● ● ● ● ● 9</div>
    </body></html>
    """

    scraper = BayerUADekalbScraper()
    scraper.fetch = lambda _: html

    item = scraper.parse_product("https://www.cropscience.bayer.ua/Products/Dekalb/Corn/DKS3747")

    attr = {a["key"]: a["value"] for a in item["attributes"]}
    assert item["name"] == "ДКС 3747"
    assert item["crop"] == "corn"
    assert attr["fao"] == "260"
    assert attr["grain_type"] == "зубовидний"
    assert attr["maturity_group"] == "середньорання"
    assert attr["positioning.Зона вирощування"] == "усі зони"
    assert attr["density.Посушливі умови"] == "50 000–55 000 шт./га"
    assert attr["rating.Холодостійкість"] == 9
    for entry in item["attributes"]:
        assert entry["selector"] == "regex_on_page_text"
        assert entry["source_url"].startswith("https://www.cropscience.bayer.ua/Products/Dekalb/")
        assert entry["evidence"]
