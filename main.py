# Importing necessary libraries from Qiskit
from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit_aer.aerprovider import AerSimulator
from qiskit.visualization import plot_histogram
# Initialize the quantum circuit with 12 qubits and 4 classical bits
qc = QuantumCircuit(5, 4)
# Encoding the input binary numbers 'A' = '10' and 'B' = '11'
# qc.x(0) # qubit remain 0
qc.x(1) # Set qubit 1 to |1⟩ for 'A'
qc.x(2) # Set qubit 2 to |1⟩ for 'B'
qc.x(3) # Set qubit 3 to |1⟩ for 'B'
# Quantum gates for the multiplication algorithm


qc.ccx(0, 2, 4) # P0
qc.measure(4, 0) # Measure P0


qc.reset(4)
qc.ccx(1, 2, 4) # X1
qc.reset(2)
qc.ccx(0, 3, 2) # X2

qc.reset(0)
qc.cx(4, 0) # P1
qc.cx(2, 0) # P1
qc.measure(0, 1) # Measure P1


qc.reset(0)
qc.ccx(4, 2, 0) # X3
qc.reset(2)
qc.ccx(1, 3, 2) # X4

qc.reset(4)
qc.cx(0, 4) # P2
qc.cx(2, 4) # P2
qc.measure(4, 2) # Measure P2

qc.reset(3)
qc.ccx(0, 2, 3) # X4
qc.measure(3, 3) # Measure P4

# Draw the circuit
print("Circuit:")
print(qc.draw(output='text'))
# Execute the circuit on the Aer simulator and retrieve results
aer_sim = Aer.get_backend('aer_simulator')
transpiled_circuit = transpile(qc, aer_sim)
qobj = assemble(transpiled_circuit)
results = aer_sim.run(qobj).result()
counts = results.get_counts()
# Output the measurement results
print(counts)
# Visualize the results in a histogram
plot_histogram(counts)