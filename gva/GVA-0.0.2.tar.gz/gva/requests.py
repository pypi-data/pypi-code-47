from requests import post

from .exceptions import VkApiError

URL = "https://api.vk.com/method"


def execute_method(api, method, **data):
    data.update(api.const)  # Добавляем токен и версию из объекта Api

    response = post(
        "%s/%s" % (URL, method),
        data=data,
    ).json()

    #  Проверка на то, пришла ли ошибка с сервера ВК
    if "error" in response.keys():
        raise VkApiError(response)

    # Иногда приходит массив из одного элемента. Это как раз на этот случай
    # З.Ы Это фича ВК Апи, но для нас это - возможный баг
    # Например, если передан user_ids. Ну, вы понели. Короче, это требует дороботки! (todo)
    if isinstance(response["response"], list):
        return response["response"][0]
    return response["response"]
