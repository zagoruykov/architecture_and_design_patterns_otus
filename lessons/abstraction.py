import abc
from typing import NamedTuple, TypedDict, Self
import unittest


class Vector(NamedTuple):
    dx: int
    dy: int


class Point(NamedTuple):
    x: int
    y: int

    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise ValueError("Cannot add non vector object")
        return Point(self.x + other.dx, self.y + other.dy)

    def __eq__(self, value: Self):
        return self.x == value.x and self.y == value.y


class GameItemMetadata(TypedDict):
    location: Point
    velocity: Vector
    direction: int
    n: int
    angleVelocity: int


class Movable(abc.ABC):
    def get_location(self) -> Point: ...
    def set_location(self, object_location: Point) -> None: ...
    def get_velocity(self) -> Vector: ...


class Rotatable(abc.ABC):
    def rotate(self): ...


class GameItem(abc.ABC):
    @abc.abstractmethod
    def get_metadata(self) -> GameItemMetadata: ...


class PlainVectorMoveSpaceshipAdapter(Movable):
    _item: GameItem

    def __init__(self, item: GameItem):
        self._item = item

    def get_location(self):
        return self._item.get_metadata().get("location")

    def set_location(self, object_location):
        self._item.get_metadata()["location"] = object_location

    def get_velocity(self):
        return self._item.get_metadata().get("velocity")


class RotateAdapter(Rotatable):
    _item: GameItem

    def __init__(self, item: GameItem):
        self._item = item

    def rotate(self):
        current_direction = self._item.get_metadata().get("direction")
        angle_velocity = self._item.get_metadata().get("angleVelocity")
        n = self._item.get_metadata().get("n")
        self._item.get_metadata()["direction"] = (
            current_direction + angle_velocity
        ) % n


class Move:
    _movable: Movable

    def __init__(self, movable: Movable):
        self._movable = movable

    def execute(self):
        new_point = self._movable.get_location() + self._movable.get_velocity()
        self._movable.set_location(new_point)


class Rotate:
    _rotatable: Rotatable

    def __init__(self, rotatable: Rotatable):
        self._rotatable = rotatable

    def execute(self):
        self._rotatable.rotate()


class Spaceship(GameItem):
    _metadata: GameItemMetadata

    def __init__(self, metadata: GameItemMetadata):
        self._metadata = metadata

    def get_metadata(self):
        return self._metadata
