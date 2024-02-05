import work 
from dictionary import cities

if __name__ == "__main__":

  for city, info in cities.items():
    print(f"\nCity: {city}")
    print(f"country: {info['country']}")
    print(f"population: {info['population']}")
    print(f"fact: {info['fact']}")

  result = work.add(5, 6)  # Call the add function from the work module
  print(result)
