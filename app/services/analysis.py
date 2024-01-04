

def calculate_simple_return(yesterday_close, today_close):
    if yesterday_close == 0:
        return None
    return (today_close - yesterday_close) / yesterday_close


def process_financial_data(financial_data):
    time_series = financial_data.get('Time Series (Daily)')
    if not time_series:
        raise ValueError('Invalid data format received from financial data source')

    sorted_dates = sorted(time_series.keys(), reverse=True)
    if len(sorted_dates) < 2:
        return None, None

    latest_date, previous_date = sorted_dates[:2]
    latest_close = float(time_series[latest_date]['4. close'])
    previous_close = float(time_series[previous_date]['4. close'])

    return calculate_simple_return(previous_close, latest_close), latest_date

def create_analysis_prompt(symbol, simple_return, date):
    if simple_return is None:
        return "Unable to calculate the return for the given data."

    return (f"The stock {symbol} had a simple return of {simple_return:.2%} on {date}. "
            "Considering this change, provide a brief analysis of the stock's performance "
            "and potential implications for future trading sessions.")
