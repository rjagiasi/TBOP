import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('results.csv')
# print(df.head)
# print(df['Filename'])

# df = pd.read_csv('/content/results.csv')
# print(df.head)
# print(df['Filename'])

df.insert(1,'INDEX',np.arange(1,22,1))

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax1.bar(df['INDEX'],df['Accuracy of the Code'])
plt.tight_layout()
# plt.legend('Overall Accuracy')
plt.title('Overall Accuaracy')
plt.ylabel('Accuracy(%)')
plt.xlabel('Videos')
plt.xticks(df['INDEX'])
plt.ylim(bottom = 25)
fig.set_size_inches(14, 5)
plt.rcParams['font.size'] = '16'
# plt.savefig('/content/Overall.png',dpi=300)

ax2 = fig.add_subplot(122)
ax2.bar(df['INDEX'],df['Percentage English Predicted'])
plt.tight_layout()
# plt.legend('Overall Accuracy')
plt.title('Percentage English')
plt.ylabel('Percentage(%)')
plt.rcParams['font.size'] = '16'
plt.xlabel('Videos')
plt.xticks(df['INDEX'])
plt.ylim(bottom = 25)
fig.set_size_inches(18, 5)
plt.savefig('Overall.png',dpi=300)


# df[]÷
