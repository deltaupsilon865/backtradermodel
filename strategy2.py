import backtrader as bt
import yfinance as yf
import pandas as pd
import matplotlib

class RSI_BB_Strategy(bt.Strategy):
    params = dict(
        rsi_period=14,
        rsi_lower=30,
        rsi_upper=70,
        bb_period=20,
        bb_devfactor=2.0
    )

    def __init__(self):
        # Per-data indicators & order tracking
        self.inds = {}
        for d in self.datas:
            rsi = bt.indicators.RSI(d.close, period=self.p.rsi_period)
            bb   = bt.indicators.BollingerBands(d.close,
                                                period=self.p.bb_period,
                                                devfactor=self.p.bb_devfactor)
            self.inds[d._name] = dict(rsi=rsi, bb=bb, order=None)
        self.start_val = None

    def next(self):
        # record starting portfolio value once
        if self.start_val is None:
            self.start_val = self.broker.getvalue()

        for d in self.datas:
            name = d._name
            ind  = self.inds[name]
            posn = self.getposition(d).size

            # If there's a live order, skip
            if ind['order']:
                continue

            # BUY condition: price dips below lower BB AND RSI < rsi_lower
            if posn == 0 and d.close[0] < ind['bb'].lines.bot[0] and ind['rsi'][0] < self.p.rsi_lower:
                size = int((self.broker.getvalue() / len(self.datas)) / d.close[0])
                ind['order'] = self.buy(data=d, size=size)
                self.log(f"{name}: BUY   size={size} @ {d.close[0]:.2f}")

            # SELL condition: price pops above upper BB OR RSI > rsi_upper
            elif posn > 0 and (d.close[0] > ind['bb'].lines.top[0] or ind['rsi'][0] > self.p.rsi_upper):
                ind['order'] = self.sell(data=d, size=posn)
                self.log(f"{name}: SELL  size={posn} @ {d.close[0]:.2f}")

    def notify_order(self, order):
        # clear the order flag when done/canceled
        if order.status in (order.Completed, order.Canceled, order.Margin, order.Rejected):
            dname = order.data._name
            self.inds[dname]['order'] = None

    def log(self, txt):
        dt = self.datas[0].datetime.date(0)
        print(f"{dt.isoformat()}  {txt}")

if __name__ == '__main__':
    cerebro = bt.Cerebro()
    cerebro.broker.setcash(100000)
    cerebro.broker.setcommission(commission=0.001)

    tickers = ["AAPL", "MSFT", "NVDA"]
    for sym in tickers:
        df = yf.download(sym, start="2020-06-25", end="2025-06-25", interval="1d")
        if isinstance(df.columns[0], tuple):
            df.columns = [c[0] for c in df.columns]
        df.rename(columns={
            'Open': 'open', 'High': 'high',
            'Low': 'low', 'Close': 'close',
            'Adj Close': 'close', 'Volume': 'volume'
        }, inplace=True)
        df.index.name = 'datetime'
        data = bt.feeds.PandasData(dataname=df, name=sym)
        cerebro.adddata(data)

    cerebro.addstrategy(RSI_BB_Strategy,
                        rsi_period=14, rsi_lower=30, rsi_upper=70,
                        bb_period=20, bb_devfactor=2.0)

    print(f"<START> Portfolio value: ${cerebro.broker.getvalue():.2f}")
    cerebro.run()
    print(f"<FINISH> Portfolio value: ${cerebro.broker.getvalue():.2f}")

    cerebro.plot()







