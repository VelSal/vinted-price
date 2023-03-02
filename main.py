price = input("Prix revendeur: ")

def vinted():

  result = (((float(price) * 5) / 100) + 0.7 + float(price))
  return result

print("Prix avec charges vinted (HFDP): " + str(vinted()) + "€")