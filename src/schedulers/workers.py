from common import bot


PHOTO_ID_EN = "AgACAgIAAxkBAAIDNmEnkCC0L-N-nM-noDS9jmowj7rRAAIMtTEbpiI4Sa7NQHmtia1JAQADAgADcwADIAQ"
PHOTO_ID_RU = "AgACAgIAAxkBAAIDUGEnogjv3cLDhnbD5hu7oYrNC-laAAJEtTEbpiI4Sc_x3T0FW7V2AQADAgADcwADIAQ"


async def memenger_send(chat_id):
    await bot.send_photo(chat_id, PHOTO_ID_RU, caption='Как успехи?')
