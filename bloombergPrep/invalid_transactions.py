"""
Array, Hash Table, Strings
Bloomberg Medium
"""

from collections import defaultdict

class Solution:
    def invalidTransactions(self, transactions: list[str]) -> list[str]:
        # Parse transactions and store
        # Group transactions using names
        # Compare transactions with the same name

        parsed = []
        for t in transactions:
            name, time, amount, city = t.split(',')
            parsed.append({
                "name": name,
                "time": int(time),
                "amount": int(amount),
                "city": city
            })

        invalid_indices = set()

        name_map = defaultdict(list)

        for i, t in enumerate(parsed):
            name_map[t["name"]].append(i) # {"alice": [0, 1]}

            if t["amount"] > 1000:
                invalid_indices.add(i)

        for name, indices in name_map.items():
            for i in range(len(indices)):
                for j in range(i + 1, len(indices)):
                    i1, i2 = indices[i], indices[j]
                    t1, t2 = parsed[i1], parsed[i2]

                    if t1["city"] != t2["city"] and abs(t1["time"] - t2["time"]) <= 60:
                        invalid_indices.add(i1)
                        invalid_indices.add(i2)

        return [transactions[i] for i in invalid_indices]
