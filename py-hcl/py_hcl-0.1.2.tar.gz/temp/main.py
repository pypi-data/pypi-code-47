from py_hcl import *  # noqa: F403
from py_hcl.transformer.pyhcl_to_firrtl.convertor import convert


class A(Module):
    io = IO(
        sel=Input(U.w(2)),
        i1=Input(U.w(3)),
        i2=Input(U.w(3)),
        o=Output(S.w(8)),
    )

    io.o <<= U(8)
    with when(io.sel[0]):
        io.o <<= io.i1
    with else_when(io.sel[1]):
        with when(io.i1[2]):
            io.o <<= io.i1 + io.sel
    with otherwise():
        io.o <<= io.i1 + io.i2


class C(Module):
    io = IO(
        i3=Input(U.w(20)),
        o3=Output(U.w(10))
    )

    io.o3 <<= io.i3


class B(A):
    io = io_extend(A)(
        i3=Input(U.w(20)),
        o3=Output(U.w(10))
    )

    c = C()
    c.i3 <<= io.i3
    io.o3 <<= c.o3


class FullAdder(Module):
    io = IO(
        a=Input(Bool),
        b=Input(Bool),
        cin=Input(Bool),
        sum=Output(Bool),
        cout=Output(Bool),
    )

    # Generate the sum
    io.sum <<= io.a ^ io.b ^ io.cin

    # Generate the carry
    io.cout <<= io.a & io.b | io.b & io.cin | io.a & io.cin


if __name__ == '__main__':
    compile_to_firrtl(FullAdder)
