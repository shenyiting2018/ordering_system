from datetime import datetime
from seckill.data_access import load_commodity_by_id, list_commodity, update_commodity
from seckill.data_access import (
    load_seckill_campaign_by_id,
    create_seckill_campaign,
    list_seckill_campaigns_by_status,
)


def update_commodity_price_by_name(
    commodity_name,
    price,
):
    commodities = list_commodity(commodity_name=commodity_name)

    for commodity in commodities:
        update_commodity(
            commodity_id=commodity.id,
            price=price,
        )


def add_seckill_campaign(
    campaign_name,
    commodity_id,
    original_price,
    seckill_price,
    start_time,
    end_time,
    stock,
):
    commodity = load_commodity_by_id(commodity_id)
    if start_time:
        start_time = datetime.strptime(
            start_time.replace(" ", "-"), "%Y-%m-%d-%H:%M:%S"
        )
    if end_time:
        end_time = datetime.strptime(end_time.replace(" ", "-"), "%Y-%m-%d-%H:%M:%S")
    total_stock = stock
    available_stock = stock
    new_campaign = create_seckill_campaign(
        campaign_name,
        commodity,
        original_price,
        seckill_price,
        start_time,
        end_time,
        total_stock,
        available_stock,
    )
    return new_campaign


def available_seckill_campaigns_list():
    available_seckill_campaigns_list = list_seckill_campaigns_by_status(2)
    return available_seckill_campaigns_list


def seckill_campaign_item_info(seckill_campaign_id):
    campaign = load_seckill_campaign_by_id(seckill_campaign_id)
    return campaign
