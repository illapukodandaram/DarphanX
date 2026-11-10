"""Generates sample data (data/sales.csv) calibrated to the dashboard totals:
Sales 7.58M, Quantity 107K, Profit 890.6K, Shipping 614.6K. Replace with real data if you have it."""
import csv, random
random.seed(7)
CITIES = [  # city, country, market, weight
("New York City","United States","US",26),("Los Angeles","United States","US",17),("Seattle","United States","US",11),
("San Francisco","United States","US",11),("Philadelphia","United States","US",10),("Houston","United States","US",6),
("Manila","Philippines","APAC",12),("Sydney","Australia","APAC",10),("Melbourne","Australia","APAC",7),
("Brisbane","Australia","APAC",7),("Gold Coast","Australia","APAC",7),("Perth","Australia","APAC",6),
("Jakarta","Indonesia","APAC",10),("Bangkok","Thailand","APAC",7),("Shanghai","China","APAC",22),("Beijing","China","APAC",20),
("London","United Kingdom","EU",8.5),("Paris","France","EU",6),("Vienna","Austria","EU",6),("Berlin","Germany","EU",20),
("Lyon","France","EU",22),("Mexico City","Mexico","LATAM",8),("Managua","Nicaragua","LATAM",8),
("Santo Domingo","Dominican Republic","LATAM",7.5),("Sao Paulo","Brazil","LATAM",18),("Lagos","Nigeria","Africa",12),
("Cairo","Egypt","EMEA",10),("Istanbul","Turkey","EMEA",12),("Toronto","Canada","Canada",6)]
CATS = {"Technology":(.375,.17),"Furniture":(.33,.10),"Office Supplies":(.295,.12)}
MODES = {"Standard Class":.60,"Second Class":.20,"First Class":.14,"Same Day":.06}
S,Q,P,SH = 7.58e6,107e3,890.6e3,614.6e3
tw = sum(c[3] for c in CITIES)
with open("data/sales.csv","w",newline="") as f:
    w = csv.writer(f); w.writerow(["City","Country","Market","Category","ShipMode","Sales","Quantity","Profit","ShippingCost"])
    for city,ctry,mkt,wt in CITIES:
        for cat,(cs,pm) in CATS.items():
            for mode,ms in MODES.items():
                j = random.uniform(.85,1.15); sh = wt/tw*cs*ms*j
                w.writerow([city,ctry,mkt,cat,mode,round(S*sh,2),round(Q*sh),round(S*sh*pm,2),round(SH*sh*(1.2 if mode in("First Class","Same Day") else .9),2)])
print("data/sales.csv written")
