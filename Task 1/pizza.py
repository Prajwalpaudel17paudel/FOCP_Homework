def calculate_pizza_price():
   """Calculates the total price of a pizza order based on BPP's pricing rules."""

   # Constants for pricing
   PIZZA_PRICE = 12.00
   DELIVERY_CHARGE = 2.50
   TUESDAY_DISCOUNT = 0.50
   APP_DISCOUNT = 0.25

   # Gather order information from the user
   num_pizzas = get_positive_integer_input("How many pizzas ordered? ")
   is_delivery = get_yes_or_no_input("Is delivery required? ")
   is_tuesday = get_yes_or_no_input("Is it Tuesday? ")
   used_app = get_yes_or_no_input("Did the customer use the app? ")

   # Calculate the base pizza price
   pizza_price = num_pizzas * PIZZA_PRICE

   # Apply Tuesday discount if applicable
   if is_tuesday:
       pizza_price *= (1 - TUESDAY_DISCOUNT)

   # Calculate delivery charge (if applicable)
   delivery_charge = DELIVERY_CHARGE if is_delivery and num_pizzas < 5 else 0

   # Calculate total price before any app discount
   total_price = pizza_price + delivery_charge

   # Apply app discount if applicable
   if used_app:
       total_price *= (1 - APP_DISCOUNT)

   # Format and display the total price
   formatted_price = f"£{total_price:.2f}"
   print(f"Total Price: {formatted_price}")


def get_positive_integer_input(prompt):
   """Prompts the user for a positive integer and validates the input."""
   while True:
       try:
           value = int(input(prompt))
           if value > 0:
               return value
           else:
               print("Please enter a positive integer!")
       except ValueError:
           print("Please enter a number!")


def get_yes_or_no_input(prompt):
   """Prompts the user for a yes/no answer and validates the input."""
   while True:
       answer = input(prompt).lower()
       if answer in ("y", "n"):
           return answer == "y"
       else:
           print("Please answer \"Y\" or \"N\".")


if __name__ == "__main__":
   print("BPP Pizza Price Calculator")
   print("==========================")
   calculate_pizza_price()
