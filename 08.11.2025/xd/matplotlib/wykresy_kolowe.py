import matplotlib.pyplot as plt;

grades = ["niedostateczny","dopuszczający","dostateczny","dobry","bardzo dobry","celujący"];
quantity = [2,5,12,10,6,1];
myexplode = [0.3,0,0,0.1,0,0.2];
colors = ['red','blue','green','yellow','black','gray'];
fig,ax = plt.subplots();
ax.pie(quantity,labels=grades,explode = myexplode,autopct='%.2f%%',colors=colors);
ax.axis('equal');
ax.legend(title="Oceny końcowe");
plt.show();
