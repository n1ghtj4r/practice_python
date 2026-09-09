class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other_category.name}")
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        # Title line: 30 characters, name centered between *
        title = self.name.center(30, "*")
        lines = [title]

        for item in self.ledger:
            description = item["description"][:23]
            amount = f"{item['amount']:.2f}"
            # Right-align amount to 7 characters
            line = f"{description:<23}{amount:>7}"
            lines.append(line)

        total = f"Total: {self.get_balance():.2f}"
        lines.append(total)

        return "\n".join(lines)


def create_spend_chart(categories):
    # Calculate total spent (only withdrawals) and spent per category
    spent = []
    total_spent = 0

    for category in categories:
        category_spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                category_spent += abs(item["amount"])
        spent.append(category_spent)
        total_spent += category_spent

    # Calculate percentages rounded down to nearest 10
    percentages = []
    for amount in spent:
        if total_spent == 0:
            percentages.append(0)
        else:
            percent = int((amount / total_spent) * 100)
            percentages.append(percent - (percent % 10))

    # Build the chart
    lines = ["Percentage spent by category"]

    # Y-axis from 100 to 0
    for i in range(100, -1, -10):
        line = f"{i:>3}|"
        for percent in percentages:
            if percent >= i:
                line += " o "
            else:
                line += "   "
        line += " "
        lines.append(line)

    # Horizontal line
    horizontal = "    " + "-" * (3 * len(categories) + 1)
    lines.append(horizontal)

    # Category names written vertically
    max_len = max(len(category.name) for category in categories)
    for i in range(max_len):
        line = "    "
        for category in categories:
            if i < len(category.name):
                line += f" {category.name[i]} "
            else:
                line += "   "
        line += " "
        lines.append(line)

    return "\n".join(lines)

# --- Test the Budget App ---

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)

print(food)
print()
print(clothing)
print()

# Create spend chart
auto = Category('Auto')
auto.deposit(1000)
auto.withdraw(150)

print(create_spend_chart([food, clothing, auto]))