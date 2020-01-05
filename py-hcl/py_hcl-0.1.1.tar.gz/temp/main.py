# from py_hcl import *
# from py_hcl.compile import compile_to_firrtl
# from py_hcl.convertor.convertor import convert
# from py_hcl.core.expr import ExprTable
# from py_hcl.utils import json_serialize
#
#
# # class A(Module):
# #     io = IO(
# #         sel=Input(U.w(2)),
# #         i1=Input(S.w(8)),
# #         i2=Input(S.w(10)),
# #         o=Output(U.w(7)[2]),
# #     )
# #
# #     io.o[0] <<= io.i1[2:0]
# #     with when(io.sel[0]):
# #         io.o[1] <<= io.i1
# #         io.o[0] <<= io.i1 + io.i2
# #     with else_when(io.sel[1]):
# #         io.o[1] <<= io.i2
# #     with else_when(io.sel[1]):
# #         with when(io.sel[1]):
# #             io.o[1] <<= io.i2
# #         io.o[1] <<= io.i2
# #     with otherwise():
# #         io.o[0] <<= io.i1 & io.i2
# #     io.o[1] <<= io.i2[4:1]
# #
# #
# # class B(Module):
# #     io = IO(
# #         sel=Input(U.w(2)),
# #         i1=Input(S.w(8)),
# #         i2=Input(S.w(10)),
# #         o=Output(U.w(7)[2]),
# #     )
# #
# #     a = A()
# #     a <<= io
# #
# #
# # class C(A):
# #     io = io_extend(A)(
# #         c=Input(U.w(90)[4]),
# #         o=Output(S.w(20)[4])
# #     )
# #     io.o <<= io.c
# #
# #
# # class D(Module):
# #     io = IO(
# #         i0=Input(U.w(8)[4]),
# #         i1=Input(U.w(8)[4]),
# #         o=Output(U.w(8)[4]),
# #     )
# #
# #     io.o <<= io.i0 & io.i1
# #
# #
# class FullAdder(Module):
#     io = IO(
#         a=Input(Bool),
#         b=Input(Bool),
#         cin=Input(Bool),
#         sum=Output(Bool),
#         cout=Output(Bool),
#     )
#
#     # Generate the sum
#     io.sum <<= io.a ^ io.b ^ io.cin
#
#     # Generate the carry
#     io.cout <<= io.a & io.b | io.b & io.cin | io.a & io.cin
#
#
# class E(Module):
#     io = IO(
#         i1=Input(Bundle(a=U.w(8), b=U.w(8), c=S.w(7)[2, 3])),
#         i2=Input(Bundle(a=U.w(8), b=U.w(8), c=S.w(7)[2, 3])),
#         o=Output(Bundle(a=U.w(8), b=U.w(8), c=S.w(7)[2, 3])),
#     )
#
#     io.o <<= io.i1 + io.i2
#
#
# if __name__ == '__main__':
#     # with open("b.json", "w+") as src:
#     #     src.write(str(B.packed_module))
#     # with open("a.json", "w+") as j:
#     #     j.write(str(A.packed_module))
#     # with open("c.json", "w+") as c:
#     #     c.write(str(C.packed_module))
#     # with open("e.json", "w+") as e:
#     #     t = json_serialize(type("t", (object,), {}))()
#     #     t.table = ExprTable.table
#     #     e.write(str(t))
#     #
#     # with open('x.fir', 'wb') as x:
#     #     m = convert(B.packed_module)
#     #     m.serialize_stmt(x)
#     # with open('y.fir', 'wb') as y:
#     #     m = convert(C.packed_module)
#     #     m.serialize_stmt(y)
#     # with open('d.fir', 'wb') as d:
#     #     m = convert(D.packed_module)
#     #     m.serialize_stmt(d)
#     # with open('fulladder.fir', 'wb') as fa:
#     #     m = convert(FullAdder.packed_module)
#     #     m.serialize_stmt(fa)
#     compile_to_firrtl(FullAdder, 'full_adder.fir')
