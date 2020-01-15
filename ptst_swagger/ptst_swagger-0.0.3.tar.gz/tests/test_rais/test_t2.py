import allure

@allure.title(" Тестируем  test_t2")
def test_t2(rais):
    r = rais.get_paths_sw()
    for rx in r:
        print('rx=', rx)
    print('r=', r)