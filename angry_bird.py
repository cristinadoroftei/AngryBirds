class Bird: 
    def __init__(self, birdRow, birdColumn):
        self.birdRow = birdRow
        self.birdColumn = birdColumn

class Pig:
    def __init__(self, pigRow, pigColumn):
        self.pigRow = pigRow
        self.pigColumn = pigColumn




class Board:
    def __init__(self, noRows, noColumns):
        self.noRows = noRows
        self.noColumns = noColumns
    
    def displayBoard(self, board, bird, pig):
        print()
        for i in range(board.noRows):
            for j in range(board.noColumns):
                if bird.birdRow == i and bird.birdColumn == j:
                    print(" B ", end = '')
                elif pig.pigRow == i and pig.pigColumn == j:
                    print(" P ", end = '')
                elif j == board.noColumns - 1 :
                    print(" * ", '\n')
                else: print(" * ", end = '' )


class Workspace:
    def __init__(self):
        self.axI = [-1, 0, 1, 0]
        self.axJ = [0, 1, 0, -1 ]

    def movements(self, bird): 
        stop = 0
        turnI = 0
        turnJ = 0
        while stop == 0 :
            print("Move:", end = '' )
            try:
                movement = input()
            except EOFError:
                break
            if movement == 'q':
                stop = 1

            elif movement == 'f':
                bird.birdRow = bird.birdRow + self.axI[turnI]
                bird.birdColumn = bird.birdColumn + self.axJ[turnJ]

            elif movement == 'l':
                if turnI == 0:
                    turnI = 3
                    turnJ = 3
                else:
                    turnI -= 1
                    turnJ -= 1
            
            elif movement == 'r':
                if turnI == 3:
                    turnI = 0
                    turnJ = 0
                else:
                    turnI += 1
                    turnJ += 1

        return bird

                
            
class Game:
    def startGame(self):
        bird = Bird(3,3)
        pig = Pig(6,5)
        board = Board(8,8)
        workspace = Workspace()
        board.displayBoard(board,bird,pig) 
        workspace.movements(bird)
        self.winOrLose(bird,pig, board)

    def winOrLose(self, bird,pig, board):
        if bird.birdRow == pig.pigRow and bird.birdColumn == pig.pigColumn:
            print("\n Yee you won")
        else:
            print("Ooops, you lost. This is how the bird ended up:")
            print()
            for i in range(board.noRows):
                for j in range(board.noColumns):
                    if bird.birdRow == i and bird.birdColumn == j:
                        print(" B ", end = '')
                    elif pig.pigRow == i and pig.pigColumn == j:
                        print(" P ", end = '')
                    elif j == board.noColumns - 1 :
                        print(" * ", '\n')
                    else: print(" * ", end = '' )

           

game = Game()
game.startGame()


