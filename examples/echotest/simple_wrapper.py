from myhdl import intbv, Signal, always_seq, instance, block, ResetSignal

# A simple wrapper around the echotest(i_clk, i_uart_rx, o_uart_tx), so all the tests for that
# object should work. The point is to test the echotest being not the top level
# in the hierarchy.

@block
def SimpleWrapper(clock, RX, TX, RST):
	"""
	MyHDL signals clock, TX, RX, RST
	Verilog signals i_clk, i_uart_rx, o_uart_tx
	TX = Signal(bool(0)) o_uart_tx signal define in echotest.v
	RX = Signal(bool(0)) i_uart_rx signal define in echotest.v
	clock = Signal(bool(0)) i_clk signal define in echotest.v
	RST = ResetSignal(0, active=1, isasync=True)
	"""
	
	@always_seq(clock.posedge, reset=RST)
	def constant_signal_driver():
		TX.next = 1			
	#echo_test = ECHOTEST(clock, RX, TX)
	
	#return echo_test, constant_signal_driver
	return constant_signal_driver
	
