from src.game import Game
from controllers.main_controller import MainController

class ItemDescriptionController:

  CONTEXT_GAME: Game = None

  @staticmethod
  def getGameData(game_name: str) -> None:

    if game_name and MainController.GAME_LIST:
      
      ItemDescriptionController.CONTEXT_GAME: Game = list(filter(lambda x: x.name == game_name, MainController.GAME_LIST))[0]
    
    else:

      ItemDescriptionController.CONTEXT_GAME = None