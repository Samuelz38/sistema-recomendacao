from typing import List
import os

from src.game import Game
from src.graph import Graph
from models.repositories.game_repository import GameRepository

class MainController:

  GAME_LIST: List[Game] = []

  @staticmethod
  def getGameList(entry: str) -> None:

    graph = Graph(os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                               "files", 
                               "graph.json") if "graph.json" in os.listdir(os.path.join(
                                 os.path.dirname(os.path.dirname(__file__)), 
                                 "files")) else "")

    entry_game: str = entry

    context_game = GameRepository.getGameByName(entry_game)

    # Não foi encontrado nenhum jogo com o nome {entry_game}!
    if not context_game:

      MainController.GAME_LIST = []
      return 

    game_id: int = context_game[0]

    recommended_games_id = graph.getRecommendedVerts(game_id)

    game_list: List[Game] = list(map(GameRepository.getGameObjectByID, recommended_games_id))

    MainController.GAME_LIST = game_list