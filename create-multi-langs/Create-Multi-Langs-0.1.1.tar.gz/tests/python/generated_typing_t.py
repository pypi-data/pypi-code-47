from .generated_typing import MultiLangs, ZH_TW, EN


def test_generated():
    ml = MultiLangs(ZH_TW)
    assert ml.hello == "您好,歡迎"
    assert ml.login == "登入"
    assert ml.select_lang == "繁體中文"

    ml.set_lang(EN)
    assert ml.hello == "Hello,Welcome"
    assert ml.login == "Login"
    assert ml.select_lang == "English"
