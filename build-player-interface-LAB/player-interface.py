import abc
import random

class Player(abc.ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self):
        move = random.choice(self.moves)
        self.position = (self.position[0] + move[0], self.position[1] + move[1])
        self.path.append(self.position)
        return self.position

    @abc.abstractmethod
    def level_up(self):
        pass


class Pawn(Player):
    def __init__(self):
        super().__init__()
        # up, down, left, right
        self.moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def level_up(self):
        # four diagonal movements
        self.moves.extend([(1, 1), (1, -1), (-1, 1), (-1, -1)])

# --- Test the classes ---
pawn = Pawn()
print("Initial position:", pawn.position)
print("Initial path:", pawn.path)
print("Initial moves:", pawn.moves)

print("\n--- Making some moves ---")
for i in range(5):
    new_pos = pawn.make_move()
    print(f"Move {i+1}: {new_pos}")

print("\nPath so far:", pawn.path)

print("\n--- Leveling up ---")
pawn.level_up()
print("Moves after level up:", pawn.moves)

print("\n--- Making more moves after level up ---")
for i in range(3):
    new_pos = pawn.make_move()
    print(f"Move {i+1}: {new_pos}")

print("\nFinal path:", pawn.path)