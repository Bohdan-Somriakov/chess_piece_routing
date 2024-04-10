from Game import Game



def main():
    size = int(input("Enter the size of the Board: "))
    game = Game(size)
    game.play()
if __name__ == "__main__":
     main()