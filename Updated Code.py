#Code for scraping all table values 
for page in list(range(1,50)):
  result = requests.get("https://www.aishub.net/stations?page={}".format(page))
  src = result.text
  document = BeautifulSoup(src, 'lxml')
  table = document.find("table")
  rows = table.find_all("tr")  # Note: this works because find_all is resursive by default
  for row in rows[2:-1]:
    cells = row.find_all(["td", "th"])
    cells_text = [cell.get_text(strip=True) for cell in cells]
    (ID, Status, Uptime, Country, Location, Ships, Distinct, Contributor) = cells_text    
    print(f"{ID}, {Status}, {Uptime}, {Country}, {Location}, {Ships} , {Distinct} , {Contributor}")
