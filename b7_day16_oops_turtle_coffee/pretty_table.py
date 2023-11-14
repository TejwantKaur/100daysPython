from prettytable import PrettyTable

table = PrettyTable()


table.add_column("Pokemon Name", ["Pikachu", "Simipour", "Diggersby", "Linoone", "Vivillon"])
table.add_column("Type", ["Electric", "Water", "Ground", "Normal", "Flying"])

table.align = "l"
print(table)