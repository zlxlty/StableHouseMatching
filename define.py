STR_LUMA = "Luma"
STR_ACHILLECIA = "Achillecia"
STR_HEX = "Hex"
STR_NEOTRON = "Neotron"
STR_VISTAR = "Vistar"
STR_ODYSSEY = "Odyssey"

STR_USER_ID = "user_id"
STR_USERNAME = "name"

HOUSE_NAMES = [STR_LUMA, STR_ACHILLECIA, STR_HEX, STR_NEOTRON, STR_VISTAR, STR_ODYSSEY]
HOUSE_ATTRIBUTES = {
    STR_LUMA: set(["奋斗", "进取", "实干"]),
    STR_ACHILLECIA: set(["正义", "批判", "勇敢"]),
    STR_HEX: set(["荣誉", "精明", "野心"]),
    STR_NEOTRON: set(["严谨", "秩序", "理性"]),
    STR_VISTAR: set(["感性", "想象", "自由"]),
    STR_ODYSSEY: set(["创新", "突破", "希望"]),
}

ATTRIBUTES_TO_HOUSE_NAMES = {
    "奋斗": STR_LUMA,
    "进取": STR_LUMA,
    "实干": STR_LUMA,
    "正义": STR_ACHILLECIA,
    "批判": STR_ACHILLECIA,
    "勇敢": STR_ACHILLECIA,
    "荣誉": STR_HEX,
    "精明": STR_HEX,
    "野心": STR_HEX,
    "严谨": STR_NEOTRON,
    "秩序": STR_NEOTRON,
    "理性": STR_NEOTRON,
    "感性": STR_VISTAR,
    "想象": STR_VISTAR,
    "自由": STR_VISTAR,
    "创新": STR_ODYSSEY,
    "突破": STR_ODYSSEY,
    "希望": STR_ODYSSEY,
}
