from __future__ import annotations
import numpy
from typing import ClassVar, Callable, Any


__all__ = [
    'Buffer', 
    'CURANDStates', 
    'Device', 
    'calc_fitness_vals', 
    'update_bests', 
    'update_positions', 
    'update_velocities',
    'func_t'
]


func_t = Callable[[numpy.ndarray[numpy.float64]], float]


class Buffer:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __getitem__(self, key: tuple[int, int]) -> float:
        ...
    def __init__(self, nrow: int, ncol: int = 1, device: Device = Device.GPU) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def __setitem__(self, key: tuple[int, int], val: float) -> None:
        ...
    def __str__(self) -> str:
        ...
    def buffer_size(self) -> int:
        ...
    def clear(self) -> None:
        ...
    def copy_to_numpy(self, out: numpy.ndarray[numpy.float64]) -> None:
        ...
    def copy_from_numpy(self, src: numpy.ndarray[numpy.float64]) -> None:
        ...
    def copy_to_buffer(self, out: "Buffer") -> None:
        ...
    def copy_from_buffer(self, src: "Buffer") -> None:
        ...
    def device(self) -> Device:
        ...
    def fill(self, val: float) -> None:
        ...
    def is_same_device(self, other: "Buffer") -> bool:
        ...
    def is_same_shape(self, other: "Buffer") -> bool:
        ...
    def ncol(self) -> int:
        ...
    def nrow(self) -> int:
        ...
    def num_elem(self) -> int:
        ...
    def shape(self) -> tuple[int, int]:
        ...
    def show(self) -> None:
        ...
    def to(self, device: Device) -> None:
        ...
    

class CURANDStates:
    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __init__(self, seed: int, nrow: int, ncol: int) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def buffer_size(self) -> int:
        ...
    def clear(self) -> None:
        ...
    def num_elem(self) -> int:
        ...


class Device:

    CPU: ClassVar[Device]  # value = <Device.CPU: 0>
    GPU: ClassVar[Device]  # value = <Device.GPU: 1>
    __members__: ClassVar[dict[str, Device]]  # value = {'CPU': <Device.CPU: 0>, 'GPU': <Device.GPU: 1>}

    @staticmethod
    def _pybind11_conduit_v1_(*args, **kwargs):
        ...
    def __eq__(self, other: Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...


def calc_fitness_val_npy(x: numpy.ndarray[numpy.float64]) -> None:
    ...
def calc_fitness_vals_npy(xs: numpy.ndarray[numpy.float64], out: numpy.ndarray[numpy.float64]) -> None:
    ...
def calc_fitness_vals(xs: Buffer, out: Buffer) -> None:
    ...

def update_bests(xs: Buffer, x_fits: Buffer, local_best_xs: Buffer, local_best_fits: Buffer, global_best_x: Buffer, global_best_fit: Buffer) -> int:
    ...
def update_positions(xs: Buffer, vs: Buffer, x_min: float, x_max: float) -> None:
    ...
def update_velocities(xs: Buffer, vs: Buffer, local_best_xs: Buffer, global_best_x: Buffer, v_sum_pow2: Buffer, w: float, c0: float, c1: float, v_max: float, rng_states: CURANDStates) -> None:
    ...
