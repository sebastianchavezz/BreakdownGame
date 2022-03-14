

from BreakOutGame.Game import Game
import pygame as pg
import neat
import os
import pickle

class BreakdownAI:
    MAX_FPS = 60
    def __init__(self,screen,width,height):
        self.screen = screen
        self.game = Game(screen,width,height)
        self.paddle = self.game.player.paddle
        self.ball = self.game.ball.rect
        self.screen.fill((0,0,0))
    def test_ai(self,net):
        
        clock = pg.time.Clock()
        run = True
        while run:
            run = self.game.is_ball_in_Game()
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    run= False
            
            keys = pg.key.get_pressed()
            output = net.activate((self.paddle.x,self.ball.x,abs(self.paddle.y-self.ball.y)))
            decision = output.index(max(output))

            if decision == 0:
                pass
            elif decision ==1:
                self.game.move_pallet(left=True)
            else:
                self.game.move_pallet(left=False)

            self.game.update_screen()
            clock.tick(self.MAX_FPS)
            pg.display.flip()
    
    
    def train_ai(self,genome,config):
        net = neat.nn.FeedForwardNetwork.create(genome,config)
        clock = pg.time.Clock()
        run = True
        while run:
            
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    quit()
            output = net.activate((self.paddle.x,self.ball.x,abs(self.paddle.y-self.ball.y)))
            decision = output.index(max(output))

            if decision == 0:
                pass
            elif decision ==1:
                self.game.move_pallet(left=True)
            else:
                self.game.move_pallet(left=False)


            
            self.game.update_screen()
            run = self.game.is_ball_in_Game() and self.game.game_rectangles.check_game_done() and self.game.infinity_loop()
            clock.tick(self.MAX_FPS)
            pg.display.flip()


        self.calculate_fitness(genome,self.game.game_rectangles.score)
        

    def calculate_fitness(self,genome,player_hit):
        genome.fitness += player_hit


def eval_genomes(genomes, config):
    width, height = 700, 1000
    window = pg.display.set_mode((width,height))
    for i, (genome_id,genome) in enumerate(genomes):
        genome.fitness =0
        game = BreakdownAI(window,width,height)
        game.train_ai(genome,config)
        

def run_neat(config):
    p =neat.Checkpointer.restore_checkpoint('neat-checkpoint-40')
    #p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))
    
    winner = p.run(eval_genomes,20)
    with open('best.pickle','wb') as f:
        print('__________________________________________________________________________________')
        pickle.dump(winner,f)


def test_ai(config):
    width, height = 700, 1000
    window = pg.display.set_mode((width,height))
    with open('best.pickle','rb')as f:
        winner = pickle.load(f)
    winner_net = neat.nn.FeedForwardNetwork.create(winner, config)
    game = BreakdownAI(window,width,height)
    game.test_ai(winner_net)
    
if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir,'confix.txt')

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)
    
    run_neat(config)

