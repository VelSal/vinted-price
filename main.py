price = input("Prix revendeur: ")

def vinted():
  result = (((float(price) * 5) / 100) + 0.7 + float(price))
  return result
print("Prix avec charges vinted (HFDP): " + str(vinted()) + "€")

shipping = input("Frais de port: ")
def vintedShipping():
  result = (vinted() + float(shipping))
  return result
print("Prix avec frais de port: " + str(vintedShipping()) + "€")