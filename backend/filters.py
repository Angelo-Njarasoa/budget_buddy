def filter_by_type(transactions, transaction_type):
    return [t for t in transactions if t["type"] == transaction_type]


def filter_by_category(transactions, category):
    return [t for t in transactions if t["categorie"] == category]


def filter_by_date(transactions, date):
    return [t for t in transactions if str(t["date"]).startswith(date)]


def filter_by_period(transactions, start_date, end_date):
    result = []

    for t in transactions:
        transaction_date = str(t["date"])[:10]

        if start_date <= transaction_date <= end_date:
            result.append(t)

    return result


def sort_by_amount(transactions, order="asc"):
    reverse = order == "desc"
    return sorted(transactions, key=lambda t: float(t["montant"]), reverse=reverse)