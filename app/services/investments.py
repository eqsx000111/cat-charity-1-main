def invest(
        target,
        sources
):
    for donation in sources:
        if target.fully_invested:
            break
        invested_amount = min(
            target.full_amount - target.invested_amount,
            donation.full_amount - donation.invested_amount
        )
        for obj in (target, donation):
            obj.invested_amount += invested_amount
            obj.recalculate_state()
