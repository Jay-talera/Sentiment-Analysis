import preProcessing as pp 
import emotions as em
import matplotlib.pyplot as plt 


fig, ax1 = plt.subplots()
ax1.bar(em.count.keys(),em.count.values())
fig.autofmt_xdate()
plt.savefig("Bar_Graph.png")
plt.show()