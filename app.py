from game import Game
def main():
    game = Game()
    print(game.active_phrase.phrase)
    game.start()

if __name__ == "__main__":
    main()

