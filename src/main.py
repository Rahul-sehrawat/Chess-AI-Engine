import sys, pygame
from const import *
from game import Game
from move import Move
from square import Square


class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption('Rue Chess')
        self.game = Game()  

    def mainloop(self):

        screen = self.screen
        game = self.game
        board = self.game.board
        ai = self.game.ai
        dragger = self.game.dragger
        self.running = True

        while self.running:
            
            if not game.selected_piece:
                game.show_bg(screen)
                game.show_pieces(screen)

            game.show_hover(screen)

            if dragger.dragging:
                dragger.update_blit(screen)

            for event in pygame.event.get():
                
                # mouse click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)

                    pos = event.pos
                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE

                    #if piece exist on this square
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        #if selected piece valid piece 
                        if piece.color == game.next_player:
                            game.select_piece(piece)
                            board.calc_moves(piece, clicked_row, clicked_col)
                            dragger.drag_piece(piece)
                            dragger.save_initial(pos)
                            # show
                            game.show_bg(screen)
                            game.show_pieces(screen)

                # mouse release
                elif event.type == pygame.MOUSEBUTTONUP:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)

                        # released pos
                        released_row = dragger.mouseY // SQSIZE
                        released_col = dragger.mouseX // SQSIZE

                        # new move object
                        initial = Square(dragger.initial_row, dragger.initial_col)
                        final = Square(released_row, released_col)
                        move = Move(initial, final)
                        
                        #if valid move - move 
                        if board.valid_move(dragger.piece, move):
                            # capture
                            captured = board.squares[released_row][released_col].has_piece()
                            # move
                            board.move(dragger.piece, move)
                            game.sound_effect(captured)
                            # draw
                            game.show_bg(screen)
                            game.show_pieces(screen)
                            # next turn is AI
                            game.next_turn()
                            
                            
                            # game-mode is now A.I 

                            if game.gamemode == 'ai':
                                # update
                                game.unselect_piece()
                                game.show_pieces(screen)
                                pygame.display.update()
                                # optimal move
                                move = ai.eval(board)
                                initial = move.initial
                                final = move.final
                                # piece
                                piece = board.squares[initial.row][initial.col].piece
                                # capture
                                captured = board.squares[final.row][final.col].has_piece()
                                # move
                                board.move(piece, move)
                                game.sound_effect(captured)
                                # draw
                                game.show_bg(screen)
                                game.show_pieces(screen)
                                game.next_turn()
                    
                    game.unselect_piece()
                    dragger.undrag_piece()

                # mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    pos = event.pos
                    motion_row = pos[1] // SQSIZE
                    motion_col = pos[0] // SQSIZE

                    game.set_hover(motion_row, motion_col)

                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        # show
                        game.show_bg(screen)
                        game.show_pieces(screen)
                        game.show_hover(screen)
                        dragger.update_blit(screen)

                # key event listener
                elif event.type == pygame.KEYDOWN:
                    
                    # game-mode :- PvP & A.I
                    if event.key == pygame.K_m:
                        game.change_gamemode()
                    
                    # Engine depth
                    if event.key == pygame.K_1:
                        ai.depth = 1
                    
                    if event.key == pygame.K_2:
                        ai.depth = 2

                    if event.key == pygame.K_3:
                        ai.depth = 3

                    if event.key == pygame.K_4:
                        ai.depth = 4

                    # Game board theme 
                    if event.key == pygame.K_t:
                        game.change_theme()
                    
                    # reset
                    if event.key == pygame.K_r:
                        game.reset()

                        screen = self.screen
                        game = self.game
                        board = self.game.board
                        ai = self.game.ai
                        dragger = self.game.dragger

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                

            pygame.display.update()
    
