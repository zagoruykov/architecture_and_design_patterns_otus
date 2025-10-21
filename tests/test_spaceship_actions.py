import unittest
from lessons.abstraction import (
    RotateAdapter,
    Spaceship,
    GameItemMetadata,
    Point,
    Vector,
    PlainVectorMoveSpaceshipAdapter,
    Rotate,
    Move,
)


class TestPlainVectorMoveSpaceshipAdapter(unittest.TestCase):
    def setUp(self):
        point = Point(12, 5)
        vector = Vector(-7, 3)
        default_metadata: GameItemMetadata = {
            "location": point,
            "velocity": vector,
            "angleVelocity": 10,
            "direction": 300,
            "n": 1000,
        }
        self.spaceship = Spaceship(default_metadata)

    def test_game_item_can_move(self):
        expected_point = Point(5, 8)
        spaceship = self.spaceship
        plain_movable_adapter = PlainVectorMoveSpaceshipAdapter(spaceship)
        move = Move(plain_movable_adapter)
        move.execute()
        self.assertEqual(spaceship.get_metadata().get("location"), expected_point)

    def test_game_item_can_rotate(self):
        expected_direction = 310
        spaceship = self.spaceship
        rotate_adapter = RotateAdapter(spaceship)
        rotate = Rotate(rotate_adapter)
        rotate.execute()
        self.assertEqual(spaceship.get_metadata().get("direction"), expected_direction)
