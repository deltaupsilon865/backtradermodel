import backtrader as bt
import yfinance as yf
import pandas as pd
import matplotlib 


class BBstrategy(bt.Strategy):
    def __init__(self):
        self.bb = bt.indicators.BollingerBands()
        self.order = None

    def log(self, txt):
        dt = self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def notify_order(self, order):
        if order.status == order.Completed:
            if order.isbuy():
                self.log(
                    f"Executed BUY (Price: {order.executed.price:.2f}, Value: {order.executed.value:.2f}, Commission: {order.executed.comm:.2f})")
            else:
                self.log(
                    f"Executed SELL (Price: {order.executed.price:.2f}, Value: {order.executed.value:.2f}, Commission: {order.executed.comm:.2f})")
            self.bar_executed = len(self)
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log("Order was canceled/margin/rejected")
        self.order = None

    def next(self):
        if self.order:
            return

        if not self.position:
            if (self.data.close[0] > self.bb.lines.mid[0]) and (self.data.close[-1] < self.bb.lines.mid[-1]):
                self.log('Buy Create, %.2f' % self.data.close[0])
                self.order = self.buy(size=10)

            elif (self.data.close[0] < self.bb.lines.mid[0]) and (self.data.close[-1] > self.bb.lines.mid[-1]):
                self.log('Sell Create, %.2f' % self.data.close[0])
                self.order = self.sell(size=10)
        else:
            if len(self) >= (self.bar_executed + 4):
                self.log('Position Closed, %.2f' % self.data.close[0])
                self.order = self.close()

if __name__ == '__main__':
    cerebro = bt.Cerebro()
    cerebro.broker.setcash(10000)
    cerebro.broker.setcommission(commission=0.001)

    df = yf.download("AAPL", start="2020-06-25", end="2025-06-25", interval="1d")
    # Ensure the DataFrame has the correct columns    

    # DOWNLOAD AND CHECK


if isinstance(df.columns[0], tuple):
    df.columns = [col[0] for col in df.columns]



    # Fix columns for Backtrader compatibility
    df.rename(columns={
        'Open': 'open',
        'High': 'high',
        'Low': 'low',
        'Close': 'close',
        'Volume': 'volume'
    }, inplace=True)
    df.index.name = 'datetime'

    data = bt.feeds.PandasData(dataname=df)
    cerebro.adddata(data)
    cerebro.addstrategy(BBstrategy)

    print('<START> Brokerage account: $%.2f' % cerebro.broker.getvalue())
    cerebro.run()
    print('<FINISH> Brokerage account: $%.2f' % cerebro.broker.getvalue())

    cerebro.plot()

