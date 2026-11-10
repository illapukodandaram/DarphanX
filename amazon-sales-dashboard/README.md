# Amazon Sales Report Dashboard (web version)
Interactive dashboard recreated from the Power BI screenshots. KPIs (Quantity, Sales, Profit, Shipping Cost),
Category & Market slicers, Ship Mode / Country / City bars, Category & Market donuts.

## Run
1. `python generate_data.py` (creates `data/sales.csv` and `data/data.js`) — optional, data.js is already included
2. Open `index.html` in a browser (internet needed once for Chart.js CDN).

## Use real data
Put your data in `data/sales.csv` with columns:
City, Country, Market, Category, ShipMode, Sales, Quantity, Profit, ShippingCost, then rebuild `data/data.js`
(`python build_js.py`).
NOTE: The original .pbix/.xlsx in the uploaded zip were empty (2 bytes), so sample data is used here.
