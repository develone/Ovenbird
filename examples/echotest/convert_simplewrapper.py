from myhdl import intbv, Signal, always_seq, instance, block, ResetSignal

from simple_wrapper import SimpleWrapper

def convert_SimpleWrapper(hdl):
	TX = Signal(bool(0))
	RX = Signal(bool(0))
	clock = Signal(bool(0))
	RST = ResetSignal(0, active=1, isasync=True)

	SimpleWrapper_inst = SimpleWrapper(clock, RX, TX, RST)
	SimpleWrapper_inst.convert(hdl=hdl)

convert_SimpleWrapper(hdl='Verilog')
