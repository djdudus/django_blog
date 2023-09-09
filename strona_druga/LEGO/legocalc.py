import os
from bricklink_api.auth import oauth
from bricklink_api.catalog_item import get_price_guide, Type, NewOrUsed, get_subsets

consumer_key = os.environ.get("BL_API_CONS_KEY")
consumer_secret = os.environ.get("BL_API_CONS_SECRET")
token_value = os.environ.get("BL_API_TOKEN_VALUE")
token_secret = os.environ.get("BL_API_TOKEN_SECRET")
auth = oauth(consumer_key, consumer_secret, token_value, token_secret)


def get_set_parts(set_number):
    print(f"szukam seta:{set_number}")
    json_obj = get_price_guide(
        Type.SET, f"{set_number}-1", new_or_used=NewOrUsed.NEW, auth=auth
    )

    result = get_subsets(Type.SET, f"{set_number}-1", instruction=True, auth=auth)

    return (
        json_obj,
        result,
    )


def get_brick_info(entry):
    notes = ""
    info2 = entry["entries"][0]
    info = entry["entries"][0]["item"]

    price_info = get_price_guide(
        info["type"],
        info["no"],
        info2["color_id"],
        new_or_used="N",
        auth=auth,
        guide_type="sold",
        region="europe",
        country_code="PL",
    )
    if price_info["data"]["avg_price"] == "0.0000":
        price_info = get_price_guide(
            info["type"],
            info["no"],
            info2["color_id"],
            new_or_used="N",
            auth=auth,
            guide_type="sold",
            region="europe",
        )
        notes = "nie ma w polsce"
    qty = info2["quantity"] + info2["extra_quantity"]
    return (
        info["no"],
        info2["color_id"],
        info["category_id"],
        info["type"],
        qty,
        float(price_info["data"]["min_price"]),
        float(price_info["data"]["avg_price"]),
        float(price_info["data"]["max_price"]),
        notes,
    )
